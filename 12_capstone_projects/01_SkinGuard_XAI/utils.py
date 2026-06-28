import json
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


IMG_SIZE = 224

CLASS_DESCRIPTIONS = {
    "akiec": "Actinic keratoses and intraepithelial carcinoma",
    "bcc": "Basal cell carcinoma",
    "bkl": "Benign keratosis-like lesions",
    "df": "Dermatofibroma",
    "mel": "Melanoma",
    "nv": "Melanocytic nevi",
    "vasc": "Vascular lesions"
}


def load_classes(path):
    with open(path, "r") as f:
        return json.load(f)


def preprocess_image(image):
    image = np.array(image)

    resized = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    image_array = np.expand_dims(
        resized.astype("float32"),
        axis=0
    )

    image_array = preprocess_input(image_array)

    return image, image_array


def predict_image(model, image, class_names):
    original_image, processed_image = preprocess_image(image)

    predictions = model.predict(processed_image, verbose=0)[0]

    predicted_index = int(np.argmax(predictions))
    predicted_label = class_names[predicted_index]
    predicted_name = CLASS_DESCRIPTIONS.get(predicted_label, predicted_label)
    confidence = float(predictions[predicted_index])

    top_indices = np.argsort(predictions)[-3:][::-1]

    top_predictions = []

    for rank, index in enumerate(top_indices, start=1):
        label = class_names[int(index)]
        name = CLASS_DESCRIPTIONS.get(label, label)
        score = float(predictions[int(index)])

        top_predictions.append({
            "Rank": rank,
            "Label": label,
            "Class Name": name,
            "Confidence": f"{score:.2%}"
        })

    return original_image, processed_image, predicted_label, predicted_name, confidence, top_predictions


def find_mobilenet_base_model(model):
    for layer in model.layers:
        if "mobilenet" in layer.name.lower():
            return layer
    return None


def get_last_conv_layer(base_model):
    for layer in reversed(base_model.layers):
        if len(layer.output.shape) == 4:
            return layer.name
    raise ValueError("No convolutional layer found.")


def make_gradcam_heatmap(processed_image, model):
    base_model = find_mobilenet_base_model(model)

    if base_model is None:
        raise ValueError("MobileNetV2 base model not found.")

    last_conv_layer_name = get_last_conv_layer(base_model)

    grad_model = tf.keras.models.Model(
        inputs=base_model.input,
        outputs=[
            base_model.get_layer(last_conv_layer_name).output,
            base_model.output
        ]
    )

    classifier_input = tf.keras.Input(shape=base_model.output.shape[1:])
    x = classifier_input

    start_classification = False

    for layer in model.layers:
        if layer.name == base_model.name:
            start_classification = True
            continue

        if start_classification:
            x = layer(x)

    classifier_model = tf.keras.Model(classifier_input, x)

    with tf.GradientTape() as tape:
        conv_outputs, base_output = grad_model(processed_image)
        predictions = classifier_model(base_output)
        predicted_index = tf.argmax(predictions[0])
        class_channel = predictions[:, predicted_index]

    grads = tape.gradient(class_channel, conv_outputs)

    pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))

    conv_outputs = conv_outputs[0]

    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]

    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(heatmap, 0)

    max_value = tf.math.reduce_max(heatmap)

    if max_value == 0:
        return np.zeros_like(heatmap.numpy())

    heatmap = heatmap / max_value

    return heatmap.numpy()


def create_gradcam_overlay(original_image, heatmap, alpha=0.45):
    heatmap_resized = cv2.resize(
        heatmap,
        (original_image.shape[1], original_image.shape[0]),
        interpolation=cv2.INTER_CUBIC
    )

    heatmap_uint8 = np.uint8(255 * heatmap_resized)

    heatmap_color = cv2.applyColorMap(
        heatmap_uint8,
        cv2.COLORMAP_JET
    )

    heatmap_color = cv2.cvtColor(
        heatmap_color,
        cv2.COLOR_BGR2RGB
    )

    overlay = cv2.addWeighted(
        original_image,
        1 - alpha,
        heatmap_color,
        alpha,
        0
    )

    return heatmap_color, overlay

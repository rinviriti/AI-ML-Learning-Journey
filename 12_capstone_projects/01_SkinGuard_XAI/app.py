import os
import pandas as pd
import gradio as gr
import tensorflow as tf

from utils import (
    load_classes,
    predict_image,
    make_gradcam_heatmap,
    create_gradcam_overlay
)


MODEL_PATH = "model/SkinGuard_XAI_Image_Model.keras"
CLASS_NAMES_PATH = "model/class_names.json"

model = tf.keras.models.load_model(MODEL_PATH)
class_names = load_classes(CLASS_NAMES_PATH)


def analyze_skin_image(image):
    if image is None:
        return (
            "Please upload a skin lesion image.",
            None,
            None,
            None,
            pd.DataFrame()
        )

    original_image, processed_image, label, name, confidence, top_predictions = predict_image(
        model,
        image,
        class_names
    )

    heatmap = make_gradcam_heatmap(
        processed_image,
        model
    )

    heatmap_image, overlay_image = create_gradcam_overlay(
        original_image,
        heatmap
    )

    result = f"""
## Prediction Result

### {name}

**Short Label:** `{label}`  
**Confidence:** **{confidence:.2%}**

---

### Medical Disclaimer

This application is for educational and research purposes only.  
It is not a certified medical device and must not be used for clinical diagnosis or treatment.
"""

    top_df = pd.DataFrame(top_predictions)

    return result, original_image, heatmap_image, overlay_image, top_df


with gr.Blocks(title="SkinGuard XAI") as demo:
    gr.Markdown(
        """
# 🩺 SkinGuard XAI

### Explainable AI for Skin Lesion Classification

Upload a dermoscopic skin lesion image and receive:

- Predicted lesion class  
- Confidence score  
- Top-3 predictions  
- Grad-CAM explainability visualization  

⚠️ **This is an educational and research demo only. It is not a medical diagnostic tool.**
"""
    )

    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(
                type="numpy",
                label="Upload Skin Lesion Image"
            )

            analyze_button = gr.Button(
                "Analyze Image",
                variant="primary"
            )

        with gr.Column(scale=1):
            prediction_output = gr.Markdown(
                label="Prediction Result"
            )

            top_predictions_output = gr.Dataframe(
                headers=["Rank", "Label", "Class Name", "Confidence"],
                label="Top 3 Predictions"
            )

    gr.Markdown("## 🔥 Grad-CAM Explainability")

    with gr.Row():
        original_output = gr.Image(
            type="numpy",
            label="Original Image"
        )

        heatmap_output = gr.Image(
            type="numpy",
            label="Grad-CAM Heatmap"
        )

        overlay_output = gr.Image(
            type="numpy",
            label="Grad-CAM Overlay"
        )

    with gr.Accordion("About this project", open=False):
        gr.Markdown(
            """
SkinGuard XAI is a Medical AI project built using the HAM10000 skin lesion dataset.

The model uses MobileNetV2 transfer learning for image classification and Grad-CAM for visual explainability.

The goal is to demonstrate an end-to-end AI workflow:

Dataset → Training → Evaluation → Inference → Explainability → Deployment
"""
        )

    analyze_button.click(
        fn=analyze_skin_image,
        inputs=input_image,
        outputs=[
            prediction_output,
            original_output,
            heatmap_output,
            overlay_output,
            top_predictions_output
        ]
    )


if __name__ == "__main__":
    demo.launch()

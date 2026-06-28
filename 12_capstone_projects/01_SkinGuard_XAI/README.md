# 🩺 SkinGuard XAI

SkinGuard XAI is an explainable Medical AI project for skin lesion classification using the HAM10000 dataset.

The project applies Deep Learning, Transfer Learning, and Explainable AI to classify dermoscopic skin lesion images and provide visual explanations using Grad-CAM.

## 🎯 Project Objective

To build an AI-based skin lesion classification pipeline that can:

- Preprocess dermoscopic skin images
- Train a deep learning model
- Apply MobileNetV2 transfer learning
- Evaluate classification performance
- Generate Grad-CAM explanations
- Support future mobile-based skin cancer screening research

## 📌 Dataset

**Dataset:** HAM10000 Skin Cancer MNIST  
**Task:** Multi-class skin lesion classification  
**Input:** Dermoscopic skin lesion images  
**Labels:** Skin lesion diagnosis categories

## 🧠 Methods Used

- Image preprocessing
- Label encoding
- Class weight handling
- CNN-based classification
- MobileNetV2 transfer learning
- Model evaluation
- Confusion matrix
- Precision, recall, and F1-score
- Grad-CAM explainability

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-2D333B?style=for-the-badge&logo=python&logoColor=FFD43B)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2D333B?style=for-the-badge&logo=tensorflow&logoColor=FF6F00)
![Keras](https://img.shields.io/badge/Keras-2D333B?style=for-the-badge&logo=keras&logoColor=D00000)
![OpenCV](https://img.shields.io/badge/OpenCV-2D333B?style=for-the-badge&logo=opencv&logoColor=5C3EE8)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-2D333B?style=for-the-badge&logo=scikitlearn&logoColor=F7931E)
![Pandas](https://img.shields.io/badge/Pandas-2D333B?style=for-the-badge&logo=pandas&logoColor=150458)
![NumPy](https://img.shields.io/badge/NumPy-2D333B?style=for-the-badge&logo=numpy&logoColor=4DABCF)
![Kaggle](https://img.shields.io/badge/Kaggle-2D333B?style=for-the-badge&logo=kaggle&logoColor=20BEFF)

---

# 🏗️ Project Workflow

```text
HAM10000 Dataset
        │
        ▼
Metadata Loading
        │
        ▼
Image Preprocessing
        │
        ▼
Image Resizing
        │
        ▼
Normalization
        │
        ▼
Label Encoding
        │
        ▼
Train / Validation Split
        │
        ▼
CNN / MobileNetV2
        │
        ▼
Transfer Learning
        │
        ▼
Model Training
        │
        ▼
Performance Evaluation
        │
        ▼
Explainability (Grad-CAM)
        │
        ▼
Skin Lesion Prediction
```

---

# 🔬 Features

✔ Medical Image Preprocessing

✔ Skin Lesion Classification

✔ CNN-based Learning

✔ Transfer Learning using MobileNetV2

✔ Explainable AI (Grad-CAM)

✔ Performance Evaluation

✔ Confusion Matrix

✔ Classification Report

✔ Multi-class Classification

---

# 📈 Model Evaluation

The trained model is evaluated using several standard Machine Learning metrics.

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics provide a comprehensive understanding of the model's performance across different lesion classes.

---

# 🧩 Explainable AI (XAI)

Medical AI models should not only produce accurate predictions but also provide understandable explanations.

SkinGuard XAI integrates **Grad-CAM (Gradient-weighted Class Activation Mapping)** to visualize which regions of a skin lesion contribute most to the model's prediction.

This helps improve transparency and supports more interpretable AI-assisted medical image analysis.

---

# 📂 Repository Structure

```text
01_SkinGuard_XAI/
│
├── README.md
├── SkinGuard_XAI.ipynb
├── requirements.txt
├── LICENSE
│
├── images/
│   ├── workflow.png
│   ├── sample_images.png
│   ├── confusion_matrix.png
│   ├── gradcam_examples.png
│   └── results.png
│
└── outputs/
    ├── metrics.csv
    ├── predictions.csv
    └── model_summary.txt
```

---

# 🚀 Future Improvements

Future versions of SkinGuard XAI may include:

- EfficientNet-based models
- Vision Transformer (ViT)
- Attention mechanisms
- Fine-tuning of Transfer Learning models
- TensorFlow Lite deployment
- Flutter mobile application
- Clinical decision support interface
- Improved explainability methods

---

# 📚 Learning Outcomes

This project demonstrates practical experience with:

- Medical Image Processing
- Deep Learning
- Computer Vision
- Transfer Learning
- Explainable AI
- Model Evaluation
- Healthcare AI Applications

---

# ⚠️ Disclaimer

This repository is intended for educational and research purposes only.

It is **not** a certified medical device and should **not** be used for clinical diagnosis, treatment planning, or healthcare decision-making.

Always consult qualified healthcare professionals for medical advice.

---

# 📜 License

This project is released under the **MIT License**.

---

# 👩‍💻 Author

**Rinvi Jaman Riti**

Artificial Intelligence • Machine Learning • Medical AI • Computer Vision

GitHub: https://github.com/rinviriti

---

## ⭐ If you found this project useful, consider giving it a star!

Your support helps motivate continued development and future open-source AI projects.

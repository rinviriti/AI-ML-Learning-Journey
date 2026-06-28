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

## 🔬 Workflow

```text
HAM10000 Dataset
        ↓
Metadata Loading
        ↓
Image Preprocessing
        ↓
Label Encoding
        ↓
Class Weight Handling
        ↓
CNN / MobileNetV2 Model
        ↓
Model Evaluation
        ↓
Grad-CAM Explainability
        ↓
Skin Lesion Prediction

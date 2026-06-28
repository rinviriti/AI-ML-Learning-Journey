# 🩺 SkinGuard XAI

An end-to-end Explainable Artificial Intelligence (XAI) system for automated skin lesion classification using Deep Learning and Transfer Learning.

This project was developed as part of my AI & Machine Learning learning journey and demonstrates a complete Medical AI pipeline from data preprocessing to deployment-ready model generation.

---

# 🚀 Project Overview

Skin cancer is one of the most common forms of cancer worldwide. Early detection can significantly improve treatment outcomes.

SkinGuard XAI uses deep learning models trained on the HAM10000 dataset to classify dermoscopic images of skin lesions. The project also explores Explainable AI techniques to improve transparency and interpretability.

---

# 🎯 Objectives

- Build a skin lesion classification system
- Compare multiple deep learning models
- Explore metadata fusion
- Apply transfer learning using MobileNetV2
- Evaluate model performance
- Prepare a deployment-ready AI model
- Support future Grad-CAM visualization

---

# 📂 Dataset

**HAM10000 (Human Against Machine with 10000 Training Images)**

Dataset contains dermoscopic images belonging to seven skin lesion classes.

Classes:

- akiec
- bcc
- bkl
- df
- mel
- nv
- vasc

Dataset Source:

https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000

---

# 🛠 Technologies Used

- Python
- TensorFlow
- Keras
- MobileNetV2
- OpenCV
- NumPy
- Pandas
- Scikit-Learn
- Matplotlib
- Kaggle
- Jupyter Notebook

---

# 🔬 Project Workflow

```
HAM10000 Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Image Preprocessing
        │
        ▼
Metadata Processing
        │
        ▼
Train / Validation / Test Split
        │
        ▼
Data Augmentation
        │
        ▼
Model Training
        │
        ├── Custom CNN
        ├── MobileNetV2
        └── MobileNetV2 + Metadata Fusion
                │
                ▼
Model Evaluation
                │
                ▼
Best Model Selection
                │
                ▼
Deployment-ready Model
```

---

# 🧠 Models Implemented

- Custom CNN
- MobileNetV2 Transfer Learning
- MobileNetV2 + Metadata Fusion

---

# 📊 Evaluation Metrics

The models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

---

# 📁 Project Structure

```text
01_SkinGuard_XAI/
│
├── SkinGuard_XAI.ipynb
├── inference.ipynb
├── app.py
├── README.md
├── requirements.txt
│
├── model/
│   ├── SkinGuard_XAI_Image_Model.keras
│   ├── SkinGuard_XAI_Metadata_Fusion_Model.keras
│   ├── class_names.json
│   └── metadata_columns.json
│
├── images/
│
└── outputs/
```

---

# 🌟 Features

- Skin lesion classification
- Image preprocessing
- Metadata integration
- Transfer learning
- Model comparison
- Evaluation metrics
- Deployment-ready model
- Explainable AI ready (Grad-CAM)

---

# 🚀 Future Improvements

- Grad-CAM visualization
- TensorFlow Lite conversion
- Flutter mobile application
- EfficientNet implementation
- Vision Transformer comparison
- Web deployment using Gradio
- Hugging Face Spaces deployment

---

# 📚 Learning Outcomes

This project helped me understand:

- Medical image preprocessing
- Deep learning workflows
- Transfer learning
- CNN architectures
- Metadata fusion
- Model evaluation
- Medical AI pipelines
- End-to-end AI project development

---

# ⚠️ Medical Disclaimer

This project is intended for educational and research purposes only.

It is **not** a certified medical device and should **not** be used for clinical diagnosis or treatment decisions.

Always consult qualified healthcare professionals for medical advice.

---

# 📄 License

This project is released under the MIT License.

---

# 👩‍💻 Author

**Rinvi Jaman Riti**

AI • Machine Learning • Deep Learning • Computer Vision • Medical AI

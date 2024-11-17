# Brain Tumor Detection Application

This project is a **Brain Tumor Detection Application** built using Python. It leverages the **YOLOv11-Large (YOLOv11l)** model for detecting and classifying brain tumors from MRI scans. The application is implemented with a **Tkinter GUI**, allowing users to upload images, visualize tumor detections, and receive detailed information about the tumor type, including grade, prognosis, symptoms, and suggested treatments.

---

## Features
- **Four-Class Tumor Detection**:
  - Glioma
  - Pituitary
  - Meningioma
  - No-Tumor
    
- **User-Friendly GUI**:
  - Upload and display MRI scans.
  - Visualize tumor detections with bounding boxes and confidence scores.
  - View textual information about the detected tumor type.
    
- **Accurate and Fast Predictions**:
  - Powered by YOLOv11l, a robust object detection model.
  - Trained on a comprehensive dataset of 7022 labeled MRI images.

---

## Dataset
The dataset used for training was sourced from Kaggle and consists of **7022 MRI scans**, categorized into four classes. The dataset was labeled using **Roboflow** and exported in YOLOv11 format.

**Access the dataset here:**  
[Brain Tumor Dataset - Google Drive](https://drive.google.com/drive/folders/1YvsKJH3kZAyhjhTQv_a7QssjRmIugvqh?usp=sharing)

---

## Methodology
1. **Dataset Collection and Preparation**:
   - Collected 7022 MRI scan images from Kaggle.
   - Labeled the images using Roboflow, generating bounding boxes for tumor regions.
   - Exported the dataset in YOLOv11 format.

2. **Model Training**:
   - Trained the **YOLOv11l model** on the dataset using **Google Colab** with GPU support.
   - Dataset was split into 70% training and 30% validation for accurate performance evaluation.
   - Optimized hyperparameters such as batch size, learning rate, and epochs to enhance detection accuracy.

3. **GUI Development**:
   - Developed a **Tkinter-based GUI** application.
   - Integrated the trained YOLOv11l model to process uploaded MRI scans.
   - Displayed results with bounding boxes and confidence scores for detected tumors.
   - Provided additional textual information, including tumor grade, prognosis, symptoms, and treatment suggestions.

---

## Installation
Follow these steps to set up and run the application:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo-name/brain-tumor-detection.git
   cd brain-tumor-detection

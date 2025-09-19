# Emotion Detection using YOLOv12

This project contains two main parts:

1. **Model Training in Google Colab**
2. **Face Detection Web App using Streamlit**

---

## 1️⃣ Model Training (Colab Notebook)

* The file `Emotion_detection_using_YOLOv12.ipynb` contains the full training process.
* It uses a custom dataset from **Roboflow Universe** for face and emotion detection.
* The model is trained using **YOLOv12** (from Ultralytics) with proper annotation and evaluation.
* Final model is saved as `face.pt`.

---

## 2️⃣ Web App (`app.py`)

* The `app.py` file is a **Streamlit app** that loads the trained `face.pt` model.
* It allows users to:

  * Upload an image
  * Detect faces and emotions
  * View bounding boxes with confidence and labels
* The app uses **OpenCV**, **Pillow**, and **Ultralytics YOLO**.

---


## 📂 Files Included

* `Emotion_detection_using_YOLOv12.ipynb` – Colab notebook for training
* `face.pt` – Trained model
* `app.py` – Streamlit app
* `README.md` – Project documentation

---

## ✅ Output Example

* Left side: Original uploaded image
* Right side: Image with detected face and emotion label
* Labels include bounding box + confidence
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/61c29531-66c9-43c5-a08e-392b3f779c34" />

---

## 🙋‍♀️ Made By

**Jagriti** 

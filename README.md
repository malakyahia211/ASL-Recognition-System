# 🤟ASL Recognition System

An End-to-End American Sign Language (ASL) Recognition System using Deep Learning to identify American Sign Language hand gestures from uploaded or captured images through an interactive web interface.

## 🚀 Live Demo

[Try the ASL Recognition System](https://asl-recognition-system-ai.streamlit.app)

## 📌 Project Overview

This project is designed to recognize American Sign Language hand gestures using a trained Deep Learning model.

The system provides an interactive web interface where users can either upload an image or capture a gesture using their camera. The trained model analyzes the gesture and returns the predicted sign along with its confidence score and the top predicted probabilities.

## ✨ Features

- Upload an ASL hand gesture image.
- Capture an ASL gesture using the camera.
- Predict the detected sign using a trained Deep Learning model.
- Display the predicted sign with its confidence score.
- Display the top prediction probabilities.
- Interactive and user-friendly Streamlit interface.
- Live deployment through Streamlit Community Cloud.

## 🧠 How It Works

1. The user uploads an image or captures a gesture using the camera.
2. The image is passed to the trained Deep Learning model.
3. The model analyzes the hand gesture.
4. The system returns the predicted sign.
5. The prediction confidence and top probabilities are displayed through the web interface.

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- Streamlit
- OpenCV
- NumPy
- Pillow
- Deep Learning
- Computer Vision
- Image Classification

## 📂 Project Structure

```text
ASL-Recognition-System/
│
├── app.py
├── backend.py
├── asl_model.keras
├── ASL1.ipynb
├── asl_banner.jpeg
├── requirements.txt
└── README.md

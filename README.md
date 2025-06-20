

---

# Behavioral Emotion Monitoring System

> **Project by:** Gurucharan Raj K, Harish R, Balaji P, Aswin C
> **Department:** AI & Data Science, St. Joseph’s Institute of Technology
> **Presentation Date:** April 2025

## 🧠 Project Overview

This project introduces a **Behavioral Emotion Monitoring System** designed to track employee emotions in real time using facial expression analysis. It leverages deep learning, computer vision, and GUI technologies to assist HR departments in monitoring workplace well-being and productivity.
![image](https://github.com/user-attachments/assets/7d72ac10-bf80-4d93-9126-9051aa9b5fd3)
![image](https://github.com/user-attachments/assets/a47e9f54-a9e2-40b3-a87f-4d717fc947e4)
![image](https://github.com/user-attachments/assets/f2c5638b-f21e-46d1-ade6-f8f102dccb2d)

## 🎯 Objectives

* Detect and classify emotions: 😄 Happy, 😐 Neutral, 😢 Sad, 😠 Angry (with extended support for 😲 Surprised, 😨 Fearful, 🤢 Disgusted).
* Record emotional state with a timestamp every **30 minutes** in CSV format.
* Provide **daily/monthly visual reports** (graphs, charts, and PDF summaries).
* Offer a **user-friendly GUI** using Tkinter for non-technical users.

## 🧪 Technologies Used

| Technology          | Role                             |
| ------------------- | -------------------------------- |
| Python              | Core Programming Language        |
| OpenCV              | Real-time Face Detection         |
| TensorFlow/Keras    | CNN-based Emotion Classification |
| Tkinter             | Graphical User Interface (GUI)   |
| Pandas & Matplotlib | Data Logging & Visualization     |
| ReportLab           | PDF Report Generation            |

## 📁 Project Structure

```
.
├── Classification.py          # Real-time emotion detection with CSV logging
├── Model_Training.py          # CNN model definition and webcam-based prediction
├── PDF_Generator.py           # Creates monthly emotion PDF reports
├── FINAL_EMOTION_ANALYSIS.ipynb  # Jupyter notebook for trend analysis
├── emotion_data/              # Folder to store day-wise CSVs
├── emotion_model.h5           # Pre-trained CNN model weights
├── emojis/                    # Emoji icons for emotion visualization
└── README.md                  # Project documentation
```

## 🚀 How It Works

1. **Face Detection:** Captures webcam feed and uses Haar Cascades to locate faces.
2. **Emotion Classification:** CNN model predicts emotion from cropped facial regions.
3. **Logging:** Saves emotion and timestamp to a CSV every 30 minutes.
4. **Visualization:** Bar/line/pie charts generated from logs.
5. **PDF Reports:** Automatically generated from collected CSVs summarizing emotional trends.

## 📷 Sample Output

* Real-time webcam feed with detected emotion label.
* Emoji displayed alongside actual camera input.
* CSV file with columns: `Timestamp, Emotion, Angry, Disgusted, Fearful, Happy, Neutral, Sad, Surprised`
* PDF report including:

  * Summary statistics
  * Emotion distribution pie chart
  * Confidence over time graph
  * Table of last 10 detected emotions

## 📊 Example CSV Row

```
2025-06-20 10:30:00, Happy, 0.01, 0.00, 0.00, 0.95, 0.02, 0.01, 0.01
```

## ✅ Results

* > 90% accuracy for trained categories.
* Real-time performance on standard laptops.
* Positive feedback from test users.
* Scalable for future cloud deployment.

## 🔐 Limitations

* Requires good lighting conditions.
* Limited to facial expression-based emotion recognition.
* Currently supports only 7 emotion classes.

## 🌟 Future Enhancements

* Integration with Slack/MS Teams for emotion-aware notifications.
* Expand to recognize additional emotions and multimodal inputs (voice, gestures).
* Cloud dashboard for team-wide analytics.

## 🛠️ How to Run

1. Ensure Python 3.x and required libraries are installed.
2. Place `emotion_model.h5` and emoji images in correct folders.
3. Run `Classification.py` for real-time emotion tracking.
4. Use `PDF_Generator.py` to generate monthly reports from `emotion_data/`.

## 📦 Requirements

```bash
pip install opencv-python keras numpy pandas matplotlib reportlab pillow pytz
```

---

## 🙏 Acknowledgements

We express our sincere gratitude to our faculty and peers for their guidance and support throughout this project. Special thanks to the Department of AI & Data Science, St. Joseph’s Institute of Technology.

---

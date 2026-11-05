# OpenCV Face Detector in Python

A lightweight Python project that uses **OpenCV** and a pre-trained **Haar Cascade classifier** to automatically detect human faces in an image and draw bounding boxes around them.

---

## Features
- **Automatic Face Detection:** Utilizes OpenCV's Haar Cascade XML classifier (`haarcascade_frontalface_default.xml`) for fast and efficient face localization.
- **Visual Highlighting:** Draws bright green rectangles and text labels over each detected face.
- **Output Exporting:** Automatically saves the processed image with detected bounding boxes as `detected_faces_output.jpg`.
- **GUI Display:** Pop up a window showing the final result instantly.

---

## Tech Stack
- **Language:** Python 3.x
- **Computer Vision Library:** OpenCV (`opencv-python`)

---

## Prerequisites & Installation

1. Make sure you have Python installed.
2. Install the required OpenCV library:
   ```bash
   pip install opencv-python
   

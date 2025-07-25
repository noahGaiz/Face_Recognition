This project is a real-time facial recognition system developed in Summer 2025. It uses computer vision to detect and recognize faces appearing on camera by comparing them to a set of known faces stored in an images folder.

How It Works
The system continuously scans the camera feed for faces.
When a face is detected, it captures the facial features using face encoding.
It then compares the live encoding to all pre-encoded images in the images directory.
If a match is found within a certain threshold, the person's name is displayed on the screen.
If no match is found, the face is labeled as "Unknown".

Image Requirements
The system only recognizes individuals whose images are stored in the images/ directory.
Each image file should be named clearly to represent the identity of the person and for it to be displayed properly later
You can add more people by simply uploading their images to the images/ folder (ensure the face is clearly visible).



Technologies Used
Python 3
OpenCV – for real-time image processing and camera input
face_recognition – built on top of dlib, used for face detection and face encoding
NumPy – for efficient array operations


Installed dependencies:
cmake
dlib
face_recognition
numpy


Features
Real-time facial recognition
High accuracy using deep learning-based face encoding
Easy to expand: just add new images to the folder
Efficient face comparison with built-in confidence scoring

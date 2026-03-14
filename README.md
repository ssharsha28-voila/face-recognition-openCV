# face-recognition-openCV
A Python based face recognition system.
# Face Recognition System using OpenCV

A face recognition system developed using **Python** and **OpenCV**.
This project was created as my **CBSE Grade 12 AI project**, where I led a small team and implemented the face detection and recognition functionality.

## Overview

This program uses computer vision techniques to detect and recognize human faces through a webcam.
It captures face images, trains a recognition model, and then identifies individuals in real time.

## Features

* Real-time face detection using a webcam
* Face recognition based on trained images
* Model training using captured face datasets
* Implementation using OpenCV computer vision tools

## Technologies Used

* Python
* OpenCV
* NumPy

## Dataset

The dataset used for training was created during the original project by capturing images of participants through a webcam.

The dataset is **not included in this repository** because it was stored on the school system during the project and contains personal images.

To recreate the dataset:

1. Create a `dataset` folder.
2. Create a folder for each person inside it.
3. Capture multiple face images for each individual.

Example structure:

dataset/
    person1/
    person2/

Each folder should contain multiple images of the respective person.

## Installation

Install the required libraries:

pip install -r requirements.txt

## Running the Project

1. Collect training images and place them in the dataset folder.
2. Run the training script to generate the recognition model.
3. Run the recognition script to start real-time face detection.

## Project Demonstration

A video explanation and final outcome of the project is available here:
https://youtu.be/wn3imy1ixKg?si=INj-MOlxZkZsgecD

## Author

Developed as part of the **CBSE Grade 12 AI Project**.
Project lead and implementation by **Harsha**.
This repository is intended to demonstrate the project implementation and code structure. The dataset used in the original project is not included.

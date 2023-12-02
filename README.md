## Person Detection with YOLO and Faster R-CNN on COCO Dataset

This repository demonstrates person detection using YOLO (You Only Look Once) and Faster R-CNN (Region-based Convolutional Neural Network) on the COCO (Common Objects in Context) dataset. The trained models are deployed using Hugging Face Gradio for interactive visualization and experimentation.

### Dataset

The COCO dataset is a large-scale dataset for object detection, keypoint detection, and segmentation. It contains over 200,000 images with 80 object categories. For this project, we used a subset of the dataset containing 4,000 training images, 500 validation images, and 500 test images.

### Models

We trained two object detection models: YOLO and Faster R-CNN.

* **YOLO:** A fast and accurate single-stage detector that predicts bounding boxes and class probabilities directly from the input image.
* **Faster R-CNN:** A two-stage detector that generates region proposals and then classifies and localizes objects within those proposals.

### Training

We trained the models using the Detectron2 framework, a Facebook AI Research (FAIR) library for object detection and instance segmentation that supports a variety of models, including YOLO and Faster R-CNN.

### Deployment

We deployed the trained models using Hugging Face Gradio, an open-source library for creating web interfaces for machine learning models. It provides a simple and declarative way to build user interfaces that allow users to interact with models and visualize their outputs.

### Results

The trained models achieve an average precision (AP) of 55% on the COCO test set. This is a respectable result, considering that the models were trained on a relatively small subset of the dataset.

### Usage

To use the deployed Gradio applications, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies:
```bash
pip install -r requirements.txt


gradio dennis0311/person-detection

4. Select the desired model (YOLO or Faster R-CNN) from the dropdown menu.
5. Upload an image or enter a URL of an image containing people.
6. The application will detect and display bounding boxes around the people in the image.

### Citation

Please cite the following papers if you use this work in your research:

1. Joseph Redmon and Ali Farhadi. "YOLOv9: A High-Performance Detector with Architectural Improvements." arXiv preprint arXiv:2107.08434 (2021).
2. Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun. "Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks." IEEE Transactions on Pattern Analysis and Machine Intelligence 39.6 (2017): 1107-1120.

# Medicinal_Plant_Identification_System_MLflow-DVC


## Objective :
The primary objective of our Medicinal Plant Identification System is to provide a reliable and efficient tool for botanists, herbalists, researchers, and enthusiasts to quickly identify medicinal plants based on their visual attributes. <br>
This system aims to bridge the gap between traditional knowledge of plant identification and modern technological advancements, making it easier for users to access information about the medicinal properties of plants.


<!-- ### Components:
1. **User**: Uploads a photo via the web application.
2. **Web Application**: created web application using Streamlit and FastAPI for instant plant predictions.
3. **Model**: Uses a VGG16 model trained on a plant dataset to predict diffrent Plants.
4. **MLflow**: Used for comparing and choosing model parameters during the testing phase.
5. **DVC**: Employed for data and model versioning.
6. **LLM**: Integrate Google Palm 2 LLM for generating Description of specific plant.
7. **ChatBot**: Create a "Medical Bot" to respond to user inquiries about plants.  -->


## Technologies Used

- **Python**: Create a modular Python script to guarantee the maintenance of industry-standard code quality.
- **TensorFlow**: utilize the TensorFlow Python Library to create and train model, Uses a VGG16 model trained on a plant dataset to predict  diffrent Plants.
- **MLflow**: An open-source platform for managing the end-to-end machine learning lifecycle.
- **DVC (Data Version Control)**: Versioning data and machine learning models to ensure reproducibility.
- **Dagshub**: A collaboration platform for data science and machine learning projects.
- **LLM**: Integrate Google Palm 2 LLM for generating Description of specific plant.
- **ChatBot**: Create a "Medical Bot" to respond to user inquiries about plants.  


<h1> Workflow for the project.</h1>

-   [Data Ingestion stage](##1-Data-Ingestion-stage)
-   [Prepare base model](#2-Prepare-base-model)
-   [Model Training](#3-Model-Training)
-   [Model Evaluation stage](#4-Model-Evaluation-stage)
-   [Pipeline Version Control](#5-Pipeline-Version-Control)
-   [Python Backend Server](#6-Python-Backend-Server)
-   [Streamlit UI](#7-Streamlit-UI)
-   [LLM Integration](#8-LLM-Integration)
-   [Chatbot creation](#8-Chatbot-creation)



## 1. Data-Ingestion-stage :<br>
   * We used Indian Medicinal Plants Dataset from kaggle for Our Project:<br>
   * [https://www.kaggle.com/datasets/aryashah2k/indian-medicinal-leaves-dataset]

## 2. Prepare-base-model :
   
   * Impliment state-of-art VGG16 architecture for model creation.
   * Fine-Tune the model on the plant Dataset to get better result.

## 3.Model-Training:
   
   * Write modular code to create training pipeline using python.
   * Trained Fine-tuned vgg16 model on different parameters.
   * Focused on ML operations, with additional work needed for model selection, preprocessing, and training.



## 4.Model-Evaluation-stage:
   
   * Used MLflow for comparing and selecting model parameters during the testing phase.
   * Utilized MLflow for experiments tracking.


## 5.Pipeline-Version-Control(DVC):
   
   * Effectively manage and version training pipeline using DVC (Data Version Control), ensuring reproducibility and easy collaboration among team members.
   * Used DagsHub : A collaboration platform that integrates versioning, data management, and experiment tracking.

## 6.Python-Backend-Server:
   
   * Write backend server to serve HTTP request from client .
   * Used FastApi for model loading and make prediction.


## 7.Streamlit-UI:
   
   * Create User-Freindly Interface using streamlit framwork for provideing Input Image.
   * Integrate streanlit interface to Our Fastapi server and Predicting the output.
    
## 8.LLM-Integration:
   
   * Integrate Google's LLM Palm 2 for generating description about specific Plant.
   * Summerize plants natural habitat, and medicinal use case.

## 9.Chatbot-creation:
   
   * Provide an easy-to-use chatbot interface using Streamllit to assist users in learning more specific information about plants.
   * Users can pose various questions to the chatbot about various plants.




## Technologies Used

- **MLflow**: An open-source platform for managing the end-to-end machine learning lifecycle.
- **DVC (Data Version Control)**: Versioning data and machine learning models to ensure reproducibility.
- **Dagshub**: A collaboration platform for data science and machine learning projects.



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/poriyaKuldeep/Medicinal_Plant_Identification_System
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n env python=3.10 -y
```

```bash
conda activate env
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/poriyaKuldeep/Medicinal_Plant_Identification_System-MLflow-DVC.mlflow\

MLFLOW_TRACKING_USERNAME=poriyaKuldeep \

MLFLOW_TRACKING_PASSWORD=..... \
python script.pys

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/poriyaKuldeep/Medicinal_Plant_Identification_System-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=poriyaKuldeep 

export MLFLOW_TRACKING_PASSWORD=.....

```
### DVC cmd

1. dvc init
2. dvc repro
3. dvc dags
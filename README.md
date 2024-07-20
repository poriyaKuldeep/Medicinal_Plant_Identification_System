# Medicinal_Plant_Identification_System_MLflow-DVC


## Objective :
The primary objective of our Medicinal Plant Identification System is to provide a reliable and efficient tool for botanists, herbalists, researchers, and enthusiasts to quickly identify medicinal plants based on their visual attributes. This system aims to bridge the gap between traditional knowledge of plant identification and modern technological advancements, making it easier for users to access information about the medicinal properties of plants.


### Components:
1. **User**: Uploads a photo via the web application.
2. **Web Application**: created web application using Streamlit and FastAPI for instant plant predictions.
3. **Model**: Uses a VGG16 model trained on a plant dataset to predict diffrent Plants.
4. **MLflow**: Used for comparing and choosing model parameters during the testing phase.
5. **DVC**: Employed for data and model versioning.


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
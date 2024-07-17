# Medicinal_Plant_Identification_System_MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

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
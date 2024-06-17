# Covid-Image-Classification
Chest X-ray radiographic images has been a initial screening tool for diagnosing the suspected COVID-19 patients from the non-infected patients. This helps the expert doctors to identify the suspected patients. This study has been performed to develop the image classification pipeline for automated diagnosis of COVID-19 infected patients from the normal patients using the chest X-ray images.
## Machine setup
### create a conda environment
This command will install the required packeges necessary for training the model.
```
conda env create -f environemnt.yml
```

### Move to the conda environment
```
conda activate environment_name
```

### Run the script
Move to the architecture (VGG16 or VGG19) folder you wish to run
```
python script.py
```
## Data Collection
Data for the study has been collected from the different open access repositories.
1. https://www.kaggle.com/tawsifurrahman/covid19-radiography-database
2. https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
3. https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge

# COVID_Image_Classification
Chest X-ray radiographic images has been a initial screening tool for diagnosing the suspected COVID-19 patients from the non-infected patients.
This study has been performed to develop the image classification pipeline for automated diagnosis of COVID-19 infected patients from the normal patients using the chest X-ray images.

clone the github repository
```
git clone https://github.com/tarun3991/Covid-Image-Classification.git
```

## Steps to follow for machine setup and running the model
### Step 1: Create a conda environment using the yml file
This command will install the required packeges necessary for training the model.
```
conda env create -f env.yml
```
Note 1: Conda version used is 23.7.4.

Note 2: You can remane the environment name accordingly by editing the name and prefix in yml file.


### Step 2: Activate the conda environment
Once the conda environment is created, you can activate the environment by using the command below
```
conda activate environment_name
```
### Step 3: Run the script
Keep the dataset and codes in same folder. While running the codes, keep track of the paths of train and test directory in your code.
Here, we have given the test dataset while you can train the model with large dataset/custom dataset by downloading data from the links below in Data Collection
```
python name_of_the_script.py
```
Note 3: This code is developed for gpu. If you want to test the codes on cpu, edit the model.py file by removing the lines 5-8.  

Note 4: Modify the hyperparameters accordingly.

Note 5: Create directories **vgg16_models** for storing the saved models, **train_log** and **tensorboard_logs** for storing the csvlogger and tensorboard data.

Note 6: You can write individual scipts for generating the plots (ROC Curve and Confusion matrix).
 
## Data Collection
Data for the study has been collected from the different open access repositories.
1. https://www.kaggle.com/tawsifurrahman/covid19-radiography-database
2. https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
3. https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge

## Checklist for Artificial Intelligence in Medical Imaging (CLAIM Checklist)
This study has been in accordance with the CLAIM checklist. Generate the report by running the claim.py file.
```
python claim.py
```
## Reference
Mongan J, Moy L, Kahn CE Jr. Checklist for Artificial Intelligence in Medical Imaging (CLAIM): a guide for authors and reviewers. Radiol Artif Intell 2020; 2(2). 
https://doi.org/10.1148/ryai.2020200029 


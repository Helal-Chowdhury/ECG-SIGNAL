## Title: ECG Signal Classification

<p align="center">
<img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/signal1.jpg" width="700" height="340">
 </p>

### Introduction
In this project, Five different types of ECG beats are taken into account to classify:
 - Non-ecotic beats
 - Supraventricular ectopic beats
 - Ventricular ectopic beats
 - Fusion beats
 - Unknown beats

I am not expert in analyzing __ECG__ signal but have background in signal processing. So, my basic intiution regarding the  __ECG__ that ([Source](https://en.wikipedia.org/wiki/Electrocardiography)) a heart beat is segmented into
__P,Q,R,S,T__. and its intervals. The duration and the magnitude of those segments may be used to identify the type of __ECG__ beat as mentioned before.
<p align="center">
<img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/SinusRhythmLabels.svg.png" width="550" height="350">
 </p>

### How to create project environment and install packages:

Create Environment and Installation Packages

```bash
conda create --name <environment name> python=3.8
conda activate <environment name>
pip install -r requirements.txt
```
In case you have difficulties with installation of specific version of tensorflow and other package use the following commands to install:
```bash
pip install tensorflow==x.x.x --no-cache-dir
pip install <package name>==x.x.x  --no-cache-dir
```

Due to push limit in Github (A single filesize should be less than 100MB).
However, To run ECG.py you need 'mitbih_test.csv. Visit the [Link](https://www.kaggle.com/datasets/shayanfazeli/heartbeat) to download the mitbih_test.csv' file.


## RUN the App
To run the app, Go to __FRONEND__ folder and shoot this command:              
```bash
streamlit run ECG.py
```


## From Web UI 
 - Select Signal

This will generate the prediction and the underlying plots for visualisation


|  	| 	| 	|
|---	|---	|---	|
|<img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig1.png" width="300" height="150"> 	| <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/Signal_v2.png" width="400" height="200">  	|  <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig3.png" width="400" height="200"> 	|

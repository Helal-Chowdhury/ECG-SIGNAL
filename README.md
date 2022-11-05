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
This project is divided into three parts:
 - Image Collections (IMAGE-COLLECTION_AND_SPLITFOLDER)
 - Training (BACKEND)
 - Deployment (FRONEND)


1. install packages
```bash
conda env update -n <yourenvname> --file environment.yaml
```
Some packages have pip dependency. In this case, use  pip to install the packages.
```bash
pip install <package name>
```
## RUN the App
To run the app, Go to __FRONEND__ folder and shoot this command:              
```bash
streamlit run Resnet.py
```


## From Web UI 
 - Select Signal

This will generate the prediction and the underlying plots for visualisation


|  	| 	| 	|
|---	|---	|---	|
|<img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig1.png" width="300" height="150"> 	| <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/Signal_v2.png" width="300" height="150">  	|  <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig3.png" width="300" height="150"> 	|

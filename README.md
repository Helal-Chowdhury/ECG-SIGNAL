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

## How to create project environment and install packages:

1. Create environment
```bash
conda create -n <yourenvname> python=x.x anaconda
```

2.activate environment
```bash
conda activate <yourenvname>
```


2 install packages

```bash
conda env update -n <yourenvname> --file environment.yaml
```
Some packages have pip dependency. In this case, use  pip to install the packages.
```bash
pip install <package name>
```


## How to Use the Project
The work flow will flow as: collect your images using _DATA_,train your model using _Backend_ and deploy using _Frontend_folder_.
Note: provide the output folder path in _IMAGE while you traing your model in the _BACKEND_FOLDER_

RUN the App
To run the app, Go to _FRONTENDFOLDER_ and shoot this command:              

```bash
streamlit run Resnet.py
```
Streamlit generate Web UI

## From web UI 
 -select model
 -upload image
 - click the Predict button to predict
 
Note: in free subscription of Github does not support to push a single filesize of more than 100 Mbyte. However, train the model and save it and test with Densene109 in your machine. Implementation of single model and multi models both are provided in _Frontend_Folder_ 



|  	| 	| 	|
|---	|---	|---	|
|<img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig1.png" width="300" height="150"> 	| <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/Signal_v2.png" width="300" height="150">  	|  <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig3.png" width="300" height="150"> 	|

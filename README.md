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

I am not expert in analyzing __ECG__ signal but have background in signal processing. So, my basic intiution regarding __ECG__ heart beat [see the Figure below, source] is segmented into
__P,Q,R,S,T__. and its intervals. The duration and the magnitude of those segments may be used to identify the type of __ECG__ beat as mentioned before.
<p align="center">
<img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/SinusRhythmLabels.svg.png" width="550" height="350">
 </p>

A template has been made for any general purpose Image Classifications problems. The project folder consists of three folders: _IMAGE_COLLECTION_FOLDERS_, _BACKEND, and _FRONEND_. For demonstration, I choose  five fruit classes. However, you can choose any class of images by using Hugging face image collection API. I use Pytorch, and Streamlit for training and deployment. Pre-trained Models: Resnet18 and Densnet109 models. However, you can find tons of pre-trained image classification models from 




|  	| 	| 	|
|---	|---	|---	|
|<img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig1.png" width="300" height="150"> 	| <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/Signal_v2.png" width="300" height="150">  	|  <img src="https://github.com/Helal-Chowdhury/ECG-SIGNAL/blob/main/sig3.png" width="300" height="150"> 	|

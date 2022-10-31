# Author: Helal Chowdhury
# Version: 1

import tensorflow as tf
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from sklearn.utils import class_weight, resample
import plotly.express as px
from keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout, BatchNormalization
from keras.models import Sequential
from keras.callbacks import EarlyStopping, ModelCheckpoint
import streamlit as st

# Setting Manual Seed for Recreation of results
#torch.manual_seed(42)
#np.random.seed(0)

st.header("ECG Heartbeat Classification")
st.info("ECG signal re-sampled to the sampling frequency of 125Hz as the input.")
url = "https://arxiv.org/pdf/1805.00794.pdf"
st.write("Check out this paper for details: [link](%s)" % url)
st.subheader("Selected Input Signal"  )
st.info("ECG signal: xlabel=Samples, ylabel= Normalized Value")

#st.subheader("Extracted ECG Beat of choosen class")
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>""", unsafe_allow_html=True)

#-----------------------------------

cnn = tf.keras.models.load_model('./ecg_model2.h5')
cnn.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

#cnn.summary()
#--------------------------------

def highlight_max(data, color="yellow"):
    """highlight the maximum in a Series or DataFrame"""
    attr = "background-color: {}".format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
    	
        is_max = data == data.max()

        return [attr if v else "" for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(
            np.where(is_max, attr, ""), index=data.index, columns=data.columns
        )

#----------------
def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = "red" if val < 0 else "black"
    return "color: %s" % color


def subheader(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:14px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)


# Read test fle
test_df = pd.read_csv('mitbih_test.csv',header=None)

# Group into individual class
df_0 = test_df[test_df[187]==0.0]#.sample(n=16000, random_state=3350)
df_1 = test_df[test_df[187]==1.0]
df_2 = test_df[test_df[187]==2.0]
df_3 = test_df[test_df[187]==3.0]
df_4 = test_df[test_df[187]==4.0]
rand_state=num=np.random.randint(100, size=1)

sample_n=df_0.sample(1)
sample_s=df_1.sample(1)
sample_v=df_2.sample(1)
sample_f=df_3.sample(1)
sample_q=df_4.sample(1)

# Select the class name

signal_name=st.sidebar.selectbox("Select Signal",( "Non-ecotic beats-0","Supraventricular ectopic beats-1","Ventricular ectopic beats-2", "Fusion beats-3","Unknown beats-4") )                                

# Selected signal will return 187 samples
def Choose_signal(signal_name):
	rand_state=np.random.randint(100, size=1)
	#st.write("Random state......",rand_state)
	df_0 = test_df[test_df[187]==0.0]#.sample(n=16000, random_state=rand_state)
	df_1 = test_df[test_df[187]==1.0]
	df_2 = test_df[test_df[187]==2.0]
	df_3 = test_df[test_df[187]==3.0]
	df_4 = test_df[test_df[187]==4.0]
	
	sample_n=df_0.sample(1)
	sample_s=df_1.sample(1)
	sample_v=df_2.sample(1)
	sample_f=df_3.sample(1)
	sample_q=df_4.sample(1)

	if signal_name=="Non-ecotic beats-0":
		#sample_n=df_0.sample(1,random_state=33)
		return(df_0.sample(1).iloc[0,:186])

	elif signal_name=="Supraventricular ectopic beats-1":
		return(df_1.sample(1).iloc[0,:186])
		#df_1.sample(1)
		#px.line(df_1.sample(1).iloc[0,:186] )
	elif signal_name=="Ventricular ectopic beats-2":
		return(df_2.sample(1).iloc[0,:186])
		#signal=df_2.sample(1)
		#px.line(df_2.sample(1).iloc[0,:186] )
	elif signal_name=="Fusion beats-3":
		return(df_3.sample(1).iloc[0,:186])
		#signal=df_3.sample(1)
		#px.line(df_3.sample(1).iloc[0,:186] )
	elif signal_name=="Unknown beats-4":
		return(df_4.sample(1).iloc[0,:186])
		#signal=df_4.sample(1)
		#px.line(df_4.sample(1).iloc[0,:186] )
	else:
		#st.write(" No signal to display"
		
		return print("Please Choose Signal")
		

# function call and plot
signal=Choose_signal(signal_name)
#st.write("Samples of bit",len(signal))
st.line_chart(signal)

# inference
signal=signal.to_numpy()
signal=signal.reshape(-1,1)
signal=signal.reshape(signal.shape[1],len(signal),signal.shape[1])
y_predict = cnn.predict(signal)
y_predict = np.around(y_predict, 2)


st.subheader("Selected signal Classified as"  )
#st.header("Identified as:{}".format(Classes1[ind])   )
# Plotting stuff in streamlit

df= pd.DataFrame(y_predict, columns=[ "Non-ecotic beats-0","Supraventricular ectopic beats-1","Ventricular ectopic beats-2", "Fusion beats-3","Unknown beats-4"])
#st.write("Selected Model: ",model_name)
    
st.dataframe(
    df.style.applymap(color_negative_red).apply(highlight_max, color="darkorange", axis=1).format("{:.2%}")
    )
#----------------------------------------
Classes1=["Non-ecotic beats-0","Supraventricular ectopic beats-1","Ventricular ectopic beats-2", "Fusion beats-3","Unknown beats-4"]

y_predict=y_predict.flatten()
li=y_predict.tolist()
ind=int(li.index(max(li)))

st.subheader("Identified as:{}".format(Classes1[ind])   )

def iterate_columns(cols, signal_name):
    for col in cols:
        if signal_name=="Non-ecotic beats-0":
            x=df_0.sample(1).iloc[0,:186]
            col.plot(x, color='blue')
        elif signal_name=="Supraventricular ectopic beats-1":
            x=df_1.sample(1).iloc[0,:186]
            col.plot(x, color='green')
        elif signal_name=="Ventricular ectopic beats-2":
            x=df_2.sample(1).iloc[0,:186]
            col.plot(x, color='red')
        elif signal_name=="Fusion beats-3":
            x=df_2.sample(1).iloc[0,:186]
            col.plot(x, color='orange')
        elif signal_name=="Unknown beats-4":
            x=df_2.sample(1).iloc[0,:186]
            col.plot(x, color='black')
	 #elif signal_name=="Supraventricular ectopic beats-1":
	     #x=df_1.sample(1).iloc[0,:186]
	 	
	#elif


fig, axes = plt.subplots(2, 3)
for row in axes:

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    iterate_columns(row, signal_name)
st.subheader("Visualize Six random Samples of :{}".format(Classes1[ind])   )
#st.subheader("Composit Signal"  )
st.pyplot(fig)

#----------------------------------

fig2, ax = plt.subplots(1, sharex=True, sharey=True)
fig2.set_size_inches(10,5)
def composite_plot(signal_name):

	rand_state=np.random.randint(100, size=1)
	st.write("Random state......",rand_state)
	df_0 = test_df[test_df[187]==0.0]#.sample(n=16000, random_state=rand_state)
	df_1 = test_df[test_df[187]==1.0]
	df_2 = test_df[test_df[187]==2.0]
	df_3 = test_df[test_df[187]==3.0]
	df_4 = test_df[test_df[187]==4.0]
	

	sample_n=df_0.sample(1)
	sample_s=df_1.sample(1)
	sample_v=df_2.sample(1)
	sample_f=df_3.sample(1)
	sample_q=df_4.sample(1)


	for i in range(0,2):
		if signal_name=="Non-ecotic beats-0":
			random_sample=df_0.sample(1).iloc[0,:186]
			plt.plot(random_sample)
		elif signal_name=="Supraventricular ectopic beats-1":
        		random_sample=df_1.sample(1).iloc[0,:186]
		elif signal_name=="Ventricular ectopic beats-2":
        		random_sample=df_2.sample(1).iloc[0,:186]
		elif signal_name=="Fusion beats-3":
        		random_sample=df_3.sample(1).iloc[0,:186]
		elif signal_name=="Unknown beats-4":
        		random_sample=df_4.sample(1).iloc[0,:186]
        	

st.subheader("Visualize 10 random Samples of {} in the single-frame".format(Classes1[ind])   )
#---------------------------
def label_0():
	for i in range(0,10):
		random_sample=df_0.sample(1).iloc[0,:186]
		plt.plot(random_sample)
	st.pyplot(fig2)

def label_1():
	for i in range(0,10):
		random_sample=df_1.sample(1).iloc[0,:186]
		plt.plot(random_sample)
	st.pyplot(fig2)

def label_2():
	for i in range(0,10):
		random_sample=df_2.sample(1).iloc[0,:186]
		plt.plot(random_sample)
	st.pyplot(fig2)

def label_3():
	for i in range(0,10):
		random_sample=df_3.sample(1).iloc[0,:186]
		plt.plot(random_sample)
	st.pyplot(fig2)
def label_4():
	for i in range(0,10):
		random_sample=df_4.sample(1).iloc[0,:186]
		plt.plot(random_sample)
	st.pyplot(fig2)

if signal_name=="Non-ecotic beats-0":
	label_0()
elif signal_name=="Supraventricular ectopic beats-1":
	label_1()
elif signal_name=="Ventricular ectopic beats-2":
	label_2()
elif signal_name=="Fusion beats-3":
	label_3()
elif signal_name=="Unknown beats-4":
	label_4()
	


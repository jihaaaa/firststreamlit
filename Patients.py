#%%writefile Patients.py
import streamlit as st
import numpy as np
import pandas as pd
import time

from PIL import Image

press=st.sidebar.header("You may choose any selection below for further information")
press=st.sidebar.selectbox('Page Number',['Page 1','Page 2','Page 3','Page 4','Page 5','Page 6','Done'])

if press=='Page 1':
    st.title("MEDICAL APPOINTMENT NO SHOWS")
    st.subheader("Data Source: JoniHoppen from Kaggle")
    st.info("Hello! I'm Najihah.")
    st.info("I utilized this dataset for my assignment to analyze whether or not a patient is going to attended for the medical appointment.")

elif press=='Page 2':
    image = Image.open('appointment.png')
    st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.title("PATIENTS' RECORD")
    
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
   
        latest_iteration.text(f'Processing... {i+1}')
        bar.progress(i + 1)
        time.sleep(0.05)
        
    record=pd.read_csv("C:/Users/user10/Desktop/Patient Appointment.csv")
    remove=["PatientId","ScheduledDay","AppointmentDay"]
    record.drop(remove, inplace=True, axis=1)
    record.rename(columns={'Hipertension':'Hypertension', 'Handcap':'Handicapped','SMS_received':'Notification(SMS)','No-show':'Attended'},inplace=True)
    record.drop(record[record['Age'] < 18].index, inplace = True)
    change = {'No':0, 'Yes': 1}
    record = record.replace({'Attended': change})
    record.head()
    st.write(record)
    
elif press=='Page 3':
    st.title("NUMBER OF PATIENTS RECORDED")
    
    col1,col2=st.columns(2)
    col1.metric("Male","25206")
    col2.metric("Female","57941")

    col3,col4=st.columns(2)
    col3.metric("Attended","4790")
    col4.metric("Attended","11532")

    col5,col6=st.columns(2)
    col5.metric("Unattended","20416")
    col6.metric("Unattended","46409")
    
    image = Image.open('graph1.png')
    st.image(image, caption=None, width=700, use_column_width=None, clamp=False, channels="white", output_format="auto")
    
elif press=='Page 4':
    st.title('CORRELATION INFO')
    
    col1,col2,col3=st.columns(3)
    col1.metric("Age Factor","-0.06")
    col2.metric("Scholarship","0.02")
    col3.metric("Hypertension","0.03")
    
    col4,col5,col6=st.columns(3)
    col4.metric("Diabetes","-0.02")
    col5.metric("Alcoholism","-0.00")
    col6.metric("Handicapped","-0.00")
                
    col7,col8=st.columns(2)
    col7.metric("Notification","0.13")   
    
elif press=='Page 5':
    st.header('Scholarship vs Attendance')
    image = Image.open('C:/Users/user10/Desktop/graph2.png')
    st.image(image, caption=None, width=500, use_column_width=None, clamp=False, channels="white", output_format="auto")
    st.subheader('Scholarship')
    a,b=st.columns(2)
    a.metric("Attended","1836")
    b.metric("Unattended","5963")
    st.subheader('Non-Scholarship')
    c,d=st.columns(2)
    c.metric("Attended","14486")
    d.metric("Unattended","60862")
    
    st.header('Notification vs Attendance')
    image = Image.open('graph5.png')
    st.image(image, caption=None, width=500, use_column_width=None, clamp=False, channels="white", output_format="auto")
    st.subheader('Received')
    e,f=st.columns(2)
    e.metric("Attended","7359")
    f.metric("Unattended","20102")
    st.subheader('Not Received')
    g,h=st.columns(2)
    g.metric("Attended","8963")
    h.metric("Unattended","46723")
    
elif press=='Page 6':
    st.title('SUMMARY')
    st.write('The total of female patients are higher compared to male. However, the percentage of attending to the appointment are mutual for both genders which are 19%.')
    st.write('There are 75348 patients who did not received scholarship and 7799 receiver. 76% of the receiver not attended the appointment. 80% of patients who not received the scholar had not attended to the appointment.')
    st.write('73% of patients who received the notification has not attended to the appointment. Meanwhile, 84% did not attended from the group who did not received any notification.')
    st.write("There are no correlation of patients' attendance with any factor including the age, health condition, scholarship, and notification." )
    st.write("By using logistic regression, this data provided 80% accuracy score for the attendance results.")
    
    st.title('SUGGESTION')
    st.write('To increase the amount of patients to attend to the appointment, maybe the hospital could offer better packages for the scholarship receivers. Plus, do some review for the background check for the patients who did not received scholarship. Hence, they could be offered one in the future. Other than that, the notification should be sent to all patients so that it can increased the total numbers of patients attended.')
else:
    st.title("THANK YOU FOR VISITING!")
    st.subheader("Your recommendation is highly appreciated.")

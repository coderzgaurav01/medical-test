import streamlit as st
import pickle
from streamlit_option_menu import option_menu

#change name and logo
st.set_page_config(page_title="Diseases prediction")

#hiding streamlit add-ons
hide_st_style="""
            <style>
            #Main Menu {visibility:hidden;}
            footer {visibility:hidden;}
            header {visibility:hidden;}
            </style>
        """
        
st.markdown(hide_st_style,unsafe_allow_html=True)


#Adding Background images
background_image_url="https://drive.google.com/file/d/1eURxMW7E8d589S__43twXQRoC2peEqLX/view?usp=drive_link"
page_bg_img = f"""
            <style>
            [data-testid="stAppViewContainer]{{
            background-image: url({background_image_url});
            background-size:cover;
            background-position:center;
            background-repeat:no-repeat;
            background-attachment:fixed;
           }}
           [data-testid="stAppViewContainer"]::before{{
               content:"";
               position:absolute;
               top:0;
               left:0;
               width:100%;
               height:100%;
               background-color: rgba(10,10,10,10);
           }}
           </style>
            """
            
st.markdown(page_bg_img,unsafe_allow_html=True)

#Load The model
models={
    'lung_cancer':pickle.load(open('model/lung_cancer_model.sav','rb')),
    'parkinsons':pickle.load(open('model/parkinson_model.sav','rb')),
    'diabetes':pickle.load(open('model/diabetes_trained_model.sav','rb')),
    'heart':pickle.load(open('model/Heart_diseases_model.sav','rb'))
}

#create a drop down menu
selected= st.selectbox(
    'Select a diseases to predict',
    ['Lung Cancer Prediction',
     'Parkinson Diseases Prediction',
     'Diabetes Prediction',
     'Heart diseases prediction'
     
    ]
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label,key=key,help=tooltip)
    elif type =="number":
        return st.number_input(label,key=key,help=tooltip,step=1)
    
#Lung Cancer Prediction Page
if selected=="Lung Cancer Prediction":
    st.title('Lung Cancer')
    st.write('Enter The following detail to predict lung cancer:')
    
    GENDER=display_input('Gender (1=Male;0=Female)','Enter Gender Of the person','GENDER','number')
    AGE=display_input('Age','Enter Age of a person','AGE','number')
    SMOKING=display_input('Smoking (1=Yes; 0=No)','Enter If the person smokes','SMOKING','number')
    YELLOW_FINGERS=display_input('Yellow Fingers (1=yes; 0=No)','Enter if the person has yellow fingers','YELLOW_FINGERS','number')
    ANXIETY=display_input('Anxiety(1=Yes; 0=No)','Enter if the person has anxiety','ANXIETY','number')
    PEER_PRESSURE=display_input('Peer Pressure (1=yes; 0=No)','Enter if the person has peer pressure','PEER_PRESSURE','number')
    CHRONIC_DISEASE=display_input('Chronic Diseases (1=yes; 0=No)','Enter if the person has a chronic diseases','CHRONIC_DISEASE','number')
    FATIGUE=display_input('Fatigue(1 = Yes; 0=NO)','Enter if the person is fatigue','FATIGUE','number')
    ALLERGY=display_input('Allergy(1=Yes;0=No)','Enter if the person experiences Allergy','ALLERGY','number')
    WHEEZING=display_input('Wheezing (1=Yes;0=No)','Enter if the person experiences Wheezing','WHEEZING','number')
    ALCOHOL_CONSUMING=display_input('Alcohol Consumption (1=Yes; 0=NO)','Enter if the person consumes alcohol','ALCOHOL_CONSUMING','number')
    COUGHING=display_input('Coughing (1=Yes; 0=No)','Enter if person suffers coughing','COUGHING','number')
    SHORTNESS_OF_BREATH=display_input('Shortness of Breath (1=Yes; 0=No)','Enter if person suffer shortness of breath','SHORTNESS_OF_BREATH','number')
    SWALLOWING_DIFFICULTY=display_input('Swallowing Difficulty (1=Yes;0=No)','Enter if person suffer swallowing difficulty','SWALLOWING_DIFFICULTY','number')
    CHEST_PAIN = display_input('Chest pain (1=Yes;0=No)','Enter if person suffer chest pain','CHEST_PAIN','number')
    
    lung_diagnosis=''
    if st.button("Lung Cancer Test Result"):
        lungs_prediction= models['lung_cancer'].predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])
        lung_diagnosis = "The Person has Lung Cancer diseases " if lungs_prediction[0]==1 else "The person does not have lung cancer diseases"
        st.success(lung_diagnosis)

#Parkinson's Diseases Prediction page
if selected=="Parkinson Diseases Prediction":
    st.title('Parkinson Diseases')
    st.write('Enter The following detail to predict Parkinsons Diseases')
    
    fo=display_input('MDVP:Fo(Hz)','Enter MDVP:Fo(Hz) value','fo','number')
    fhi=display_input('MDVP:Fhi(Hz)','Enter MDVP:Fhi(Hz) value','fhi','number')
    flo=display_input('MDVP:Flo(Hz)','Enter MDVP:Flo(Hz) value','flo','number')
    jitter=display_input('MDVP:Jitter(%)','Enter MDVP:Jitter(%)','jitter','number')
    jitter_abs=display_input('MDVP:Jitter(Abs)','Enter MDVP:Jitter(Abs) value','jitter_abs','number')
    rap=display_input('MDVP:RAP','Enter MDVP:RAP value','rap','number')
    ppq=display_input('MDVP:PPQ','Enter MDVP:PPQ value','ppq','number')
    ddp=display_input('Jitter:DDP','Enter Jitter:DDP value','ddp','number')
    shimmer=display_input('MDVP:Shimmer','Enter MDVP:Shimmer value','shimmer','number')
    shimmer_db=display_input('MDVP:Shimmer(dB)','Enter MDVP:Shimmer(dB) value','shimmer_db','number')
    apq3=display_input('Shimmer:APQ3','Enter Shimmer:APQ3 value','apq3','number')
    apq5=display_input('Shimmer:APQ5','Enter Shimmer:APQ5 value','apq5','number')
    apq=display_input('MDVP:APQ','Enter MDVP:APQ value','apq','number')
    dda=display_input('Shimmer:DDA','Enter Shimmer:DDA value','dda','number')
    NHR=display_input('NHR','Enter NHR value','NHR','number')
    HNR=display_input('HNR','Enter HNR value','HNR','number')
    RPDE=display_input('RPDE','Enter RPDE value','RPDE','number')
    DFA=display_input('DFA','Enter DFA value','DFA','number')
    spread1=display_input('spread1','Enter spread1 value','spread1','number')
    spread2=display_input('spread2','Enter spread2 value','spread2','number')
    D2=display_input('D2','Enter D2 value','D2','number')
    PPE=display_input('PPE','Enter PPE value','PPE','number')
    
    parkinsons_diagnosis =''
    if st.button("Parkinsons Diseases Test Result"):
        parkinsons_prediction=models['parkinsons'].predict([[fo,fhi,flo,jitter,jitter_abs,rap,ppq,ddp,shimmer,shimmer_db,apq3,apq5,apq,dda,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        parkinsons_diagnosis = "The Person has Parkinsons diseases" if parkinsons_prediction[0]==1 else "The person does not have parkinson diseases"
        st.success(parkinsons_diagnosis)
        
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")
    st.write("Enter The folloeing detail to predict Diabeties")
    
    Pregnancies=display_input("Pregnancies","Enter your Pregnency detail","Pregnancies",'number')
    Glucose=display_input("Glucose","Enter Glucose Level",'Glucose','number')
    BloodPressure=display_input("BloodPressure",'Enter Blood Pressure level','BloodPressure','number')
    SkinThickness=display_input("SkinThickness",'Enter Skin thickness detail',"SkinThickness",'number')
    Insulin=display_input('Insulin','Enter Insulin level','Insulin','number')
    BMI=display_input('BMI',"Enter Bmi level",'BMI','number')
    DiabetesPedigreeFunction=display_input('DiabetesPedigreeFunction','Enter DiabetesPedigreeFunction detail','DiabetesPedigreeFunction','number')
    Age=display_input('Age',"Enter Age of the Patient",'Age','number')
    
    diabetes_diagnosis=''
    if st.button("Diabetes test Result"):
        diabetes_prediction=models['diabetes'].predict([[Pregnancies,Glucose	,BloodPressure,	SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        diabetes_diagnosis="The Person is Diabetic" if diabetes_prediction[0]==1 else "The Person is not Diabetic"
        st.success(diabetes_diagnosis)
        
#Heart Diseases Prediction
if selected=='Heart diseases prediction':
    st.title('Heart Diseases prediction')
    st.write("Enter the following detail to predict heart infection")
    
    age=display_input('Age','Enter age of patient','age','number')
    sex=display_input('Gender(1=Male||0=female)','Enter gender of patient','sex','number')
    cp=display_input('Cp','Enter cp of patient','cp','number')
    trestbps=display_input('Trestbps','Enter Trestbps of patient','trestbps','number')
    chol=display_input('Chol','Enter cholestrol level of patient','chol','number')
    fbs=display_input('fbs(1=yes|0=No)','Enter Fbs of patient','fbs','number')
    restecg=display_input('restecg(1=yes|0=No)',"Enter restecg of patient",'restecg','number')
    thalach=display_input('thalach',"enter thalach of patient",'thalach','number')
    exang=display_input('exang1=yes|0=No)','Enter exang of patient','exang','number')
    oldpeak=display_input('oldpeak','Enter oldpeak of Patient','oldpeak','number')
    slope=display_input('slope','Enter slope of patient','slope','number')
    ca=display_input('ca','Enter ca of paient','ca','number')
    thal=display_input('thal','Enter thal of patient ','thal','number')
    
    heart_diagnosis=''
    if st.button('Heart Test Result'):
        heart_prediction=models['heart'].predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        heart_diagnosis="The Person is Infected from Heart diseases" if heart_prediction[0]==1 else "The person is not infected"
        st.success(heart_diagnosis)
#To run this app use command python -m streamlit run app.py

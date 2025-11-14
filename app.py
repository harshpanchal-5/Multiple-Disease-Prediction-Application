import os
import pickle
import streamlit as stl
from streamlit_option_menu import option_menu

#Loading the saved Model

diabeties_model= pickle.load(open('diabetes.sav','rb'))
heart_model=pickle.load(open('heart.sav','rb'))
parkinson_model=pickle.load(open('parkinson.sav','rb'))


#Design Sidebar Navigator

with stl.sidebar:
    selected = option_menu('Machine Learning Hospital',
                           ['Diabeties Predection', 'Heart Predection',
                            'Cancer Predection','Parkinson Predection'],
                            icons=['capsule','heart','activity','asterisk'],
                            default_index=0 )
    
if (selected == 'Diabeties Predection'):
    stl.title('Diabeties Predection using AIML')
    # getting the input data from the user
    col1, col2, col3 = stl.columns(3)

    with col1:
        Pregnancies = stl.text_input('Number of Pregnancies')

    with col2:
        Glucose = stl.text_input('Glucose Level')

    with col3:
        BloodPressure = stl.text_input('Blood Pressure value')

    with col1:
        SkinThickness = stl.text_input('Skin Thickness value')

    with col2:
        Insulin = stl.text_input('Insulin Level')

    with col3:
        BMI = stl.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = stl.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = stl.text_input('Age of the Person')

    # codeing For predection
    Diabetes_diagnosis= ''
    if stl.button('Diabetes Test Result: '):
        
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        Diabetes_prediction = diabeties_model.predict([user_input])
        # Diabetes_prediction= diabeties_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,Age]])

        if (Diabetes_prediction[0]==1):
            Diabetes_diagnosis= "The Person is Diabetes..."
        else:
            Diabetes_diagnosis= "The Person is Not Diabetes..."

    stl.success(Diabetes_diagnosis)




if (selected == 'Heart Predection'):
    stl.title('Heart Predection using AIML')


    col1, col2, col3 = stl.columns(3)

    with col1:
        age = stl.text_input('Age')

    with col2:
        sex = stl.text_input('Sex')

    with col3:
        cp = stl.text_input('Chestl Pain types')

    with col1:
        trestbps = stl.text_input('Resting Blood Pressure')

    with col2:
        chol = stl.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = stl.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = stl.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = stl.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = stl.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = stl.text_input('ST depression induced by exercise')

    with col2:
        slope = stl.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = stl.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = stl.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if stl.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    stl.success(heart_diagnosis)



    
if (selected == 'Parkinson Predection'):
    stl.title('Parkinson Predection using AIML')
    col1, col2, col3, col4, col5 = stl.columns(5)

    with col1:
        fo = stl.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = stl.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = stl.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = stl.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = stl.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = stl.text_input('MDVP:RAP')

    with col2:
        PPQ = stl.text_input('MDVP:PPQ')

    with col3:
        DDP = stl.text_input('Jitter:DDP')

    with col4:
        Shimmer = stl.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = stl.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = stl.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = stl.text_input('Shimmer:APQ5')

    with col3:
        APQ = stl.text_input('MDVP:APQ')

    with col4:
        DDA = stl.text_input('Shimmer:DDA')

    with col5:
        NHR = stl.text_input('NHR')

    with col1:
        HNR = stl.text_input('HNR')

    with col2:
        RPDE = stl.text_input('RPDE')

    with col3:
        DFA = stl.text_input('DFA')

    with col4:
        spread1 = stl.text_input('spread1')

    with col5:
        spread2 = stl.text_input('spread2')

    with col1:
        D2 = stl.text_input('D2')

    with col2:
        PPE = stl.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if stl.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinson_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    stl.success(parkinsons_diagnosis)



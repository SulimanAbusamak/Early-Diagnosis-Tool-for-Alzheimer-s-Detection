#Installing Streamlit
#pip install streamlit

#to run webapp,  streamlit run webapp.py   in terminal




import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_icon=":brain:",page_title="Alzheimer's tool",layout="wide")

model = joblib.load("model.pkl")


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def predic(Age, EducationLevel,FamilyHistoryAlzheimers, MMSE, FunctionalAssessment,
       MemoryComplaints, BehavioralProblems, ADL, Confusion,
       Disorientation, PersonalityChanges, DifficultyCompletingTasks,
       Forgetfulness):
  inp = [Age, EducationLevel,FamilyHistoryAlzheimers, MMSE, FunctionalAssessment,
       MemoryComplaints, BehavioralProblems, ADL, Confusion,
       Disorientation, PersonalityChanges, DifficultyCompletingTasks,
       Forgetfulness]
  inp2array = np.asarray(inp)
  inp2reshaped = inp2array.reshape(1,-1)
  prediction = model.predict(inp2reshaped)

  if prediction[0] == 0:
    st.success("You Don't have from Alzheimer")
  else:
    st.error("There is a chance that you have Alzheimer")



def encodingYesNo(ans):
  if str(ans).lower()=="yes":
    return 1
  else:
    return 0




st.markdown("<h1 style='text-align: center;'>Early Diagnosis Tool for Alzheimer's Detection </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>this tool is used to recognize the initial symptoms of Alzheimer’s disease, which usually appear in the third or fourth stage out of the seven stages </h2>", unsafe_allow_html=True)
st.markdown("------")
col1, col2 = st.columns(2)
with col1:
  Age = st.number_input("Enter your age", min_value=1, max_value=120)
  MMSE = st.number_input("Enter your MMSE test result:",min_value=0.0, max_value=30.0,step=0.000000001, format="%.9f")
  ADL = st.number_input("Enter your ADL test result:",min_value=0.0, max_value=16.0,step=0.000000001, format="%.9f")
  FunctionalAssessment = st.number_input("Enter your Functional assessment test result:",min_value=0.0, max_value=10.0,step=0.000000001, format="%.9f")
  EducationLevel= encodingYesNo(st.select_slider("Enter your Education Level  from 0 to 3 (0 being having no education at all and 3 having high education level): ",[0,1,2,3]))
  FamilyHistoryAlzheimers = encodingYesNo(st.select_slider("Enter whether you have Family history of alzheimer",["No","Yes"]))
  MemoryComplaints = encodingYesNo(st.select_slider("Enter whether you have Memory Complaints",["No","Yes"]))
  BehavioralProblems = encodingYesNo(st.select_slider("Enter whether you have Behavioral Problems",["No","Yes"]))

with col2:
  Confusion= encodingYesNo(st.select_slider("Enter whether you have Confusion",["No","Yes"]))
  Disorientation= encodingYesNo(st.select_slider("Enter whether you have Disorientation",["No","Yes"]))
  PersonalityChanges= encodingYesNo(st.select_slider("Enter whether you have Personality changes",["No","Yes"]))
  DifficultyCompletingTasks= encodingYesNo(st.select_slider("Enter whether you have Difficulty completing tasks ",["No","Yes"]))
  Forgetfulness =  encodingYesNo(st.select_slider("Enter whether you suffer from forgetfulness ",["No","Yes"]))
  st.markdown("------")
  if st.button("Show Result: "):
    predic(Age, EducationLevel,FamilyHistoryAlzheimers, MMSE, FunctionalAssessment,MemoryComplaints, BehavioralProblems, ADL, Confusion,Disorientation, PersonalityChanges, DifficultyCompletingTasks,Forgetfulness)
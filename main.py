import streamlit as st
from translate import Translator
import spacy



# Create a title for the chatbot app
st.title("My Chatbot")



source_lang = st.sidebar.selectbox('Translate from:', ['Kannada', 'English'])
target_lang = st.sidebar.selectbox('Translate to:', ['Kannada', 'English'])

translator = Translator(from_lang=source_lang, to_lang=target_lang)

def translate_message(message):
    translated_message = translator.translate(message)
    return translated_message

user_input = st.sidebar.text_input('Enter your message')
translated_input = translate_message(user_input)

st.sidebar.write('Translated message:', translated_input)






#intent


# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Define intents and their associated symptoms
intents= {
    "Fungal Infection": ["itching", "skin rash", "nodal skin eruptions", "dischromic patches"],
    "Allergy": ["continuous sneezing", "shivering","watering from eyes"],
    "Drug Reaction":["stomach pain","burning sensation","spotting urination","skin rash"],	
    "Diabetes":[" weight loss"," blurry vision","irregular sugar level","excesive dry skin","feeling hunger oftenly","feeling dizzy"], 
    "Jaundice":["vomiting","fever"," yellowish skin","dark urine","abdominal pain"],	
    "Malaria":["chills","vomiting","high fever","sweating","headache","muscle pain"],	
    "Chicken pox":["headache","loss of appetite","mild fever","swelled lymph nodes","red spots over body"],		
    "Dengue":["skin rashes","joint pain","decrease of platelets","vomiting","high fever"],	
    "Heart attack":	["vomiting","breathlessness","excess sweating","chest pain"],	

    # Add more intents with associated symptoms
}





# User input
user_input1= st.text_input("Enter your symptoms:")

# NLP processing
doc = nlp(user_input1.lower())

# Intent matching
matched_intent = None
for intent, symptoms in intents.items():
    if any(symptom in doc.text for symptom in symptoms):
        matched_intent = intent
        break
# Display result
if matched_intent:
    st.subheader("Predicted Disease:")
    st.write(matched_intent)
else:
    st.text("  ")
    

st.text("OR!!! ,If you want to know more about the Predicted disease. CLICK the disease which is predicted")   

st.sidebar.write('Translated message:', matched_intent)
st.sidebar.text("HOME REMEDIES")

checkbox1 = st.sidebar.checkbox("Precautions")
checkbox2 = st.sidebar.checkbox("Home Remedies")

if checkbox1:

    checkbox_allergy = st.sidebar.checkbox("allergy")
    checkbox_FungalInfection = st.sidebar.checkbox("FungalInfection")
    checkbox_Diabetes=st.sidebar.checkbox("Diabetes")
    checkbox_Malaria=st.sidebar.checkbox("Malaria")
    checkbox_ChickenPox=st.sidebar.checkbox("ChickenPox")
    checkbox_Dengue=st.sidebar.checkbox("Dengue")
    checkbox_HeartPain=st.sidebar.checkbox("HeartPain")



    if checkbox_allergy:
       Allergy=st.sidebar.text("bath twice,use detol or neem in bathing water,keep infected area dry,use clean cloths")
       #st.sidebar.write("Precuatione for the disease",Allergy , matched_intent)
       st.sidebar.markdown("**Precuatione for the disease**")
       st.sidebar.markdown("**{}**".format(Allergy))
       st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_FungalInfection:
       Fungal_infection=st.sidebar.text("apply calamine,	cover area with bandage,use ice to compress itching")
       st.sidebar.write("Precuatione for the disease")
       st.sidebar.markdown("**{}**".format(Fungal_infection))
       st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_Diabetes:
       Diabetes=st.sidebar.text("have balanced diet,exercise,consult doctor,follow up")
       st.sidebar.write("Precuatione for the disease")
       st.sidebar.markdown("**{}**".format(Diabetes))
       st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_Malaria:
       Malaria=st.sidebar.text("Consult nearest hospital,avoid oily food,avoid non veg food,keep mosquitos out")
       st.sidebar.write("Precuatione for the disease")
       st.sidebar.markdown("**{}**".format(Malaria))
       st.sidebar.markdown("**{}**".format(matched_intent))


    if checkbox_ChickenPox:
       Chicken_pox=st.sidebar.text("use neem in bathing ,consume neem leaves,take vaccine,avoid public places")
       st.sidebar.write("Precuation for the disease")
       st.sidebar.markdown("**{}**".format(Chicken_pox))
       st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_Dengue:
       Dengue=st.sidebar.text("drink papaya leaf juice,avoid fatty spicy food,keep mosquitos away,keep hydrated")
       st.sidebar.write("Precuation for the disease")
       st.sidebar.markdown("**{}**".format(Dengue))
       st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_HeartPain:
       HeartPain=st.sidebar.text("call ambulance,chew or swallow asprin,keep calm")
       st.sidebar.write("Precuation for the disease")
       st.sidebar.markdown("**{}**".format(HeartPain))
       st.sidebar.markdown("**{}**".format(matched_intent))



   

if checkbox2:
    checkbox_allergy = st.sidebar.checkbox("allergy")
    checkbox_FungalInfection = st.sidebar.checkbox("Fungal Infection")
    checkbox_Diabetes=st.sidebar.checkbox("Diabetes")
    checkbox_Malaria=st.sidebar.checkbox("Malaria")
    checkbox_Jaundice=st.sidebar.checkbox("Jaundice")
    checkbox_ChickenPox=st.sidebar.checkbox("Chicken Pox")
    checkbox_Dengue=st.sidebar.checkbox("Dengue")
    checkbox_HeartPain=st.sidebar.checkbox("Heart Pain")
    checkbox_DrugReaction=st.sidebar.checkbox("Drug Reaction")

    if checkbox_allergy:
       Allergy=st.sidebar.text("Dehumidifier,Essential Oils,HEPA Filters,Herbs and Supplements,Nasal Spray,Neti Pot,Showering,Steam.")
       #st.sidebar.write("Home Remedies for the disease",Allergy , matched_intent)
       st.sidebar.markdown("Home Remedies for the disease")
       st.sidebar.markdown("**{}**".format(Allergy))
       st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_FungalInfection:
        FungalInfection=st.sidebar.text("Eat Yoghurt and Probiotics, Wash with Soap and Water , Use Apple Cider Vinegar,Use Tea Tree Oil,Use Coconut Oil,Use Turmeric")
        #st.sidebar.write("Home Remedies for the disease",FungalInfection , matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(FungalInfection))
        st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_Diabetes:
        FungalInfection=st.sidebar.text("Stress management,Eating right,Exercise,Onion,Bel,Neem,Babul,Aloe Vera ")
        #st.sidebar.write("Home Remedies for the disease",Diabetes, matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(Diabetes))
        st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_Malaria:
        Malaria=st.sidebar.text("Ginger,Turmeric, Cinnamon , Tulsi ,Neem ")
        #st.sidebar.write("Home Remedies for the disease",Malaria, matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(Malaria))
        st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_Jaundice:
        Jaundice=st.sidebar.text(" Natural Sunlight for neonatal jaundice, Restriction In Diet, Sugarcane Juice,Papaya Leaves,Black cumin,Mint, Amla")
        #st.sidebar.write("Home Remedies for the disease",Jaundice, matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(Jaundice))
        st.sidebar.markdown("**{}**".format(matched_intent))
    
    if checkbox_ChickenPox:
    
        ChickenPox=st.sidebar.text("Apply calamine lotion,Serve sugar-free popsicles,Bathe in oatmeal, Wear mittens to prevent scratching, Take baking soda baths ")
        #st.sidebar.write("Home Remedies for the disease",ChickenPox, matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(ChickenPox))
        st.sidebar.markdown("**{}**".format(matched_intent))
    
    if checkbox_Dengue:
        Dengue=st.sidebar.text("Neem,Papaya , Dudhi,Kalmegh ,Golden eye- grass,Tulsi ,Karela ")
        #st.sidebar.write("Home Remedies for the disease",Dengue, matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(Dengue))
        st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_HeartPain:
        HeartPain=st.sidebar.text("Almonds,Apple cider vinegar,Drinking a hot drink,Apply a cold pack")
        #st.sidebar.write("Home Remedies for the disease",HeartPain, matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(HeartPain))
        st.sidebar.markdown("**{}**".format(matched_intent))

    if checkbox_DrugReaction:
        DrugReaction=st.sidebar.text("Saline nasal irrigation,Air filters,Butterbur,Bromelain,Acupuncture")
        #st.sidebar.write("Home Remedies for the disease",DrugReaction, matched_intent)
        st.sidebar.markdown("Home Remedies for the disease")
        st.sidebar.markdown("**{}**".format(DrugReaction))
        st.sidebar.markdown("**{}**".format(matched_intent))

    

    







from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import streamlit as st


intents_data = {
    "Fungal Infection": ["itching", "skin rash", "nodal skin eruptions", "dischromic patches"],
    "Allergy": ["continuous sneezing", "shivering", "chills", "watering from eyes"],
    "Drug Reaction":["stomach pain","burning sensation","spotting urination","skin rash"],	
    "Diabetes":[" weight loss"," blurry vision","irregular sugar level","excesive dry skin","feeling hunger oftenly","feeling dizzy"], 
    "Jaundice":["vomiting","high fever"," yellowish skin","dark urine","abdominal pain"],	

    # Add more intents with associated symptoms
}




# Sample code, replace with your actual data
train_data = [(" ".join(symptoms), intent) for intent, symptoms in intents_data.items()]

# Split data into features and labels
X, y = zip(*train_data)

# Train a classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y)


from transformers import GPT2LMHeadModel, GPT2Tokenizer

gpt2_model = GPT2LMHeadModel.from_pretrained("gpt2")
gpt2_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def generate_gpt2_response(user_input):
    inputs = gpt2_tokenizer.encode(user_input, return_tensors="pt")
    outputs = gpt2_model.generate(inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
    response = gpt2_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response


user_input = st.text_input("Enter your symptoms:")
intent = model.predict([user_input])[0]  # Use your trained classifier here

if intent in intents_data:
    # Use intent-specific logic or responses here
    st.write("Predicted Intent:", intent)
#st.write("Intent-specific response or actions...")
else:
    # Use GPT-2 for a generic response
    response = generate_gpt2_response(user_input)
    st.write("ChatGPT:", response)
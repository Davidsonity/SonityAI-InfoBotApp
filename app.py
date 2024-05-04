from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import random
import json
import streamlit as st
from queue import Queue

max_len = 23  # max length of the sequence used to train te model is 23

greetings = ['hi', 'hello', 'greetings', 'sup', "what's up", 'hey']
greet_responses = ['hi', 'hello', 'hi there', 'hey']


# Load the model
model = load_model('model.h5')

# Load the tokenizer
with open('tokenizer.pickle', 'rb') as t_handle:
    tokenizer = pickle.load(t_handle)

# Load the label encoder
with open('label_encoder.pickle', 'rb') as l_handle:
    label_encoder = pickle.load(l_handle)

# Load the rephrase JSON file and convert it to a dictionary
with open('dict_phrases.json', 'r') as file:
    dict_rephrase = json.load(file)


# Create a queue to store chat messages
messages = Queue()

# Define a function to display the chat messages
def display_chat():
    while not messages.empty():
        msg = messages.get()
        st.write(msg)

# Create the main Streamlit app
def main():
    st.subheader("InfoBot Project (Sonity AI)")
    st.write("Welcome to the Chat Box app! This project demonstrates a basic chat application using machine learning techniques to provide instant and automated responses to user inquiries about a specific individual.")

    # Create an input box for user to type messages
    user_input = st.text_input("Type your message here:")

    # Add a button to submit the message
    if st.button("Send"):
        # Check if its a greeting
        for word in user_input.split():
            if word.lower() in greetings:
                reply = random.choice(greet_responses) + ", what would you like to know about me?"
            else:
                # Tokenize and pad the user input
                user_sequence = tokenizer.texts_to_sequences([user_input])
                user_X = pad_sequences(user_sequence, maxlen=max_len)
                # Make prediction
                prediction = model.predict(user_X)
                # Decode the prediction
                decoded_prediction = label_encoder.inverse_transform(np.argmax(prediction, axis=1))
                key = decoded_prediction[0]
                reply = random.choice(dict_rephrase[key])
        messages.put(reply)

    # Display the chat messages
    display_chat()

if __name__ == "__main__":
    main()





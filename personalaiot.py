#rule based chatbot

import datetime
import time
from unicodedata import name

from streamlit import user

loginpage = input("Do you want to login to Personal chat bot? (yes/no) ")

if loginpage.lower() == "yes":
    print("Welcome to Personal chat bot! Please wait while we log you in...")
    time.sleep(2)
    ragistration = input("Do you want to register for Personal chat bot? (yes/no) ")

    if ragistration.lower() == "yes":
        print("Please wait while we create your account...")
        time.sleep(2)
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        time.sleep(2)

        print("Your account has been created! You can now log in with your username and password.")

    enterusername = input("Please enter your username: ")
    enterpassword = input("Please enter your password: ")
    time.sleep(2)

    print("You are now logged in!",username)
else:
    print("Okay, maybe next time. Have a great day!")

presenthour = datetime.datetime.now().hour

if presenthour < 5:
    print("Good night!",username,"its to late sleep now") 
elif presenthour < 12:
    print("Good Morning!",username,"welcome to Personal chat bot")
elif presenthour < 18:
    print("Good Afternoon!",username,"welcome to Personal chat bot")  
elif presenthour < 22:
    print("Good Evening!",username,"welcome to Personal chat bot")  
else:
    print("Good night!",username,"sleeping time its late now")



print("Hello, World! welcome to Personal chat bot")
print("This is a simple chatbot that can answer your questions and have a conversation with you.")
print("You can ask me anything, and I will do my best to answer you.")

#chat bot memory

responses = {
    "hi": "Hello! How can I help you today?",
    "what is your name": "I am a simple chatbot.",
    "what can you do": "I can answer your questions and have a conversation with you.",
    "how are you": "I am doing well, thank you for asking!",
    "who are you": "I am a simple chatbot created to assist you with your questions and have a conversation with you.",
    "motivate me": "You can do anything you set your mind to! Believe in yourself and keep pushing forward.",
    "bye": "Goodbye! It was nice talking to you.",
    "happy": "I'm glad to hear that! Is there anything else I can help you with?",
    "sad": "I'm sorry to hear that. Is there anything I can do to help?",
    "angry": "I'm sorry to hear that. Is there anything I can do to help?",
    "thank you": "You're welcome! I'm here to help you with anything you need.",
}
#method/functions to get responses from the chatbot

def get_response(user_question):
    user_question = user_question.lower()
    for eachKey in responses.keys():
        if eachKey in user_question:
            return responses[eachKey]
    return responses.get(user_question , "I'm sorry, I don't understand that. Can you please rephrase your question?")

    

#take user input and respond

while True:
    user_input = input("plz ask question: ").lower()
    reply = get_response(user_input)
    print("bot: " + reply)
    if "bye" in user_input:
        print("bot: " + responses["bye"])
        break
    
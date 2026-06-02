# 🤖 Personal AI-OT Chatbot (personalaiot.py)

A simple rule-based chatbot implementation featuring login authentication, time-based greetings, and keyword-driven responses. This is a beginner-friendly alternative implementation to the main chat assistant.

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation & Setup](#-installation--setup)
- [Usage](#-usage)
- [Code Structure](#-code-structure)
- [Response Dictionary](#-response-dictionary)
- [Examples](#-examples)
- [Limitations](#-limitations)
- [Troubleshooting](#-troubleshooting)
- [Learning Concepts](#-learning-concepts)

## 🎯 Overview

This is a **rule-based chatbot** implementation using a simple dictionary-based approach. It demonstrates fundamental programming concepts including:
- Conditional logic (if-elif-else)
- Dictionary data structures
- Function definitions
- User input/output
- While loops
- String manipulation

**Status:** Educational implementation | **Difficulty:** Beginner | **Type:** Rule-based

## ✨ Features

### Authentication System
- **Login Prompt** - User must decide to login or skip
- **Registration** - Create new user account with username and password
- **Login** - Authenticate with username and password
- **Session Greeting** - Personalized welcome message

### Time-Based Greetings
Automatically greets user based on current time:
- **00:00 - 04:59** - "Good night!"
- **05:00 - 11:59** - "Good Morning!"
- **12:00 - 17:59** - "Good Afternoon!"
- **18:00 - 21:59** - "Good Evening!"
- **22:00 - 23:59** - "Good night!"

### Response System
- **Dictionary-Based Responses** - 11 predefined keyword-response pairs
- **Keyword Matching** - Searches for keywords in user input
- **Fallback Response** - Default message for unrecognized input
- **Keyword Search** - Partial matching (e.g., "hi" found in "hi there")

### Conversation Features
- **Continuous Chat Loop** - Keep chatting until user says goodbye
- **Exit Handling** - Graceful exit when user says "bye"
- **Lowercase Processing** - Case-insensitive input matching
- **Simple Interface** - No complicated menus or commands

## 🔧 Requirements

- **Python 3.6 or higher**
- **Libraries Used:**
  - `datetime` - For time-based greetings (standard library)
  - `time` - For sleep delays (standard library)
  - `unicodedata` - For name handling (standard library)
  - `streamlit` - Imported but not actively used in basic version

**Note:** The `streamlit` import won't cause errors but isn't utilized in this script. Remove it if you want a pure standard library version.

## 📥 Installation & Setup

### Step 1: Verify Python Installation
```bash
python --version
# or
python3 --version
```
Ensure version is 3.6+

### Step 2: Navigate to Project Directory
```bash
cd "c:\Users\omdho\Desktop\TUSHAR\python full cource notes\mini project 2 personal chat assistant"
```

### Step 3: Run the Script
```bash
python personalaiot.py
```

### Step 4: Follow On-Screen Prompts
- Answer login question
- Register if desired
- Start chatting!

## 🚀 Usage

### Standard Execution Flow

```
$ python personalaiot.py

Do you want to login to Personal chat bot? (yes/no): yes
Welcome to Personal chat bot! Please wait while we log you in...
Do you want to register for Personal chat bot? (yes/no): yes
Please wait while we create your account...
Please enter a username: tushar
Please enter a password: mypassword123
Your account has been created! You can now log in with your username and password.
Please enter your username: tushar
Please enter your password: mypassword123
You are now logged in! tushar

Good Morning! tushar welcome to Personal chat bot

Hello, World! welcome to Personal chat bot
This is a simple chatbot that can answer your questions and have a conversation with you.
You can ask me anything, and I will do my best to answer you.

plz ask question: hi
bot: Hello! How can I help you today?

plz ask question: what is your name
bot: I am a simple chatbot.

plz ask question: how are you
bot: I am doing well, thank you for asking!

plz ask question: bye
bot: Goodbye! It was nice talking to you.
```

### Skipping Login

```
Do you want to login to Personal chat bot? (yes/no): no
Okay, maybe next time. Have a great day!
```

## 📂 Code Structure

### Main Sections

#### 1. Imports
```python
import datetime      # For time-based greetings
import time          # For sleep delays
from unicodedata import name  # Imported but unused
from streamlit import user    # Imported but unused
```

#### 2. Login/Registration Section
```python
loginpage = input("Do you want to login to Personal chat bot? (yes/no) ")

if loginpage.lower() == "yes":
    # Registration logic
    # Login logic
    # Store username for later use
```

#### 3. Time-Based Greeting
```python
presenthour = datetime.datetime.now().hour

if presenthour < 5:
    print("Good night!")
elif presenthour < 12:
    print("Good Morning!")
# ... more conditions
```

#### 4. Response Dictionary
```python
responses = {
    "hi": "Hello! How can I help you today?",
    "what is your name": "I am a simple chatbot.",
    # ... 11 total response pairs
}
```

#### 5. Response Function
```python
def get_response(user_question):
    user_question = user_question.lower()
    for eachKey in responses.keys():
        if eachKey in user_question:
            return responses[eachKey]
    return responses.get(user_question, 
           "I'm sorry, I don't understand that...")
```

#### 6. Chat Loop
```python
while True:
    user_input = input("plz ask question: ").lower()
    reply = get_response(user_input)
    print("bot: " + reply)
    if "bye" in user_input:
        print("bot: " + responses["bye"])
        break
```

## 📚 Response Dictionary

| Keyword | Response |
|---------|----------|
| `hi` | "Hello! How can I help you today?" |
| `what is your name` | "I am a simple chatbot." |
| `what can you do` | "I can answer your questions and have a conversation with you." |
| `how are you` | "I am doing well, thank you for asking!" |
| `who are you` | "I am a simple chatbot created to assist you..." |
| `motivate me` | "You can do anything you set your mind to!..." |
| `bye` | "Goodbye! It was nice talking to you." |
| `happy` | "I'm glad to hear that! Is there anything else...?" |
| `sad` | "I'm sorry to hear that. Is there anything I can do...?" |
| `angry` | "I'm sorry to hear that. Is there anything I can do...?" |
| `thank you` | "You're welcome! I'm here to help you..." |
| **(default)** | "I'm sorry, I don't understand that..." |

## 💡 Examples

### Example 1: Complete Login and Chat Session
```
$ python personalaiot.py

Do you want to login to Personal chat bot? (yes/no): yes
Welcome to Personal chat bot! Please wait while we log you in...
Do you want to register for Personal chat bot? (yes/no): yes
Please wait while we create your account...
Please enter a username: john
Please enter a password: password123
Your account has been created! You can now log in with your username and password.
Please enter your username: john
Please enter your password: password123
You are now logged in! john

Good Evening! john welcome to Personal chat bot

Hello, World! welcome to Personal chat bot
This is a simple chatbot that can answer your questions and have a conversation with you.
You can ask me anything, and I will do my best to answer you.

plz ask question: motivate me
bot: You can do anything you set your mind to! Believe in yourself and keep pushing forward.

plz ask question: thank you
bot: You're welcome! I'm here to help you with anything you need.

plz ask question: bye
bot: Goodbye! It was nice talking to you.
```

### Example 2: Unrecognized Input
```
plz ask question: what's the weather?
bot: I'm sorry, I don't understand that. Can you please rephrase your question?

plz ask question: tell me a joke
bot: I'm sorry, I don't understand that. Can you please rephrase your question?
```

### Example 3: Partial Keyword Matching
```
plz ask question: hey hi there
bot: Hello! How can I help you today?
(Matches "hi" in the input)

plz ask question: i am feeling sad today
bot: I'm sorry to hear that. Is there anything I can do to help?
(Matches "sad" in the input)
```

### Example 4: Skip Login
```
$ python personalaiot.py

Do you want to login to Personal chat bot? (yes/no): no
Okay, maybe next time. Have a great day!
```

## 🔴 Limitations

### Current Issues
1. **Variable Scope Error** - `username` variable may not be defined if user skips login
   - This causes a crash if user skips login (the time-based greeting tries to use `username`)
   
2. **No Data Persistence** - Credentials not actually saved or verified
   - Accepts any username/password combination
   - Doesn't validate against saved accounts
   
3. **Limited Response Set** - Only 11 predefined responses
   - Cannot handle complex questions
   - No learning capability
   
4. **Unused Imports** - `streamlit` and `unicodedata` imported but not used
   
5. **Basic Pattern Matching** - Simple substring search
   - Cannot understand context
   - Cannot handle similar phrases
   
6. **No Conversation History** - Conversations not saved
   - Each session is independent
   - No learning from interactions

### Known Bugs
- **NameError if Login Skipped** - Trying to print `username` when user chooses "no" will crash
- **Any Password Accepted** - No real authentication validation
- **Greeting Always Shows** - Username may be undefined

## 🔧 Troubleshooting

### Issue: Program Crashes with "NameError: name 'username' is not defined"
**Cause:** User selected "no" to login, but code tries to use `username` variable
**Solution:** Add this fix to handle undefined username:
```python
# After login section, add:
if loginpage.lower() != "yes":
    username = "Guest"  # Set default if login skipped
```

### Issue: Login Doesn't Actually Verify Credentials
**Cause:** This is a demo - no actual user database exists
**Solution:** This is expected behavior for a learning project

### Issue: Chatbot Doesn't Understand My Question
**Cause:** Your input doesn't contain any keywords from the response dictionary
**Solution:** 
- Use simpler keywords from the response list
- Try: "hi", "bye", "how are you", "what is your name"

### Issue: Chatbot Keeps Running After "bye"
**Cause:** The word "bye" must be present in the input
**Solution:** Type exactly "bye" or include it in your message (e.g., "bye bye")

### Issue: Multiple Time Zones Show Wrong Time
**Cause:** Python uses system time
**Solution:** Ensure your system clock is set correctly

## 📚 Learning Concepts

This script demonstrates several Python fundamentals:

### 1. **Dictionaries**
```python
responses = {"key": "value", ...}  # Data structure for storing key-value pairs
```

### 2. **Loops**
```python
while True:           # Infinite loop for chat
    # code
for eachKey in responses.keys():  # Iterate through dictionary keys
    # code
```

### 3. **Conditionals**
```python
if loginpage.lower() == "yes":    # String comparison
elif presenthour < 12:            # Numeric comparison
    # code
```

### 4. **Functions**
```python
def get_response(user_question):  # Define function with parameter
    # Process and return value
    return responses[user_question]
```

### 5. **String Methods**
```python
user_input.lower()      # Convert to lowercase
if eachKey in user_question:  # Check substring existence
```

### 6. **Input/Output**
```python
input("prompt: ")       # Get user input
print("output")         # Display output
```

### 7. **Control Flow**
```python
if "bye" in user_input:
    break               # Exit the loop
```

## 🔄 Comparison: personalaiot.py vs chat.py

| Feature | personalaiot.py | chat.py |
|---------|-----------------|---------|
| **Complexity** | Simple/Beginner | Advanced |
| **Data Persistence** | None | JSON file |
| **Response Type** | Dictionary-based | ML-based intent detection |
| **Memory** | No memory | Learns user preferences |
| **User Management** | Basic auth (demo) | User profiles |
| **History** | Not saved | Saved automatically |
| **Scalability** | Limited | Highly scalable |
| **Learning Curve** | Easy | Moderate |
| **Production Ready** | No | Yes |

## 📝 Improvements Needed

To make this production-ready:
1. Fix the username variable scope issue
2. Add actual database for user credentials
3. Expand response dictionary (100+ responses)
4. Implement conversation history
5. Add natural language processing
6. Remove unused imports
7. Add error handling
8. Implement logging system

## 📞 Notes

- This is an **educational implementation** for learning Python basics
- Use [chat.py](./README.md) for a more advanced, production-ready version
- Great starting point for beginners learning Python fundamentals
- Demonstrates dictionary-based knowledge representation

---

**Version:** 1.0  
**Type:** Educational Implementation  
**Difficulty:** Beginner  
**Learning Focus:** Python Fundamentals  
**Last Updated:** June 2, 2026

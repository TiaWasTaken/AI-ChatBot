<h1 align="center">🤖 ChatBot with AI</h1>

## Overview

Welcome to the ChatBot AI! This intelligent chatbot is powered by Google's Generative AI model to provide dynamic and accurate responses to user questions. The ChatBot AI allows customization of the user experience, including selecting a name, emoji, and color for the username. Additionally, it offers various commands to manage the chatbot's instructions and enhance interaction.

## Features

- **User Customization:** Choose your username, emoji, and text color for a personalized chat experience.
- **AI-Powered Responses:** The chatbot uses Google's Generative AI to provide intelligent and dynamic answers.

### Dependencies
You will need to install the following dependencies in order to run this code.

```python
pip install google-generativeai
```

```python
pip install python-dotenv
```

Also in order to run it you will need an API key for google gemini, which you can create [here](https://aistudio.google.com/app/apikey)

- **Interactive Help Menu:** Access a list of available commands to navigate the chatbot's functionalities.
- **Instruction Management:** Set and clear instructions to guide the chatbot's behavior.

## How It Works

### AI Model

The chatbot uses Google's Generative AI model (Gemini Pro) to generate responses. It starts a chat session with the model and processes user inputs to provide relevant answers.

### Core Functions

### User Customization
The chatbot allows users to customize their chat experience by selecting a username, emoji, and text color:

https://github.com/TiaWasTaken/AI-ChatBot/assets/151725770/2b28d7d4-150a-412d-bd33-5177b9514438


## Commands
### Help
Displays a help menu with all available commands.

### Set Instructions
Sets instructions for the chatbot to guide its behavior.

```python
def set_instructions(new_instructions: str):
    global instructions
    instructions = new_instructions
    print("\n📝 \033[1;34;40mChatBot:\033[1;37;40m Instructions set.")
```

### Clear Instructions
Clears the current instructions for the chatbot.

```python
def clear_instructions():
    global instructions
    instructions = ""
    print("\n🗑️ \033[1;34;40mChatBot:\033[1;37;40m Instructions cleared.")
```

## Example
### Starting the ChatBot
When you start the chatbot, you'll be prompted to select a name, emoji, and color for your username. For example:

```python
[Type Skip to select 'You'] Select name: Alice
Select an emoji for your username:
1. 👽
2. 💍
3. 🦊
...
Type the number of the emoji you want: 3
Select a color for your username:
red
green
yellow
...
Type the name of the color you want: blue
```

### Interacting with the ChatBot
Type your question and the chatbot will respond based on the AI model. For example:

```python
Alice🦊 blue: What is the capital of France?
🤖 ChatBot: Paris
```

If you need help, type help to see the list of available commands.

### Setting Instructions
You can set instructions to guide the chatbot's behavior:

```python
Alice🦊 blue: set_instructions Be an expert in computer science.
📝 ChatBot: Instructions set.
```

### Clearing Instructions
To clear the current instructions:

```python
Alice🦊 blue: clear_instructions
🗑️ ChatBot: Instructions cleared.
```

### Exiting the ChatBot
To exit the chatbot, type exit, quit, bye, or goodbye.

```python
Alice🦊 blue: goodbye
👋 ChatBot: Goodbye! Have a nice day!
```

<h2 align="center">Enjoy using your customizable ChatBot with AI!</h2>

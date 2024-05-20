<h1 align="center">🤖 ChatBot with AI</h1>

## Overview

Welcome to the ChatBot AI! This intelligent chatbot is powered by Google's Generative AI model to provide dynamic and accurate responses to user questions. The ChatBot AI allows customization of the user experience, including selecting a name, emoji, and color for the username. Additionally, it offers various commands to manage the chatbot's instructions and enhance interaction.

## Features

- **User Customization:** Choose your username, emoji, and text color for a personalized chat experience.
- **AI-Powered Responses:** The chatbot uses Google's Generative AI to provide intelligent and dynamic answers.

### Dependencies
You will need to install the following dependencies in order to run this code. Also in order to run it you will need an API key 

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

```python
def get_user_name() -> str:
    name = input("\n\033[1;33;40m[Type Skip to select 'You'] Select name: \033[1;37;40m")
    if name.lower() == "skip":
        return "You"
    return name

def get_user_emoji() -> str:
    emojis = ["👽", "💍", "🦊", "🕶️", "🍄", "🍒", "🎲", "🍀", "🥚", "🎧", "🐸"]
    print("\n\033[1;33;40mSelect an emoji for your username:\033[1;37;40m")
    for i, emoji in enumerate(emojis, start=1):
        print(f"\033[1;32;40m{i}.\033[1;37;40m {emoji}")
    choice = int(input("\n\033[1;33;40mType the number of the emoji you want: \033[1;37;40m"))
    return emojis[choice - 1]

def get_user_color() -> str:
    colors = {
        "red": "\033[1;31;40m",
        "green": "\033[1;32;40m",
        "yellow": "\033[1;33;40m",
        "blue": "\033[1;34;40m",
        "magenta": "\033[1;35;40m",
        "cyan": "\033[1;36;40m",
        "white": "\033[1;37;40m",
    }
    print("\n\033[1;33;40mSelect a color for your username:\033[1;37;40m")
    for color_name, color_code in colors.items():
        print(f"{color_code}{color_name}\033[1;37;40m")
    choice = input("\n\033[1;33;40mType the name of the color you want: \033[1;37;40m").lower()
    return colors.get(choice, "\033[1;37;40m")
```

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

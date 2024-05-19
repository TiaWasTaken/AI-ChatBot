import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

# Configure the API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Initialize the chat without initial history
chat = model.start_chat(history=[])
instructions = ""


def get_user_name() -> str:
    name = input(
        "\n\033[1;33;40m[Type Skip to select 'You'] Select name: \033[1;37;40m"
    )
    if name.lower() == "skip":
        return "You"
    return name


def get_user_emoji() -> str:
    emojis = ["👽", "💍", "🦊", "🕶️", "🍄", "🍒", "🎲", "🍀", "🥚", "🎧", "🐸"]
    print("\n\033[1;33;40mSelect an emoji for your username:\033[1;37;40m")
    for i, emoji in enumerate(emojis, start=1):
        print(f"\033[1;32;40m{i}.\033[1;37;40m {emoji}")
    choice = int(
        input("\n\033[1;33;40mType the number of the emoji you want: \033[1;37;40m")
    )
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
    choice = input(
        "\n\033[1;33;40mType the name of the color you want: \033[1;37;40m"
    ).lower()
    return colors.get(choice, "\033[1;37;40m")


def set_instructions(new_instructions: str):
    global instructions
    instructions = new_instructions
    print("\n📝 \033[1;34;40mChatBot:\033[1;37;40m Instructions set.")


def clear_instructions():
    global instructions
    instructions = ""
    print("\n🗑️ \033[1;34;40mChatBot:\033[1;37;40m Instructions cleared.")


def display_help():
    help_message = """
    \nℹ️ \033[1;34;40mChatBot Help Menu:\033[1;37;40m
    \033[1;32;40mhelp\033[1;37;40m: Display this help message
    \033[1;32;40mset_instructions <instructions>\033[1;37;40m: Set instructions for the bot
    \033[1;32;40mclear_instructions\033[1;37;40m: Clear the current instructions
    \033[1;32;40mexit / quit / bye / goodbye\033[1;37;40m: Exit the chatbot
    """
    print(help_message)


def chat_bot():
    print(
        "\n✅ \033[1;32;40mChat bot is ready! Type 'help' or 'h' to view the list of commands\033[1;37;40m"
    )

    user_name: str = get_user_name()
    user_emoji: str = get_user_emoji()
    user_color: str = get_user_color()
    user_display: str = f"{user_emoji}{user_color} {user_name}:\033[1;37;40m"

    bot_emoji = "🤖"
    bot_color = "\033[1;34;40m"
    bot_display: str = f"{bot_emoji} {bot_color}ChatBot:\033[1;37;40m"

    while True:
        user_input: str = input(f"\n{user_display} \033[1;37;40m")

        if user_input.lower() in ["bye", "goodbye", "exit", "quit"]:
            print("\n👋 \033[1;34;40mChatBot:\033[1;37;40m Goodbye! Have a nice day!")
            break

        if user_input.lower().startswith("set_instructions "):
            new_instructions = user_input[len("set_instructions ") :].strip()
            set_instructions(new_instructions)
            continue

        if user_input.lower() == "clear_instructions":
            clear_instructions()
            continue

        if user_input.lower() == "help":
            display_help()
            continue

        full_input = f"{instructions} {user_input}" if instructions else user_input
        response = chat.send_message(full_input)
        ai_answer = response.text.strip()
        print(f"\n{bot_display} {ai_answer}")


if __name__ == "__main__":
    chat_bot()

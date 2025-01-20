from colorama import Fore, Style, init
import os
from g4f.client import Client
from player_stats import *
from methods import *

# Initialize colorama
init()

def main():
    # Clear the terminal
    os.system('cls||clear')

    # Display the content of `glory.txt`
    try:
        with open('glory.txt', 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(Fore.RED + "Error: 'glory.txt' not found." + Style.RESET_ALL)

    # Read the academy prompt
    try:
        with open('academy_prompt.txt', 'r') as p:
            academy_prompt = ''.join(p.readlines())  # Combine lines into a single string
    except FileNotFoundError:
        print(Fore.RED + "Error: 'academy_prompt.txt' not found." + Style.RESET_ALL)
        academy_prompt = "Default academy prompt: Tell me about a soccer academy in "

    # Get the user's choice
    try:
        start_option = int(input(
            Fore.GREEN + "1. Play Li Gma's Story \n" +
            Fore.BLUE + "2. Play your own story \n" +
            Fore.RED + "3. Play an AI Generated Story \n" +
            Style.RESET_ALL + "Select an option: "
        ))
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number (1, 2, or 3)." + Style.RESET_ALL)
        return

    # Option logic
    if start_option == 2:
        os.system('cls||clear')

        # Create player
        player = create_player()  # Captures the Player instance

        # Generate academy name
        academy = ai_gen(academy_prompt, player)  # Pass the Player instance to ai_gen

        # Begin the story
        begin_story(academy, player)  # Pass academy and player to begin_story
    else:
        print(Fore.RED + "This option is not implemented yet." + Style.RESET_ALL)

if __name__ == "__main__":
    main()

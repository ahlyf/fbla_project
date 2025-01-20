from player_stats import Player
from g4f.client import Client
from colorama import Fore, Style, init

# Initialize colorama for colored terminal output
init()

def create_player():
    print(Fore.BLUE + "Welcome to your superstar's journey!")
    name = input(Fore.BLUE + "Enter your name: ")
    position = input(Fore.BLUE + "Choose your position (Forward/Midfielder/Defender/Goalkeeper): ")
    country = input(Fore.BLUE + "Enter your country: ")
    return Player(name, position, country)

def ai_gen(prompt, player):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": prompt + player.country
        }],  # Access player's country
        web_search=False
    )
    return response.choices[0].message.content

def begin_story(academy, player):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": f"Write a 5-sentence paragraph about a kid named {player.name} who grew up with soccer. Make it random but realistic. They go to play in a real academy(include the real academy's name) in {player.country} as a {player.position}."
        }],  # Access player's country
        web_search=False
    )
    print(response.choices[0].message.content)

# Main sequence
if __name__ == "__main__":
    academy = "Future Elite Soccer Academy"
    player = create_player()  # Creates a new Player instance
    begin_story(academy, player)  # Pass both academy and player to the story function
    prompt = "Tell me about the soccer culture in "
    ai_response = ai_gen(prompt, player)  # Pass the Player instance to the AI generator
    print("AI Response:", ai_response)

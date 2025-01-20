from player_stats import Player
from g4f.client import Client
import random

def play_opponent(prompt, player):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Name another club academy in the world to be the opponents for this team. Only have the name and nothing else. The opponents have to be " + player.age}],
        web_search=False
    )
    return response.choices[0].message.content

def make_choice():
    print("Choose your action:")
    print("1. Pass")
    print("2. Shoot")
    print("3. Tackle")
    choice = input("Enter the number of your choice: ")
    return choice

def evaluate_choice(choice, player):
    """Evaluate the player's choice and return the outcome."""
    outcome = ""
    card = None

    if choice == "1":
        if random.random() > 0.2:
            outcome = "Great pass! Your teammate is now in a good position."
            player.reputation += 5
        else:
            outcome = "Bad pass! The opponent intercepted it."
            player.reputation -= 3
    elif choice == "2":
        if random.random() > 0.5:
            outcome = "Goal! You've scored for your team!"
            player.reputation += 10
        else:
            outcome = "Missed shot! The opponent's goalkeeper saved it."
            player.reputation -= 2
    elif choice == "3":
        if random.random() > 0.7:
            outcome = "Clean tackle! You won the ball back for your team."
            player.reputation += 7
        else:
            outcome = "Foul! The referee didn't like that."
            player.reputation -= 5
            card = random.choice(["yellow", "red", None])
    else:
        outcome = "Invalid choice. You lost your turn."
        player.reputation -= 1

    return outcome, card

def play_match(opponent_team, player):
    print("Welcome to the match!")
    print("You will be playing against " + opponent_team)

    if player.reputation >= 45:
        print("Good news! You're a starter in this match!")
    else:
        print("Unfortunately, you're on the bench for this match.")
        return

    print("Kickoff! The match has begun.")
    
    for minute in range(1, 91, 10):  # Simulate actions every 10 minutes
        print(f"Minute {minute}:")
        choice = make_choice()
        outcome, card = evaluate_choice(choice, player)
        print(outcome)

        if card:
            print(f"You've received a {card} card!")
            if card == "red":
                print("You're sent off! Your match is over.")
                break

        print(f"Your current reputation: {player.reputation}")
        
        if player.reputation < 45:
            print("Your reputation has dropped too low. You've been substituted.")
            break

    print("The match has ended!")
    print(f"Final reputation: {player.reputation}")


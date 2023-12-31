import random


def get_choices():
    # player_choice = "rock"
    player_choice = input("Enter a choice(rock, paper, scissors): ")
    # computer_choice = "paper"
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):   # we are passing two pieces of information
    # print("You chose " + player + ", computer chose " + computer)
    print(f"Your chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie"   # we are returning a String
    # elif player == "rock" and computer == "scissors":
    #     return "Rock smashes scissors! You win!"
    # elif player == "rock" and computer == "paper":
    #     return "Paper covers rock! You lose!"

    # WE WILL REFACTOR THE ABOVE 4 LINES, using nested ifs
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."

    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper! You lose."
        else:
            return "Paper covers rock! You win!"

    elif player == "scissors":
    # else:
        if computer == "rock":
            return "Rock smashes scissors! You lose."
        else:
            return "Scissors cut paper! You win!!"
    else:
        return "Wrong input"
# check_win("rock", "paper")

# Now we will call the functions and play the game
choices = get_choices()   # it will return a dictionary
# p_choice = choices["player"]
# c_choice = choices["computer"]
# result = check_win(p_choice, c_choice)

result = check_win(choices["player"], choices["computer"])
print(result)



# def greeting():
#     return "Hi"
#
#
# response = greeting()
# print(response)

# choices = get_choices()
# print(choices)

# dict = {"name": "beau", "color": choices}

# # list
# food = ["pizza", "carrots", "eggs"]
# #get a random item using the random library
# dinner = random.choice(food)   # pass the list as argument
# print(dinner)

# # f-strings:
# age = 25
# print(f"Jim is {age} years old.")

# accessing the dictionary elements

# choices = {"player": "paper", "computer": "paper"}
# p_choice = choices["player"]  # get choice of player


import art
import game_data
import random

def game_start():
    game = True
    player_score = 0
    used_number = []

    while game:
        print(art.logo)

        if len(used_number) >= len(game_data.data):
            print(f"Your final score is: {player_score}! You beat the game")
            exit()

        if player_score == 0:
            a_number = random.randint(0, 49)
        else:
            a_number = b_number
            used_number.append(b_number)

        print(f"Compare A: {game_data.data[a_number]['name']}, a {game_data.data[a_number]['description']}, from {game_data.data[a_number]['country']}.")

        print(art.vs)

        b_number = random.randint(0, 49)
        while b_number in used_number:
            b_number = random.randint(0, 49)

        print(f"Against B: {game_data.data[b_number]['name']}, a {game_data.data[b_number]['description']}, from {game_data.data[b_number]['country']}.")
        answer = input("Who has the most followers? Type A or B").upper()

        player_score = higher_lower(answer, a_number, b_number, player_score )

def higher_lower(player_answer, aa_number, bb_number, player_score ):
    if game_data.data[aa_number]['follower_count'] > game_data.data[bb_number]['follower_count']:
        correct_answer = 'A'
    elif game_data.data[aa_number]['follower_count'] < game_data.data[bb_number]['follower_count']:
        correct_answer = 'B'


    if player_answer == correct_answer:
        print("Correct you get 1 point!")
        player_score += 1
        print(f"Current score: {player_score}")
        return player_score
    else:
        print("Wrong answer")
        print(f"Your final score is: {player_score}")
        play_again = input("Would you like to play again? y or n").upper()
        if play_again == 'Y':
            return game_start()
        else:
            exit()

game_start()
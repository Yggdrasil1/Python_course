# rock paper scissors
# Write a set of if/else/elif statements that compare two variables 'user_input' and 'computer_input'
# These variables contain the strings `rock`, `paper', or 'scissors'
# Implement the rules as if/else/elif statements after line 10 with an indentation of 4 spaces, see example (line 10+11)
# Return a string saying 'tied game', 'you win', or 'computer wins' after every statement
# If there is no error when you run the script, you succeded
# Push the solution in your repo

def rock_paper_scissors(user_input, computer_input):
	if user_input is 'rock' and computer_input is 'paper':
		return 'computer wins'







if __name__ == "__main__":
	possibilities = ['rock', 'paper', 'scissors']
	for user_choice in possibilities:
		for computer_choice in possibilities:
			if user_choice == computer_choice:
				assert rock_paper_scissors(user_choice, computer_choice) is 'tied'
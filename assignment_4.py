import numpy as np

class RockPaperScissors:
    """
    Implementation of the game Rock, Paper, Scissors
    """

    scissors = {'rock': False, 'paper': True}
    rock = {'scissors': True, 'paper': False}
    paper = {'scissors': False, 'rock': True}
    
    choices = {'scissors': scissors, 'rock': rock, 'paper': paper}
    winner = {'Tied':"No Winner! ", 'human':"YOU WON! ",'ai':"You lost! "}

    def __init__(self):

	self.human_points = 0
	self.ai_points = 0
	self.my_choice = None
	self.ai_choice = None
	self.gewinner = None
	self.new_round = True	
		

    def computer_choice(self):
        """
        The computer chooses a value
        """

	self.ai_choice = np.random.choice(['rock','paper','scissors'])

    def human_choice(self):
        """
        The human player chooses a value
        """

        self.my_choice = str(raw_input("Choose 'rock','paper' or 'scissors': "))
	print(self.my_choice)

    def evaluate_game(self):
        """
        Evaluate the values of the two players
        """

        if self.my_choice == self.ai_choice:
	    self.gewinner = 'Tied'

	else:
	    if RockPaperScissors.choices[self.my_choice][self.ai_choice]:
		self.gewinner = 'human'

	    else:
		self.gewinner = 'ai'

    def print_result(self):
        """
        Visualise game result
        """
	
	print("%s Computer has %s" %(RockPaperScissors.winner[self.gewinner], self.ai_choice))

        print("Points: You vs AI ")
	print("\t %d vs %d" % (self.human_points, self.ai_points) )

    def count_points(self):
        """
        Count the points of all rounds
        """

        if self.gewinner == 'human':
	    self.human_points += 1
	if self.gewinner == 'ai':
	    self.ai_points += 1

    def new_game_question(self):
        """
        Ask human player for new game
        """
	human_answer = str(raw_input("Would you like to play another round? (y/n)"))

	if human_answer in ['y', 'Y', 'yes', ]: 
	    self.new_round = True
	
        else:
	    self.new_round = False
	    

    def run(self):

	while(self.new_round == True):
	    
	    RockPaperScissors.human_choice(self)
	    RockPaperScissors.computer_choice(self)
	    RockPaperScissors.evaluate_game(self)
	    RockPaperScissors.count_points(self)
	    RockPaperScissors.print_result(self)
	    RockPaperScissors.new_game_question(self)
	
	print("See you again, human!")


if __name__ == "__main__":
   game = RockPaperScissors()
   game.run()

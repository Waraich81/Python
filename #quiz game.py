#quiz game

questions =("who is PM of Canada:",
            "how many tires car have:",
            "Why are you gay?:",
            "Who are you?:")

options = (("A: Babbu Maan","B: Harman Cheema", "C:Sonu Sito","D: Mark Carney"),
           ("A:0","B:4","C:18","D:20"),
           ("A:I am Gay","B:Whos says I am Gay?","C:Bhatti is Gay","D:Not Gay"),
           ("A:Boy","B:Girl","C:Jatt","D:Nigger banda"))

answers = ('D','B','C','D')

guesses = []
score = 0
question_num = 0

for question in questions:                
    print("-----------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
        question_num += 1



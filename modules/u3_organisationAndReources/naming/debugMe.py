"""
Prog:   yesNoProgram.py
Name:   Samuel doyle
Date:   18/04/18
Desc:   Answers yes or no to any question.
"""
#inport random
import random
# Ask the user for a question.
question = input('Ask me anything!')

# Check for special input.
if  question == 'Quit':
    print('Goodbye.)
elif question == 'Hi' or 'Hello':
    print('Whats up?')

# Answer yes or no randomly.
else:
num = random.randint(0,4);
if num == "1":
    print("Yes!")
if num == '2':
    "No"
done

# Exercise 4.7: Star Wars Random Name Generator using random choice

import random

# create lists
first_name = ['Luke', 'Han', 'Princess', 'Boba', 'Obi-Wan']
last_name = ['Skywalker', 'Solo', 'Leia', 'Fett', 'Kenobi']
verb = ['stole', 'crashed', 'ate']
noun = ['Millennium Falcon', 'banana', 'Jedi Master']

# create random name and random sentence using random.choice()
random_name = f'{random.choice(first_name)} {random.choice(last_name)}'
random_sentence = f'{random.choice(first_name)} {random.choice(last_name)} {random.choice(verb)} the {random.choice(noun)}'

# Print random name and random sentence
print(f'Your Star Wars name is: {random_name}')
print(f'A long time ago in a galaxy far, far away {random_sentence}')

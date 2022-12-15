import random

# Create a lucky dip ticket: create an empty array and set the ticket length (or number of digits to 0)
randomTicket = []
ticketLength = 0

# using a while loop, add a random integer to our array while the ticket length (or no. of digits) is less than 7 digits
while ticketLength < 7:
    number = random.randint(1, 40)

    if number not in randomTicket:
        # We append the number in the lottery ticket (as long as it is not already in the random ticket array)
        randomTicket.append(number)
        # We increase our ticket length by 1 digit
        ticketLength = ticketLength + 1

# sort the numbers in the randomTicket
randomTicket = sorted(randomTicket)

# Time for the lottery draw: create an empty array for the winning ticket numbers and set the ticket length to 0
winningTicket = []
drawLength = 0

# using a while loop, add a random integer to our array while the draw length (or no. of digits) is less than 7 digits
while drawLength < 7:
    number = random.randint(1, 40)

    if number not in winningTicket:
        # We append the number in the lottery ticket (as long as it is not already in the random ticket array)
        winningTicket.append(number)
        # We increase our ticket length by 1 digit
        drawLength = drawLength + 1

# sort the numbers in the winningTicket
winningTicket = sorted(winningTicket)

# Now using a for loop, assess the number of digits matched to the winning ticket
numbersMatched = 0
for number in winningTicket:
    if number in randomTicket:
        numbersMatched = numbersMatched + 1

# use if/elif/else statements to calculate the winnings based on the number of digits matched
if numbersMatched < 3:
    winnings = 0

elif numbersMatched < 4:
    winnings = 20

elif numbersMatched < 5:
    winnings = 40

elif numbersMatched < 6:
    winnings = 100

elif numbersMatched < 7:
    winnings = 10000

else:
    winnings = 1000000

# print outcome inc winnings amount, numbers matched and ticket numbers.
if winnings > 0:
    print(f'''\
    CONGRATULATIONS! YOU WON £{winnings}!
    The winning lottery ticket numbers are {winningTicket}.
    Your lottery ticket numbers are:  {randomTicket}.
    You had {numbersMatched} matching numbers!''')

else:
    print(f'''\
    Sorry you won £{winnings}, with no matching numbers.
    The winning lottery ticket numbers are: {winningTicket}.
    Your lottery ticket numbers are: {randomTicket}.''')

import random
number=random.randint(0,100)
attempts=0

while True:
    attempts+=1
    guess=int(input('Give it a guess:\t'))
    if guess==number:break
    elif guess<number:print('Opps!!! Think Higher')
    else: print('Got yourself too farr!! Think a bit lower ;)')
    
print(f'Great job! You guessed the numbers in {attempts} attempts')
import random
import datetime 

computer_number = random.randint(1, 100)
continue_game = True
user_guesses = []
start_time = datetime.datetime.now()

while(continue_game):
    user_guess = int(input('Uzmini skaitli starp 1 un 100: '))
    user_guesses.append(user_guess)

    if user_guess  == computer_number:
        print('Apsveicu, uzmineji!')
        continue_game = False
    elif user_guess < computer_number:
        print('Mini lielaku!')
    elif user_guess > computer_number:
        print('Mini mazaku!')
    else:
        print('Kluda!')
print('Game over!')

sum_of_differences = 0
for n in user_guesses:
    sum_of_differences += abs(n - computer_number)

print(f'Videja starpiba ir {sum_of_differences/len(user_guesses)}')
print(f'Tu speleji {datetime.datetime.now()-start_time}sekundes')
print(f'Tu mineji {len(user_guesses)} reizes!')

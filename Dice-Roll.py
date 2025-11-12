import random
while True:
  num = int(input('enter a num how many dice want to roll:'))
  if num == 0 or num>10:
     print('invaid input')
  else:
        choice = input('enter y/n:').lower()
        if choice == 'y':
             for i in range(num):
                   dice1=random.randint(1,6)
                   dice2=random.randint(1,6)
                   print(f'{dice1},{dice2}')
        elif choice == 'n':
             print('thanks for playing')
             break
        else:
             print('invalid input')

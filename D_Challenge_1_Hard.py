number = int(input("Type a number between 1 and 100 for the computer to guess: "))

print("You chose %s" % str(number))

from random import randint
from time import sleep

count = 0
end = False
low = 1
high = 100

while end == False:
  print()
  print("Guessing number...")
  sleep(1)
  guess = randint(low,high)
  print("The number is: " + str(guess))
  print()
  count += 1

  if guess == number:
      print("The number was correctly guessed in %s tries!" % str(count))
      end = True
      break

  answer = input("Is the number (h)igher og (l)ower than the guess? ")

  if answer == "h":
      low = guess+1
  elif answer == "l":
      high = guess-1
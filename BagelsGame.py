#Inspired by AL SWEIGART. Modified by Basudev Basnet to suit the Nepali audiance.

import random
import time

MAX_DIGIT = 2
MAX_GUESS = 7


def givesSecretNum():
	numbers = list(range(10))
	random.shuffle(numbers)
	ComputerGussedNum = ''
	for i in range(MAX_DIGIT):
		ComputerGussedNum += str(numbers[i])

	return ComputerGussedNum


def givesClues(guess, secretNum):
	if guess == secretNum:
		return 'Tapai lay right guess garnu bhayo. Badai Cha!'

	clue = []

	for i in range(len(guess)):
		if guess[i] == secretNum[i]:
			clue.append('Fermi')
		elif guess[i] in secretNum:
			clue.append('Pico')

	if len(clue) == 0:
		return 'Bagles'

	clue.sort()
	return ' '.join(clue)


def checkWeatherOrNotDigit(num):
	if num == '':
		return False

	for i in num:
		if i not in '0 1 2 3 4 5 6 7 8 9'.split():
			return False
	return True


print('Tapai ko naam k ho?')
name = input()

print(name + ' Ji, Tapai lai Bagels Game ma swagat cha. Yo game ma mu %s digit guess garchu.\nTapai lay game jitna ko lagi mailayo sockako number guess garnu parnacha .' %(MAX_DIGIT))
print('''
	 SABDA			RA TASKO ARTHA
	'Fermi'			Tapi ko guess sahi cha ra sahi order ma cha
	'pico'  		Tapi ko guess sahi tara incorrrect order ma cha
	'Bangle'		Milana''')
time.sleep(1)
print('Ma Number guess gardai chu....\n')
time.sleep(10)

while True:
	secretNum = givesSecretNum()
	print('Mailay number guess garay. Tapai lay sahi answer guess garna %s mauka paunu hunaycha\n' %(MAX_GUESS))
	time.sleep(5)
	print('Suru Garum Hai')


	guessTaken = 1
	while guessTaken <= MAX_GUESS:
		guess = ''
		while len(guess) != MAX_DIGIT or not checkWeatherOrNotDigit(guess):
			print('Guess #%s: ' %(guessTaken))
			guess = input()
			


		print(givesClues(guess, secretNum))
		guessTaken += 1

		if guess == secretNum:
			break
		if guessTaken > MAX_GUESS:
			print('Tapai lay correct guess garna saknu bhayana. Sahi guess thayo: %s' %(secretNum))

	print('Tapai Yo game pheri khelna chanuhuncha. (yes or no)')
	if not input().lower().startswith('y'):
		break
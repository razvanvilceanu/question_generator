from random import randint
import keyboard
import time

def pause():
	while True:
		if keyboard.read_key() == 'q':
			break

def unique_i(intrebari):
	print("###Intrebari unice###")
	while True:
		try:

			intrebare = intrebari[randint(0, len(intrebari) -1)]
		except ValueError:
			print("Nu mai sunt intrebari!")
			exit(0)
		time.sleep(1)
		print(intrebare)
		intrebari.remove(intrebare)
		pause()

def repeat_i(intrebari):
	print("###Intrebari repetate###")
	while True:
		try:

			intrebare = intrebari[randint(0, len(intrebari) -1)]
		except ValueError:
			print("Nu mai sunt intrebari!")
			exit(0)
		time.sleep(1)
		print(intrebare)
		pause()

print(" 1. Intrebari unice \n 2. Intrebari repetate \n 3. Iesire")
choice = int(input("Alege un tip:"))

if choice == 3:
	exit(0)

# with open('intrebari clase medicamente.txt', 'r') as fin:
# 	intrebari = fin.readlines()
with open('Intrebari clase medicamente.txt', 'r') as fin:
	intrebari = fin.readlines()

print("Numar intrebari: ", len(intrebari))

if choice == 1:
	unique_i(intrebari)

elif choice == 2:
	repeat_i(intrebari)


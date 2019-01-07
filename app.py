from time import sleep as delay
import random

host = str(raw_input("Choose target (url): "))

attp = [
	"Packet",
	"Applying"
]
attf = [
	"auth.",
	"session.",
	"auth",
	"session",
	"offer",
	"offer."
]

status = {
	"OK": '\033[92m',
	"FAIL": '\033[91m',
	"UNKNOWN": '\033[93m',
	"ENCRYPTED": '\033[94m'
}

def getStatus(): # XXX
	if(random.randint(0, 7) > 6):
		return random.choice(status.keys())
	else:
		return "OK"

def init():
	a = random.randint(100, 500) # 100 -> 500

	for i in range(a):
		b = getStatus()

		print(
			str(random.choice(attp)) + " " + str(random.choice(attf)) + str(i * random.randint(0, 15)) +
			str("." * random.randint(2, 10)) + status[b] + b + '\033[0m'

		)
		delay(random.uniform(0.001, 0.2))

	print(status["OK"] + "SUCCESS!" + '\033[0m');

try:
	init()
except:
	print("a")
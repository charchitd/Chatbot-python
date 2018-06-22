import random

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'yo', 'yo!', 'hey']
random_greeting = random.choice(greetings)

question = ['How are you?', 'Hows you?', 'How are you doing?']
responses = ['Okay',"I'm fine", "i'm good"]
random_response = random.choice(responses)


while True:
	userInput = input(">>> ")
	if userInput in greetings:
		print(random_greeting)
	elif userInput in question:
		print(random_response)
	else:
		print("I did not understand what you said")

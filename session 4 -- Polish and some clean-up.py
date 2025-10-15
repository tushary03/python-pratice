#theme - clean-up and refactor

import time
print("===============================================================")
print("                      BOT v.0.4                                ")
print("===============================================================")

name = input("\nBot: howdy!, whats your name?:\n You: ")
time.sleep(0.5)
print("Processing. . .")
time.sleep(1)

user_response = input("Bot: how are you feeling today? [select one -> happy,bored,tired,excited]--[type it out]:\n You: ")
time.sleep(0.5)
print("Processing. . .")
time.sleep(1)


#mood variables to counter or reply the user response
keyword_happy = "happy"
keyword_bored = "bored"
keyword_tired = "tired"
keyword_excited = "excited"

#inside the bored elif condition needed blocks
keyword_joke = "joke"
keyword_fact = "fact"


# Functions for user response
def happy_mood():
    """ happy response reply"""
    counter_reason_h = input(f"Bot: whats the occasion or rather reason for being so happy, {name}!?[can you tell me in 2 words]\n You: ")
    time.sleep(0.5)
    print("Processing . . .")
    time.sleep(1)
    print(f"That '{counter_reason_h}' such a good reason to be happy. ")

def bored():
    """bored response reply"""
    counter_response_b = input("Bot: Oh no! Want me to tell you a random fun fact or joke?\n You: ")
    time.sleep(0.5)
    print("Processing . . .")
    time.sleep(1)
    if counter_response_b.lower() == keyword_joke:
            print ("Why don't scientists trust atoms?")
            print("Because they make up everything!")
    elif counter_response_b == keyword_fact:
            print("Honey never spoils")
    else:
        print("Bot: Wrong Input!!")

def tired():
    """tired response reply"""
    print("Bot: Try to reduce screen time and layflat on ground it might help it might help with being fatigued.")

def excited():
    """excited response reply"""
    counter_response_e = input("bot: What is the thing you are so excited for? [Describe in 2 words.]\n You: ")
    print(f"Bot: That's amazing, i hope you achieve '{counter_response_e}'.")

#logic for response by calling function.
if user_response.lower() == keyword_happy:
    happy_mood()
    print(f"\n\nBot: Hope the day goes as joyful as {user_response},Bye")
elif user_response.lower() == keyword_bored:
    bored()
    print(f"\n\nBot: Hope this helps, Bye")
elif user_response.lower() == keyword_tired:
    tired()
    print(f"\n\nBot: Have a good rest, Bye")
elif user_response.lower() == keyword_excited:
    excited()
    print(f"\n\nBot: I hope the rest of day goes same as {user_response}, bye")

else: print("\n\nBot: Wrong input, not specified!")
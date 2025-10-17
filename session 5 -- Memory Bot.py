import time
import json
import os

print("==========================================================================")
print("                       Chatbot 0.05                                       ")
print("==========================================================================")


name_user = input("Bot: Hey, whats your name?\n You: ")
time.sleep(0.5)
print("Processing. . .")
time.sleep(1)

user_mood = input("Bot: How are you feeling Today? [pick one: happy, bored, excited, hungry]\n You: ")
time.sleep(0.5)
print("Processing. . .")
time.sleep(1)

# variables for mood
keyword_happy = "happy"
keyword_bored = "bored"
keyword_tired = "tired"
keyword_excited = "excited"
keyword_hungry = "hungry"

# variables for bored fun & fact input/output
keyword_joke = "joke"
keyword_fact = "fact"

#functions for user interaction and answer question

#happy response function
def happy_mood():
    response_happy = input("Bot: What is the reason for your to be this happy\n You: ")
    time.sleep(0.5)
    print("Processing. . .")
    time.sleep(1)
    print(f"Bot: that '{response_happy}' is such a good reason to be happy and joyful")


#bored response function
def bored_mood(response_bored):
    response_bored = input("Bot: OH no!, that's not good would like to tell me a joke or fact [select any one]\n You: ")
    time.sleep(0.5)
    print("Processing. . .")
    time.sleep(1)
    if response_bored.lower() == keyword_joke:
        print("Bot: Why is sky blue? , Because god decided it to paint blue!")
        time.sleep(0.5)
        print("Processing. . .")
        time.sleep(1)

    elif response_bored.lower() == keyword_fact:
        print("Bot: You know, Honey never spoils!")
        time.sleep(0.5)
        print("Processing. . .")
        time.sleep(1)
    else: print("Bot: Error wrong input!!!\n !!!!!!!!!!!!!!!!!!!!!!!!!")

#tired response function
def tired_mood():
    response_tired = input("Bot: Are you using your phone or pc and feeling drowsiness [yes or no]")
    time.sleep(0.5)
    print("Processing. . .")
    time.sleep(1)
    if response_tired == "yes":
        print("Bot: You should take a break and a short nap")
        time.sleep(0.5)
        print("Processing. . .")
        time.sleep(1)
    elif response_tired == "no":
        print("Bot: Taking a short-nap might help.")
    else: print("Bot: Error wrong input!!!\n !!!!!!!!!!!!!!!!!!!!!!!!!")


#excited response function
def excited_mood():
    response_excited = input("Bot: Can you tell me the reason to be this excited.\n You: ")
    time.sleep(0.5)
    print("Processing. . .")
    time.sleep(1)
    print(f"That '{response_excited}' such a good thing.")

#hungry response function
def hungry_mood():
    response_hunger = input("Bot: Would like me to tell you a quick recipe for something.[yes or no]\n You: ")
    time.sleep(0.5)
    print("Processing. . .")
    time.sleep(1)
    if response_hunger == "yes":
        print("Bot: Great, Open google and type 'quick homemade snack-low effort'.\n You: ")
    else: print("Bot: Ok, you can restart the bot if u have any more queries.")

if user_mood == keyword_happy:
    happy_mood()
    print(f"Bot: Goodbye")
elif user_mood == keyword_bored:
    bored_mood()
    print(f"Hope this helps, Bye")
elif user_mood == keyword_tired:
    tired_mood()
    print(f"Hope you have a good rest, {name_user} Bye")
elif user_mood == keyword_excited:
    excited_mood()
    print(f"Bot: Goodbye")
elif user_mood == keyword_hungry:
    hungry_mood()
    print(f"Bot: Hope this helps, bye")
else: print("Bot: CHOICE DOESNT EXIST RETRY!!!")

#saving response to file (json) for new-conversation

memory_bot_data = {
    "name" : name_user,
    "mood" : user_mood

}

#writing the user data for future reference
with open("memory_for_bot.json", "w") as json_file:
    json.dump(memory_bot_data, json_file, indent = 4 )

memory = "memory_for_bot.json"

#reading the user data

with open(memory, "r")as json_file:
    memory_data = json.load(json_file)

print(memory_data)



print("=================================================================================")
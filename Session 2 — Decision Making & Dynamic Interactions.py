                      # theme - Smart bot reaction
import time

#name input function
name = input("Bot: Howdy, Whats your name?\n You: ")
time.sleep(0.5)
print("Processing . . .")
time.sleep(1)

#user response
user_response = input(f"Bot: so hey, {name} how are you feeling today?\n You: ")
time.sleep(0.5)
print("Processing . . .")
time.sleep(1)

#mood variables to counter or reply the user_response
keyword_happy = "happy"
keyword_bored = "bored"
keyword_tired = "tired"
keyword_excited = "excited"

#inside the bored elif condition neede blocks
keyword_joke = "joke"
keyword_fact = "fact"

#user responses answer giving logic

#happy response logic
if user_response.lower() == keyword_happy:
    counter_reason_h = input(f"Bot: whats the occasion or rather reason for being so happy, {name}!?[can you tell me in 2 words]\n You: ")
    time.sleep(0.5)
    print("Processing . . .")
    time.sleep(1)
    print(f"That '{counter_reason_h}' such a good reason to be happy.")

#bored response logic: this elif block contains logic for being bored and giving fact and a joke to entertain the user
elif user_response.lower() == keyword_bored:
    counter_response_b = input("Bot: Oh no! Want me to tell you a random fun fact or joke?\n You: ")
    time.sleep(0.5)
    print("Processing . . .")
    time.sleep(1)

    if counter_response_b.lower() == keyword_joke:
        reason_1 = input("Why don't scientists trust atoms?")
        print("Because they make up everything!")
    elif counter_response_b == keyword_fact:
        print("Honey never spoils")
    else: print("Bot: Wrong Input!!")

#tired advice output
elif user_response.lower() == keyword_tired:
    print("Bot: Try to reduce screen time and layflat on ground it might help it might help with being fatigued.")
#excited logical output
elif user_response.lower() == keyword_excited:
    counter_response_e = input("bot: What is the thing you are so excited for? [Describe in 2 words.]\n You: ")
    print(f"Bot: That's amazing, i hope you achieve '{counter_response_e}'.")
#last output after all above
else: print("wrong input")
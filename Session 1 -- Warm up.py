import time

# variables for input

#name input and process dummy in between next age input
name = input("Bot: whats your name \n You: ")
time.sleep(0.5)
print("Processing . . .")
time.sleep(1)

#age input and process dummy in between next interest input
age = int(input("Bot: How old are you \n You: "))

#conditional according to age of the user/guest
if age <= 18:
    print('Bot: Ah, a young explorer!')
elif age <= 30:
    print("Bot: Cool, right in your prime time!")
else: print("Bot: Wow full of wisdom and experience")

time.sleep(0.5)
print("Processing . . .")
time.sleep(1)

#interest dummy and process dummy in between final print
interest = input("Bot: what do you love doing the most \n You: ")
time.sleep(0.5)
print("Building your short bio . . .")
time.sleep(1)

#output for the small bio
print(f"Awesome here's your short bio,\n 'your name is {name} and your age is {age},\n your specially love {interest}' ")
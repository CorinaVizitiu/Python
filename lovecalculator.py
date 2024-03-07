print("Welcome to the Love Calculator! ❤️")
print("Please enter your names to check your compatibility.")

name1 = input("What is your name? ").strip()
name2 = input("What is their name? ").strip()

combined_names = name1 + name2
lower_names = combined_names.lower()

# Calculate the first digit
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

# Calculate the second digit
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# Combine digits to get the final score
score = int(str(first_digit) + str(second_digit))

# Provide a more detailed and personalized message based on the score
if (score < 10) or (score > 90):
    print(f"Your love score is {score}! You go together like coke and mentos – explosive! 💥")
elif (score >= 40) and (score <= 50):
    print(f"Your love score is {score}. You are alright together. 🌟")
else:
    print(f"Congratulations! Your love score is {score}. 💖")

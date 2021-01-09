user_input = input("Hi! What is your name?")
print("Hello", user_input, "let's talk about food.")
fstart = input("What is your favourite starter?")+(", ")
fmain = input("What is your favourite main course?")+(" and ")
fdess = input("What is your favourite dessert?")
fdrink = input("What is your favourite drink?")+(".")
meal = fstart+fmain+fdess

print("Your favourite meal is", meal, "with a glass of", fdrink)

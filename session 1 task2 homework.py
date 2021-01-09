user_input = input ("Hi! What is your name?")
print("Hello", user_input, "pick a number between 1 and 100 and I will tell you a joke!")
another = str("yes")

while another == "yes":

    choice = int(input("What number do you choose?"))

    if 0 < choice <= 25:
        print ("There are 10 types of people in this world, those who know binary and those who don't")

    if 25 < choice <= 50:
        print ("A programmer is walking along a beach and finds a lamp.  He rubs the lamp, and a genie appears.")
        print ("'I am the most powerful genie in the world.  I can grant you any wish, but only one wish.'")
        print ("The programmer pulls out a map, points to it and says, 'I want peace in the Middle East.'")
        print ("The genie responds, 'Gee, I don’t know.  Those people have been fighting for millennia.  I can do just about anything, but this is likely beyond my limits.")
        print ("The programmer then says, 'Okay, well, I am a programmer.  Please make all my users satisfied with my software and let them ask for sensible changes.'")
        print ("The genie replies 'Let me see that map again.'")

    if 50 < choice <=75:
        print ("Why is a computer so smart?")
        print ("Because it listens to its motherboard.")

    if 75 < choice <=100:
        print(user_input, "cus you're a joke...geddit? (it's mean, I know!)")


    another = str(input("Do you want to hear another? yes or no?"))

    while another not in ("yes", "no"):
        another = str(input("Do you want to hear another? yes or no?"))

    if another == "yes":
        print("Fantastic! Pick another number between 1 and 100.")
        continue

    if another == "no":
        print("FINE! BE LIKE THAT!")
        break




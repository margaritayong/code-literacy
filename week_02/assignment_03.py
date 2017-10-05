# let the user know what's going on
print ("Good Morning!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
femaleName = raw_input("Enter a female name: ")
adjective1 = raw_input("Enter one adjective: ")
color1 = raw_input("Name a bright color: ")
animal1 = raw_input("Name an animal: ")
adjective2 = raw_input("Enter one more adjective: ")
evilName = raw_input("What's your favorite villain's name: ")
animal2 = raw_input("Name a big animal: ")
gameName = raw_input("Enter your favorite game: ")
maleName = raw_input("Enter a male name: ")


# this is the story. it is made up of strings and variables.
story = femaleName + ", the " + adjective1 + " puppy with " + color1 + " fur, " \
"feels like an outsider because her neighbor, " + evilName + ", the " + animal1 + \
", told her that she actually is a " + animal2 + ". " \
"However, when " + femaleName + " tries to play " + gameName + " with other " + animal2 + "s, " \
"they rapidly ignore her. Luckily, " + maleName + " is always there for her and even though " \
"he is a white cat, he dyes his fur " + color1 + " so that " + femaleName + " doesn't feel alone." 

# finally we print the story
print (story)
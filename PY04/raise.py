# Example code to illustrate the use of "raise"
#

###########################
# Prove that the program actually starts up without problems
# and entice curious learners to figure out how this works
border = "-"

print(border*25)

print("\n\nThe program starts off running normally.\n")


#############################
# Pause for dramatic effect
from time import sleep
sleep(2)

#############################
# Resume execution

print("\nThen it runs into a situation or condition you want to address,\n")

#############################
# Pause again for dramatic effect
# No need to re-import the function since we already did
sleep(2)

print("For Example:\n\n")
sleep(2)

textblock = '''
if user_input == "%":
    raise Exception("User seems to be trying to break something on purpose.
    Terminating the program completely.")

'''

print(textblock)

# Pause slightly longer
sleep(3)

print("Now we will actually raise an exception.\n\n")

print(border*25)

#############################
# Pause again for dramatic effect
sleep(2)

#############################
# Intentionally cause an exception
raise Exception("I can do this anywhere!\n")

#############################
# Try do do something after the exception occurs
print("I survived the exception and all I got was this lousy printout.\n")

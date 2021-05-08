# Example of functions

# We have to define a function before we can use it
# Therefore, even though main() will be the starting point
# for our program, we need to define all of our functions before we 
# actually call it.

def main():
    print("From here we can now refer to other functions.\n")
    receiving_variable = function_we_will_define_below()
    print(receiving_variable)

def function_we_will_define_below():
    # We will send a single word back
    send_me_back = "Success!"
    return send_me_back

# Now that we are done defining functions we can call main()
main()

    


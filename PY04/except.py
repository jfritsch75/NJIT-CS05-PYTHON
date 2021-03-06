# This code demonstrates use of "except" for processing exceptions
# Unlike the use of "raise", which can be done anywhere in the
# program that you choose, the use of "except" requires the framework
# of "try". You can think of this as "pitch" and "catch" - first
# we will use "try" to "pitch" a block of code, and if any exceptions
# are generated, one of our "except" directives will "catch them".
#


# Initialize value1
value1 = 0

while value1 != "X":

    try:
        # Create our selection menu
        print("Exception Key:\n")
        print("* Enter 'A' to cause a ZeroDivisionError Exception.\n")
        print("* Enter 'B' to cause a TypeError Exception.\n")
        print("* Enter 'C' to print the URL for a list of Python Exception Types.\n")
        print("* Enter 'F' to force an exception.\n")
        print("* Enter 'X' to gracefully exit.\n")
        print("* Enter anything else to simply restart the loop.\n")
        value1 = input("Enter your selection: ")
        # Force uppercase to match the if statement below
        value1 = value1.upper()
        

        # Parse our selection options and take action.
        if value1 == "A":
            breakthis = 100 / 0
        elif value1 == "B":
            breakthat = 100 / value1
        elif value1 == "C":
            print("https://docs.python.org/3/library/exceptions.html\n")
            exit(0)
        elif value1 == "F":
            # You can "raise" an exception from anywhere!
            raise Exception("This is a custom message applied to the exception you just forced.\n")
            exit(4)
        else:
            pass

    # Print a custom message when we trigger a ZeroDivisionError
    except ZeroDivisionError:
        print("This is a custom message applied to all ZeroDivisionError exceptions.\n")
        exit(1)

    # Print a custom message when we trigger a TypeError
    except TypeError:
        print("***This is a custom message applied to all TypeError exceptions.\n")
        exit(2)

    # Print a custom message for any other Exception types not already
    # explicitly defined.
    except Exception:
        print("***This is a custom message applied to any exception that is not a ZeroDivisionError or TypeError.\n")
        exit(3)

    # Explicitly confirm that no exceptions occurred
    else:
        print("***No exceptions were encountered.\n")

    # Execute some "clean up" or "housekeeping" if/as required
    finally:
        print("***This line will print out no matter what is chosen\n")


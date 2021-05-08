def show_name():
    print(f"The value of __name__ in module anything is {__name__}")

def main():
    print("This only runs if I execute this program directly.\n")

if __name__ == '__main__':
    main()



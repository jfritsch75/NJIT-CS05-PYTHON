import name1 as name1
import name2 as name2
import anything as anything

def show_name():
    print(f"The value of __name__ in the main program is {__name__}")

def main():
    show_name()
    name1.show_name()
    name2.show_name()
    anything.show_name()

if __name__ == '__main__':
    main()



import firstprogram as fp
import name2 as name2
import anything as anything

def show_name():
    print(f"The value of __name__ in the main program is {__name__}")

def main():
    show_name()
    fp.show_name()
    name2.show_name()
    anything.show_name()

if __name__ == '__main__':
    main()



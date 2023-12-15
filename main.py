import os

def main():
    """Main function of the program"""
    print("Hello World!")
    print(os.system("ls -l"))
    print(os.system("pwd"))
    print("Finished!")
    print("New changes")


if __name__ == "__main__":
    main()

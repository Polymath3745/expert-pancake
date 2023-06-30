def main():
    x = int(input("What's x? "))
    print("x squared is ", square(x))

def square(n):
    return n + n 

# this is so when I import this file in another, the main function
# of this file will not run as well.
if __name__ == "__main__":
    main()
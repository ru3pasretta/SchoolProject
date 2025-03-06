def get_random_number(n):
    return random.randint(0, n)

def main():
    print("Welcome to the Random Number Generator!")
    number = int(input("Enter a number: "))
    print("Your randomly generated number is", get_random_number(number))

if __name__ == "__main__":
    main()

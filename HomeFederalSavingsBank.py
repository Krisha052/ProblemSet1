
def main():
    greeting = input("Greeting: ")
    amount = greeting_money(greeting)
    print(f'${amount}')

def greeting_money(greeting):
    g = greeting.strip().lower()
    if g.startswith("hello"):
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
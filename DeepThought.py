
def main():
    question = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
    question = question.lower().strip() #strings are immutable so we need to create a new one
    
    if question in ['42', 'forty-two', 'forty two']:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
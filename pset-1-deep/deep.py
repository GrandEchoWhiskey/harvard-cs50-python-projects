QUESTION = "What is the Answer to the Great Question of Life, the Universe, and Everything? "

def main():
    answer = input(QUESTION)
    answer = answer.replace(" ", "")
    answer = answer.lower()
    passing = ["42", "fortytwo", "forty-two"]
    if answer in passing:
        print("Yes")
        return
    print("No")
    return

if __name__ == "__main__":
    main()
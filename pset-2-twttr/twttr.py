lowercase = ['a', 'e', 'i', 'o', 'u']

def main():

    new_str = ""
    inp = input("Input: ")

    for char in inp:

        if char.lower() in lowercase:
            continue

        new_str += char

    print("Output: " + new_str)
    
    return

if __name__ == "__main__":
    main()
fruits = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'strawberries': 50,
    'sweet cherries': 100,
    'watermelon': 80
}

def main():

    f = input("Item: ").lower()
    if f in fruits.keys():
        print("Callories: " + str(fruits[f]))

    return

if __name__ == "__main__":
    main()
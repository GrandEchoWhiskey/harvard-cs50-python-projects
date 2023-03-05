[<- Back to course](../README.md)

<p align="center"><a href="https://cs50.harvard.edu/python/2022/">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/course/harvard100.png" /><br>
</a></p>
<h1 align="center">CS50's Introduction to Programming with Python<br><br>Plates</h1>

<p align="center"><a href="#">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/programming/python.png" />
</a></p>

### Background:
#### Plate Checker
The code provided checks whether a given vehicle license plate is valid or not. A plate is considered valid if it satisfies the following criteria:

- The length of the plate should be between 2 and 6 characters.
- The plate should consist of only alphanumeric characters (A-Z, 0-9).
- The first or the second character should be an alphabet (A-Z).
- The plate should alternate between alphabet and numeric characters, starting with an alphabet.

The is_valid() function takes a string as input and returns a Boolean indicating whether the input string satisfies all the above conditions or not. The main() function takes user input for the plate string and then prints "Valid" or "Invalid" based on the output of the is_valid() function.

The alpha list contains all the uppercase alphabets, and the digit list contains all the digits from 0 to 9. The is_valid() function checks if each character in the input string is either an alphabet or a digit. If the character is neither an alphabet nor a digit, the function immediately returns False. If the length of the string is less than 2 or greater than 6, the function also returns False.

The function then checks whether the first or the second character of the string is an alphabet. If not, the function returns False. The function then checks that the characters in the string alternate between alphabets and digits, starting with an alphabet. If any of these conditions are not met, the function returns False.

If all the conditions are met, the function returns True, indicating that the input string is a valid vehicle license plate.

### Getting Started:
Export this directory using SVN.
```
svn export https://github.com/GrandEchoWhiskey/harvard-cs50-python-projects/trunk/pset-2-plates
```
Change directory
```
cd pset-2-plates
```
Now run the script
```
python plates.py
```

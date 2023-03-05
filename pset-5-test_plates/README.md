[<- Back to course](../README.md)

<p align="center"><a href="https://cs50.harvard.edu/python/2022/">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/course/harvard100.png" /><br>
</a></p>
<h1 align="center">CS50's Introduction to Programming with Python<br><br>Test Plates</h1>

<p align="center"><a href="#">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/programming/python.png" />
</a></p>

### Background:
#### Test bank.py
This is a unit test for the is_valid function in the plates module. This function checks if a given vehicle plate is valid or not. A valid plate should have the following characteristics:

- Have exactly six characters (letters or digits)
- Start with two letters
- End with four digits
- Not contain any symbols other than letters or digits
- Not start with a zero

The unit test contains seven test cases:

- `test_ok`: Test for a valid plate
- `test_too_long`: Test for a plate with more than six characters
- `test_too_short`: Test for a plate with less than six characters
- `test_starting_number`: Test for a plate that does not start with two letters
- `test_letter_after_number`: Test for a plate that ends with a letter instead of a digit
- `test_symbols`: Test for a plate that contains symbols other than letters or digits
- `test_zero_placement`: Test for a plate number that starts with 0

If any of these test cases fail, it means that the is_valid function does not behave as expected and needs to be fixed.

To run the unit tests, simply execute the script. If all tests pass, there will be no output. If a test fails, an error message will be printed to the console.
### Getting Started:
Export this directory using SVN.
```
svn export https://github.com/GrandEchoWhiskey/harvard-cs50-python-projects/trunk/pset-5-test_plates
```
Change directory
```
cd pset-5-test_plates
```
Now test the script
```
pytest test_plates.py
```
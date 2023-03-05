[<- Back to course](../README.md)

<p align="center"><a href="https://cs50.harvard.edu/python/2022/">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/course/harvard100.png" /><br>
</a></p>
<h1 align="center">CS50's Introduction to Programming with Python<br><br>Test Bank</h1>

<p align="center"><a href="#">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/programming/python.png" />
</a></p>

### Background:
#### Test bank.py
The value function takes a string argument and returns an integer value based on the first word in the string:

If the first word is "hello", the function returns 0
If the first word starts with the letter "h" (case-insensitive), but is not "hello", the function returns 20
Otherwise, the function returns 100.
The TestSum class contains six test cases, each with an input string and the expected output value from the value function. The test cases cover different scenarios for both lower and upper case letters.

The unittest.main() function is called to run the test cases and print the results. If any of the tests fail, an error message will be printed with details about the expected and actual results.

### Getting Started:
Export this directory using SVN.
```
svn export https://github.com/GrandEchoWhiskey/harvard-cs50-python-projects/trunk/pset-5-test_bank
```
Change directory
```
cd pset-5-test_bank
```
Now test the script
```
pytest test_bank.py
```

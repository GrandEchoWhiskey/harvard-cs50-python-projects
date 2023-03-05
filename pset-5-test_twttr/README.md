[<- Back to course](../README.md)

<p align="center"><a href="https://cs50.harvard.edu/python/2022/">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/course/harvard100.png" /><br>
</a></p>
<h1 align="center">CS50's Introduction to Programming with Python<br><br>Test Twttr</h1>

<p align="center"><a href="#">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/programming/python.png" />
</a></p>

### Background:
#### Test twttr.py
This is a simple program that takes a string and returns a shortened version of it. The program is implemented in twttr.py. There is also a test suite implemented in test_twttr.py using the unittest framework.

The shorten function takes a string as input and returns a shortened version of it. The function performs the following operations:

- It removes all numbers from the string.
- It removes all punctuation marks from the string.
- It converts all vowels (both uppercase and lowercase) to their respective consonants (B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z) and leaves all consonants unchanged.
- It returns the shortened string.

The test suite in test_twttr.py includes five test cases to ensure that the shorten function works as expected:

- test_output checks that the shorten function returns the same string if no changes are made.
- test_lower checks that the shorten function correctly converts all lowercase vowels to consonants.
- test_upper checks that the shorten function correctly converts all uppercase vowels to consonants.
- test_numbers checks that the shorten function removes all numbers from the string.
- test_punctuation checks that the shorten function removes all punctuation marks from the string.

### Getting Started:
Export this directory using SVN.
```
svn export https://github.com/GrandEchoWhiskey/harvard-cs50-python-projects/trunk/pset-5-test_twttr
```
Change directory
```
cd pset-5-test_twttr
```
Now test the script
```
pytest test_twttr.py
```
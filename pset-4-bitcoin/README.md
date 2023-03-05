[<- Back to course](../README.md)

<p align="center"><a href="https://cs50.harvard.edu/python/2022/">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/course/harvard100.png" /><br>
</a></p>
<h1 align="center">CS50's Introduction to Programming with Python<br><br>Bitcoin</h1>

<p align="center"><a href="#">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/programming/python.png" />
</a></p>

### Background:
#### Converting Bitcoin to USD
This program fetches the current Bitcoin to USD exchange rate from the CoinDesk API and converts the given Bitcoin amount to USD based on the input provided through the command-line argument.

The program checks for the presence of the command-line argument and validates whether it is a number or not. If the argument is not a number or if it is missing, an appropriate error message is displayed.

The program then fetches the current Bitcoin to USD exchange rate from the CoinDesk API and calculates the equivalent USD value of the provided Bitcoin amount. The result is displayed with the dollar sign and comma separators.

### Getting Started:
Export this directory using SVN.
```
svn export https://github.com/GrandEchoWhiskey/harvard-cs50-python-projects/trunk/pset-4-bitcoin
```
Change directory
```
cd pset-4-bitcoin
```
Now run the script
```
python bitcoin.py
```

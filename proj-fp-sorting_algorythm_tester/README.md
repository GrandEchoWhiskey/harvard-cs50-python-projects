[<- Back to course](../README.md)

<p align="center"><a href="https://cs50.harvard.edu/python/2022/">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/course/harvard100.png" /><br>
</a></p>
<h1 align="center">CS50's Introduction to Programming with Python<br><br>Final Project<br>Sorting Algorythm Tester</h1>

<p align="center"><a href="#">
  <img src="https://github.com/GrandEchoWhiskey/grandechowhiskey/blob/main/icons/programming/python.png" />
</a></p>

#### Video Demo:  [youtu.be/vaul02EMQoY](https://youtu.be/vaul02EMQoY)

### Description:

Easy to use python sorting module tester. It shows sorting time of few different algorythms.
Initially added:
- quick sort
- merge sort
- shell sort
- heap sort
- boubble sort

Usage:
```
python project.py <sorted, reversed, random> length [*alogythms | all]
```

#### Your algorythm is not included or you want to create own algorythm?
Nothing easier than that. Just create your python file and create a "sort" function with one argument: the list you want to sort. 
The created file is now a module. Open project.py and insert the module name (filename without .py extension) in the IMPORTABLE list.

Use below to run your algorythm:
```
python project.py random 1000 your_module_name
```

#### Files:
- project.py - main project file - includes the sorting modules, and connects them with the user interface.
- test_project.py - project unittests - tests the functions of project.py
- quicksort.py - sorting module - quick sort module
- mergesort.py - sorting module - merge sort module
- shellsort.py - sorting module - shell sort module
- heapsort.py - sorting module - heap sort module
- bubblesort.py - sorting module - bubble sort module


### Getting Started:
Export this directory using SVN.
```
svn export https://github.com/GrandEchoWhiskey/harvard-cs50-python-projects/trunk/proj-fp-sorting_algorythm_tester
```
Change directory
```
cd proj-fp-sorting_algorythm_tester
```
Now run the script
```
python project.py
```

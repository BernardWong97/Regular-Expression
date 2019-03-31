# Graph Theory Project (Regex|NFA)

Project for Graph Theory course module. A program that can
build a non-deterministic finite automaton (NFA) from a regular expression,
and can use the NFA to check if the regular expression matches any given
string of text.

## Getting Started

Clone this git repo to download the program's script files.

### Prerequisite

```
Python 3 and above
```

## Running the program

### Run
The "runner.py" script file is the main script of the program.

Suppose the script is in "C:\Regular-Expression\runner.py" or ~/Regular-Expression\runner.py on Unix-like systems.

To run the program, open your machine's terminal/command prompt:

#### Windows

```
- Open Command Prompt:    Start menu -> Run  and type cmd
- Type:     D:\Anaconda\python.exe C:\Regular-Expression\runner.py
- Note: The first path is where your python CLI executable is located, Python is not installed in this path, change the path accordingly.
```

#### Mac OS X

```
- Open Terminal:   Finder -> Go menu -> Applications -> Terminal
- Type:     python ~/Regular-Expression\runner.py
```

#### Linux

```
- Open a command prompt (e.g. xterm)
- Type:     python ~/Regular-Expression\runner.py
```

### Usage

- This will be display if the program runs correctly:
```
=== Welcome To Regular Expression String Matching Program ===
This program supports 5 regular expression's metacharacters:
    * : 0 or more
    + : 1 or more
    ? : 0 or 1
    . : concatenate
    | : one or the other
Please input regular expression in infix notation:
```
- Input a regular expression, for example:
```
(L.e+.r.o+.y+)|(J.e?.n.k.i+.n.s*)
```
- It will then ask for a string for matching, do enter a string:
```
Please input a string for matching:
LeeEeerooooOOOoooooyyyYYYYYYYyyyyyy
```
- After input, it will ask if the matching should be case sensitive or not:
```
Do you want case sensitive matching? (Y/N)
n
```
- The result should be display as below:
```
Result of matching "(L.e+.r.o+.y+)|(J.e?.n.k.i+.n.s*)" and "LeeEeerooooOOOoooooyyyYYYYYYYyyyyyy" = "True"
```
- The program then prompt for continuous matching:
```
New matching? (Y/N)
n
Thank you for using Regular Expression String Matching Program!
=== Bye Bye! ===
```

## Running the tests

A test script is available to test all the functions within the program.
To run the test script, same as how you run the runner but change the file name in the path to "regex_test.py".

## Script files

These script files supply different functions to the program.

#### shunting_yard.py
Uses Shunting Yard Algorithm to convert infix expression to postfix expression.

#### thompsons.py
Transform postfix expression into NFA.

#### regular_expression.py
Takes in a regular expression postfix notation, a string and a boolean for case insensitivity (default is false).  
If the regular expression have no '.' operator, will add the operator into it ( like "abcd" become "a.b.c.d").  
Matching the regular expression and the string (both case sensitive and insensitive).

#### runner.py
The main function of the program which responsible for user interactions.

#### regex_test.py
The unit testing script of the program.

## Warning

<b>The program will not detect for faulty regular expression input.</b>

## Researches

These are the references/researches to help build the program:
- Regular Expression
    - [Python re library](https://docs.python.org/2/library/re.html)
    - [Wikipedia Regular Expression](https://en.wikipedia.org/wiki/Regular_expression)
    - [w3schools python regex](https://www.w3schools.com/python/python_regex.asp)
    - [Regex operator precedence StackOverflow](https://stackoverflow.com/questions/36870168/operator-precedence-in-regular-expressions)
    - [POSIX extended regex syntax](https://www.boost.org/doc/libs/1_56_0/libs/regex/doc/html/boost_regex/syntax/basic_extended.html#boost_regex.syntax.basic_extended.operator_precedence)
    - [Regular expression metacharacters](https://help.relativity.com/9.3/Content/Relativity/Regular_expressions/Regular_expression_metacharacters.htm)
    - [Python Doc how to regex](https://docs.python.org/3/howto/regex.html)
- Non-deterministic Finite Automaton (NFA)
    - [Wikipedia NFA](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
    - [Building a RegExp machine Part 1,2](https://medium.com/@DmitrySoshnikov/building-a-regexp-machine-part-1-regular-grammars-d4986b585d7e)
    - [Regular Expression to NFA](https://www.youtube.com/watch?v=RYNN-tb9WxI)
- Documenting functions
    - [Docstrings in Python](https://www.datacamp.com/community/tutorials/docstrings-python)
    - [Python Project Documentation](https://docs.python-guide.org/writing/documentation/)
    - [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)
    - [Devguide Documenting Python](https://devguide.python.org/documenting/)
- Unit testing
    - [Getting Started With Testing in Python](https://realpython.com/python-testing/)
    - [Python Doc Unit testing framework](https://docs.python.org/3/library/unittest.html)
    - [Testing Your Code](https://docs.python-guide.org/writing/tests/)

## Author

* [**Bernard Wong**](https://github.com/BernardWong97)
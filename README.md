# CPSC-323-Project-01
This is Raxel Ortiz and Alan Cortez group submission for CPSC 323-02 project 1.

## Set up
We developed this this lexer analyzer using Python. To get started be sure to:
1. have python with a version greater or equal to 3 installed
2. install the tabulate pip library
3. and to clone the repository [(read more here)](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

## How it works

Our program works by essentially reading the input text that is provided inside of `source_code.txt` and converts that information into a string. This string is then used in our `lexer()` function to essentially loop through all of the input and compare each character to see what type it is. Our main types of states are: identifiers, keywords, real (numbers), assignment (arithmetic), seperator, and operators. In our `lexer()` function we use simple REGEX patterns to compare the current character and see if it matches any of our states. When it finds a satisfactory match then we append that Token and Lexen into an array which we return once we reach the end of the input string. Finally we just open our `output.txt` file and print the tokens inside of that file.

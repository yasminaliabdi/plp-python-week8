# Personal Mini-Toolkit

## What This Project Does
This is a menu-driven Python program that brings together variables, loops, conditionals, and lists. It offers three different interactive tools.

## How to Run
1. Open your terminal.
2. Navigate to the project folder.
3. Run the command: `python toolkit.py`

## Tools Included
1. **Simple Calculator** - Performs basic math (+, -, *, /) using conditionals.
2. **To-Do List** - Allows you to add, view, and remove tasks using a list and a loop.
3. **Number Guessing Game** - A loop-based game using random numbers and conditionals.

## Reflection
The hardest part of this project was making sure the menu loop worked properly and didn't crash when the user typed an invalid choice. The bug that took the longest to fix was handling the `ValueError` in the calculator when the user typed a letter instead of a number. I had to use a `try/except` block to catch it. If I had one more week, I would add a feature to save the To-Do list to a text file so it remembers the tasks even after the program closes.
# Gathering Fee Calculator

## Background
When you hanging out with your friends, you may encounter a situation that someone pay the bills(resturants, party, etc) for everyone first, after fews days, you have no idea how much you should pay / receive because the bills were a complete mess.  

## Program I/O
- Input: A 2D list in JSON format
    - e.g. [["PersonA", 30, "PersonB"], ["PersonA", 20, "PersonC"], ["PersonD", 20, "PersonA"]...]
    - ["PersonA", 30, "PersonB"] represents PersonA lends PersonB $30
    - The data type of "PersonA" and "PersonB" must be str, 30 must be either int or float
- Output: Stdout showing each person's receivable, payable and net flow (receivable - payable)
    - PersonA's receivable is: 30(PersonB) + 20(PersonC) = 50.0
    PersonA's payable is: 20(PersonD) = 20.0
    PersonA's net flow is: 50.0 - 20.0 = 30.0

## File Structure
- .devcontainer/: Settings of VSCode lcoal development with container
- .gitignore
- *_main.py: Main program
- people.py: a module
- person.py: a module
- transaction.py: a module
- Dockerfile: Used for creating container
- requirements.txt: Listing dependencies for container to install
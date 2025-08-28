Group Members: 
Abdallah Aliyu Ahmad - 211103094
Ubong Clement - 211103005
Aminu Abubakar - 211103099

#ABOUT PROJECT :
This project simulates the "Monty Hall problem", a famous probability puzzle based on a game show scenario:

1. A car is hidden behind one of 3 doors, and goats are behind the others.  
2. The player picks one door.  
3. The host (Monty) opens a different door that always reveals a goat.  
4. The player can either "stay" with their original choice or "switch" to the other unopened door.  

Mathematically:
- If the player "stays", the chance of winning is "1/3".  
- If the player "switches", the chance of winning is "2/3".  

This program demonstrates this principle by running multiple simulations and plotting the results.

How to Run Using Codespaces:
You can run this project directly in your browser using GitHub Codespaces:

Go to this repository on GitHub.

Click the green "Code" button, then choose the Codespaces tab.

Select "Create codespace on main".

Wait for the Codespace to load (it opens an online VS Code environment).

Open the integrated terminal in Codespaces and run: Monty Hall.py

Example output:
Demo of a single game (verbose mode):
Car is behind door 1
Player chose door 0
Monty opened door 2 (goat)
Player SWITCHES to door 1
Player WINS!
------------------------------
Out of 10000 trials with 3 doors:
  Staying won 3301 times (33.01%)
  Switching won 6699 times (66.99%)


# Google Mexico - Software Engineering Interview 🇲🇽

Round 1 of the interview process for the Software Engineer III position in Google Mexico.

As usual, I didn't pass the interview. Life sucks, programming sucks, everything sucks :unamused:

## Problem statement 📋

In a board composed of 'L', 'R', and '_' characters, like "R__LR_R_L", a move consists of either replacing one occurrence of "\_L" with "L\_", or replacing one occurrence of "R\_" with "\_R". 
Given the starting board and the ending board, Implement an algorithm to check if there exists a sequence of moves to transform the starting board to the ending board.

Examples:
```
starting_board = "_LLR_L_L"
ending_board   = "LL__RLL_"

OUTPUT: True
```
```
starting_board = "RL"
ending_board   = "LR"

OUTPUT: False
```

## Solution :pencil:

If the number of Ls or Rs are different in the starting board and the ending board, we return False.

Also, the Ls and Rs in both boards must appear in the same order, an L can't "jump" an R and viceversa. If the letters appear in different order, we return False.

Then, we create the following lists to compare the indices of the Ls in both boards:
- **starting_L:** Indices of the Ls in the starting board
- **ending_L:** Indices of the Ls in the ending board

If the i<sup>th</sup> L in the starting board is at index j and its corresponding L in the ending board is at index k, such that j < k, then the ending board can not be obtained from the starting board in any number of moves because Ls can not be swapped to the right.

Hence, it is enough to check if ```starting_L[i] < ending_L[i]```. If the comparison evaluates to True, we return False.

The same goes for the Rs. We create the following lists:
- **starting_R:** Indices of the Rs in the starting board
- **ending_R:** Indices of the Rs in the ending board

And then we check if ```starting_R[i] > ending_R[i]```. Since Rs can not be swapped to the left, if the comparison evaluates to True we return False.

## Time Complexity :mag_right:

The time complexity of the algorithm is ***O(N)*** where $N$ is the size of the board.

## Space Complexity :mag_right:

The space complexity of the algorithm is ***O(|starting_L| + |starting_R| + |ending_L| + |ending_R|)*** because of the 4 auxiliary lists

However, notice that |starting_L| + |starting_R| + |ending_L| + |ending_R| $\leq$ $N$

Hence, the overall space complexity will be ***O(N)***, where $N$ is the size of the board.

---
⌨️ with ❤️ by [Johann Gordillo](https://github.com/JohannGordillo) 😊

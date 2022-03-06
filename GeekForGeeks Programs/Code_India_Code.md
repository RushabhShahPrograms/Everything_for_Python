# Minimum Moves

You are given two positive integers, ** A ** and ** B **.

In one move, you can perform any of the following operations

1. Add 1 to ** A **, i.e. update A=A+1
2. Add 1 to ** B **, i.e. update B=B+1
3. Pick any non-negative integer ** X ** and update ** A = A | X **
  - Here " | " represents the Bitwise Or operator.
  - ** Note: ** You can choose different ** X ** in different moves.


Print the minimum number of moves required to make ** A ** and ** B ** equal.


** Input Format: **
The first line of the input contains a single integer ** T ** denoting the number of test cases.

The descriiption of ** T ** test cases is as follows:
- The first and only line of each test case contains two space-separated positive integers, ** A ** and ** B **.


** Output Format: **
For each testcase, print the minimum number of moves required to make ** A ** and ** B ** equal followed by a newline character.

** Note: ** Generated output is white space sensitive, do not add any extra space on the unnecessary new line characters.


** Constraints: **
- 1<= ** T ** <=10^5
- 1<= ** A,B ** <=10^18


** Example: **
```
** Sample Input: **
3
1 3
7 24
10 1

** Sample Output: **
1
2
9

** Explanation: **
Testcase 1:
Choose X = 2 and apply third move
now A = A | 2 = 3
Hence, one move was required.
Testcase 2: 
Choose X = 16 and apply third move
now A = A | 16 = 23
Apply the first move 
now A = A + 1 = 24
Hence, two move was required.
```

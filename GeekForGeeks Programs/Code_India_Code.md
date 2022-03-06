# Minimum Moves

You are given two positive integers, **A** and **B**.

In one move, you can perform any of the following operations

1. Add 1 to **A**, i.e. update A=A+1
2. Add 1 to **B**, i.e. update B=B+1
3. Pick any non-negative integer **X** and update **A = A | X**
  - Here " | " represents the Bitwise Or operator.
  - **Note:** You can choose different **X** in different moves.


Print the minimum number of moves required to make **A** and **B** equal.

**Input Format:**

The first line of the input contains a single integer **T** denoting the number of test cases.

The descriiption of **T** test cases is as follows:
- The first and only line of each test case contains two space-separated positive integers, **A** and **B**.

**Output Format:**

For each testcase, print the minimum number of moves required to make **A** and **B** equal followed by a newline character.

**Note:** Generated output is white space sensitive, do not add any extra space on the unnecessary new line characters.

**Constraints:**
- 1<= **T** <=10^5
- 1<= **A,B** <=10^18

**Example:**
```
Sample Input:
3
1 3
7 24
10 1

Sample Output:
1
2
9

Explanation:
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

**Solution:**
```
#Solution please
```

# Split The Array

You are given an array **A** of length **N**. You can split the array into non-empty consecutive subarrays. Different subarrays can have different lengths, and every element in the array should be included in exactly one subarray. If the **ith** element of the array is at the **jth** position in the kth subarray, then it adds the following beauty to the array:
• (-1)^(j+k)%2* Ai


Find the **maximum** beauty obtainable by optimally partitioning the array.

**Input Format:**

The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases is as follows:
- The first line of each test case contains an integer **N** - the array's length.
- The second line of each test case contains **N** space-separated integers - **A1, A2,...AN**


**Output Format:**

For each test case, print the **maximum** beauty obtainable by optimally partitioning the array followed by a newline character.

**Note:** Generated output is white space sensitive, do not add any extra spaces on unnecessary newline characters.

**Constraints:**
- 1<= **T** <=2500
- 1<= **N** <=10000
- 0<= **|Ai|** <=10^9


**Example:**
```
Sample Input:
4
6
7 -9 -2 8 7 -6
5
6 2 2 7 6
5
7 1 7 5 4
4
-1 -6 -9 -8

Sample Output: 
39
15
14
6

Explanation: 
Test Case 1: 
One optimal way is to split the 
array as [7, -9][-2, 8][7, -6]. 
For i = 1, the value of j and k 
are 1 and 1 respectively,
For i = 2, the value of j and k 
are 2 and 1 respectively,
For i = 3, the value of j and k 
are 1 and 2 respectively,
For i = 4, the value of j and k 
are 2 and 2 respectively,
For i = 5, the value of j and k 
are 1 and 3 respectively,
For i = 6, the value of j and k 
are 2 and 3 respectively,
The beauty is +7-(-9)-(-2)+8+7-(-6)= 39
Test Case 2: 
One optimal way is to split the 
array as [6, 2] [2, 7] [6]. 
The beauty is +6-2-2+7+6= 15.
```

**Solution:**
```
#solution please
```

# The Duality Task

The duality of array A is defined as the maximum length among all non-empty subsequences of array A whose Greatest Common Divisor is greater than 1.

You are given two arrays, **A** and **B**, of the same size **N**. Consider a new array **C** of size **N** initially equal to **A**. In one operation, you can replace any element of **C** with any value. The beauty of array **C** is defined as the number of indices **i** (1<=i<=N) where **Ci** and **Bi** have the **same** value.

Find the **maximum** possible beauty of array **C** such that the duality of array **C** is **greater than or equal** to the duality of array **A** by performing any number of operations.

**Input Format:**

The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases is as follows:
- The first line of each test case contains integer **N**, the array **A** and **B** size. 
- The second line contains **N** space-separated integers **A1, A2,.., AN**. 
- The third line contains **N** space-separated integers, **B1, B2,--, BN**.


**Output Format:** 

For each test case, print the maximum possible answer followed by a newline character.

**Note:** The generated output is white space sensitive, do not add any extra spaces on unnecessary newline characters.

**Constraints:**
- 1<= **T** <= 10^4 
- 1<= **N** <=2 * 10^5 
- 1<= **Ai, Bi** <= 10^6 

the sum of **N** over all test cases does not exceed 5 * 10^5



**Example:**
```
Sample Input:
2
3
3 2 6
3 6 6
1
2
4

Sample Output:
3
1

Explanation:
Testcase 1: 
All possible non-empty subsequences 
of array A whose gcd is greater than
1 are [3], [2], [6], [3, 6], [2, 6]
The length of the longest such 
sequence is 2,
hence duality of array A is 2.

Initially, the array C = [3, 2, 6]. 
It is optimal to change the second 
element of array C to 6. 
Now array C = [3, 6, 6]
The  duality of array C is 3, 
which is greater than the duality of 
array A and the number of indices 
where Ci and Bi are the same is 3.
Hence maximum possible beauty will be 3.
```

**Solution:**
```
#solution please
```

# Special Number Count

**Special Number:** It is a positive integer with the greatest common divisor of the sum of **quartic** power of its digits and the **product** of its digits greater than **1**.

For example, 123 is a **special number**. (sum of quartic power of its digits = 14 + 24 + 34 = 1 + 16 +81 = 98 and the product of its digits = 1*2*3=6. The greatest common divisor of 98 and 6 is 2, which is greater than 1)

You are given an integer **n**, calculate the number of special numbers **x (1 <= x <= n)**.

**Input Format:** 

The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases is as follows:
- The first and the only line of each test case contains an integer **n**.

**Output Format:** 

For each test case, print the number of special numbers **x (1 <= x <= n)** followed by a newline character. **Note:** Generated output is white space sensitive, do not add any extra spaces on unnecessary newline characters.

**Constraints:** 
- 1 <= **T** <= 5
- 1 <= **n** <=10^8

**Example:**
```
Sample Input:
2
2
101

Sample Output:
1
43

Explanation:
Testcase 1: 
for x = 1
sum of quartic power of digits = 14 = 1
product of digits = 1
Greatest common divisor of 1 and 1 is 1
hence 1 is not a special number.

for x = 2
sum of quartic power of digits = 24 = 16
product of digits = 2
Greatest common divisor of 16 and 2 is 2
hence 2 is a special number

Testcase 2: 
All special numbers ≤ 101 are
{2, 3, 4, 5, 6, 7, 8, 9, 20, 22, 
24, 26, 28, 30, 33, 36, 39, 40, 
42, 44, 46, 48, 50, 55, 60, 62, 
63, 64, 66, 68, 69, 70, 77, 80, 
82, 84, 86, 88, 90, 93, 96, 99, 101}
```

**Solution:**
```
#solution please
```

# GCD as Linear Combination of 2 Integers

## Introduction
This is a part in the GCD (Greatest Common Divisor) section in the Discrete Mathematics course. According to one of their theorems, a GCD of any two numbers (a and b)
can be written as a linear combination of these two numbers with integer coefficients, that is: gcd = ax + by. <br>
This algorithm (called Extended Euclidean Algorithm) deals with this problem. <br>

## Input
Two integers a and b seperated by space. The integer a can be the same or larger or smaller than b, but in the code we will automatically set a as the larger one.

## Output
Two integers (call them x and y), they are coefficients satisfying the following equation: gcd = ax + by

## Sample Input
Input: 6 14 <br>
Output: -2 1 <br>
Explaination: GCD of 6 and 14 is 2, so we have: 2 = 6 x (-2) + 14 x 1 <br>
<br>
Input: 0 0 <br>
Output: 1 0 <br>
Explaination: It's commonly accepted that gcd(0,0) is 0, so 0 = 1 x 0 + 0 x 0 <br>
<br>
Input: 10 10 <br>
Output: 1 0 <br>
Explaination: GCD(a,a) = a so 10 = 10 x 1 + 10 x 0


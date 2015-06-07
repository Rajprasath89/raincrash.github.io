---
author: sricharanchiruvolu
comments: true
date: 2013-12-07 13:19:00+00:00
layout: post
slug: algorithm-analysis-counting-the-number-of-steps
title: 'Algorithm analysis: Counting the number of steps'
wordpress_id: 159
---

Counting the no.of steps required for an algorithms determines time complexity (i.e. the time required for the program to execute, in terms of time). To get the exact timing information without actually running it is something that we probably can't do. 

Consider the following python code:
    
    <code><br></br>1 def count(x):<br></br>2  y = 0<br></br>3  while x > 0:<br></br>4   x = x - 5<br></br>5   y = y + 1<br></br>6  print y<br></br>7 print count(50)<br></br></code><br></br>

Now, How can we find the time complexity of the above code? It executes a statement, and then it goes into a while loop and repeats these two statements some number of times. Then when it's all done, it does one more statement. We didn't talk about the number of steps that it take to do a print statement if there's a function, but we're going to call it one for the print statement plus however many steps it takes to execute the function call.

It starts off at 50, going to go down by 5s until it hits 0. There is going to be 10 times that it's executing these two statements. That's 20,21,22, and the print statement is 23.

What if we just say we don't know what n is. Someone is going to tell us n later. We're like to know the number of steps, the amount of time that it takes to execute this formula, as a function of n. 
    
    <code><br></br>1 print count(n)<br></br></code><br></br>

As x is counting down by 5s, it's going to keep doing this until it gets to be 0 or less.It's like whatever this x is, which is really whatever this n is, divided by 5 but rounded up, because if you have something like 6, x is going to be 6. It's going to do this loop. X is going to get decremented to 1. It's going to do it again. The only way that it wouldn't have done that if it was exactly 5. Put 5 in, it executes it once. Subtract 5 away form it and end up with 0. It doesn't repeat the loop at that point. What we really want here is to take n divided by 5 and round it up. This `math.ceiling `function does that. It rounds a non-integer number up to the nearest integer. That's the number of times that these two statements are going to be executed. We multiply that by 2, and then there's 3 other statements that are going to get executed.This formula will actually tell us the number of steps as a function of n that this countdown will do.Here's the actual formula.
    
    <code><br></br>1 steps  = 3 + 2 * math.ceil(n/5.0)<br></br></code>

Now consider the following code:
    
    <code><br></br>1 def pro(a,b):<br></br>2  x = a; y = b<br></br>3  z = 0<br></br>4  while x > 0:<br></br>5   z = z + y<br></br>6   x = x - 1<br></br>7  return z<br></br></code>

If you didn't figure it out yet, the above code will execute the product of two numbers! Yeah, It's just it. The product of two numbers, no big deal. The time complexity of the above function would be `2*a + 3`. Since, there are three simple, one unit-time statements and the loop requires `2*a `times to execute. 

The final example, consider the **Russian Peasants Algorithm**, also called Ancient Egyptian Algorithm. The algorithm used to multiply numbers before the invention of computers.
    
    <code><br></br>1 def RPA(a,b):<br></br>2  x = a; y = b<br></br>3  z = 0<br></br>4   if x % 2 == 1: z = z + y<br></br>5   y = y << 1<br></br>6   x = x >> 1<br></br>7  return z<br></br></code>

Counting the Number of steps in Russian Peasants Algorithm:

The number of times the loop is executed is same as the number of steps required to for x to be 0, halved every time. So, How many times can you divide a number X in half (rounding down) before it hits zero? The answer would be `[log2X] + 1 `. Now number of unit-times the statements of the loops are executed would be `3([log2X] + 1)`.

Finally, the number of steps required for the Russian Peasants Algorithm to execute:

`3([log2X] + 1) + 3 + (Number of '1' bits in a )`  


Simplifying the above would give :
    
    <code> <= 4([log<sub>2</sub>X]) + 7 </code> 

Note that the time complexity is exponentialy faster than that of `  pro(a,b) `program that we have written. In this way we could compare two programs without execution by this simple time complexity method.

  


---
author: sricharanchiruvolu
comments: true
date: 2013-12-15 16:11:00+00:00
layout: post
slug: data-structures-for-a-primer-queue
title: Data Structures For a Primer - QUEUE
wordpress_id: 157
---

Queue, similar to a stack, have restrictions on where you can add and remove elements. If stack has an analogy with a pile of treys, a queue is similar to a cafeteria line; the first person at the first is served first, followed by the second an so on to the end of the line. New people are added to the line from the back. Thus, this is of a **F**irst **I**n, **F**irst **O**ut (**FIFO**) type.  
  
The following terminology is associated with Queue:  
  
**Enqueue **The addition of an element to a Queue  
**Dequeue** Removing an element from a Queue  
  
Wait a second! The programming of a Queue is not as easy as programming a Stack. If a person leaves a line, everyone in the line must step forward. Now, imagine if only one person could move at a time. So, now every person at the back fills the place left behind by the first. Now imagine that no one can leave or be added to the line until everyone has stepped forward! so,**_ it is difficult to program a queue that is fast._**  
**_  
_** There are two ways for impliment a queue. First is to just an array and shift all the elements to accomidate enqueues and dequeues.  
  
The slowness of the first method is slow as with many elements, the shifting takes time. The other method is to shift enqueues and dequeues, rather shifting the elements. In the cafeteria line scenario, if the first of the line continually moves backwards as each person leaves the line, then the people don't need to step forward or backwards, which saves time!  
  
This is complicated to program when compared to the first method.Instead of keeping track of just the enqueue point (the "end"), we also need to keep track of the dequeue point (the "front"). This all gets even more complicated when we realize that after a bunch of enqueues and dequeues, the line will need to wrap around the end of the array. Think of the cafeteria line. As people enter and leave the line, the line moves farther and farther backwards, and eventually it will circle the entire cafeteria and end up at its original location.

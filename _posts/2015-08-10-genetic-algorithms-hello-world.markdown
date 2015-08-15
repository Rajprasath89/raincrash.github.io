---
author: sricharanchiruvolu
comments: true
date: 2015-08-10 10:00:00+00:00
layout: post
slug: genetic-algorithms-hello-world
title: A "Hello World!" to the genetic algorithms
disqus: y
tags:
- algorithms
- genetic algorithms
- bioinformatics
categories:
- bioinformatics
---

Genetic Algorithms(GA) is a method of __breeding__ computer programs and solutions to optimization or search problems by means of simulated evolution. They are often used in fields such as engineering to create incredibly high quality products; utilizing their ability to search through a huge combination of parameters to find the (nearly) best match.

They are based on the concept of evolution by natural selection observed in nature. Surprisingly, GA essentially replicate the way in which life uses evolution to find solutions to real world problems. This can be used to find solutions to incredibly complicated (complicated to compute) problems and solve other optimization solutions. GA can also be used to create sandboxes to study evolution and cognitive science.

__Understanding the game of chance__

Let's programmatically try to simulate the process of evolution that happens on earth. God creates a bunch of __organisms__. Each of them have a unique set of __genes__ (of course, they're randomly chosen). Let's name them as  the first __generation__. Each of the organisms have a unique trait that determines their survival, (we'll call it __fitness__). Now, say that organisms that are more fit tend to get together and reproduce and produce a second generation of offsprings. Also assume that the first generation die after reproduction (i.e. they no longer exist in the __population__). The second generation now reproduces and the cycle repeats.

The GA keeps producing new generations until a __perfect organism__ is evolved or a certain threshold (say 10000th generation of offsprings) is achieved.

__Approaching the _perfect_ solution__

A canonical GA requires the following components:

- A __representation__ of candidate solution
- A way of calculating the correctness of a candidate solution, the __fitness function__.
- A __mutation function__ that changes a candidate solution _slightly_, in an attempt to obtain a better candidate.


I would like to develop three GA solutions before I dive into parallelization of GAs.

1. The first one would be a simple GA to arrive at an expression of additions/ subtractions for a given number. (e.g. Input = 27, Output = 2 + 24 - 5 + 6).

2. The second is the modelling of canonical GA. __Natural selection__ based.

3. The third one is implementing the __travelling salesman problem__ using GA.

Once this is done, I will work on the parallelization of the same using GPGPUs. So, stay tuned!

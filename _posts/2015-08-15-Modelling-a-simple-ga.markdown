---
author: sricharanchiruvolu
comments: true
date: 2015-08-15 10:00:00+00:00
layout: post
slug: modelling-a-simple-ga
title: Modelling a simple genetic algorithm
disqus: y
tags:
- algorithms
- genetic algorithms
- bioinformatics
categories:
- bioinformatics
---

Modelling the genetic algorithms is pretty straightforward. This would be a pathway for finding solutions to complex search problems.

Let's try to model a simple genetic algorithm. As mentioned in the previous post, genetic algorithms are based on the process of natural selection.

A prerequisite from the previous post:
<pre>
A canonical GA requires the following components:
- A __representation__ of candidate solution
- A way of calculating the correctness of a candidate solution, the __fitness function__.
- A __mutation function__ that changes a candidate solution _slightly_, in an attempt to obtain a better candidate.
</pre>

To model the process of natural selection, we create the population (a randomly generated one). We calculate the __fitness__ of each individual of the population. We then consistently improve the population's overall fitness. This helps us to discard misfits and only keep the more fit individuals of the population.

The next most important part is the __crossover__. Crossover creates new individuals by combining (desirable?) aspects of the individuals selected. This is in the hope that we create more fit offsprings which inherit the best traits of their parents.

Now comes the __mutation__. We need to consider the anamolies. we'll add a bit of randomness into our population's genetics.

We continue the above until we reach the termination condition.

<blockquote> TODO: A C++ implementation of GA based on Natural Selection</blockquote>
<blockquote> TODO: A C++ implementation of Travelling salesman using GA</blockquote>

---
author: sricharanchiruvolu
comments: true
date: 2015-03-29 16:01:23+00:00
layout: post
slug: copyleft-physics-engine
disqus: y
title: 'Copyleftgames - Physics Engine'
tags:
- computer graphics
- games
- graphics
- physics
- copyleftgames
---

# A Real-time Physics Engine for Pysoy
*Proposal for Google Summer of Code - 2015   CopyLeftGames.org*

# *Personal details*

**Name:** Sricharan Chiruvolu ( IRC - raincrash / sricharanized )

**Email:** sricharanized(at)gmail(dot)com

**Degree:** B.Tech, Computer Science and Engineering

**College/ Univ:** Amrita School of Engineering, Bengaluru, India

# SYNOPSIS

Will be replacing the existing physics engine (ODE) with our own.

Modified components would include the joints, bodies, fields, and most importantly, collisions between objects.
Collision primitives planning to support are sphere, box and plane.

We will be addressing the following contact cases
- Point-point contacts
- edge-edge contacts
- edge-face contacts
- face-face contacts

We will be addressing the following primitive collisions with seperate algorithms:
- Two spheres colliding
- Sphere and plane colliding
- Box and plane colliding
- Sphere and box colliding
- Two boxes colliding

Most of the other higher geometric collisions can be based on the above.

# *Motivation*

The proposed project aims to Improve the Pysoy's physics system.

Pysoy is currently dependent on ODE (Open Dynamics Engine) for dynamic simulation. ODE is a great resource, but it doesn't meet the requirements that pysoy needs. Pysoy is proposed to run smoothly on both mobile and web and there is a need for a physics engine that is minimal, stable and more importantly, focussed on speed over accuracy. Pysoy doesn't require a high-precision engine as there is a need for using simplified calculations and decreased accuracy to compute in time for the game to respond at an appropriate rate for gameplay. Higher precision reduces the positional/force errors, but at the cost do greater CPU power needed for the calculations, which is not desirable in our case.

Thus, there is a need to replace the existing physics engine with our own. Modified components would include the joints, bodies, fields, and most importantly, collisions between objects.

# *Project Proposal*


## Implementation plan

Physics Engines, as the name implies are software that can simulate physics on a computer. These most commonly include rigid body dynamics such as simple convex primitives (boxes, spheres, cylinders, etc) colliding with each other and reacting to the resulting forces, but not deforming in the process, i.e. they maintain their shape and size and thus volume throughout the whole simulation. For reasons of computational complexity, the soft dody dynamics are used less-often, at least in real time physics simulations, where speed is of paramount importance.

On the higher level, our physics engine cycle does the following:

- Simulation: The engine goes through every object we are simulating, moves, rotates e.t.c and updates 
everything.

- Detecting Collisions: All the geometries in the scene are tested against each other to see which ones collide and a list of colliding objects with their point of contacts is generated. Goes through every object in the simulation and basically, it creates a list of every pair of objects that has collided as a result of simulation. We are not trying to decide what should happen to these objects after collision in this stage.

- Dynamically Responding to the collisions: Going through the list of all the pairs of colliding objects and decide how it should update them, how the collisions are to be handled e.t.c. 
The cycle now starts again with simulation and so on.


## Detecting Collisions

This would be done in two phases:

- A quick test to get a list of all possible colliding pairs can be done instead of directly calculating the contact points for each pair of bodies. This can be achieved by bounding volume principles.

- Once the above testing is done and we have detected the collisions between the bounding volumes, we are now in a position to carry out the full collision detection. Typically, we are comparing each geomentry with other in this stage. Different combinations of primitive collisions (shape vs shape) are to be implimented. 
Various optimization methods can be incorporated while detecting collisions:
Instead of using the brute force O(n2) method of testing each geometry against each other, techniques such as spatial coherence (where the proximity of objects are found by diving­ up the space) and/or temporal coherence (where the fact that the results from one time step are usually closely related to the results from the previous timestep) can be done.

In addition, we can employ hierarchical bounding volumes, i.e. bounding volumes for each part of a larger geometry where we progressively test bounding volumes lower in the hierarchy upon successful collision tests.
Quadtrees might be an even more effective first-pass in collision detection algorithm. Analysing the difference between using quadtrees and using a simple fixed grid will be done prior to the implimentation.

Collision primitives planning to support: sphere, box and plane.


## Generating contacts, the joints and fields

Contact generation is more complex than single-intersection collision detection and takes more processor time to complete. 

Rather, we will have a two-stage process of contact generation: a fine collision detection step to determine whether there are contacts to generate and then a contact generation step to work out the contacts that are present. We need to make sure that fine collision detection runs as fast as possible. We can dramatically improve the speed by performing collision detection against a simplified geometry rather than the full-resolution rendering geometry.

The problem is generating a collision geometry. Contact generation is an overhead. If this chunky geometry consists of certain geometric primitives—namely, spheres, boxes, planes, and capsules, then the collision detection algorithms can be simpler than for general-purpose meshes. How exactly such a geometry is generated is the question. I need to do a lot of research on this as there are very few resources I managed to find.
Once such mechanism is established, we can manage various permutations of primitives. The simplest shape on which to perform collision detection and contact generation on is the sphere. Despite being fast, however, spheres aren’t always terribly useful. Boxes are also relatively quick to process and can be used in more situations. What we also need to consider is the collision of objects with the background level geometry. Most commonly this means collisions with the ground or some other plane (walls can typically be represented as planes too). To support these, we’ll also consider collisions between primitives and planes.

The contact data we will be looking for are the collision point and the collsion normal (stored as a data structure).With this, we will be addressing how each contact case and there parameters. This includes:

- Point-point contacts
- edge-edge contacts
- edge-face contacts
- face-face contacts

Finally, we will be addressing the following primitive collisions with seperate algorithms:

- Two spheres colliding
- Sphere and plane colliding
- Box and plane colliding
- Sphere and box colliding
- Two boxes colliding

Most of the other higher geometric collisions can be based on the above.

## Responding to the collisions

The collision detection stage returns the collision pairs (the constraints (contacts, joints) and world transforms) that are now solved in this step.

This would be done in three phases:

- Mapping the given collision pairs into LCP (Linear complementary problem)
- Solving the LCP equations. Implementing numerical integration techniques: Euler’s method (for conceptual understanding), velocity verlet (for most simple games/kinematics), midpoint method (for most simple applications/general forces), Runge-Kutta methods (for advanced and accurate simulation).
- Map back the calculated results to the scene. This involves the calcuated force, integrate them to get velocity and new positions.

Understanding and implementing various algorithms like separating axis theorem GJK algorithm will optimise the calculation overload both in detecting collision stage and responding to collision stage. Further research will be done prior to the implimentation.

Contact resolution is a way in which touching objects are processed. We won't be using “Jacobian-based” approach, a physically realistic way to calculate the exact interaction between different contacts and calculate an overall set of effects to apply. It suffers from being very time consuming, complex math is involved, solving the equations require “millions” of calculations. 
Instead, we will be calculating a new set of equations based on the contacts and constraits between objects. Rather than use Newton’s laws of motion, we can create our own set of laws for just the specific configuration of objects we are dealing with.

## References and cool links

I found the following references useful, although not directly appropriate for our use.

- [Rigid Body Physics Engine](http://www-cs-students.stanford.edu/~eparker/files/PhysicsEngine/)
- [Nonconvex Rigid Bodies with Stacking](http://www.cs.ubc.ca/~rbridson/docs/rigid_bodies.pdf)
- And ofcourse, [ODE](https://sourceforge.net/projects/opende/files/) codebase.

## Beyond GsoC

I will be contributing to the development of the organization, especially with adding WebGL and HTML (plugin free) client support. There will always be something that needs improvement in a constantly evolving organization.

Also, the physics engine would have a lot of improvizations that need to be addressed. Including,
Soft body physics support:  The scope of soft body dynamics is quite broad, ranging form bouncing, bending and squishing, including simulation of soft organic materials such as muscle, fat, hair and vegetation, as well as other deformable materials such as clothing and fabric. This is really a broad concept. But, once a physics engine is wireframed, the softbody support can get into it pretty easily.
Maybe, boyancy too.

Handling wheeled, bipedal moments seperately:  Handling bipedal characters separately would be a great benefit for future game devs. There would be a collision joint that is unique for bipedal characters rather than depending of the native physics engine.

We can work on this as a non-deadline based project or chop them into various GCI tasks.

# Availability

I’m pretty sure that i’ll be able to devote about 40 - 50 hours every week to the project during the GSoC coding period. 

# Issues/ Shortcomings

As such, the limitation of any physics engine is the approximation of the positions and forces acting upon an object. These approximations can sometimes lead to drastic changes in the behaviour of the bodies.
This issue can be compromised if the engine can deliver  “realistic enough” results without consuming greater CPU powers needed for the calculations.

# About me

- [About](/index.html)

I am planning to blog my progress atleast once in two weeks. I think this is a good way to post progress on my project.

I am fairly new to GSoC as this will be my first experience, but I am looking forward to build this amazing application with you and begin my journey in Open Source!

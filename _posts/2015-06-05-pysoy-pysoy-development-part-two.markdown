---
author: sricharanchiruvolu
comments: true
date: 2015-06-05 11:18:47+00:00
layout: post
slug: pysoy-pysoy-development-part-two
title: 'Pysoy Development, Part Two'
wordpress_id: 273
disqus: y
tags:
- computer graphics
---

A long time ago, I have written an introductory article on pysoy, now after a few weeks here's the _Part Two_.

In this article, I would love to give an introduction about how the background stuff happens in the _soy_ module. Pysoy is just the `CPython` wrapper of _Libsoy_, which is the neural schema, the place where all the magic happens.

> _Libsoy_ is written in Genie and C. Genie is a comrade of Vala, both developed under the GNOME project. They use the GObject system and complie to C. 

Genie had a very few resources I could get my hands on, nevertheless, the language seems to be developer friendly. The syntax is very much similar to python. I really loved the paradigms used, esp. the properties and ownership stuff. (see: [Projects/Genie](https://wiki.gnome.org/Projects/Genie))

Genie allows you to write pretty high level stuff in very less LOC. All you have to do is write the C Wrappers and as Genie uses a 'valac' compiler to compile to C, you can achieve C-like speeds. The CPython PyObject API helps us to wrap a python module around this. A python module that runs on C and written in Genie. This is exactly what Libsoy + Pysoy is. Fascinating, huh!

There's a catch of course! You can't just go away with the nice Genie logic. Whenever the CPython entry points a.k.a the public API used by python is changed, you need to write the essential CPython wrappers, add necessary bindings e.t.c. Yes, for every function of every object. Which might be a daunting process.


So, that's it. You have Libsoy, you write your logic in Genie. The valac complier genie uses generates C code. That's what Libsoy is all about. Next, you write wrappers (using PyObject C API), you get a really cool CPython based module. That's what Pysoy is about. The game developer is abstracted with a really nice _soy_ module for import.

The engine is in it's infant stage. It's being developed by many students around the world at an impressive speed though. The project would also include Lightmelody and Playerd modules which would handle the networking and controller stuff respectively of the this 3D cloud based engine for multiple platforms.

---
author: sricharanchiruvolu
comments: true
date: 2014-12-13 14:58:18+00:00
layout: post
slug: writing-kernel-modules-101-one-what-is-a-kernel-module
title: 'Writing Kernel Modules 101: : What is a Kernel Module?'
disqus: y
wordpress_id: 71
categories:
- os
tags:
- Kernel
- linux
- OS
---

Kernel modules are pieces of code that can be loaded or unloaded into the kernel on demand. Strictly speaking, this is the definition of a 'loadable' kernel module. A module can be built-in or loadable. The advantage of loadability being that there isn't any need for booting the kernel again and again after every load. To load or remove modules they have to be configurated appropriately. In this tutorial session on kernel modules we will be going through this configuration process.

To write your own kernel modules, you need to have basic understanding of processes in an operating system. You should have implimented basic OS level code (like using fork() function, few CPU scheduling algorithms e.t.c). A frim grip on C programming is also essential.

Being a novice programmer myself, I will be learning and blogging simultaneously. Feel free to refer the "**The Linux Kernel Module Programming Guide**" for authentic information.****

In this tutorial, I will be discussing various algorithms and techniques on writing your own kernel modules. All the code is written in C and ran on Ubuntu 14.04 (debian based) linux system. Feel free to comment your queries.

So, let's get started.

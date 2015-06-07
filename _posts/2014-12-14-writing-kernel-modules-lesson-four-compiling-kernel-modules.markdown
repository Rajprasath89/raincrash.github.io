---
author: sricharanchiruvolu
comments: true
date: 2014-12-14 06:21:05+00:00
layout: post
slug: writing-kernel-modules-lesson-four-compiling-kernel-modules
title: 'Writing Kernel Modules::Compiling Kernel Modules'
disqus: y
wordpress_id: 91
categories:
- os
tags:
- Kernel
- linux
- OS
---

It's important to know how [Makefiles](http://mrbook.org/tutorials/make/) work. Another way (easier one) is by using `kbuild`. We will discuss about it soon.


    
    obj-m += first.o
    
    all:
    	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
    
    clean:
    	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
    


Now, This is just a sample of how the file looks. We will write our first program, `first.c` in the next tutorial. After this, we use **make **command to the build the kernel module.

Now it is time to insert your freshly-compiled module into the kernel with `insmod ./first.ko`. The latest kernel versions require you to name the object files with `.ko` extension to diiferentiate that from the usual ones. The diiference would be the `.modinfo` file that comes along. We will see what it is in the next tutorial.

As we already know, all the kernel modules that are loaded are listed in the `/proc/modules`. Once you write your first module, you can `cat` our file and see if it's loaded or not. To remove our module from the kernel, use `rmmod first`.

So, let's start writing our modules now.

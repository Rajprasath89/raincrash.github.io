---
author: sricharanchiruvolu
comments: true
date: 2014-12-14 07:43:57+00:00
layout: post
slug: writing-kernel-modules-lesson-five-our-first-kernel-module
title: 'Writing Kernel Modules:: Our first kernel module'
disqus: y
wordpress_id: 97
categories:
- os
tags:
- Kernel
- linux
- OS
---

Finally, It's time to write our first kernel module. But before that, do you know what `printk()` is? It's not an output statement. It is used to log information or give warnings for the kernel. The kernel uses the loglevel to decide whether to print the message to the console. The kernel displays all messages with a loglevel below a specified value on the console.

You specify a loglevel like this:

    
    	printk(KERN_WARNING "This is a warning!\n");
    	printk(KERN_DEBUG "This is a debug notice!\n");
    	printk("I did not specify a loglevel!\n")
    


The `KERN_WARNING` and `KERN_DEBUG` strings are simple defines found in <linux/ kernel.h>. They expand to a string such as "<4>" or "<7>" that is concatenated onto the front of the printk() message. The kernel then decides which messages to print on the console based on this specified loglevel and the current console loglevel, `console_loglevel`. If you do not specify a loglevel, it defaults to `DEFAULT_MESSAGE_LOGLEVEL`, which is currently `KERN_WARNING`. Because this value might change, you should always specify a loglevel for your messages.

Here's a what each `loglevel` mean:



	
  *  KERN_EMERG - An emergency condition; the system is probably dead

	
  * KERN_ALERT - A problem that requires immediate attention

	
  * KERN_CRIT - A critical condition

	
  * KERN_ERR - An error

	
  * KERN_WARINING - A warning

	
  * KERN_NOTICE - A normal, but perhaps noteworthy, condition

	
  * KERN_INFO - An informational message

	
  * KERN_DEBUG - A debug message typically superfluous


Okay. Enough of prerequisites. Here is our first kernel module code. Don' t compile it yet. We will improvise the code. This is just the basic template.

    
    /* 
    	Our first kernel module - first.c 
       	Author: Sricharan Chiruvolu
       	Date: 14 Dec 2014
    */
    #include <linux/module.h>
    #include <linux/kernel.h>
    
    int init_module(void){
    
    	//Our initial code goes here...
    
    	return 0;
    }
    
    void cleanup_module(void){
    
    	//The terminating code goes here...
    }
    
    


The `init_module` function is called after the module is loaded into the kernel and the `cleanup_module` function is called just before removing the module from the kernel.

Note that the use of `cleanup_module` function is to explicitly undo the changes of `init_module` and remove the module safely from the kernel.

Also, all the source code can be downloaded [here](https://github.com/raincrash/Writing-Kernel-Modules). Each program is committed according to this tutorial. So you can visit the previous commits for the appropriate one.



* * *



Now, let's add some output statements to our program. As already mentioned, we will use `printk()`.


    
    
    /* 
    	Our first kernel module - first.c 
       	Author: Sricharan Chiruvolu
       	Date: 14 Dec 2014
    */
    #include 
    #include 
    
    int init_module(void){
    
    	printk(KERN_ALERT "This is our first program.");
    
    	return 0;
    }
    
    void cleanup_module(void){
    
    	printk(KERN_ALERT "End of our first program.");
    }
    



Now we are ready to test our module. After writing the proper Makefile, run the `**make**` command. If you have any issues refer to the previous [tutorial](http://sricharanized.wordpress.com/2014/12/14/writing-kernel-modules-lesson-four-compiling-kernel-modules/).

You should get something like this in your terminal

    
    
    make -C /lib/modules/3.13.0-43-generic/build M=/home/sricharan/kernel modules
    make[1]: Entering directory `/usr/src/linux-headers-3.13.0-43-generic'
      CC [M]  /home/sricharan/kernel/first.o
      Building modules, stage 2.
      MODPOST 1 modules
      CC      /home/sricharan/kernel/first.mod.o
      LD [M]  /home/sricharan/kernel/first.ko
    make[1]: Leaving directory `/usr/src/linux-headers-3.13.0-43-generic'
    
    



Your first kernel module is ready. Load it to the kernel with the following command `insmod first.ko`. Note that you need sufficient privileges to do so.

Our LKM is loaded into the kernel. As already discussed in the previous [tutorial](http://sricharanized.wordpress.com/2014/12/14/writing-kernel-modules-lesson-four-compiling-kernel-modules/), you can check out `/proc/modules` for our kernel module.

As of now, let's remove it from the kernel. Run the `rmmod first` command to do so.
In the following tutorials we will dive deep into more advanced LKM code.

---
author: sricharanchiruvolu
comments: true
date: 2014-12-15 08:38:28+00:00
layout: post
slug: writing-kernel-modules-lesson-five-multiple-file-modules-argument-passing
title: 'Kernel Modules::Multiple file modules'
disqus: y
wordpress_id: 117
categories:
- os
tags:
- Kernel
- linux
- OS
---

Before we get into the real stuff, there are a few must-knows that are worth discussing. Note the our purpose of this tutorial set is to write our own LKMs and Rootkits for our own purposes. Few of them might have to be written in multiple files or require some arguments to be passed. We will discuss these issues now.
**
Command-line Arguments**

Command-line arguments are declared by defining the variables that take these arguments as global and using the `module_param()` macro. The variable declaration is usually described at the beginning of the module. The `insmod` is used to pass the values at runtime. Arrays of Integers or Strings are called using `module_param_array` and `module_param_string` macros.

The `module_param_desc` is used to document arguments that the module can take.

This is how command-line variables are declared.

    
    <code>
    int number = 100;
    module_param(number, int , 0); // module_param(variable_name, variable_type , permissions);
    
    // This is how arrays are declared
    
    int numberArray[5];
    module_param_array(numberArray, int, NULL, 0); /* not interested in count */
    
    int numberArray2[30];
    int count;
    module_param_array(numberArray2, short, count, 0); /* put count into "count" variable */
    
    </code>


Here's a sample program using command-line arguments.

    
    <code>
    /*  
        Using Command-line arguments
        Author: Sricharan Chiruvolu
        Date: 14 Dec 2014
     */
    #include <linux/module.h>    
    #include <linux/kernel.h>
    #include <linux/init.h>
    #include <linux/moduleparam.h>
    #include <linux/stat.h>
    
    
    #define DRIVER_AUTHOR "Sricharan Chiruvolu "
    #define DRIVER_DESC   "The First Program - Template"
    
    //Declaring a few variables...
    static short int short_number = 1;
    module_param(short_number, short, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
    MODULE_PARM_DESC(short_number, "A short Number");
    
    
    static int number = 54;
    module_param(number, int, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
    MODULE_PARM_DESC(number, "A Number");
    
    
    static long int long_number = 33553466;
    module_param(long_number, short, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP);
    MODULE_PARM_DESC(long_number, "A long Number");
    
    
    static char *char_string = "Hello";
    module_param(char_string, charp, 0000);
    MODULE_PARM_DESC(char_string, "A character string");
    
    static int __init first_init(void)
    {
    	int integerA;
    	printk(KERN_INFO "This is our first program.");
    	printk(KERN_INFO "short_number is a short integer: %hd\n", short_number);
    	printk(KERN_INFO "number is an integer: %d\n", number);
    	printk(KERN_INFO "long_number is a long integer: %ld\n", long_number);
    	printk(KERN_INFO "char_string is a string: %s\n", char_string);
    
    	return 0;
    }
    
    static void __exit first_exit(void)
    {
    	printk(KERN_ALERT "End of our first program.");
    }
    
    module_init(first_init);
    module_exit(first_exit);
    MODULE_LICENSE("GPL");
    MODULE_AUTHOR(DRIVER_AUTHOR);	
    MODULE_DESCRIPTION(DRIVER_DESC);
    
    /*  
     *  This module uses /dev/testdevice.  The MODULE_SUPPORTED_DEVICE macro might
     *  be used in the future to help automatic configuration of modules, but is 
     *  currently unused other than for documentation purposes.
     */
    MODULE_SUPPORTED_DEVICE("testdevice");
    
    </code>


Now that we know how to send command-line arguments let's. We will next see how multiple file modules work.



* * *



Quite often, it is logically suitable to write multi-file kernel modules. Let's write one now. We will use two files `third_one.c` and `third_one.c` for this.

`third_one.c` will look like this:

    
    <code>
    /*  
        Using multiple files - Part one
        Author: Sricharan Chiruvolu
        Date: 16 Dec 2014
     */
    #include <linux/kernel.h>
    #include <linux/module.h>
    int init_module(void)
    {
    	printk(KERN_INFO "Hello, world - this is the kernel speaking\n");
    	return 0;
    }
    </code>


and the other one, `third_two.c` will be:

    
    <code>
    /*  
        Using multiple files - Part two
        Author: Sricharan Chiruvolu
        Date: 16 Dec 2014
     */
    
    #include <linux/kernel.h>
    #include <linux/module.h>
    
    void cleanup_module()
    {
    	printk(KERN_INFO "Short is the life of a kernel module\n");
    }
    </code>


You can see that it's just the same program as our [first](http://sricharanized.wordpress.com/2014/12/14/writing-kernel-modules-lesson-five-our-first-kernel-module/) but is in two different files.

We are only supposed to change our Makefile to build both the object files of our program one after the other and create a combined object code. The modified `Makefile` looks like this.

    
    <code>
    obj-m += combined_module.o
    combined_module-objs := third_one.o third_two.o
    
    all:
    	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) modules
    
    clean:
    	make -C /lib/modules/$(shell uname -r)/build M=$(PWD) clean
    </code>


You can now run `make` command to find the `combined_module.ko` kernel module.

We have successfully written a basic multi-file kernel module. In the next tutorial, we will discuss about character device drivers. So, stay tuned.

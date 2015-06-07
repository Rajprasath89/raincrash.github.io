---
author: sricharanchiruvolu
comments: true
date: 2014-12-14 14:09:50+00:00
layout: post
slug: writing-kernel-modules-lesson-five-the-macros
title: 'Writing Kernel Modules::The Macros'
disqus: y
wordpress_id: 105
categories:
- os
tags:
- Kernel
- linux
- OS
---

After writing our first [program](http://sricharanized.wordpress.com/2014/12/14/writing-kernel-modules-lesson-five-our-first-kernel-module/), we are now ready to modify it a litte. We will be using `module_init` and `module_exit` macros to rename our default `init_module()` and `cleanup_module()` respectively. Remember that you need to call these functions before calling the macros.

Also, We will be adding `__int` and `__exit` macros. These are macros to locate some parts of the linux code into special areas in the final executing binary. __init, for example instructs the compiler to mark this function in a special way. At the end the linker collects all functions with this mark at the end (or begin) of the binary file. If you what to know more you can read the [init.h](http://lxr.free-electrons.com/source/include/linux/init.h) file along with the comments. This is the advantage of working with an open source operating system!

When the LKM starts, this code runs only once (initialization). After it runs, the kernel can free this memory to reuse it.

This is how our code was before we implimented it using modules.

    
    /* 
    	Our first kernel module - first.c 
       	Author: Sricharan Chiruvolu
       	Date: 14 Dec 2014
    */
    #include <linux/module.h>
    #include <linux/kernel.h>
    
    int init_module(void){
    
    	printk(KERN_INFO "This is our first program.");
    
    	return 0;
    }
    
    void cleanup_module(void){
    
    	printk(KERN_INFO "End of our first program.");
    }
    
    


We will now modify it as follows.

    
    /* 
    	Edited first.c; Added macros module_init and module_exit
       	Author: Sricharan Chiruvolu
       	Date: 14 Dec 2014
    */
    #include <linux/module.h>
    #include <linux/kernel.h>
    #include <linux/init.h>
    
    static int __init firstInit(void)
    {
    	
    	printk(KERN_ALERT "This is our first program.");
    	return 0;
    }
    
    static void __exit firstExit(void)
    {
    	printk(KERN_ALERT "End of our first program.");
    }
    
    module_init(firstInit);
    module_exit(firstExit);
    



Now you can `make` it. You will see that it behaves in the similar way as before. The difference? The attribute __init, , will cause the initialization function to be discarded, and its memory reclaimed, after initialization is complete. It only works, however, for built-in drivers; it has no effect on modules. __exit, instead, causes the omission of the marked function when the driver is not built as a module; again, in modules, it has no effect.

The use of __init (and __initdata for data items) can reduce the amount of memory used by the kernel. There is no harm in marking module initialization functions with __init, even though currently there is no benefit either. Management of initialization sections has not been implemented yet for modules, but it's a possible enhancement for the future.

Next comes the `MODULE_LICENCE` macro. Latest Kernels provide a mechanism to specify if the module is under GPL licence or not. A warning will be printed when you try to run it. To avoid this, you need to specify that the kernel module you have written is open source. To know more about GPL licence, you can visit [this](http://www.gnu.org/copyleft/gpl.html). You need to add the `MODULE_LICENCE` to prevent all such warnings. 

Here's what included in the `[linux/module.h](http://lxr.free-electrons.com/source/include/linux/module.h)` about the GPL licence. Notice that the `MODULE_DISCRIPTION` and `MODULE_AUTHOR` have their usual meanings and are essential to be included in the LKM code.

    
    <code>
    /*
     * The following license idents are currently accepted as indicating free
     * software modules
     *
     *	"GPL"				[GNU Public License v2 or later]
     *	"GPL v2"			[GNU Public License v2]
     *	"GPL and additional rights"	[GNU Public License v2 rights and more]
     *	"Dual BSD/GPL"			[GNU Public License v2
     *					 or BSD license choice]
     *	"Dual MIT/GPL"			[GNU Public License v2
     *					 or MIT license choice]
     *	"Dual MPL/GPL"			[GNU Public License v2
     *					 or Mozilla license choice]
     *
     * The following other idents are available
     *
     *	"Proprietary"			[Non free products]
     *
     * There are dual licensed components, but when running with Linux it is the
     * GPL that is relevant so this is a non issue. Similarly LGPL linked with GPL
     * is a GPL combined work.
     *
     * This exists for several reasons
     * 1.	So modinfo can show license info for users wanting to vet their setup 
     *	is free
     * 2.	So the community can ignore bug reports including proprietary modules
     * 3.	So vendors can do likewise based on their own policies
     *  #define MODULE_LICENSE(_license) MODULE_INFO(license, _license)
     *
     * Author(s), use "Name " or just "Name", for multiple
     * authors use multiple MODULE_AUTHOR() statements/lines.
     *
     * #define MODULE_AUTHOR(_author) MODULE_INFO(author, _author)
     *
     * What your module does.
     * #define MODULE_DESCRIPTION(_description) MODULE_INFO(description, _description)
     */
    </code>



Now, we will add the required Macros as well as GPL license to our code.

Here's the final code.

    
    <code>
    /*  
        Added macros and Documentation to first.c
        Author: Sricharan Chiruvolu
        Date: 14 Dec 2014
     */
    #include <linux/module.h>
    #include <linux/kernel.h>
    #include <linux/init.h>
    #define DRIVER_AUTHOR "Sricharan Chiruvolu "
    #define DRIVER_DESC   "The First Program - Template"
    
    static int __init first_init(void)
    {
    	printk(KERN_ALERT "This is our first program.");
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



Now that we have written our first LKM at production level, we will be writing more advanced kernel modules in the following tutorials. We will be learning about /proc file system, Charaacter device files e.t.c.

Note the all the code is available at my [github](https://github.com/raincrash/Writing-Kernel-Modules) page. Stay Tuned.


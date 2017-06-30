---
author: sricharanchiruvolu
comments: true
date: 2014-12-13 15:25:34+00:00
layout: post
slug: writing-kernel-modules-101-lesson-two
title: 'Kernel Modules 101: : Basic Commands'
wordpress_id: 75
categories:
- os
tags:
- Kernel
- linux
- OS
---

**Some essential commands before getting started into Kernel Development**


1. **lsmod** - In linux systems, `lsmod` prints the contents of the `/procs/modules` file. It shows the currently loaded kernel modules. Here, _module_ denotes the name of the loaded module. _size_ denotes the size of the module, not the memory used by it. _Used by_ provides the list of refering modules and their count. Also, If the module controls its own unloading via a can_unload routine then the use count displayed by lsmod is always -1, irrespective of the real use count


2. **modinfo** - It is the command used to know the information associated with a certain module. Its syntax is `modinfo module_name`

3. **systool**- `systool` is used for various purposes. We will limit ourselves to list the options that are set for a loaded module. This is how it's done `systool -v -m module_name`


4. **modprobe** - `modprobe` is a Linux program originally written by Rusty Russell and used to add a loadable kernel module (LKM) to the Linux kernel or to remove a LKM from the kernel. It can also be used to display the comprehensive configuration of all the modules:


`modprobe -c | less`


To display the configuration of a particular module:

    
`modprobe -c | grep module_name`


Also, it can be used to list the dependencies of a module, including the module itself:

    
`modprobe --show-depends module_name`


Try these commands once. If you couldn't understand what is printed on the console at this moment, it's okay. We will be discussing all of them soon. So Stay Tuned.

---
author: sricharanchiruvolu
comments: true
date: 2014-12-13 15:45:14+00:00
layout: post
slug: writing-kernel-modules-101-lesson-three-what-modprobe-does
title: 'Kernel Modules 101:: What modprobe does?'
disqus: y
wordpress_id: 80
categories:
- os
tags:
- Kernel
- linux
- OS
---

**What does modprobe do?**

As we have discussed already, modprobe command loads or removes a loadable kernel module. It was previously used as `'modutils'` and is now included in _module-init-tools_ package in newer linux kernel versions. There are various similar commands like `insmod` and `rmmode` but `modprobe` dominates them all due to various reasons.

The `modprobe` offers the following features:



	
  * an ability to make more intuitive decisions about which modules to load

	
  *  an awareness of module dependencies, so that when requested to load a module, modprobe adds other required modules first

	
  *  the resolution of recursive module dependencies as required


This makes modprobe unique and essential. The _modprobe_ program also has more configuration features than other similar utilities. It is possible to define module aliases allowing for some automatic loading of modules. If you are interested to know more, read the man pages of module-init-tools and see for yourself what's really going on.

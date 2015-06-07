---
author: sricharanchiruvolu
comments: true
date: 2014-01-19 04:41:00+00:00
layout: post
slug: how-to-reset-your-linux-root-password
title: How to reset your Linux Root Password
wordpress_id: 152
---

The following steps will help you to reset your Linux Root (superuser) Password. Most of the linux have a boot loader package called GRUB. If your linux  is using GRUB boot loader, you can boot into single user mode by  interrupting the bootloader and booting into the 'Recovery Mode' of the Linux.  
  
Steps:  


  * Restart your Linux.
  * Press 'Esc' key until you are in the GNU GRUB menu.
  * Use the Arrow keys to Boot into the 'Recovery Mode' of your Linux.
  * Press 'B' key.
  * Here we are, we have gained root access to the filesystem!
  * Type 'passwd' 
  * Now enter the password of your choice and restart the Linux.
We have successfully changed the Root Password.  
  
Now, You can change other users' passwords as follows. Note that you need to login as root user.  
  
Steps:  


  * Use sudo -s or su - command in the terminal to login as root.
  * To change password of specific user account, type 'passwd userNameGoesHere'.
  * For example, to change the password of the user 'hrishi', type 'passwd hrishi'. Now, Enter the password of your choice. say 'inctfhrishi'.
  * Restart your linux.

In this way, you can change the password of any user, provided you have GNU GRUB bootloader and it is not password protected.

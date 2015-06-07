---
author: sricharanchiruvolu
comments: true
date: 2014-01-19 05:01:00+00:00
layout: post
slug: how-to-reset-your-linux-root-password-without-grub-boot-loader
title: How to Reset your Linux Root Password without GRUB boot loader
wordpress_id: 151
---

If your Linux doesn't have GNU GRUB boot loader or you cannot access it as it is password protected, you can use this method to change your root (superuser) password.

  


 All you need is a live CD of any linux of your choice. Just follow the steps below to achieve this:

  * Boot from the Live CD.
  * Choose an option that states 'Boot Linux without making changes to your computer' or something of that sort.
  * When the system boots up, open the terminal. 
  * Type **sudo fdisk -l**. In the output we are concerned to  know which partition Linux is installed on and what name the hard disk  is using. 
  * In my case it is **/dev/sda1** is the required partition. If you are sure about the partition you can skip this step.
  * Next we need to mount the Linux partition. Create a directory to act as mount point for the partition. Use ‘**sudo mkdir /media/linx_part**‘.
  *  Mount the linux partition using the command ‘**sudo mount /dev/sda1 /media/linx_part**‘.
  * Change Root to the mount directory – ‘**sudo chroot /media/sda1**‘
  * Type **passwd** and then enter the new password to change the password.
  * Type **reboot** to restart the system. 
To prevent others from hacking into your system, all you need to do is to setup a password to access your GNU GRUB menu and using any Linux Disk Encryption Tool to encrypt file system.  
  
Use "**loop-AES**" to encrypt disk partitions, removable media, swap space and other devices. This will prevent others to hack into your Linux Computer.

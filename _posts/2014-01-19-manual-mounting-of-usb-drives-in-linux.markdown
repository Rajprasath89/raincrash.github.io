---
author: sricharanchiruvolu
comments: true
date: 2014-01-19 06:30:00+00:00
layout: post
slug: manual-mounting-of-usb-drives-in-linux
title: Manual Mounting of USB drives in Linux
wordpress_id: 148
---

When a USB doesn't mount automatically, you can manually mount it. For this you need to login as root (superuser) and do the following process.  
  
Steps:  


  * Login as Root. 
  * Check if the computer have recognized the USB you plugged in by the** lsusb** command. 
    
    cs50/home/sricharan # lsusb 

  * Create a  directory where your USB drive will be mounted.
    
    cs50/home/sricharn # cd Desktop/<br></br>cs50/home/sricharan/Desktop # mkdir flash<br></br>cs50/home/sricharn/Desktop #<br></br>

  * We need to get the appropriate device which is attached to your flash drive. To do this, simply issue the following command in the same terminal window.  
**dmesg | grep -i “SCSI device”**
    
    cs50/home/sricharan/Desktop # dmesg | grep -i "SCSI device"

  * When you’ve found the correct device, Usually it would be sda, sdb, sdc, etc.  Enter the following command into the same terminal window:
    
    cs50/home/sricharan/Desktop # pwd<br></br>/home/sricharan/Desktop<br></br>cs50/home/sricharan/Desktop # mount -t vfat -o uid=jason,gid=users /dev/sda /home/sricharan/Desktop/flash<br></br>cs50/home/sricharan/Desktop #

  
  
Your flash drive is now mounted and ready to use.  If you followed  the instructions exactly, there is a new folder on your desktop named  “flash” which can be used to put files, images, music, or anything else  you want!  
  
When you’re done copying, simply pop out the drive and you’re on your way.   


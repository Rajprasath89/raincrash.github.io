---
author: sricharanchiruvolu
comments: true
date: 2014-01-19 06:48:00+00:00
layout: post
slug: viewing-and-changing-permissions-of-directories-in-linux
title: Viewing and Changing Permissions of Directories in Linux
wordpress_id: 147
---

To check for permissions of a directory in linux, use the following command  
  

    
    <code>$ ls -ld directory</code>

  
To set permissions for various directories in linux, use chmod.  
  
The "chmod" is a Linux command that will let you SET PERMISSIONS i.e. assign who can read/write/execute on a  file.  
  
When using chmod, you need to be aware that there are three types  of Linux users that you are setting permissions for. Therefore, when  setting permissions, you are assigning them for "yourself", "your group" and "everyone else" in the  world. These users are technically know as:  
  
Owner  
Group  
World  
  
Therefore, when setting permissions on a file, you will want to assign all three levels of permissions, and not just one user.  
  
Think of the chmod command actually having the following syntax...  
  
**_chmod owner group world FileName_**  
  
There are three types of permissions that Linux allows for each file.  
  
read  
write  
execute  
  
  
You will need to convert the word read or write or execute into the numeric equivalent (octal) based on the table below.  
  
4 read (r)  
2 write (w)  
1 execute (x)  
  
    
For example,  
  
  **_chmod 400 mydoc.txt_** read by owner  
**chmod 100 mydoc.txt** execute by owner  
  
Also,  You need to add up the numbers to get other types of permissions,  
  
   
7 = 4+2+1 (read/write/execute)  
6 = 4+2 (read/write)  
5 = 4+1 (read/execute)  
4 = 4 (read)  
3 = 2+1 (write/execute)  
2 = 2 (write)  
1 = 1 (execute)  
  
For example,  
  
_**chmod 666 mydoc.txt**_ read/write by anybody!   
_**chmod 755 mydoc.txt**_ rwx for owner, rx for group and rx for the world  
_**chmod 777 mydoc.txt**_ read, write, execute for all! 

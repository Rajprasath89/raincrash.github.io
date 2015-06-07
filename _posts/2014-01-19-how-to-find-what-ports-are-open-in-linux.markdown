---
author: sricharanchiruvolu
comments: true
date: 2014-01-19 06:07:00+00:00
layout: post
slug: how-to-find-what-ports-are-open-in-linux
title: How to find what ports are open in Linux
wordpress_id: 149
---

To find out what ports are open / listening on your Linux, use the following netstat commands in the terminal. Note that you need to login as root (superuser) to use them.

  


`# netstat --listen `

`# netstat -tulpn`

  


  
The first would let you see what ports are listening and the second will list the processes. To have a total reference of all the netstat commands, check out the man page for netstat.

  


Assume that TCP port 3306 was opened by mysqld process having PID # 1138.

  


You can verify this using /proc, enter:

  


`# ls -l /proc/1138/exe`

  


  


``You can use grep command to filter out information:

`# netstat -tulpn | grep :80`

  


You can alse  use the fuser commands.

  


  


To find out the processes PID that opened tcp port 7000, enter:  
  
`# fuser 7000/tcp`  
  
To  find out process name associated with PID # 3813, enter:  


`# ls -l /proc/3813/exe  `

``  


To kill a process use the following command

  


`fuser -k 8080/tcp`

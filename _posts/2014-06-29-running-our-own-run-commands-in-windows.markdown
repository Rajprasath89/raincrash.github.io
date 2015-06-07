---
author: sricharanchiruvolu
comments: true
date: 2014-06-29 18:48:00+00:00
layout: post
slug: running-our-own-run-commands-in-windows
title: Running our own RUN commands in windows
wordpress_id: 146
---

We can write our own RUN commands in windows. We can thereby start an application by hitting CTRL-R and the our custom command.  
  
Let us consider writing the custom command for Adobe Photoshop. You can use any application other than something that already has a direct command.  
  
Right click on the desktop and make a new shortcut. As you select the shortcut a dialog box appears asking for the path for which you like to create the shortcut for.  
  
Now provide the path of the application's .exe file. It is usually found in C-Drive's program files folder.  
  
Next provide a relative name to this shortcut folder, say "ps" for photoshop. Now click on Finish button. The shortcut of the respective application will be created on your desktop.  
  
Cut and paste the created shortcut into the root drive i.e. C:/Windows/ . Provide the administrator password if necessary.  
  
Now, you are done with the process of creating a RUN command. Hit CTRL-R and type your custom command to open the application.

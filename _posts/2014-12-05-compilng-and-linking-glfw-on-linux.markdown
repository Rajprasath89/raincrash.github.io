---
author: sricharanchiruvolu
comments: true
date: 2014-12-05 08:09:49+00:00
layout: post
slug: compilng-and-linking-glfw-on-linux
title: Compilng and linking GLFW on Linux
wordpress_id: 42
categories:
- opengl
tags:
- computer graphics
- foss
- glfw
- opengl
---

If you are new to OpenGL programming and are using terminal and vim as I do, you might find some issues in including the required libraries and linking them for execution in you linux machine.

To successfully build and run OpenGL programs that includes GLFW libraries on my ubuntu 14.04, I did the following:




	
  * Update the Graphics drivers - Go to **System Settings** >> **Software and Updates** >> **additional drivers** and install the required drivers.

	
  * Download the latest version of GLFW from the website [http://www.glfw.org.](http://www.glfw.org)

	
  * Extract the archive. Open terminal and `cd` to the GLFW's main directory.

	
  * For example,

    
    `cd glfw-3.0.4`

	
  * Get the sudo privileges using
   
    `sudo -i`

	
  * Now, run the following command,

    
     `cmake -G "Unix Makefiles"`


> Note that you need to have cmake and various other **build dependencies** installed. Try using `sudo apt-get build-dep glfw3` or manually install the required dependencies.

	
  * Then, run `make` and then `make install`.

	
  * You have successfully build GLFW!

	
  * Now use a test program to test if everything is in place. You can use my simple test code that creates a blank window and defines OpenGL context. Here is the code: [https://github.com/raincrash/sricharanizedBlogCode/blob/master/init-glfw.cpp.](https://github.com/raincrash/sricharanizedBlogCode/blob/master/init-glfw.cpp)

	
  * To execute this file,say main.cpp, you require various **development libraries** like GL, GLU X11, Xrandr e.t.c. Now link the required libraries,

  `g++ -std=c++11 -Wall -o  main main.cpp -lglfw3 -lGLU -lGL -lX11 -lXxf86vm -lXrandr -lpthread -lXi`
    
	
  * Note that the linking is done sequentially, so the order is important.
	
  * Now execute the program,
    
    `./main`
	
  * If everything's OK, an empty window must be displayed.



You have successfully ran an OpenGL program with GLFW library installed in your Linux.



---
author: sricharanchiruvolu
comments: true
date: 2014-12-05 05:28:51+00:00
layout: post
slug: opengl-glfw
title: Initializing context in opengl with GLFW
wordpress_id: 19
categories:
- opengl
tags:
- glfw
- graphics
- opengl
---

Initializing OpenGL is done by adding context, the state machine that stores all the date that is required to render your application. When you close your application, the context is destroyed and everything is cleaned up.

OpenGL specification doesn't include creating a window, or defining a context. Hence, we use other libraries to abstract this process. This helps us to make cross-platform applications and save the real essence of OpenGL.

The coding pattern these libraries follow is similar. We begin by specifying the properties of the window. The application will then initiate the event loop. Event handling such as mouse clicks, updating rendering states and drawing.

Here's how it looks

    
    #include <RequiredHeaders>
    
    int main(){
    
       createWindow();
       createContext();
    
     while(windowIsOpen){
       while (event == newEvent()){
         handleThatEvent(event);
       }
    
       updateScene();
    
       drawRequiedGraphics();
       presentGraphics();
     }
       return 0;
    }
    


The _back buffer  _stores the results while rendering a scene to make sure user only sees the final state. The `presentGraphics();` will copy the result in the back buffer and make it visible to the viewer by placing the result in the _front buffer_.

GLFW helps us to inform the drivers that our application is ready for the future and does not depend on the deprecated functions. Supporting resizable windows requires the resources to be reloaded and buffers need to be recreated to adapt the new size.

Coming to what libraries to be used along with OpenGL, we do have a lot of options: [https://www.opengl.org/wiki/Related_toolkits_and_APIs.](https://www.opengl.org/wiki/Related_toolkits_and_APIs.)

We will be using GLFW for window and context creation as well as handling inputs. I choose GLFW as it gives more control to OpenGL that other libraries trying hard to be an all-in-one solution and defining there own drawing functions. GLFW gives you a window and OpenGL context with just two function calls.

**Building**



	
  * Download the necessary library files: [http://www.glfw.org/download.html](http://www.glfw.org/download.html). I will be using version 3.0.4. You can also compile the libraries yourself.

	
  * Add the `lib` folder in the appropriate library path and link it with `GLFW`.

	
  * Add <code>include</code> folder to your library path.


**Using GLFW**

Include the GLFW header in your program

    
    #include <GLFW/glfw3.h> ;
    
    int main(){
    
    }
    


You need to initialize GLFW when the program starts and ask it to clean-up at the end. `glfwInit();` and `glfwTerminate();` with do the work respectively.
Before we create a window, we need to do some configuration.

    
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 2);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
    
    glfwWindowHint(GLFW_RESIZABLE, GL_FALSE);
    
    GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL", nullptr, nullptr); // Windowed
    GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL", glfwGetPrimaryMonitor(), nullptr); // Fullscreen
    
    


The above code specifies that it requires GLFW version 3.2 at the least and also that we want a context that only supports the new core functionality. Width, height and window title also needs to be aptly specified. The configuration allows you to specify an existing OpenGL context to share resources like textures with. It also include a function to specify additional requirements for a window. We will address all of them as we dive deep.

Now make the context active:

    
    glfwMakeContextCurrent(window);
    


Now you are supposed to create an event loop. GLFW uses a _closed _event loop that is you only handle events when you need to.

    
    while(!glfwWindowShouldClose(window))
    {
        glfwSwapBuffers(window);
        glfwPollEvents();
        ...
    }
    
    


Note that `glfwSwapBuffers(window)` and `glfwPollEvents()` are two required function calls which swaps the front and back buffers after you have finished drawing and retrives window events respectively.
If you are making fullscreen applications, you can handle an escape key to return to the desktop.

    
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
        glfwSetWindowShouldClose(window, GL_TRUE);
    
    


You have now initialized a window with OpenGL context.

Before we procced, have a glance at the GLFW documentation:[ http://www.glfw.org/docs/latest/quick.html](http://www.glfw.org/docs/latest/quick.html).

Here's the code. [ https://github.com/raincrash/sricharanizedBlogCode/blob/master/init-glfw.cpp](https://github.com/raincrash/sricharanizedBlogCode/blob/master/init-glfw.cpp)

We will soon be drawing stuff in this window.

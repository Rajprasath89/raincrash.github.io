---
author: sricharanchiruvolu
comments: true
date: 2014-12-05 16:01:23+00:00
layout: post
slug: an-introduction-to-graphic-shaders-part-one
title: An Introduction to Graphic Shaders - Part One
wordpress_id: 50
categories:
- opengl
tags:
- computer graphics
- foss
- graphics
- opengl
---

Shader in computer graphics is something that tells a computer to draw something in a specific and unique way. The language in which these shaders are programmed depends on the target environment. OpenGL uses OpenGL Shading Language (GLSL), the official Direct3D shading language is High Level Shader Language (HLSL). There are also quite a few famous shading libraries and languages including Cg by Nvidia and Metal Shading Language by Apple.

We will be discussing mostly about GLSL shaders. In OpenGL rendering pipeline, there are various shaders:



	
  * Vertex Shaders

	
  * Evaluation Shaders (Tessellation Shaders)

	
  * Geometry Shaders

	
  * Fragment Shaders

	
  * Compute Shaders


It isn't necessary to learn about all the shader handling functions for real-time graphics programming. It is only required to know what data that the graphic card needs to draw a scene correctly. This data usually comes from _vertex attributes._ You need to define a proper _world position. _OpenGL defines its world coordinates just like a sheet of graph paper, with (0,0,0) at the center of the scene. Note that this isn't the case with other graphic languages where the center would be at the top-right corner.

Let's define a triangle by specifying its vertices as an array.

    
    float data[] = {
          0.0f, 1.0f, // vertex A
          1.0f,-1.0f, // vertex B
         -1.0f,-1.0f  // vertex C
    }
    


We then need to define a way for uploading this vertex data to the GPU. This is done by OpenGL's _Vertex Buffer Object _ (VBO) feature.

This is how it's done.

    
    //Initialise VBO - do only once, at start of program
    //Create a variable to hold the VBO identifier
    GLuint triangleVBO;
     
    //Vertices of a triangle (counter-clockwise winding)
    float data[] = {1.0, 0.0, 1.0, 0.0, 0.0, -1.0, -1.0, 0.0, 1.0};
    //try float data[] = {0.0, 1.0, 0.0, -1.0, -1.0, 0.0, 1.0, -1.0, 0.0}; if the above doesn't work.
     
    //Create a new VBO and use the variable id to store the VBO id
    glGenBuffers(1, &triangleVBO);
    


VBO avoids sending the data everytime the screen is rendered. We will discuss about it's functioning later.

Notice the datatype `GLuint`. It's a cross-plantform substitute of `unsigned int`. You will need this `triangleVBO` number to activate the VBO and destroy it when you are done with it.

To actually upload data to the VBO you have the active object.

    
    glBindBuffer(GL_ARRAY_BUFFER, triangleVBO);
    


The enum value `GL_ARRAY_BUFFER` means "use that buffer object for vertex data". We will pounder about what that means later.

Now that the VBO is active, we can copy the vertex data to it. This is how it's done.

    
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), data, GL_STATIC_DRAW);
    


Notice that it doesn't refer to the `triangleVBO` id. It already know the active object. The final argument, `GL_STATIC_DRAW` defines the usage of the vertex data we just uploaded.



	
  * `GL_STATIC_DRAW`: The vertex data will be uploaded once and drawn many times

	
  * `GL_DYNAMIC_DRAW`: The vertex data will be changed frequently and also drawn many times

	
  * `GL_STREAM_DRAW`: The vertex data is changed almost everytime it's drawn


The vertices with their attributes has been copied to the graphic card. But isn't not ready to be used yet. Now we need to specify how the graphic card would handle all the attributes. Now the **shaders** comes to place.

**A simple vertex shader**

Let's take a simple example to start with.

    
    
    #version 150
    
    in vec2 position;
    
    void main()
    {
        gl_Position = vec4(position, 0.0, 1.0);
    } 
    



All vertices of our primitive program will have to go through this program.

More discussion will be available in Part two.

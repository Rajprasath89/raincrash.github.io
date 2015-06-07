---
author: sricharanchiruvolu
comments: true
date: 2015-04-22 06:39:27+00:00
layout: post
slug: pysoy-pysoy-development-part-one
title: '[Pysoy] - Pysoy Development, Part One'
disqus: y
wordpress_id: 178
categories:
- GSoC
tags:
- computer graphics
- game
- game engine
- google
- gsoc
- programming
- pysoy
- summer
- technology
---



_In this blogpost, I would like to describe the engine from a game developer's perspective and as a general introduction to the organization and the engine itself._









_Future posts would include technical discussions, engine development e.t.c._









**What exactly does copyleftgames do?**









_They maintain and license games!_









They maintain gaming softwares under copyleft licenses (mostly GNU AGPLv3, I guess). And I’m planning to work on [Pysoy](http://www.pysoy.org/), a cloud game engine. The games are intended to run on the server and playable on multiple devices. Well, pysoy along with [playerd](http://www.playerd.org/) (a service for abstacting input devices and user data) and [lightmelody](http://www.lightmelody.org/) ( a network library for cloud games) would facilitate gaming on a wide variety of devices to which pysoy is ported to.









**How do I make pysoy games?**










<blockquote>Currently, developing games directly is pretty difficult. You will have to work more on the engine than your game itself to do so.</blockquote>










Get a linux machine. Download the engine (libsoy and pysoy) , build and install it. Once, installed you can import the the _soy_ module and use it.









I won’t be discussing the installation process or any programming details here. This blogpost is an introduction to the engine itself.













A simple scene can be written in ~40 lines of code.





**Understanding _soy_ package**









I would like to give an introduction some on essential submodules and classes in soy module. For further details you can always look into pydocs associated with each module/class name.










<blockquote>To get help on any module/class, you type python3 -c “import soy; help(soy.)” in your command window.</blockquote>










First, the _Client_. Clients in pysoy are intended to manage window creation, define context and data state of the object e.t.c. Currenty, the controllers are proposed to be managed by playerd and audio will soon be integrated as a texture to the body itself. Client instances are created locally with _soy.Client_object.









Other essential submodules of the soy package includes








    
  * atoms

    
  * bodies

    
  * scenes

    
  * materials

    
  * textures

    
  * widgets

    
  * fields and joints







_Atoms, _as the name suggests are the building blocks. The data types that helps the other submodules. Atoms include Color, Position, Size, Rotation, Vector and many other essential classes.









_Bodies _are the objects in a scene. Matter that’s made up of atoms. They render to the scene, intercact, collide with each other. Sphere and Boxes are the obvious ones. Billboards and portals are examples of complicated bodies. Camera and Light are also considered as bodies_ (_Why?_ You will soon understand).









_Scenes_ are where the bodies are present. It would contain geometry, viewpoint, texture, lighting, and shading information as a description of the virtual scene as in the real world. Room is the one that’s commonly used. Depending on the gameplay, scenes can be created. Typical examples include Room, Landscape and Space.









_Materials_ govern the appearance of bodies in a scene. Materials define how the object looks and what properties can it have. Examples include Wireframed, Textured and Colored.









_Texturing_ is the application of a type of surface to a 3D image. Heightmaps, Cubemaps, Bumpmaps are some trivial examples. SVGs can also be mapped to a material as a texture. Future iterations of the engine would include Audio as a texture.









_Widgets_ are the tricky ones, they define the rendering areas. Containers, Canvas and Projectors are few examples. Perhaps, Projector is the one that’s frequently used. It is used to “Project” the output of the camera to the screen. Widow objects can also be created from the Widgets submodule. They automatically create Client instances. comes









_Fields_ effect the scenes. They manipulate the bodies inside that scene. Examples include Buoyancy, Wind e.t.c.









_Joints_ connect bodies. They are typically used to create complex structures from primitive bodies. The anchor point of a joint is associated with that scene. Ball and Socket, Pivot e.t.c. are some examples.









_The next blogpost would be related to the graphics and rendering part of the engine and it's development._



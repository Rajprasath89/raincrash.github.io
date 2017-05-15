---
author: sricharanchiruvolu
comments: true
date: 2015-03-30 16:01:23+00:00
layout: post
slug: copyleft-deferred-renderer
disqus: y
title: 'Copyleftgames - Deferred Renderer'
tags:
- computer graphics
- games
- graphics
- deferred renderer
- copyleftgames
---

# Deferred Rendering pipeline for Pysoy
*Proposal for Google Summer of Code - 2015   CopyLeftGames.org*

# *Personal details*

**Name:** Sricharan Chiruvolu ( IRC - raincrash / sricharanized )

**Email:** sricharanized(at)gmail(dot)com

**Degree:** B.Tech, Computer Science and Engineering

**College/ Univ:** Amrita School of Engineering, Bengaluru, India

# SYNOPSIS

Classing rendering (also called forward rendering) can, in the worst case, require num_objects * num_lights batches to render a scene. Deferred shading changes that to num_objects + num_lights, which can often be a lot less. We can thus achieve O(1) depth complexity for lighting. Memory is no longer an issue. So, pysoy can migrate to a deferred renderer.

Aim to create a deferred rendering pipeline that is as unobtrusive as possible – we do not want the users of the engine to have to use it differently because of the way that its rendered. So, we want an engine that can:

- Interact with the game engine in the same way that the forward renderer does.
- The pipeline switch should still be as flexible as forward rendering.

Working on optimization techniques including Stencil culling algorithm for rendering deferred lights and scissor rectangles. Multiple Render Targets (MRT) capability.

Compactability of adding some advanced post-filters without another full scene render.

The Deferred rendering architecture will include the following stages:
- Geometry stage 
- Lighting stage 
- Post-processing stage
- View stage

# *Motivation*

In a standard forward rendering pipeline, the lighting calculations have to be performed on every vertex and on every fragment in the visible scene, for every light in the scene. The expensive lighting calculations have to execute for each visible fragment of every polygon on the screen, regardless if it overlaps or is hidden by another polygon's fragments. 

Also, many of the fragments will never make it to the screen because they were removed with depth testing, and thus the lighting calculation was wasted on them. 

Classing rendering (also called forward rendering) can, in the worst case, require num_objects * num_lights batches to render a scene. Deferred shading changes that to num_objects + num_lights, which can often be a lot less. We can thus achieve O(1) depth complexity for lighting.

If we migrate to deferred rendering pipeline we can easily extend the deferred renderer to calculate light volume mapping, extend to various post-effect schemes (new post-processing effects are easily achievable using the G-Buffer as input. If  we wanted to perform these effects without deferred shading, we would've had to render the whole scene again) e.t.c.


# *Project Proposal*


## Implementation plan

Refactoring is the key. We will have to create a deferred rendering pipeline that is as unobtrusive as possible – we do not want the users of the engine to have to use it differently because of the way that its rendered. So, we want an engine that can:

1. Interact with the game engine in the same way that the forward renderer does.
2. The pipeline switch should still be as flexible as forward rendering.

The second issue is the optimization. We need to make sure G-Buffer pass is cheap. There are a lot of optimization methods that can be implemented, clipping, occlusion query, stencil cull, etc. We will be working on using Stencil culling algorithm for rendering deferred lights.

In the beginning, all of the objects render their "lighting related info" to a texture, the G-Buffer. This means their colours, normals, depths and any other info that might be relevant to calculating their final colour. 

Then, the lights in the scene are rendered as geometry (sphere for point light, cone for spotlight and full screen quad for directional light), and they use the G-buffer to calculate the colour contribution of that light to that pixel.

In order to write to all its buffers, it would require rendering one pass per buffer. However, if the current graphics card supports Multiple Render Targets (MRT) capability, it is possible to write to all buffers in a single pass. We won't render the scene straight to the back buffer; instead we render everything into a bunch of textures using a multiple render target (MRT). With MRTs we can render into different textures with a single call. This will avoid to transform the vertices more than once boosting our performance.


## Deferred Rendering

We will have four distinct stages in deferred shading: geometry stage, lighting stage, post-processing stage and final stage.

**We will first implement a G-Buffer.**

**Geometry stage**

We will make the G-Buffer as the current render target. Once that the G-buffer is ready to receive data, the scene will be rendered. Firstly, we update the G-buffer's depth buffer. Next, material and geometric information of the scene are sent and a fragment shader is responsible for filling the rest of the G-buffer's data.

We have to postpone the transparent objects at this stage. An inspect pass will decide that the object is transparent, we will not add an auto-generated pass to the GBuffer, but instead copy it to render it regularly later (in final stage).

Another way of handling transparent objects for cheap lighting is:  [this](http://www.john-chapman.net/content.php?id=13) . We can implement this idea as it is.

**What data is passed to the G-Buffer**

The four textures generated by the material pass would include: (a) normal, (b) diffuse, (c) specular and (d) encoded depth as color.Choosing a texture format is not a trivial decision, and has quite a big impact on performance. Further research will be done prior implementation.

**Lighting stage**

The output of the geometry stage is the G-Buffer contents. They are the normal, diffuse, spcular and depth maps and will be the input for our lighting pass shader together with per light related information like position, color and radius.

We now have a prepared G-buffer with all the intermediate data we need to light the scene. Now, we will render each light to the scene, calculating its contribution to the final image.

When using deferred shading we do not need to know what geometry is illuminated by what light and could just process all lights we find visible to the viewer. While we traverse the scene for visible geometry we simply store the lights we find on the way (so lights do not need to know which geometry they will influence). 

We will use view culling applied to the light volumes and some type of occlusion culling to try to reduce the number of lights we need to render.

We will also be using [Stencil culling algorithm](http://kayru.org/articles/deferred-stencil/) for rendering deferred lights.

**Post-processing stage**

Another advantage of deferred rendering, is that some advanced post-filters require full-scene renders to get intermediate information about the scene and use it. If the G-Buffer contains this information, we can apply these effects without another full scene render. 

We will make sure that it is easy to pass information (such as textures) from different render sequences to each other.


**Final Stage**

The final image is shown; swap the buffers and show the scene. This might scale the resulting image to fit the target view window dimensions as the buffers used for deferred shading can have a different resolution than the final screen resolution.

At this stage, we can take care of the transparent objects, as mentioned [here](http://www.john-chapman.net/content.php?id=13).

Thus, a new rendering pipeline is developed.

### References and cool links

I found the following references useful, although some not directly appropriate for our use.

- [Deferred Rendering Architecture](https://hal.inria.fr/inria-00480869/document)
- [GPU Gems - Nvidia](http://http.developer.nvidia.com/GPUGems3/gpugems3_ch19.html)
- [Deferred Rendering Demystified](http://www.gamedev.net/page/resources/_/technical/graphics-programming-and-theory/deferred-rendering-demystified-r2746)
- [Transparency - A](http://www.john-chapman.net/content.php?id=13)
- [Transparency - B](http://techblog.floorplanner.com/rendering-transparency-in-a-deferred-pipeline/)

**Beyond GsoC**

Once such deferred renderer is developed, it can be extended to support:

- Shadow mapping
- Light volume clipping
- Add new post-effects such as SSAO using the post-effect system

I will also be working on transition of ODE-based to a new physics engine.

I will be contributing to the development of the organization, especially with adding WebGL and HTML (plugin free) client support.

We can work on this as a non-deadline based project or chop them into various GCI tasks.

# Availability

I’m pretty sure that i’ll be able to devote about 40 - 50 hours every week to the project during the GSoC coding period. 

# Issues/ Shortcomings

1. There are several algorithmic drawbacks with deferred shading - transparent objects are hard to handle, anti-aliasing can not be used on legacy hardware, additional memory consumption because of the G-Buffer.

2. In addition to that, deferred shading is harder to implement - it overrides the entire pipeline. Pretty much everything is rendered using manual shaders - which probably means a lot of shader code.

# About me

- [About](/index.html)

I am planning to blog my progress atleast once in two weeks. I think this is a good way to post progress on my project.

I am fairly new to GSoC as this will be my first experience, but I am looking forward to build this amazing application with you and begin my journey in Open Source!

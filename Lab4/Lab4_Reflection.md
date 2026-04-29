# Lab 4 Reflection

## Setup — The Game Loop
[OBSERVE] The loop has three numbered sections. In plain English, what does each section do? Why do you think they have to happen in that order?
- 1st: It handles events, like when the user wants to quit or press keys.
- 2nd: It updates what is happening, like movement, mouse position, and particles.
- 3rd: It draws everything on the screen so we can see it. 

## Part 2: Movement
### 2A
[OBSERVE] What happens when the circle reaches the edge? Trace through the bounce logic in your head — why does negating vx cause a bounce?
- When the circle reaches the edge, it bounces back. Negating vx changes the horizontal direction. For example, if it was moving right, it starts moving left.

### 2c
[OBSERVE] How many times per second does the print fire? What controls that rate?
- The print fires about 60 times per second because the game loop runs at 60 FPS. The clock.tick(FPS) controls that rate.

## Part 3: Classes and Particles
### 3A
[OBSERVE] Describe what happens when you click. Where do the particles go and why? Look through __init__ — what determines the direction each particle travels?
- When I click, many small particles come out from where I click. They go in different directions. This happens because in __init__ the angle and speed are random, so every particle moves different way..

### 3B
[OBSERVE] How does the behavior change? What is the maximum number of particles alive at once? What controls that?
- Now when I hold the mouse, particles keep coming again and again, not just one time. There is a lot of particles on screen. The max number depends on how fast we create them and how fast they die (life and decay).

### 3C
[OBSERVE] Try set_alpha(80) and set_alpha(5). Describe the difference. What does alpha control about the trail?
- When I use set_alpha(80), the trail disappears faster. When I use set_alpha(5), the trail stays longer and looks smoother. Alpha controls how fast the old drawing fades away.

## Part 4: Generative Art Mode
### 4A
[OBSERVE] Hold the right mouse button. What happens to the particles? Release it. What happens then?
- When I hold the right mouse button, the particles move toward the mouse like its taking it in. When I release it, they stop following and just move normal again. 

### 4B
[OBSERVE] Press space to cycle modes while painting. Which mode looks most "alive"? What is it about the color that creates that feeling?
- The fire-ish(red and orange) mode looks more alive to me because the colors look like real fire and it feels more active.

### 4C
[OBSERVE] Turn gravity off and paint with the mouse. How does the behavior change? What kind of natural system does zero-gravity mode remind you of?
- When gravity is off, particles don’t fall down. They move freely around. It looks like space or something floating.

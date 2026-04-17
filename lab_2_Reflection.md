# lab 2
## Model 1:
1. Describe what you see during the first 10 seconds. How does the pattern change over time?
    * Just a rectangle shaped block forming in to a doubled layered rectangles 
2. Click and drag on the canvas. What happens where you paint? Does the pattern respond differently in areas that are already patterned versus empty areas?
    * It kind erases it but keeps the outline of the erased part and make more unique patterns out of it

## Model 2:
1. Without changing anything, describe the overall behavior after ~20 seconds. Do the colors cluster? Scatter? Chase each other?
    * Some cluster together specially green but they are mainly scattered around looking like they are fighting each other but then run from each other.
2. Run the script again (a new random attraction matrix is generated each time). How different is this run from the last? What does that tell you about the role of the attraction matrix?
    * This time the red ones are clustered together and the other ones are scattered around. It looks like they are chasing each other. about the role of the attraction matrix i think it just 
## Model 3:
1. For the first several seconds, the trails stay close together. Then they diverge. Approximately how long does it take before the trails look completely different from each other?
    * 20 to 30 seconds
2. Try changing base_angle to np.pi * 0.2 (a small, low-energy swing). Do the trails diverge as quickly? Why do you think that is?
    * At first, the trails do not diverge quickly and they stay close together. But after some time, they start to diverge fast. I think this happens because the system starts with low energy and small movement, so differences are small at the beginning. As time goes on, even small differences grow larger and cause the paths to separate quickly.
## Model 4:
1. Run the script twice without changing anything. Describe how the two galaxies differ. What is the source of that variation?
    * The two galaxies look similar, but they are not exactly the same. The stars are placed in different positions, the brightness changes a little, and the clumps are in different spots. This happens because the code uses random values each time it runs.
2. Change NUM_ARMS to 2, then 6. How does the visual feel change?
    * When I change it to 2, the galaxy looks more simple and open. When I change it to 6, it looks more full and crowded. The number of arms changes how dense and detailed the galaxy looks.
    
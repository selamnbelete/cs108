# Lab 5 Reflection 

## Model 1 — Parametric Surface: The Torus
1. Change R to 0.5 and r to 1.5 (swap them). Describe what happens to the shape. What does this tell you about the relationship between the two radii?
- When I changed R to 0.5 and r to 1.5, the torus looked strange and more twisted. It did not look like a normal donut anymore. This shows that the big radius and small radius work together to control the shape. Usually the main radius should be bigger than the tube radius.
2. Replace with the below version. How does the density pattern change?
- In the new version, the points looked more organized and smooth. Before, the points looked random, but now the density pattern looks more even and clean around the torus.

## Model 2 — Particle System: Nebula
3. Change vel to np.random.randn(N, 3) * 0.005. How does this change the feel of the simulation?
- When I changed vel to np.random.randn(N, 3) * 0.005, the particles moved much slower. The simulation felt calmer and softer, like slow smoke or fog.
4. Comment out the pos[np.abs(pos) > 5] *= -0.5 line. What happens over time? What does this line do?
- When I removed the pos[mask] *= -0.5 line, the particles slowly moved far away from the center. After some time, many particles disappeared from the screen. This line helps keep the particles inside the space.

## Model 3 — Simulation: 3D Reaction-Diffusion Field
5. Change res from 30 to 15, then to 50. What are the tradeoffs?
- When res was 15, the simulation was faster but not very detailed. When res was 50, the simulation looked smoother and more detailed, but it became slower. The tradeoff is between speed and quality.

## Model 4 — Generative Art: Lissajous Ribbon
6. Change a, b, c to 3, 4, 5 then to 2, 3, 7. How do the ratios between the three frequencies affect the shape?
- Changing a, b, and c changed the ribbon shape a lot. Different number ratios made different patterns. Some looked more smooth and balanced, while others looked more complex and tangled.
7. The curve is drawn as individual points. Change size from 2 to 6. What does the ribbon look like now?
- When I changed the size from 2 to 6, the ribbon looked thicker and brighter. The points connected together more and looked like a glowing cloud.

## Model 5 — Quantum Star Bloom (3D Data Visualization)
8. Orbit and rotate the structure slowly. Where do the brightest regions form? Do they correspond to fixed “clusters,” or do they appear and disappear over time?
- The brightest regions formed in different parts of the structure while it was moving. They did not stay in one fixed place. The bright clusters appeared and disappeared over time.
9. Watch how regions of high color intensity evolve. Do they remain stable, drift, or reorganize into new structures?
- The high color areas kept changing shape. Some parts drifted slowly, while others mixed together and formed new structures. The animation looked alive and always changing.
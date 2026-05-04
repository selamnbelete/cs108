# Lab 5 Reflection 

## Model 1 — Parametric Surface: The Torus
1. Change R to 0.5 and r to 1.5 (swap them). Describe what happens to the shape. What does this tell you about the relationship between the two radii?
2. Replace with the below version. How does the density pattern change?

## Model 2 — Particle System: Nebula
3. Change vel to np.random.randn(N, 3) * 0.005. How does this change the feel of the simulation?
4. Comment out the pos[np.abs(pos) > 5] *= -0.5 line. What happens over time? What does this line do?

## Model 3 — Simulation: 3D Reaction-Diffusion Field
5. Change res from 30 to 15, then to 50. What are the tradeoffs?

## Model 4 — Generative Art: Lissajous Ribbon
6. Change a, b, c to 3, 4, 5 then to 2, 3, 7. How do the ratios between the three frequencies affect the shape?
7. The curve is drawn as individual points. Change size from 2 to 6. What does the ribbon look like now?

## Model 5 — Quantum Star Bloom (3D Data Visualization)
8. Orbit and rotate the structure slowly. Where do the brightest regions form? Do they correspond to fixed “clusters,” or do they appear and disappear over time?
9. Watch how regions of high color intensity evolve. Do they remain stable, drift, or reorganize into new structures?
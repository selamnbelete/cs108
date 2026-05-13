# Lab 6 Reflection

## Part 1: FFT Audio Visualizer

**[OBSERVE1]**
- During the quiet section, the bars moved less and stayed smaller. During the loud section, the bars moved a lot more and got taller. Most of the bigger movement was on the left side, which is the low frequencies like bass and drums. The right side also moved, but not as much.

**[OBSERVE2]** 
- When I changed peak_decay = 0.97 to 0.5, the pink dots fell down much faster. Before, they stayed at the top for a little while, but with 0.5 they disappeared very quickly. The visualizer looked more jumpy and less smooth.

## Part 2: Algorithmic MIDI with mido and pygame
**[OBSERVE3]**
- No, it did not sound the same every time. The melody changed a little each run because the code uses random.choice() and random.randint(). Those random parts choose different notes, durations, and velocities each time.

**[OBSERVE4]**
- When I changed it to bpm=60, the melody sounded slower and more calm. It kinda felt emotional or relaxing. When I changed it to bpm=220, it sounded very fast and more exciting, but also more chaotic and harder to follow. The faster speed changed the whole feeling of the music, not only the tempo.

**[OBSERVE5]**
- With depth=1, the melody was simple and short. With depth=2, it became more detailed and repeated more patterns. With depth=3, the music sounded much more complex and busy. It felt like the same small pattern kept repeating inside bigger patterns.

## Part 3: Euclidean Rhythms
**[OBSERVE6]**
- When I played E(4,4), I heard a beat on every step, like a steady drum beat. When I played E(1,8), I only heard one beat and then silence for the rest. These two extremes show that the algorithm is spreading the beats evenly across the slots.

**[OBSERVE7]**
- Yes, the combination sounded like a real drumbeat from actual music. The different layers worked together and made it sound more full. When I changed the middle layer to E(4,8), the rhythm sounded more regular and less interesting because the beats became more evenly repeated.

## Part 4: Cellular Automaton Music
**[OBSERVE8]**
- Each seed made completely different music. The notes and patterns changed depending on the seed number. When I used the same seed twice, I got the same music again. This happened because the random numbers are repeated the same way with the same seed.

**[OBSERVE9]**
- When I changed it to > 0.5, the music became much busier and louder because there were more living cells at the start. Sometimes it sounded messy. When I changed it to > 0.9, the music became more quiet and simple because there were fewer notes playing. The starting density really changed how active the music became later.

## Model 5: Ollama → JSON → Sound
**[OBSERVE10]**
- No, I did not get the same melody twice. Even with the same prompt, the notes and rhythm changed a little each time. This shows that LLMs generate sequences with randomness, so the output is not always exactly the same.

**[OBSERVE11]**
- Your prompt:Compose a happy jazz melody with a smooth relaxing feeling.
- What the model composed (describe the melody): The melody sounded soft and calm with some higher notes that made it feel happy. The rhythm was smooth and not too fast. It kind of sounded like background music in a cafe.

## Model 6: Ollama → ABC Notation → MIDI → Sound
**[OBSERVE11]**
- Yes, the Dorian melody sounded different from a normal minor melody. It still sounded a little dark, but not as sad. It had a more mysterious and smooth feeling. The waltz melody also sounded different because the 3/4 rhythm made it feel like dancing music.

## Model 7: Ollama → Python Code → Sound
**[OBSERVE12]**
- jhgk

**[OBSERVE13]**
- Your prompt:
- did the code run? What did it produce?


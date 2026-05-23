# Sequence Generator for Shape-Color-Pattern Stimuli

This script generates a randomised sequence of experimental trials in the format **`XX.YY.ZZ`**, where:

- **`XX`** = Shape (hex `00`–`07`, 8 unique shapes)  
- **`YY`** = Color  (hex `00`–`03`, 4 colors)  
- **`ZZ`** = Pattern (hex `00`–`03`, 4 patterns)

Every possible `Shape.Color` pair appears **exactly once** (8 × 4 = 32 trials).  
Patterns are randomly assigned to colors **for each shape** – no two shapes share the same color‑pattern mapping.

The generator enforces **cooldown constraints** to avoid close repetitions that could bias results:

- **Shape cooldown** – a shape may not reappear within the next **4 trials** (i.e., at least 4 different shapes must occur between two occurrences of the same shape).  
- **Pattern cooldown** – a pattern may not reappear within the next **2 trials** (at least 2 different patterns must occur between two occurrences of the same pattern).

Colors have no cooldown; they are balanced across all shapes.

Every run produces a **different randomised order** that satisfies all constraints.

---

## How the Code Works

1. **Dictionary of pairs** – each shape gets two parallel lists: colors and patterns, randomly paired 1‑to‑1.  
2. **Round‑based selection** – all shapes start with 4 color‑pattern pairs. The algorithm works in *rounds* (max length → 3 → 2 → 1), picking every shape exactly once per round.  
3. **Repetition check** – short‑term memory tracks the last trial index of each shape and pattern. A candidate is eligible only if both cooldowns have expired.  
4. **Random pick** – a random eligible shape is chosen, then a random valid color‑pattern pair from that shape.  
5. **Output & update** – the trial string (`shape.color.pattern`) is saved, the used pair is removed, and the memory is updated.  
6. **Repeat** until all 32 trials are generated.

If a deadlock ever occurs (extremely unlikely with these loose constraints), the algorithm simply restarts automatically.

---

## Customisation Points (top of the script)

```python
NUM_ITEMS      = 8    # number of shapes (0x00–0x07)
NUM_VARIATIONS = 4    # number of colors (0x00–0x03)
NUM_STYLES     = 4    # number of patterns (0x00–0x03)

ITEM_COOLDOWN  = 4    # min. trials between same shape
STYLE_COOLDOWN = 2    # min. trials between same pattern
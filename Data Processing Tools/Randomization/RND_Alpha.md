# Sequence Generator – RND_Alpha

This generator produces an ordered sequence of experimental conditions, each combining a **Shape**, a **Color**, and a **Pattern**. The output is a list of codes in the format `XX.YY.ZZ`, where:

- `XX` = Shape ID (two‑digit hex, e.g. `00`–`07` for up to 8 shapes)  
- `YY` = Color ID (`00`–`03` for up to 4 colors)  
- `ZZ` = Pattern ID (`00`–`03` for up to 4 patterns)

Every shape–color pair appears exactly once, and each shape receives a randomised pattern assignment. The sequence also enforces **spacing rules** to avoid close repetitions:

- A shape cannot appear again within **4** other conditions.  
- A pattern cannot appear again within **2** other conditions.

---

## Example Configuration

**Shapes (8)**  
`00` = Circle, `01` = Square, `02` = Triangle, `03` = Star,  
`04` = Diamond, `05` = Hexagon, `06` = Cross, `07` = Heart.

**Colors (4)**  
`00` = Red, `01` = Blue, `02` = Green, `03` = Yellow.

**Patterns (4)**  
`00` = Solid, `01` = Dotted, `02` = Striped, `03` = Checkered.

**Resulting sequence length:** 8 shapes × 4 colors = 32 conditions.

---

## Sample Output (first 5 lines)
05.02.01  
01.00.03  
03.03.00  
07.01.02  
00.01.00  
…

---

## Interpreting a Code

`05.02.01` → **Hexagon**, **Green**, **Dotted**.

| Shape | Color | Pattern |
|-------|-------|---------|
| `05` → Hexagon | `02` → Green | `01` → Dotted |

Use the tables above to map every code to a human‑readable condition.

---

## Key Design Features

- **Full coverage** – Every shape is tested with every color exactly once.
- **Randomised patterns** – Pattern assignments are shuffled within each shape, ensuring all patterns appear equally (8 times each).
- **Spaced repetitions** – You will never see the same shape again until at least 4 other shapes have passed, and a pattern will not repeat within 2 other conditions. This avoids clustering and potential carry‑over effects.

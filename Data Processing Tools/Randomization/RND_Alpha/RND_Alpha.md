# Sequence Generator – RND_Alpha

This generator produces a simple pre-generated semi-randomized ordered sequence, combining 3 variables. The output is a list of codes in the format `XX.YY.ZZ`, where:

- `XX` = Independent Var 1 - (General Category)
- `YY` = Non-Dependant - (Randomize Picture/Variations)  
- `ZZ` = Testing Variable - (must be identical in length to "YY")

Every XX - YY pair appears exactly once, and each XX receives a randomised ZZ assignment. The sequence also enforces **spacing rules** to avoid close repetitions:

- XX cannot appear again within set conditions.  
- ZZ cannot appear again within set conditions.

---

## Usage Case  

Used for sequences comparing changes (ZZ) utilizing examples of (XX) with (YY) variations.  

In the case below, it is utilized for creating a random sequence comparing patterns across shapes, while ensuring each Shape, Color and Pattern is Unique.  

---

## Example Configuration

**XX - Shapes (8)**  
`00` = Circle, `01` = Square, `02` = Triangle, `03` = Star,  
`04` = Diamond, `05` = Hexagon, `06` = Cross, `07` = Heart.

**YY - Colors (4)**  
`00` = Red, `01` = Blue, `02` = Green, `03` = Yellow.

**ZZ - Patterns (4)**  
`00` = Solid, `01` = Dotted, `02` = Striped, `03` = Checkered.

**Resulting sequence length:** 8 shapes × 4 patterns = 32 conditions.

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

|   Shape - XX   |   Color - YY | Pattern - ZZ  |
|----------------|--------------|---------------|
| `05` → Hexagon | `02` → Green | `01` → Dotted |

Use the tables above to map every code to a human‑readable condition.

---

## Key Design Features

- **Full coverage** – Every XX is tested with every YY exactly once.
- **Randomised patterns** – ZZ assignments are shuffled within each XX, ensuring all ZZ appear equally.
- **Spaced repetitions** – You will never see the same XX or ZZ again until at least a set number of itr's have passed. This avoids clustering and potential carry‑over effects.

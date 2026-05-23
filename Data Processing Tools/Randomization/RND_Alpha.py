import random


# CUSTOMISATION – change these three numbers as needed
# =============================================================================
NUM_ITEMS       = 20   # 0x00 … 0x13  (up to 0xFF = 256)
NUM_VARIATIONS  = 9    # 0x00 … 0x08
NUM_STYLES      = 9    # 0x00 … 0x08

# Cooldown requirements (must stay at least this many other codes apart)
ITEM_COOLDOWN   = 5    # skip 5 items → 6 positions between repetitions
STYLE_COOLDOWN  = 3    # skip 3 styles → 4 positions between repetitions
# =============================================================================


def generate_hex_sequence():
    # ---- Create the hexadecimal identifiers ----
    items      = [f"{i:02X}" for i in range(NUM_ITEMS)]       
    variations = [f"{i:02X}" for i in range(NUM_VARIATIONS)]  
    styles     = [f"{i:02X}" for i in range(NUM_STYLES)]     

    # ---- Step 1: Build the dictionary ----------------------------------------
    # Each item gets a random pairing of variation and style.
    # Stored as two parallel lists (variations, styles) that shrink as we pick.
    item_pool = {}
    for item in items:
        shuffled_styles = styles[:]
        random.shuffle(shuffled_styles)
        item_pool[item] = (variations[:], shuffled_styles)   # (var_list, style_list)

    # ---- Short‑term memory for cooldown (last position where used) -----------
    last_item_pos  = {item: -1 for item in items}
    last_style_pos = {style: -1 for style in styles}

    result_sequence = []
    pos = 0

    # ---- Repeat rounds until all 180 codes are generated --------------------
    while True:
        # Determine the current maximum length among remaining items
        remaining_items = [it for it in items if len(item_pool[it][0]) > 0]
        if not remaining_items:
            break

        max_len = max(len(item_pool[it][0]) for it in remaining_items)
        # Items that still need to be picked in this round (all have max_len)
        round_candidates = [it for it in remaining_items if len(item_pool[it][0]) == max_len]

        # Process this round: pick each candidate exactly once
        while round_candidates:
            # ---- Step 3: Repetition check ----------------------------------
            eligible = []
            for it in round_candidates:
                # Item cooldown: must not have been used in the last ITEM_COOLDOWN positions
                if last_item_pos[it] != -1 and pos - last_item_pos[it] <= ITEM_COOLDOWN:
                    continue
                # Check if at least one style of this item satisfies the style cooldown
                has_valid_style = any(
                    last_style_pos[style] == -1 or pos - last_style_pos[style] > STYLE_COOLDOWN
                    for style in item_pool[it][1]
                )
                if has_valid_style:
                    eligible.append(it)

            # In the extremely unlikely event of a deadlock, restart the run
            if not eligible:
                return generate_hex_sequence()

            # ---- Step 2: Random pick -----------------------------------------
            chosen_item = random.choice(eligible)
            vars_list, styles_list = item_pool[chosen_item]

            # Find all valid (var, style) indices for the chosen item
            valid_indices = [
                idx for idx, style in enumerate(styles_list)
                if last_style_pos[style] == -1 or pos - last_style_pos[style] > STYLE_COOLDOWN
            ]
            chosen_idx = random.choice(valid_indices)

            chosen_var   = vars_list[chosen_idx]
            chosen_style = styles_list[chosen_idx]

            # ---- Step 4: Build the output string -----------------------------
            code = f"{chosen_item}.{chosen_var}.{chosen_style}"
            result_sequence.append(code)
            print(code)   # display; you can also collect it in a list/file

            # ---- Step 5: Update memory and pool ------------------------------
            last_item_pos[chosen_item]   = pos
            last_style_pos[chosen_style] = pos

            # Remove the used pair from the item’s lists
            vars_list.pop(chosen_idx)
            styles_list.pop(chosen_idx)

            round_candidates.remove(chosen_item)   # done for this round
            pos += 1

    return result_sequence

# ---- Example run ----
if __name__ == "__main__":
    seq = generate_hex_sequence()
    print(f"\nGenerated {len(seq)} codes.")

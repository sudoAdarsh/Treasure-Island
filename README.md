# Treasure Island: The Awakening

A cinematic, text-based adventure game written in Python.  
Embark on a journey full of choices, suspense, and danger. Will you uncover the legendary treasure or meet a grim fate on the island?

---

## Overview

This is an immersive **command-line adventure game** featuring:

- ASCII art logo with dramatic reveal
- Typing-effect text for a cinematic experience
- Multiple decision scenes: Crossroad, Misty Lake, and the Three Doors
- Branching story paths with different endings (win or game over)
- Option to restart the game at any point by typing `"restart"`
- Lightweight — runs in any terminal without external libraries

---

## Requirements

- Python **3.7 or newer**
- Works on Windows, Linux, or macOS (uses `os.system` for clearing screen)

No external libraries are required.

---

## How to Play

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/treasure-island.git
   cd treasure-island
   ```

2. Run the game:

   ```bash
   python main.py
   ```

---

## Game Scenes & Controls

### Scenes

1. **Crossroad** – Choose between the left forest path or the right cliff path.
2. **Misty Lake** – Decide whether to wait for a boat or swim across.
3. **Three Doors** – Pick the Red, Blue, or Green door to determine your fate.

### Controls

- **Typing choices** → Type the exact option displayed (case-insensitive)
- **Restart** → Type `"restart"` anytime to begin from the first scene
- **Replay** → Run the script again to replay the game

---

## Notes

- Game includes **ASCII art intro** for a cinematic effect.
- Decisions are **branch-based** — one wrong choice leads to `Game Over`.
- The game prints messages with **dynamic typing effect** for better immersion.
- Easily extendable: add more scenes, doors, or endings to expand the adventure.

---

## Author

**Adarsh Upadhyay**

# Asteroids

A Python implementation of the classic Asteroids game, built with Pygame.

## Running Locally

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (recommended)

### Installation and Running

**Using `uv` (Recommended):**
```bash
# Clone the repository and navigate to the project directory
uv run main.py
```

**Using standard Python (`pip`):**
```bash
# Clone the repository and navigate to the project directory
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install .
python main.py
```

## Extending the Project
You've done all the required steps, but if you'd like to make the game your own, here are some ideas:

- Add a scoring system
- Implement multiple lives and respawning
- Add an explosion effect for the asteroids
- Add acceleration to the player movement
- Make the objects wrap around the screen instead of disappearing
- Add a background image
- Create different weapon types
- Make the asteroids lumpy instead of perfectly round
- Make the ship have a triangular hit box instead of a circular one
- Add a shield power-up
- Add a speed power-up
- Add bombs that can be dropped

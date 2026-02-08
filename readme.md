## Snake in Python

A simple Snake game with singleplayer, local two-player, and multiplayer modes.

-- note
Multiplayer code is mess. It works but do not look at the code :d

### Requirements

- Python 3.11+ recommended
- pygame

### Run

Singleplayer or local two-player:

```powershell
python .\snake.py
```

Multiplayer (start server first, then run two clients):

```powershell
python .\server.py
python .\snake.py
```

### Controls

Singleplayer:

- Move: WASD

Two-player (local):

- Player 1: WASD
- Player 2: Arrow keys

Menu shortcuts:

- 1: Singleplayer
- 2: Two-player

### Project structure

- snake.py: Pygame UI and game modes
- server.py: Multiplayer server
- client.py: Multiplayer client

### Notes

- For multiplayer, you need two game windows connected to the same server.
- The server uses localhost and port 55400 by default.

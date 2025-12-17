# Python Chess Game

A simple **command-line chess game** in Python using the [`python-chess`](https://pypi.org/project/chess/) library. Play interactively against another human by entering moves in **Standard Algebraic Notation (SAN)**.

---

## Features

- Interactive command-line chess board
- Supports all legal chess moves, including castling, en passant, and promotion
- Detects check, checkmate, stalemate, and draws
- Handles invalid moves gracefully
- Easy to run and modify

---

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/Ira-Singh-Parmar/python-chess-game.git
cd python-chess-game
```

Install dependencies:

```pip install chess```

---

## How to Play

**Run the game**:

python play_chess.py


Enter moves in Standard Algebraic Notation (SAN), e.g.:

- Pawn moves: e4, d5

- Knight moves: Nf3

- Bishop moves: Bc4

- Castling: O-O (king-side), O-O-O (queen-side)

- Captures: Nxe5, exd5

To quit the game anytime, press ```Ctrl+C```

---

**Notes** :

- Make sure your Python file is not named chess.py, otherwise it will conflict with the python-chess library.

- This game is for two players on the same computer; no AI is included.


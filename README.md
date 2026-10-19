# Python Mini-Games & Creative Graphics Showcase

A collection of classic 2D arcade games, puzzle challenges, grid-based tactical RPG mechanics, and procedural Turtle graphics art sketches built with **Python**, **Pygame**, **Tkinter**, and **Turtle**.

## 🎮 Games & Demos Catalog

### 🕹️ Arcade & Puzzle Games
1. **Tetromino (`tetromino.py`)**:
   - Classic falling-block game with line clearing, score multiplier, next-piece preview, and background MIDI music (`tetrisb.mid`).
   - Run: `python tetromino.py`
2. **Turn-Based Tactical RPG (`tacticalRPG.py`)**:
   - Grid-based strategy mechanics featuring player movement, enemy turn tracking, obstacle collisions, and combat actions.
   - Run: `python tacticalRPG.py`
3. **Memory Puzzle (`memorypuzzle.py`)**:
   - Grid-based visual memory matching game challenging players to reveal and pair identical icons.
   - Run: `python memorypuzzle.py`
4. **Slide Puzzle (`slidepuzzel.py`)**:
   - Classic 15-puzzle sliding block challenge with solvable board randomization.
   - Run: `python slidepuzzel.py`
5. **Pong Ball Game (`PongBallGame.py`)**:
   - Classic retro paddle-and-ball table tennis game.
   - Run: `python PongBallGame.py`
6. **Bounce Ball Series (`bounceball.py`, `BouncingBallGame.py`, `TheBouncingBallGame.py`)**:
   - Physics-based bouncing ball arcade games with paddle collision mechanics.
   - Run: `python bounceball.py`
7. **Tic-Tac-Toe (`TicTakToe.py`)**:
   - Two-player turn-based board game with Tkinter GUI.
   - Run: `python TicTakToe.py`
8. **Rock Paper Scissors (`RockPaperScissors.py`)**:
   - Quick interactive game against computer RNG with score tallying.
   - Run: `python RockPaperScissors.py`

### 🎨 Turtle Graphics & SVG Vector Art
Automated vector sketching engines that parse SVG contours and recreate portraits stroke-by-stroke using Python's `turtle` module:
- **`drstrange.py`**: Doctor Strange portrait sketching
- **`ironman.py`**: Iron Man mask and armor sketch
- **`radhekrishna.py`**: Radhe Krishna artistic contour drawing
- **`hanumanji.py`**: Lord Hanuman portrait sketch
- **`shivji.py`**: Lord Shiva portrait sketch
- **`sidhumoosewala.py`**: Sidhu Moose Wala portrait sketch
- **`flower.py`**: Procedural rainbow spiral rosette geometry

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShivamKR12/games.git
   cd games
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux / macOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch any game or demo, for example:
   ```bash
   python tetromino.py
   ```

---

## 🛠️ Tech Stack

- **Libraries**: Pygame, Tkinter, Turtle, OpenCV (`cv2`), svgpathtools, tqdm
- **Audio**: MIDI (`tetrisb.mid`)

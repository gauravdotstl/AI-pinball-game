# Pinball Game

This is a simple Pinball game built using Python and the Pygame library. The game features two sliders that automatically follow the ball, and a bouncing ball whose speed increases with each collision. The objective is to keep the ball in play using the sliders.

## Features
- Two AI-controlled sliders (left and right) that follow the ball.
- A ball that bounces off the sliders and the screen boundaries.
- The ball's speed increases after every collision with a slider.
- Game resets when the ball goes out of bounds.

## Requirements
- Python 3.7 or later
- Pygame library

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pinball-game.git
   cd pinball-game
   ```

2. Install the required dependencies:
   ```bash
   pip install pygame
   ```


1. Run the game script:
   ```bash
   python pinball_game.py
   ```
2. Watch as the AI sliders keep the ball in play. The game will reset if the ball goes out of bounds.


## Customization
- Adjust `slider_speed` to change the speed of the sliders.
- Modify `ball_speed` for different initial speeds of the ball.
- Change `speed_increase_percentage` to control how much the ball's speed increases after collisions.




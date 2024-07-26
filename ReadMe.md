# Text-Based Adventure Game

## Overview

This is a simple text-based adventure game implemented in Python. Players navigate through a dungeon, making choices to explore rooms, pick up items, and solve puzzles. The ultimate goal is to find the treasure and escape the dungeon.

## Features

- **Room Exploration**: Navigate through different rooms in the dungeon.
- **Item Management**: Pick up and use items.
- **Interactive Commands**: Use text-based commands to interact with the game.
- **Simple Game Mechanics**: Basic logic and interaction for a fun experience.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/text-based-adventure-game.git
2. **Navigate to the Project Directory**

    cd text-based-adventure-game
    Run the Game

### How to Play
1. **Commands**
    Movement Commands:

        north: Move to the room to the north.
        south: Move to the room to the south.
        east: Move to the room to the east.
        west: Move to the room to the west.
    Item Commands:

        take [item]: Pick up the specified item if it is present in the current room.
        use [item]: Use the specified item from your inventory.
    Inventory Command:

        inventory: Display the items currently in your inventory.

### Example Gameplay
    Welcome to the Dungeon Adventure Game!

    You are at the entrance of the dungeon. There is a dark hallway to the north.
    Available commands: north, south, east, west, take [item], use [item], inventory

    What do you want to do? north

    You are in a long hallway. There are rooms to the north and south, and a door to the east.
    Available commands: north, south, east, west, take [item], use [item], inventory

    What do you want to do? take Magic Book

    You have taken the Magic Book.
    Available commands: north, south, east, west, take [item], use [item], inventory

    What do you want to do? use Magic Book

    You read the Magic Book and discover a secret passage!
    Available commands: north, south, east, west, take [item], use [item], inventory

    What do you want to do? east

    You are in the treasure room! There is a chest here.
    Available commands: north, south, east, west, take [item], use [item], inventory

    What do you want to do? use Treasure

    Congratulations! You have found the treasure and escaped the dungeon!

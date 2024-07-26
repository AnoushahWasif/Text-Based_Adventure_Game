class Room:
    def __init__(self, description, north=None, south=None, east=None, west=None, item=None):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.item = item

class AdventureGame:
    def __init__(self):
        # Define rooms and their connections
        self.rooms = {
            'Entrance': Room('You are at the entrance of the dungeon. There is a dark hallway to the north.', north='Hallway'),
            'Hallway': Room('You are in a long hallway. There are rooms to the north and south, and a door to the east.', north='Treasure Room', south='Entrance', east='Library'),
            'Library': Room('You are in a dusty library. There is a strange book on a pedestal.', west='Hallway', item='Magic Book'),
            'Treasure Room': Room('You are in the treasure room! There is a chest here.', south='Hallway', item='Treasure'),
        }
        self.current_room = 'Entrance'
        self.inventory = []

    def print_status(self):
        room = self.rooms[self.current_room]
        print(f"\n{room.description}")
        if room.item and room.item not in self.inventory:
            print(f"You see a {room.item}.")
        print("Available commands: north, south, east, west, take [item], use [item], inventory")

    def move(self, direction):
        room = self.rooms[self.current_room]
        next_room = getattr(room, direction, None)
        if next_room:
            self.current_room = next_room
            self.print_status()
        else:
            print("You can't go that way.")

    def take_item(self, item):
        room = self.rooms[self.current_room]
        if room.item == item:
            self.inventory.append(item)
            room.item = None
            print(f"You have taken the {item}.")
        else:
            print(f"There is no {item} here.")

    def use_item(self, item):
        if item in self.inventory:
            if item == 'Magic Book' and self.current_room == 'Library':
                print("You read the Magic Book and discover a secret passage!")
                self.rooms['Library'].east = 'Treasure Room'
            elif item == 'Treasure' and self.current_room == 'Treasure Room':
                print("Congratulations! You have found the treasure and escaped the dungeon!")
                exit()
            else:
                print(f"You can't use the {item} here.")
        else:
            print(f"You don't have a {item}.")

    def play(self):
        print("Welcome to the Dungeon Adventure Game!")
        self.print_status()
        while True:
            command = input("\nWhat do you want to do? ").strip().lower()
            if command in ['north', 'south', 'east', 'west']:
                self.move(command)
            elif command.startswith('take '):
                self.take_item(command.split(' ', 1)[1])
            elif command.startswith('use '):
                self.use_item(command.split(' ', 1)[1])
            elif command == 'inventory':
                print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'empty'}")
            else:
                print("Invalid command. Please try again.")

if __name__ == "__main__":
    game = AdventureGame()
    game.play()

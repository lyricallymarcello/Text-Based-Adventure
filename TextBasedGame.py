# Marcellus Johnson - IT140 - 21EW4 - 7 - ProjectTwo

# The Dictionary Links A Room To Other Rooms And The Items In Those Rooms
rooms = {
    'Chamber of Awakening': {'North': 'Room of Rest', 'East': 'Armory', 'West': 'Apprentice Chamber',
                             'exit game': 'Exit Room'},
    'Room of Rest': {'South': 'Chamber of Awakening', 'West': 'Dark Room',
                     'North': 'Hall', 'exit game': 'Exit Room', 'item': 'Potion'},
    'Armory': {'West': 'Chamber of Awakening', 'exit game': 'Exit Room', 'item': 'Shield'},
    'Apprentice Chamber': {'East': 'Chamber of Awakening', 'North': 'Dark Room', 'exit game': 'Exit Room',
                           'item': 'Cloak'},
    'Dark Room': {'East': 'Room of Rest', 'South': 'Apprentice Chamber', 'North': "Mage's Quarters",
                  'exit game': 'Exit Room', 'item': 'Mythril'},
    "Mage's Quarters": {'East': 'Hall', 'South': 'Dark Room', 'exit game': 'Exit Room', 'item': 'Staff'},
    'Hall': {'North': "Destiny's Embrace", 'South': 'Room of Rest', 'East': "Master's Room",
             'West': "Mage's Quarters", 'exit game': 'Exit Room'},
    "Destiny's Embrace": {'South': 'Hall', 'exit game': 'Exit Room', 'item': 'Keyblade'},
    "Master's Room": {'West': 'Hall', 'item': 'Master of Masters'},
    'Exit Room': {'exit game': 'Exit Room'},
}


# Function For Player Status
def player_status(current_room):
    print('--------------------')
    print('You are currently in the', current_room + '.')
    print('Inventory:', inventory)
    if rooms.get(current_room).get('item') is None:
        pass
    else:
        print('You see the', rooms.get(current_room).get('item'))


# Function To Explain Premise And Print Instructions
def instructions():
    # Print A Main Menu And The Commands
    print('The Key of Light Adventure Game')
    print('--------------------')
    print("You are a wanderer whose journey has brought them to a mysterious tower.")
    print("This Tower is known as Memory's Skyscraper.")
    print('Collect 6 items to fulfill the prophecy and emerge victorious...')
    print('...or be destroyed by the Master of Masters.')
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


# Function To Add Item To Inventory
def get_item(user_choice):
    if user_choice == rooms.get(current_room).get('item'):
        print('You obtained:', rooms.get(current_room).get('item'))
        inventory.append(rooms.get(current_room).get('item'))
        del rooms[current_room]['item']
    else:
        print('There is no such item in this room.')


# Function To Print If Player Wins Game
def win_game():
    print('You have what you need to defeat the Master of Masters!')
    print('The Master charges forward. The Items of Prophecy Transform you into The Warrior of Light!')
    print('Using your newfound strength you defeat the Master of Masters!')
    print('Congratulations! Thank you for playing the game.')


def lose_game():
    print('You do not have the required items to fulfill the prophecy.')
    print('The Master kills you. Your death is painful and slow.')
    print('GAME OVER.')
    print('Thank you for playing the game.')


# Main Function
if __name__ == '__main__':
    # Start Player In The Chamber of Awakening
    current_room = 'Chamber of Awakening'
    # Premise And Instructions
    instructions()
    # Initialize Variables & List
    user_choice = None
    inventory = []

    player_status(current_room)

    # Game Loop
    while True:
        if current_room != "Master's Room":
            user_input = input('Which action will you take?: ').split()
            if len(user_input) != 2:
                print('That is not a valid option. Try again.')
                player_status(current_room)
            else:
                command = user_input[0]
                user_choice = user_input[1]
                # If User Types "get" First
                if command == 'get':
                    get_item(user_choice)
                    player_status(current_room)
                # If User Types "go" First
                elif command == 'go':
                    if user_choice in rooms[current_room]:
                        current_room = rooms[current_room][user_choice]
                        player_status(current_room)
                    else:
                        print('That is not a valid option. Try Again.\n')
                else:  # Input Validation
                    print('That is not a valid option. Try Again.\n')
        else:
            if current_room == "Master's Room":
                if len(inventory) == 6:
                    win_game()
                    break
                else:
                    lose_game()
                    break

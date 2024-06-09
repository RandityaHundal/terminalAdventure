`current_room = "start"

while True:

    if current_room == "start":

        print("You are in a dark room. There is a door to your right and left. Which one do you take?")
        choice = input("Options: left, right\n")

        if choice == "left":
            
            current_room = "left_room"
            
        elif choice == "right":
            
            current_room = "right_room"
            
        else:
            print("Invalid option. Please try again.")
            
    elif current_room == "left_room":
        
        print("You find a clue. It's a bloody knife. Do you pick it up or leave it?")
        choice = input("Options: pick it up, leave it\n")
        
        if choice == "pick it up":
            
            current_room = "end_game"
            
        elif choice == "leave it":
            
            current_room = "start"
            
        else:
            
            print("Invalid option. Please try again.")
            
    elif current_room == "right_room":
        
        print("You find a note. It says 'Beware the murderer'. Do you continue or leave?")
        choice = input("Options: continue, leave\n")
        
        if choice == "continue":
            
            current_room = "end_game"
            
        elif choice == "leave":
            
            current_room = "start"
            
        else:
            
            print("Invalid option. Please try again.")
            
    elif current_room == "end_game":
        
        print("The murderer appears and the game ends. You can play again.")
        current_room = "start"

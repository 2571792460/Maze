from models.maze import Maze


up = "w"
down = "s"
left = "a"
right = "d"
num_item = 4


def main():

    maze = Maze('maze.txt')
    print("Start of maze game \n")

    while True:
        maze.display()
        print()
        command = input("Please Move: ")
        parsed_command = str(command).lower()
        print()
        isInvalid = True
        (new_x, new_y) = maze._player_position
        if parsed_command == up:
            new_x -= 1
        elif parsed_command == down:
            new_x += 1

        elif parsed_command == left:
            new_y -= 1

        elif parsed_command == right:
            new_y += 1

        if maze.can_move_to(new_x, new_y):
            isInvalid = False
            if maze.is_item(new_x, new_y):
                maze._player.pick_up_item(maze._map[new_x][new_y])
            if maze.is_exit(new_x, new_y):
                print("**** Exit Reached ****")
                if len(maze._player._backpack) == num_item:
                    print("You have won the game")
                else:
                    print("You lost the game because you did not collect all items")
                break
            (current_x, current_y) = maze._player_position
            maze._map[current_x][current_y] = maze.space_symbol
            maze._map[new_x][new_y] = maze.player_symbol
            maze._player_position = (new_x, new_y)
        if isInvalid:
            print("Invlaid Command")


if __name__ == "__main__":
    main()

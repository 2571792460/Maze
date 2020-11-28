import pygame
import pygame.locals
from maze.models.maze import Maze
from maze.models.picture import Wall, Character, Items, Floor, Exit
from maze.models.player import Player
from maze.views.maze_view import MazeView
from maze.models.score import Score
import datetime
import wave

class App:

    def run(self):

        """"Main function to run the game"""

        # Set up the screen

        mazeview = MazeView()
        window = mazeview.build_screen()

        # New character image
        character = Character()
        # New wall image
        wall = Wall()
        # New item image
        item = Items()
        # New exit image
        exit = Exit()
        # New floor image
        floor = Floor()
        # New Player
        player = Player()
        # New maze
        maze = Maze('maze.txt')
        # Create a countdown timer
        timer = 60
        dt = 0

        # Set up player start position
        player_line_number = 0
        player_column_number = 0

        # Create Win and Lose text
        font = pygame.font.SysFont("comicsansms", 35)
        text_win = font.render('You have Win the Game', True, (0, 255, 0))
        text_lost = font.render('You lost the Game', True, (0, 255, 0))

        textRect_win = text_win.get_rect()
        textRect_lost = text_lost.get_rect()

        # Update player position
        for i, sub_list in enumerate(maze.map):
            for n, elements in enumerate(sub_list):
                if elements == "P":
                    character.rect.x = n * 100
                    character.rect.y = i * 100
                    player_line_number = i
                    player_column_number = n

        # Game Title is called maze game
        pygame.display.set_caption("maze game")

        file_path = './models/Bog-Creatures-On-the-Move .wav'
        file_wav = wave.open(file_path)
        frequency = file_wav.getframerate()
        pygame.mixer.init(frequency=frequency)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        music = pygame.mixer.Sound(file_path)
        music.play(-1)

        running = True
        while running:
            # Paint the screen grey
            window.fill((100, 100, 100))

            # music = pygame.mixer.Sound("./models/Bog-Creatures-On-the-Move.mp3")
            # music.play()

            # Event loop - quit if closed or 'escape' is pressed
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False
                elif event.type == pygame.locals.KEYDOWN:
                    if event.key in (pygame.locals.K_ESCAPE, pygame.locals.K_SPACE):
                        running = False

            # Base on maze.txt, arrange wall image, item image and exit image at proper position
            for i, sub_list in enumerate(maze.map):
                for n, elements in enumerate(sub_list):
                    if elements == "X":
                        window.blit(wall.image, (n * 100, i * 100))
                    elif elements == "0" or elements == "1" or elements == "2" or elements == "3":
                        window.blit(item.image, (n * 100, i * 100))
                    elif elements == "E":
                        window.blit(exit.image, (n * 100, i * 100))
                    else:
                        window.blit(floor.image, (n * 100, i * 100))

            # Create a new Clock object
            clock = pygame.time.Clock()
            timer -= dt
            dt = clock.tick(10) / 1000

            text_time = font.render(str(round(timer, 2)), True, (0, 255, 0))
            textRect_time = text_time.get_rect()
            window.blit(text_time, textRect_time)
            if timer <= 0:
                window.fill((255, 255, 255))
                window.blit(text_lost, textRect_lost)
                dt = 0
                text_time_cost = font.render(str(round(60 - timer, 2)), True, (0, 255, 0))
                window.blit(text_time_cost, (0, 100))

            text_backpack = font.render("You have collect {} items. (Total of 4)".format(len(player.backpack)), True, (0, 255, 0))
            # Make player move base on keyboard command
            keys = pygame.key.get_pressed()
            # Show number of items collected in backpack
            if keys[pygame.locals.K_i]:
                window.blit(text_backpack, (0, 100))

            # Make player move base on keyboard command
            elif keys[pygame.locals.K_d]:
                # Move the player right by 100 pixels
                if maze.can_move_to(player_line_number, player_column_number + 1) is True:
                    player_column_number = player_column_number + 1
                    character.rect.x = min(character.rect.x + 100, 700)
                    if maze.is_item(player_line_number, player_column_number) is True:
                        player.pick_up_item(maze.map[player_line_number][player_column_number])
                        maze.map[player_line_number][player_column_number] = maze.space_symbol

            elif keys[pygame.locals.K_a]:
                # Move the player left by 100 pixels
                if maze.can_move_to(player_line_number, player_column_number - 1) is True:
                    player_column_number = player_column_number - 1
                    character.rect.x = max(character.rect.x - 100, 0)
                    if maze.is_item(player_line_number, player_column_number) is True:
                        player.pick_up_item(maze.map[player_line_number][player_column_number])
                        maze.map[player_line_number][player_column_number] = maze.space_symbol

            elif keys[pygame.locals.K_w]:
                # Move the player up by 100 pixels
                if maze.can_move_to(player_line_number - 1, player_column_number) is True:
                    player_line_number = player_line_number - 1
                    character.rect.y = max(character.rect.y - 100, 0)
                    if maze.is_item(player_line_number, player_column_number) is True:
                        player.pick_up_item(maze.map[player_line_number][player_column_number])
                        maze.map[player_line_number][player_column_number] = maze.space_symbol

            elif keys[pygame.locals.K_s]:
                # Move the player down by 100 pixels
                if maze.can_move_to(player_line_number + 1, player_column_number) is True:
                    player_line_number = player_line_number + 1
                    character.rect.y = min(character.rect.y + 100, 600)
                    if maze.is_item(player_line_number, player_column_number) is True:
                        player.pick_up_item(maze.map[player_line_number][player_column_number])
                        maze.map[player_line_number][player_column_number] = maze.space_symbol

            # Update the player image
            window.blit(character.image, character.rect)

            # When player is at exit position, check player backpack and print proper text
            if maze.is_exit(player_line_number, player_column_number) is True:
                if len(player.backpack) == 4:
                    window.fill((255, 255, 255))
                    window.blit(text_win, textRect_win)
                    dt = 0
                    text_time_cost = font.render(str(round(60 - timer, 2)), True, (0, 255, 0))
                    window.blit(text_time_cost, (0, 100))
                    window.blit(text_backpack, (0, 200))
                    date = datetime.datetime.now().strftime("%c")
                    score = (int(timer) * 1) + (len(player.backpack) * 10)
                    # player_name = input("Enter a player name")
                else:
                    window.fill((255, 255, 255))
                    window.blit(text_lost, textRect_lost)
                    dt = 0
                    text_time_cost = font.render(str(round(60 - timer, 2)), True, (0, 255, 0))
                    window.blit(text_time_cost, (0, 100))
                    date = datetime.datetime.now().strftime("%c")
                    score = (int(timer) * 1) + (len(player.backpack) * 10)
                    # player_name = input("Enter a player name")

            # Update the screen
            pygame.display.update()
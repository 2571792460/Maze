# Maze
***
##### Maze is a python game that player need to collect items in a maze.


### Required libraries
##### In order to run Maze properly, you need to install pygame
1. ```python3 -m pip install -U pygame --user``` to install pygame
2. ```python3 -m pygame.examples.aliens``` to test pygame
##### To test Maze runs properly, you need to install pytest
1. ```pip install -U pytest``` to install pytest
2. ```$pytest --version``` to check pytest version



### Project Structure
The main structures of Maze are based on MVC design pattern.
##### main.py
This is the main which is used to run Maze.
##### maze.txt
This the the original maze layout.
##### controllers
This is the controllers folder. This folder contains all control system.
```__init__.py, app.py```
##### models
This is the models folder. This folder contains all the attributes and behaviours.
```__init__.py, maze.py, picture.py, player.py```
##### views
This is the views folder. This folder contains all information user can see.
```__init__.py, maze_view.py```
##### tests
This is the unittest folder. This folder contains all tests for controllers, models and views.



### Run Maze
1. Open `maze` folder with PyCharm
2. Run `main.py`



### Play Maze
##### elements:

**player**

![player](./maze/models/player.png)

**item**

![player](./maze/models/item.png)

**exit**

![player](./maze/models/exit.png)

##### move: 

`w` move up `s` move down `a` move left `d` move right

`esc` to exit Maze

##### Win/Lose condition:

If player collects all items and moves to exit, player wins.

If player haven't collected all items and moves to exit, player lose.



### unit test

|Method tested|ID|Comment|																			
|-------------|-----|--------------|	
|__init__|010A|maze class has attribute "_map", "_numRow", '_numCol', '_player', '_player_position'|
|can move|010B|maze can move to (1,1) , can not move to (0.0)|				
|is item|010C|(1,1) is an item and (1,3) is not an item|					
|is exit|010D|(4,6 ) is exit and (1,1) is not exit|
|__init__|020A|player class has attribute "_backpack"|					
|pick up item|020B|player backpack could pick up item "A"|
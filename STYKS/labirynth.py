import include
import random

maze1 = """   ##################################
         #           #              #
#  #  ####  #  #  #  ####  ####  #  #
#  #        #  #  #     #     #  #  #
#######  #  #######  ####  ##########
#     #  #  #  #  #        #  #  #  #
#  ####  ####  #  #  #  ####  #  #  #
#  #  #        #     #     #     #  #
#  #  ##########  ####  #######  #  #
#              #  #     #           #
#  ################  #  #  ####  ####
#              #     #     #  #     #
#  ##########  ####  ####  #  ####  #
#  #                 #        #      
##################################   """

maze2 = """   ##################################
      #                    #        #
#  #  #  #  #######  ####  #######  #
#  #  #  #  #     #     #           #
#  #############  ####  ####  #  ####
#           #  #           #  #  #  #
#  #######  #  ####  #############  #
#  #     #     #  #     #           #
#  ####  #  #  #  ####  #  #  #  ####
#  #  #     #     #     #  #  #     #
#  #  #  ####  #######  ####  ####  #
#     #  #  #  #     #           #  #
#  #  ####  #  #  ####  #  ####  ####
#  #        #           #     #      
##################################   """

maze3 = """   ##################################
                  #     #  #        #
#  #######  #  #######  #  #######  #
#        #  #  #  #  #  #           #
####  ##########  #  #  ####  #  ####
#     #  #     #              #     #
#  #  #  ####  #######  ##########  #
#  #     #        #           #     #
####  #  #  ####  #######  #  ####  #
#     #     #        #  #  #     #  #
#  ##########  ####  #  #  #  ####  #
#  #        #  #        #  #  #     #
####  #######  #  ####  #  #  #  #  #
#              #  #        #  #  #   
##################################   """

maze_list = (maze1,maze2,maze3)

def labirynth():
    print("Zszedłeś do katakumb pod Wyrocznią. Wyglądają na prawdziwy labirynt")
    print("Aby się po nim poruszać wpisuj kierunek ruchu. Możesz również napisać ilość oczek po kierunku")
    print("Przykład: [Prawo 10]")
    print("Aby się wydostać, wpisz POWRÓT")

    global axis_x
    global axis_y

    def maze_move(command,amount):
        global axis_x
        global axis_y
        wall = 0
        while amount != 0:
            if command in include.up_set:
                if not axis_y > 0:
                    wall = 1
                elif encoded_maze[axis_y - 1][axis_x] == "#":
                    wall = 1
                else:
                    axis_y -= 1
            elif command in include.down_set:
                if not axis_y < max_y:
                    wall = 1
                elif encoded_maze[axis_y + 1][axis_x] == "#":
                    wall = 1
                else:
                    axis_y += 1
            elif command in include.left_set:
                if not axis_x > 0:
                    wall = 1
                elif encoded_maze[axis_y][axis_x - 1] == "#":
                    wall = 1
                else:
                    axis_x -= 1
            elif command in include.right_set:
                if not axis_x < max_x:
                    wall = 1
                elif encoded_maze[axis_y][axis_x + 1] == "#":
                    wall = 1
                else:
                    axis_x += 1
            amount -= 1
        if wall == 1:
            print("Ściana!")
            input()

    encoded_maze = random.choice(maze_list)
    encoded_maze = encoded_maze.splitlines()
    max_y = len(encoded_maze) -1
    for element in range(max_y+1):
        encoded_maze[element] = list(encoded_maze[element])

    max_x = len(encoded_maze[1]) -1
    #input()
    axis_x = max_x
    axis_y = max_y
    encoded_maze[0][0] = "X"

    # Decode maze
    while True:
        action = ""
        amount = 0
        #print(axis_x)
        #print(axis_y)
        encoded_maze[axis_y][axis_x] = "■"
        for element in encoded_maze:
            print(' '.join(element))

        command = input()
        encoded_maze[axis_y][axis_x] = " "

        action = command.split(' ', 1)[0]
        amount = include.stringify(command.split(' ', 1)[1:])
        if amount == "":
            amount = 1
        amount = int(amount)
        if command in include.back_set:
            return "FAILURE"

        maze_move(action,amount)

        if axis_x == 0 and axis_y == 0:
            print("Dotarłeś do celu!")
            input()
            return "SUCCESS"

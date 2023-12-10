input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",]

# read from input.txt
with open('Day2/input.txt', 'r') as f:
    input = f.readlines()

# only 12 red cubes, 13 green cubes, and 14 blue cubes
# max_red = 12
# max_green = 13
# max_blue = 14
sum_of_power_games = 0
for game in input:
    # Parse the input, get the game id, and the cube counts
    game_id = game.split(":")[0]
    game_id = game_id.split(" ")[1]
    cube_counts = game.split(":")[1]
    # Split the cube counts into the rounds
    rounds = cube_counts.split(";")
    
    red_per_game = 0
    green_per_game = 0
    blue_per_game = 0
    for round in rounds:
        red_per_round = 0
        green_per_round = 0
        blue_per_round = 0
        # Split the round into the colors
        colors = round.split(",")
        for color in colors:
            # Split the color into the count and the color
            count = color.split(" ")[1]
            color = color.split(" ")[2]
            # trim whitespace and newlines
            color = color.strip()
            # Add the count to the correct color
            if color == "red":
                red_per_round += int(count)
            elif color == "green":
                green_per_round += int(count)
            elif color == "blue":
                blue_per_round += int(count)
            else:
                print("Error: unknown color")
        if red_per_round > red_per_game:
            red_per_game = red_per_round
        if green_per_round > green_per_game:
            green_per_game = green_per_round
        if blue_per_round > blue_per_game:
            blue_per_game = blue_per_round
        print(round)
        print("Round: {} red, {} green, and {} blue.".format(red_per_round, green_per_round, blue_per_round))
        print("Max  : {} red, {} green, and {} blue.".format(red_per_game, green_per_game, blue_per_game))
        print("---")
    print("Game {} has {} red, {} green, and {} blue.".format(game_id, red_per_game, green_per_game, blue_per_game))
    power_game = red_per_game * green_per_game * blue_per_game
    sum_of_power_games += power_game
        
print("The sum of the power games is {}.".format(sum_of_power_games))
        
        
input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",]

# read from input.txt
with open('Day2/input.txt', 'r') as f:
    input = f.readlines()

# only 12 red cubes, 13 green cubes, and 14 blue cubes
max_red = 12
max_green = 13
max_blue = 14
valid_ids = []
for game in input:
    # Parse the input, get the game id, and the cube counts
    game_id = game.split(":")[0]
    game_id = game_id.split(" ")[1]
    cube_counts = game.split(":")[1]
    # Split the cube counts into the rounds
    rounds = cube_counts.split(";")
    # Parse the cube counts
    red_per_round = 0
    green_per_round = 0
    blue_per_round = 0
    valid = True
    for round in rounds:
        if not valid:
            break
        # Split the round into the colors
        colors = round.split(",")
        for color in colors:
            # Split the color into the count and the color
            count = color.split(" ")[1]
            color = color.split(" ")[2]
            # Add the count to the correct color
            if color == "red":
                red_per_round += int(count)
            elif color == "green":
                green_per_round += int(count)
            elif color == "blue":
                blue_per_round += int(count)
        if red_per_round > max_red or green_per_round > max_green or blue_per_round > max_blue:
            print("Game {} is invalid.".format(game_id))
            valid = False
            break
        else:
            red_per_round = 0
            green_per_round = 0
            blue_per_round = 0
    if valid:
        print("Game {} is valid.".format(game_id))
        valid_ids.append(game_id)
        
sum_of_valid_ids = 0
for id in valid_ids:
    sum_of_valid_ids += int(id)
print("The sum of the valid game ids is {}.".format(sum_of_valid_ids))
        
        
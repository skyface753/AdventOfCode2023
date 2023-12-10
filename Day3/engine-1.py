input = [
"467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598..",
    ]

# read from input.txt
with open('Day3/input.txt', 'r') as f:
    input = f.readlines()

# Get all numbers, which have a adjacent symbol (also diagonal), but no distance
symbols = [] 
# [
#    {},
#    {3: '*'},
#    {},
#    {6: '#'} 
# ]
for line in input:
    # fill the symbols list 
    symbols.append({})
    # remove newlines
    line = line.strip()
    for i in range(len(line)):
        if line[i] != "." and not line[i].isdigit():
            symbols[-1][i] = line[i]

sum = 0
# go through the digits and check if they have a symbol in their vicinity
for index, line in enumerate(input):
    number = ""
    has_symbol = False
    for i in range(len(line)):
        if line[i].isdigit():
            number += line[i]
            # check if there is a symbol over 
            # index = index of line (y)
            # i = index of number (x)
            # Check if there is a symbol over (left, top, right), same (left, right), or under (left, bottom, right)
            if index > 0:
                if i > 0:
                    if i - 1 in symbols[index - 1]:
                        has_symbol = True
                if i in symbols[index - 1]:
                    has_symbol = True
                if i + 1 < len(line):
                    if i + 1 in symbols[index - 1]:
                        has_symbol = True
            if i > 0:
                if i - 1 in symbols[index]:
                    has_symbol = True
            if i + 1 < len(line):
                if i + 1 in symbols[index]:
                    has_symbol = True
            if index + 1 < len(input):
                if i > 0:
                    if i - 1 in symbols[index + 1]:
                        has_symbol = True
                if i in symbols[index + 1]:
                    has_symbol = True
                if i + 1 < len(line):
                    if i + 1 in symbols[index + 1]:
                        has_symbol = True
                        
            # symbol_over = symbols[index - 1] if index - 1 >= 0 else None
            # is_symbol_over = False
            # if symbol_over is not None:
            #     if i - 1 >= 0 and i - 1 in symbol_over:
            #         is_symbol_over = True
            #     if i in symbol_over:
            #         is_symbol_over = True
            #     if i + 1 < len(line) and i + 1 in symbol_over:
            #         is_symbol_over = True
            # symbol_same = symbols[index] if index in symbols else None
            # is_symbol_same = False
            # if symbol_same is not None:
            #     if i - 1 >= 0 and i - 1 in symbol_same:
            #         is_symbol_same = True
            #     if i in symbol_same:
            #         is_symbol_same = True
            #     if i + 1 < len(line) and i + 1 in symbol_same:
            #         is_symbol_same = True
            # symbol_under = symbols[index + 1] if index + 1 < len(input) else None
            # is_symbol_under = False
            # if symbol_under is not None:
            #     if i - 1 >= 0 and i - 1 in symbol_under:
            #         is_symbol_under = True
            #     if i in symbol_under:
            #         is_symbol_under = True
            #     if i + 1 < len(line) and i + 1 in symbol_under:
            #         is_symbol_under = True
            # if is_symbol_over or is_symbol_same or is_symbol_under:
            #     has_symbol = True
            # print("Is symbol over: {}, is symbol same: {}, is symbol under: {}".format(is_symbol_over, is_symbol_same, is_symbol_under))
        else:
            if number != "":
                print("Number: {} has symbol: {}".format(number, has_symbol))
                sum += int(number) if has_symbol else 0
                number = ""
                has_symbol = False
            
            
            
            
print(symbols)
print("Sum: {}".format(sum))
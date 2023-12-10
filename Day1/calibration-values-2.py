lines = ["78seven8"]

with open('Day1/calibration-input.txt', 'r') as f:
    lines = f.readlines()

zahlen = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digits = []
for line in lines:
    # digits are not always at the same position
    # so we have to find them
    # digits can be written as words or numbers
    # we have to find both
    found = {}
    # find words, e.g. "eight" => set found[0] = 8
    for zahl in zahlen:
        index = line.find(zahl)
        if index > -1:
            found[index] = zahlen.index(zahl)
            # Use rfind to find the last occurence of the word
            last_index = line.rfind(zahl)
            if last_index > index:
                found[last_index] = zahlen.index(zahl)
                
    # find numbers
    for index, char in enumerate(line):
        if char.isdigit():
            found[index] = int(char)
                
    # sort the positions
    positions = sorted(found.keys())
    # build the number
    number = ""
    for position in positions:
        number += str(found[position])
    # get the first and last number
    first = int(number[0])
    last = int(number[-1])
    # concatenate the first and last number
    digits.append(int(str(first) + str(last)))

print(digits)        
    
sum = 0
for digit in digits:
    sum += digit
print(sum)



lines = []
with open('calibration-input.txt', 'r') as f:
    lines = f.readlines()
print(lines)

digits = []
# get the first and the last digit of each line
# and convert them to integers
# pqr3stu8vwx -> 38
for line in lines:
    # digits are not always at the same position
    # so we have to find them
    firstDigit = None
    lastDigit = None
    for char in line:
        if char.isdigit():
            if firstDigit is None:
                firstDigit = char
                lastDigit = char
            else:
                lastDigit = char
    digits.append(int(firstDigit + lastDigit))
sum = 0
for digit in digits:
    sum += digit
print(sum)


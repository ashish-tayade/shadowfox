# 05_loops.py
import random

# Dice simulation
rolls = [random.randint(1,6) for _ in range(20)]

print("6 count:", rolls.count(6))
print("1 count:", rolls.count(1))

consecutive_six = 0
for i in range(len(rolls)-1):
    if rolls[i] == 6 and rolls[i+1] == 6:
        consecutive_six += 1

print("Two 6s in row:", consecutive_six)

# Workout
total = 0
while total < 100:
    total += 10
    tired = input("Are you tired? (yes/no): ")
    if tired.lower() in ['yes','y']:
        skip = input("Do you want to skip remaining? (yes/no): ")
        if skip.lower() in ['yes','y']:
            break
    print("Remaining:", 100-total)

if total >= 100:
    print("Congratulations! You completed workout")
else:
    print("You completed", total, "jumping jacks")
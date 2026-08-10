energy = 5
score = 0

for turn in range(1, 5):
    if turn % 2 == 0:
        energy -= 2
        score += energy
    else:
        energy += 1
    print(turn, energy, score)
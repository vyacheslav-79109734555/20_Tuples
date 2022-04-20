scores = [25, 35, 45, 55, 65]
for player in range(len(scores)):
    scores[player] += 10
    print(f"{player} - {scores[player]}")
print(scores)

print('*************************')
scores = [25, 35, 45, 55, 65]
for player, score in enumerate(scores):
    scores[player] += 10
    print(f'{player} - {score}')
print(scores)


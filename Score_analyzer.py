#empty list
scores = []

#main program loop
while True:
    entry = input("Enter a score(or type 'done to finish):")
    if entry == 'done':
        break
    else:
        scores.append(int(entry))

#Score analyzer portion       
if len(scores) > 0:
    max_score = max(scores)
    min_score = min(scores)
    avg_score = sum(scores) / len(scores)
    print(f"Highest score: {max_score}")
    print(f"Lowest score: {min_score}")
    print(f"Average score: {avg_score}")
    



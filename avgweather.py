import pandas as pd
import random

t = range(70, 111)

pastweek = {
    'days' : ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun'],
    'temps' : [random.choice(t), random.choice(t), random.choice(t),
            random.choice(t), random.choice(t), random.choice(t),
            random.choice(t)]
}

df = pd.DataFrame(pastweek, columns=['days', 'temps'])

print("Here are the average temperatures\nfor the past week:")
print(df)

totaltemp = 0
for i in pastweek['temps']:
    totaltemp += i

avgtemp = totaltemp / 7
aboveavg = []
for i in pastweek['temps']:
    if i > avgtemp:
        current = pastweek['temps'].index(i)
        aboveavg.append(pastweek['days'][current])
    else:
        continue

print(f'The average temp has been {avgtemp}.')
print(f'{aboveavg} have been above average temperatures')
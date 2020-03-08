import csv 
from time import sleep

def suspense(sleep_len):
    for _ in range(50):
        sleep(sleep_len)
        print("=", end="", flush=True)
    print()

trainer_teams = {}
trainer_scores = {}

print("""
             `;,;.;,;.;.'
              ..:;:;::;: 
        ..--''' '' ' ' '''--.  
      /' .   .'        '.   .`\\
     | /    /            \   '.|
     | |   :             :    :|
   .'| |   :             :    :|
 ,: /\ \.._\ __..===..__/_../ /`.
|'' |  :.|  `'          `'  |.'  ::.
|   |  ''|    :'';          | ,  `''\\
|.:  \/  | /'-.`'   ':'.-'\ |  \,   |
| '  /  /  | / |...   | \ |  |  |';'|
 \ _ |:.|  |_\_|`.'   |_/_|  |.:| _ |
/,.,.|' \__       . .      __/ '|.,.,\\
     | ':`.`----._____.---'.'   |
      \   `:\"""-------'""' |   |
       ',-,-',             .'-=,=,
""")

print("Starting autograder...")
suspense(0.01)
print("Reading teams...")
suspense(0.02)

with open('pokemonTeams.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # Column title
            # print('First row' + str(row))
            line_count += 1
        else:
            pokemon_team = [int(pokemon_num) for pokemon_num in row[1:]]
            trainer_scores[row[0]] = 0
            trainer_teams[row[0]] = pokemon_team

pokemonStat = {} 
with open('pokemon.csv') as pokemonStats: 
    csv_reader = csv.reader(pokemonStats, delimiter=',') 
    line_count = 0 
    for row in csv_reader: 
        if line_count != 0: 
            pokemonStat[int(row[0])] = [int(row[i]) for i in range(4, 10)]
        line_count += 1


scores = []
count = 0

print("Calculating scores...")
suspense(0.04)

for person in trainer_teams: 
    scores.append([person] + [0] * 6)
    for pokemon in trainer_teams[person]: 
        for i in range(6): 
            scores[count][i + 1] += pokemonStat[pokemon][i]
    count += 1 

for i in range(1, 7):
    scores = sorted(scores, key=lambda x: x[i])
    for s in range(len(scores)):
        trainer_scores[scores[s][0]] += s

i = 1

print("Finalizing rankings...")
suspense(0.03)
print()

for k, v in sorted(trainer_scores.items(), key=lambda item: -item[1]):
    print("#%d: %s with a score of %s" % (i, k, v))
    i += 1
import pandas as pd

df = pd.read_csv(r'z:\Python\overwatch_matches.csv')

# 1. See only Anran
anran_only = df[df['My_Hero'] == 'Anran']

# 2. Count the total games
total_games = len(anran_only)

# 3. Filter again to get ONLY Anran games were a "win"
anran_wins = anran_only[anran_only['Result'] == 'Win']
total_wins = len(anran_wins)
# Sombra games filetr
sombra_games = anran_only[anran_only['Enemy_Counter'] == 'Sombra']

# 4. dothe math
# We multiply by 100 to turn a decimal like 0.55 into a percent
win_rate = (total_wins / total_games) * 100
# winrate for the sombra games
sombra_wins = len(sombra_games[sombra_games['Result'] == 'Win'])
sombra_total = len(sombra_games)

# Handle the zerodivision just in case there were no Sombra games
if sombra_total > 0:
    sombra_win_rate = (sombra_wins / sombra_total) * 100
    print(f"Anran Win Rate vs Sombra: {sombra_win_rate:.2f}%")
else:
    print("No games found against Sombra")

print(f"Total Anran Games: {total_games}")
print(f"Total Wins: {total_wins}")
print(f"Anran Win Rate: {win_rate:.1f}%")

# Get a unique list of all enemies you've faced
all_enemies = anran_only['Enemy_Counter'].unique()

print(f"{'Enemy Hero':<15} | {'Win Rate':<10} | {'Games Played'}")
print("-" * 40)

# The loop: calculate stats for every enemy automatically
for enemy in all_enemies:
    # Filter for this specific enemy
    enemy_subset = anran_only[anran_only['Enemy_Counter'] == 'Win']

    # Calculate stats
    total_games = len(enemy_subset)
    wins = len(enemy_subset[enemy_subset['Result'] == 'Win'])

    if total_games > 0:
        win_rate = (wins / total_games) * 100
        # This formatting makes it look like a professional table
        print(f"{enemy:<15} | {win_rate:>8.1f}% | {total_games:>12}")

import matplotlib.pyplot as plt

# We need to store our results in lists to graph them
enemy_names = []
win_rates = []

for enemy in all_enemies:
    enemy_subset = anran_only[anran_only['Enemy_Counter'] == enemy]
    total_games = len(enemy_subset)
    wins = len(enemy_subset[enemy_subset['Result'] == 'Win'])
    all_enemies = [enemy if enemy != 'None' else 'No Counter' for enemy in all_enemies]

    # Only graph heroes you<ve played at least 5 times
    if total_games > 5 and enemy != 'None':
        enemy_names.append(enemy)
        win_rates.append((wins / total_games) * 100)
 
# Create the horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(enemy_names, win_rates, color='skyblue')

# Add a "Danger Line" at 50%
plt.axvline(x=50, color='red', linestyle='--', label='50% Win Rate')

# Polish the look
plt.title('Anran Performance vs. Enemy Counters', fontsize=14)
plt.xlabel('Win Rate (%)')
plt.xlim(0, 100)
plt.legend()
plt.tight_layout()

# Save it for the Monday Report
plt.savefig(r'z:\Python\ow_counter-analysis.png')
plt.show()

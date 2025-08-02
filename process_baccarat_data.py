import json
import os
import pandas as pd

def get_winner(player_hand, banker_hand):
    player_score = sum(min(10, int(card[0]) if card[0].isdigit() else (1 if card[0] == 'A' else 10)) for card in player_hand)
    banker_score = sum(min(10, int(card[0]) if card[0].isdigit() else (1 if card[0] == 'A' else 10)) for card in banker_hand)

    player_score %= 10
    banker_score %= 10

    if player_score > banker_score:
        return 'Player'
    elif banker_score > player_score:
        return 'Banker'
    else:
        return 'Tie'

data_dir = './data'
output_data = []

for filename in os.listdir(data_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'r') as f:
            shoe_data = json.load(f)
            for hand in shoe_data['hands']:
                player_hand = hand[0]
                banker_hand = hand[1]
                winner = get_winner(player_hand, banker_hand)
                output_data.append({'winner': winner})

df = pd.DataFrame(output_data)
df.to_csv('baccarat_outcomes.csv', index=False)
print('Données traitées et sauvegardées dans baccarat_outcomes.csv')



import random
import csv

def get_hand_value(hand):
    value = 0
    for card in hand:
        if card in ['K', 'Q', 'J']:
            value += 0
        elif card == 'A':
            value += 1
        else:
            value += int(card)
    return value % 10

def deal_card():
    return random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])

def play_baccarat_hand():
    player_hand = [deal_card(), deal_card()]
    banker_hand = [deal_card(), deal_card()]

    player_value = get_hand_value(player_hand)
    banker_value = get_hand_value(banker_hand)

    if player_value >= 8 or banker_value >= 8:
        pass  # Natural win
    elif player_value <= 5:
        player_hand.append(deal_card())
        player_value = get_hand_value(player_hand)

        if (banker_value <= 2) or \
           (banker_value == 3 and player_hand[2] != '8') or \
           (banker_value == 4 and player_hand[2] in ['2', '3', '4', '5', '6', '7']) or \
           (banker_value == 5 and player_hand[2] in ['4', '5', '6', '7']) or \
           (banker_value == 6 and player_hand[2] in ['6', '7']):
            banker_hand.append(deal_card())
            banker_value = get_hand_value(banker_hand)

    elif banker_value <= 5:
        banker_hand.append(deal_card())
        banker_value = get_hand_value(banker_hand)

    if player_value > banker_value:
        return 'Player'
    elif banker_value > player_value:
        return 'Banker'
    else:
        return 'Tie'

def generate_baccarat_data(num_hands):
    with open('baccarat_results_generated.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['winner'])
        for _ in range(num_hands):
            writer.writerow([play_baccarat_hand()])

if __name__ == '__main__':
    generate_baccarat_data(2000000)
    print('Generated 2,000,000 baccarat hands and saved to baccarat_results_generated.csv')

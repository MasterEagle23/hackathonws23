from models.bet import Bet
import datetime
from operator import itemgetter


def no_of_active_players(players: dict) -> int:
    out = 0
    for player in players:
        if player.get("status") == "ACTIVE":
            out = out + 1

    return out


def best_hand(cards: list) -> (dict, int):
    """
    :param cards:
    :return: (best_hand, value)

    Royal Flush: 30939
    Straight Flush 1/37260

    Flush ()
    Straight (HV*100 000): 600 000 - 1 400 000
    Three-of-a-kind (V*10 000): 20 000 - 140 000
    Two Pair (V*100+V*100)*10: 5000 - 2700
    Pair (V*100): 200 - 1400
    High Card (V): 7 - 14
    """
    # conv ranks to values
    for card in cards:
        if card[0] == "J":
            card[0] = 11
        elif card[0] == "Q":
            card[0] = 12
        elif card[0] == "K":
            card[0] = 13
        elif card[0] == "A":
            card[0] = 14
        else:
            card[0] = int(card[0])

    # sort list by values
    cards = sorted(cards, key=itemgetter(1))

    # list of values
    values = []
    for i in range(len(cards)):
        values[i] = cards[i][0]

    # check for straight
    for card in cards:
        pass
    # todo here


def decide(table: dict) -> Bet:
    # debug timestamp
    print(f"---\n[{datetime.datetime.now()}]\n")
    we = table.get("players")[table.get("activePlayer")]

    hand_cards = list([])
    for card in we.get('cards'):
        hand_cards = hand_cards + [(card.get('rank'), card.get('suit'))]
    # print(f"hand_cards: {hand_cards}")

    common_cards = []
    for card in table.get("communityCards"):
        common_cards = common_cards + [(card.get('rank'), card.get('suit'))]
    # print(f"common_cards: {common_cards}")

    hand_cards = [hand_cards[-1], hand_cards[-2]]
    print(f"Cards: {len(hand_cards)}, H:{hand_cards}, C: {common_cards}")

    # calc sum of hand
    rank_sum = 0
    for card in hand_cards:
        if card[0] == "J":
            rank_value = 11
        elif card[0] == "Q":
            rank_value = 12
        elif card[0] == "K":
            rank_value = 13
        elif card[0] == "A":
            rank_value = 14
        else:
            rank_value = int(card[0])
        rank_sum = rank_sum + rank_value
    print(f"rank_sum: {rank_sum}")

    hand_value = rank_sum
    # pair
    if hand_cards[0][0] == hand_cards[1][0]:
        hand_value = hand_value * 5

    # two of suit
    if hand_cards[0][1] == hand_cards[1][1]:
        hand_value = hand_value * 1.1

    # min sum to play
    if hand_value < 22:
        bet_amount = 0
        print(f"Fold for low Value")

    # don't raise with only one other player
    elif len(table.get("players")) < 3:
        bet_amount = table.get("minimumBet")
        print(f"Min Bet for few players")

    # raise with good hand
    elif hand_value > 50:
        bet_amount = table.get("minimumBet") + (hand_value / 10) * table.get("minimumRaise") * (1 / table.get('round'))

    # min raise
    else:
        bet_amount = table.get("minimumBet") + table.get("minimumRaise")

    # don't raise with a medium hand
    if we.get('stack') - bet_amount <= 0 and hand_value < 30:
        bet_amount = 0
        print(f"dont raise all in with mid")

    print(f"Bet: {bet_amount} = min {table.get('minimumBet')}, "
          + f" round {table.get('round')}, value {hand_value}, stack {we.get('stack')}, players {len(table.get('players'))}")

    return Bet(int(min(we.get("stack"), bet_amount)))

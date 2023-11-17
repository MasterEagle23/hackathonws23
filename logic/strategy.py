from models.bet import Bet
from models.table import Table
import datetime


def decide(table: Table) -> Bet:
    print(f"---\n[{datetime.datetime.now()}]\n")
    we = table.players[table.activePlayer]

    hand_cards = list([])
    for card in we.cards:
        hand_cards = hand_cards + [(card.rank.value, card.suit.value)]

    common_cards = []
    for card in table.communityCards:
        common_cards = common_cards + [(card.rank.value, card.suit.value)]

    hand_cards = [hand_cards[-1], hand_cards[-2]]

    print(f"Cards: {len(hand_cards)}, {hand_cards}, ")

    rank_sum = 0
    print(rank_sum)
    for card in hand_cards:
        if card[0] == "J":
            rank_value = 11
        elif card[0] == "Q":
            rank_value = 12
        elif card[0] == "K":
            rank_value = 13
        elif card[0] == "A":
            rank_value = 15
        else:
            rank_value = int(card[0])
        rank_sum = rank_sum + rank_value
        print(rank_sum)

    # pair
    if hand_cards[0][0] == hand_cards[1][0]:
        rank_sum = rank_sum * 10

    # two of suit
    if hand_cards[0][1] == hand_cards[1][1]:
        rank_sum = rank_sum * 1.5

    if rank_sum < 15:
        bet_amount = 0
    else:
        bet_amount = table.minimumBet + ((1 / table.round + len(table.players))
                                         * (rank_sum / len(hand_cards)) / 10) * we.stack

    # dont go all in with a medium hand
    if bet_amount - we.stack <= 0 and rank_sum < 25:
        bet_amount = 0

    print(f"Bet: {bet_amount} = min {table.minimumBet}, "
          + f" round {table.round}, sum {rank_sum}, stack {we.stack}, players {len(table.players)}")
    del we
    return Bet(int(bet_amount))

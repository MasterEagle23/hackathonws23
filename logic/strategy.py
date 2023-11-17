from models.bet import Bet
from models.table import Table
import datetime


def decide(table: Table) -> Bet:
    print(f"---\n[{datetime.datetime.now()}]\n")
    we = table.players[table.activePlayer]

    card_list = list([])
    for card in we.cards:
        card_list = card_list + [(card.rank.value, card.suit.value)]

    card_list = [card_list[-1], card_list[-2]]

    print(f"Cards: {len(card_list)}, {card_list}, ")

    rank_sum = 0
    print(rank_sum)
    for card in card_list:
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

    if card_list[0][0] == card_list[1][0]:
        rank_sum = rank_value * 10

    if rank_sum < 15:
        bet_amount = 0
    else:
        bet_amount = table.minimumBet + ((1 / table.round) * (rank_sum / len(card_list)) / 10) * we.stack
    print(f"Bet: {bet_amount} ({table.minimumBet} + "
          + f"(1/{table.round}) * ({rank_sum}/{len(card_list)})/10) * {we.stack}")
    del we
    return Bet(int(bet_amount))

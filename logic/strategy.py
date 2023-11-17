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

    if rank_sum < 10:
        bet_amount = 0
    else:
        bet_amount = table.minimumBet + ((1 / table.round) * we.stack * (rank_sum / len(card_list)))/100
    print(f"Bet: {bet_amount} ({table.minimumBet} + (1/{table.round}) * {we.stack} * ({rank_sum}/{len(card_list)}))/100")
    del we
    return Bet(int(bet_amount))

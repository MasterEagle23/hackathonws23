from models.bet import Bet
from models.table import Table
import datetime


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)
    we = table.players[table.activePlayer]

    card_list = []
    for card in we.cards:
        card_list = card_list.append((card.rank.value, card.suit.value))

    print(f"[{datetime.datetime.now()}]\nCards: {len(card_list)}, {card_list}, ")

    rank_sum = 0
    for card in we.cards:
        if card.rank.value == "J":
            rank_value = 11
        elif card.rank.value == "Q":
            rank_value = 12
        elif card.rank.value == "K":
            rank_value = 13
        elif card.rank.value == "A":
            rank_value = 15
        else:
            rank_value = int(card.rank.value)
        rank_sum = rank_sum + rank_value

    if rank_sum < 10:
        bet_amount = 0
    else:
        bet_amount = table.minimumBet + (1 / table.round) * we.stack * (rank_sum / 10)
    print(f"Bet: {bet_amount} ({table.minimumBet} + (1/{table.round}) * {we.stack} * ({rank_sum}/10))")
    del we
    return Bet(int(bet_amount))

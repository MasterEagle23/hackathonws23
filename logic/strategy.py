from models.bet import Bet
from models.table import Table
import datetime


def decide(table: Table) -> Bet:
    # TODO: Add Poker Logic Here... :)
    we = table.players[table.activePlayer]

    print(f"[{datetime.datetime.now()}]Cards: {we.cards}")

    rank_sum = 0
    for card in we.cards:
        rank_sum = rank_sum + card.rank

    if rank_sum < 10:
        bet_amount = 0
    else:
        bet_amount = table.minimumBet + (1/table.round) * we.stack * (rank_sum/10)
    print(f"Bet: {bet_amount}")

    return Bet(int(bet_amount))

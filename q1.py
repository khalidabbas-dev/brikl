import argparse
import itertools


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--coin_list", nargs="+", type=int,
                        help="List of available coins")
    parser.add_argument("--amount", type=str, help="Amount")

    return parser


parser = init_argparse()
args = parser.parse_args()

args.coin_list.sort()
coin_list = args.coin_list
cash = float(args.amount)


def calculate_cash_coin(coins_set, amount):

    for i in range(len(coins_set) + 1, 0, -1):
        items = list(itertools.combinations(coins_set, i))
        for item in items:
            if sum(item) == amount:
                return item, len(item)
    return -1, "insufficient coins available for exchange"


if __name__ == '__main__':
    result = calculate_cash_coin(set(coin_list), cash)
    print(result)

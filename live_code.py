"""
Есть биржа, на которой продается и покупается зерно. Цена покупки и продажи одинакова.

пример: [13, 6, 3, 4, 10, 2, 3]

это исторические данные
предположим что в прошлый понедельник цена на покупку и продажу зерна была 13
на следующий день она стала 6, потом 3
Нужно найти индексы дня покупки и последующей продажи для получения максимальной выгоды. Вернуть массив из 2х элументов - индекс дня покупки и индекс дня продажи. Если выигрышных вариантов нет - вернуть пустой массив.

В данном случае нам было бы выгодно купить за 3 и продать в последствии за 10 - с выгодой в 7

profit([13, 6, 3, 4, 10, 2, 3])
# [2, 4] >> купили за 3 (индекс 2) и продали за 10 (индекс 4)

profit([13, 6, 3, 1])
# [] >> нет выигрышных вариантов

"""


class StockProfit:
    PROFIT_LIST = [13, 6, 3, 4, 10, 2, 3]

    def get_the_profit(self, number: int) -> None:
        index_current_number = self.PROFIT_LIST.index(number)

        # in the result list comprehension getting indexes and int for bigger profit
        result = [[idx, x] for idx, x in enumerate(self.PROFIT_LIST) if number < x and idx > index_current_number]
        if len(result) > 1:
            # get max result of more than 1 possible profit from self.PROFIT_LIST

            max_result = self.get_max_result(result)
            print("profit_list: ", self.PROFIT_LIST)
            self.PROFIT_LIST.pop(index_current_number)
            self.PROFIT_LIST.pop(max_result[0])
            print(f"купили за {number} (индекс {index_current_number}) и "
                  f"продали за {max_result[-1]} (индекс {max_result[0]})")
        elif len(result) == 0:
            # popping the result without profit

            print("profit_list: ", self.PROFIT_LIST)
            self.PROFIT_LIST.pop(index_current_number)
            print(f"нет выигрышных вариантов для суммы {number}")
        else:
            # in case we got one possible profit

            print("profit_list: ", self.PROFIT_LIST)
            self.PROFIT_LIST.pop(index_current_number)
            self.PROFIT_LIST.pop(result[-1][0] - 1)
            print(f"купили за {number} (индекс {index_current_number}) и "
                  f"продали за {result[-1][1]} (индекс {result[-1][0]})")

    # get max profit of more than of possible profits
    def get_max_result(self, lst: list) -> list:
        new_result = list()
        for i in range(len(lst)):
            new_result.append(lst[i][1])
        return [self.PROFIT_LIST.index(max(new_result)), max(new_result)]


if __name__ == "__main__":
    profit = StockProfit()

    profit.get_the_profit(13)
    profit.get_the_profit(6)
    profit.get_the_profit(3)

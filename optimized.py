import csv

data_csv = 'data/dataset2_Python+P7.csv'

MAX_INVEST = 500

def import_data(data_csv):
    dispo_stock_list = []
    with open(data_csv, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dispo_stock_list.append((row['name'], float(row['price']), float(row['profit'])))
        return dispo_stock_list


def filter_and_sort_data(dispo_stock_list):
    """
    filter and sort data
    """
    # filter positive price
    dispo_stock_list = list(filter(lambda stock: stock[1] > 0, dispo_stock_list))
    # filter positive profit
    dispo_stock_list = list(filter(lambda stock: stock[2] > 0, dispo_stock_list))
    # remove duplicate
    dispo_stock_list = list(set(dispo_stock_list))
    # sort by profit
    dispo_stock_list = sorted(dispo_stock_list, key=lambda stock: stock[2], reverse=True)
    return dispo_stock_list


def optimized(dispo_stock_list):

    best_stock_list = []
    best_stock_list_price = 0
    best_stock_list_profit = 0

    for stock in dispo_stock_list:
        stock_price = stock[1]
        if best_stock_list_price + stock_price <= MAX_INVEST:
            stock_profit_percent = stock[2]
            stock_profit = stock_profit_percent / 100 * stock_price
            best_stock_list_price += stock_price
            best_stock_list_profit += stock_profit
            best_stock_list.append(stock)

    best_stock_list_price = round(best_stock_list_price, 2)
    best_stock_list_profit = round(best_stock_list_profit, 2)
    output = (best_stock_list, best_stock_list_price, best_stock_list_profit)
    return output

dispo_stock_list = import_data(data_csv)
dispo_stock_list = filter_and_sort_data(dispo_stock_list)
print(dispo_stock_list)
len_dispo_stock_list = len(dispo_stock_list)
output = optimized(dispo_stock_list)
print(output)
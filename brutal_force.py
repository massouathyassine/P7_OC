import itertools
import numpy as np
import csv

def csv_data(file):
    data_read = []
    with open(file, newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for share in data:
            if float(share["price"]) > 0 and float(share["profit"]) > 0:
                data_read.append(
                    (
                        share["name"],
                        int(share["price"]),
                        int(share["profit"]),
                    )
                )
    return data_read

max_price = 500
total_spent = 0
actions_bought = []
actions_bought_name = []
all_combinations = []
all_combinations_bought = []
all_combinations_bought_name = []

for r in range(len(csv_data("data/listaction.csv")) + 1):
    combinations_object = itertools.combinations(csv_data("data/listaction.csv"), r)
    all_combinations += list(combinations_object)

for combination in all_combinations:
    for x in combination:
        total_spent += x[1]
        if total_spent <= 500:
            actions_bought_name.append(x[0])
            actions_bought.append(((x[1]) * (x[2])))
    total_spent = 0
    if len(actions_bought) > 1:
        actions_bought = np.sum(actions_bought)
        all_combinations_bought.append(actions_bought)
        all_combinations_bought_name.append(actions_bought_name)
    actions_bought = []
    actions_bought_name = []

max_value = int(max(all_combinations_bought))
max_index = all_combinations_bought.index((max_value))
max_value /= 100
print("Le meilleur bénéfice est obtenu avec les actions suivantes :" + str(all_combinations_bought_name[max_index]))
print('il est de' + str(max_value) + " Euro")


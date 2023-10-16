import names
import csv
import random
import time
from tqdm import tqdm

print("Big Fatty CSV V1.0 by @HenryNerd on Github")
print()
print()
print("  ____  _         ______    _   _            _____  _______      __")
print(" |  _ \(_)       |  ____|  | | | |          / ____|/ ____\ \    / /")
print(" | |_) |_  __ _  | |__ __ _| |_| |_ _   _  | |    | (___  \ \  / / ")
print(" |  _ <| |/ _` | |  __/ _` | __| __| | | | | |     \___ \  \ \/ /  ")
print(" | |_) | | (_| | | | | (_| | |_| |_| |_| | | |____ ____) |  \  /   ")
print(" |____/|_|\__, | |_|  \__,_|\__|\__|\__, |  \_____|_____/    \/    ")
print("           __/ |                     __/ |                         ")
print("          |___/                     |___/                          ")
print()

header = ['Name', 'Age', 'Purchase Amount', 'Date', 'Time']
num_records = int(input("How many pices of data do you want to generate? "))
rows = []
pbar = tqdm(total=num_records)
for i in range(num_records):
    name = names.get_full_name()
    age = random.randint(18, 65)
    purchase_amount = round(random.uniform(20, 100), 2)
    date_time = time.strftime("%d-%m-%Y %H:%M:%S",time.gmtime())

    rows.append([name, age, purchase_amount, date_time.split()[0], date_time.split()[1]])
    pbar.update(1)

pbar.close()


with open("BigFatty.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print("*File Saved as BigFatty.csv")
print()
print("Genration Complete")
print("Thank you for using this service")

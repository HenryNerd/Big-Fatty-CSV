import csv
import random
import os
from names_generator import generate_name
from tqdm import tqdm

requestedTimes = 0
actualTimes = 0

while True:
    # Title Screen
    os.system('clear')
    print("  ____  _         ______    _   _            _____  _______      __")
    print(" |  _ \(_)       |  ____|  | | | |          / ____|/ ____\ \    / /")
    print(" |  _ <| |/ _` | |  __/ _` | __| __| | | | | |     \___ \  \ \/ /  ")
    print(" | |_) | | (_| | | | | (_| | |_| |_| |_| | | |____ ____) |  \  /   ")
    print(" |____/|_|\__, | |_|  \__,_|\__|\__|\__, |  \_____|_____/    \/    ")
    print("           __/ |                     __/ |                         ")
    print("          |___/                     |___/                          ")
    print()
    print()
    print("1: Generate file")
    print("2: Open file location")
    print("3: Exit")
    command = input("User $~: ")
    #1: Generate file
    if command == "1":
        os.system('clear')
        requestedTimes = int(input("How many people to generate: "))
        filename = "Big Fatty.csv"
        fields = ['Name', 'DOB', 'Timestamp', 'Purchase Amount']
        pbar = tqdm(total=requestedTimes)
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            while actualTimes < requestedTimes:
                name = generate_name()
                day = random.randint(1, 28)
                month = random.randint(1, 12)
                year = random.randint(1940, 2010)
                dob = f"{day}.{month}.{year}"
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                timestamp = f"{hour}:{minute}"
                purchaseAmount = random.randint(50, 10000)
                rows = [name, dob, timestamp, purchaseAmount]
                csvwriter.writerow(rows)
                actualTimes += 1
                pbar.update(1)
        pbar.close()
    elif command == "2":
        os.system('open .')
    elif command == "3":
        break
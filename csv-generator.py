import csv
import random
import time

out_filename = 'data.csv'


def generator():
    min = int(input('Start ID: '))
    count = int(input('Count: '))
    max_v = int(input('MAX Value: '))

    print()
    start = time.time()

    with open(out_filename, 'w', newline='') as csvfile:
        fieldnames = ['HOUSEHOLD_ID', 'OFFER_CODE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_ALL)

        writer.writeheader()
        for item in range(min, min + count, 1):
            writer.writerow({'HOUSEHOLD_ID': item, 'OFFER_CODE': int(random.random() * max_v)})
            print(item, 'OK')

    finish = time.time()
    print('\n\tFinished', '(' + str(int(finish - start)) + 's)')

if __name__ == '__main__':
    generator()

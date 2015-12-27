import csv
import datetime
import time

in_filename = 'data.csv'
out_format = 'out/PROD_segment_X_EYC_{date}_{key}.csv'


def main():
    start = time.time()
    date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d')
    with open(in_filename, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        current = 0
        data = filter(None, reader)
        for row in data:
            if current % 100 == 0 and current:
                print('Items', str(current - 99) + '-' + str(current), '[OK]')
            current += 1
            with open(out_format.format(date=date, key=row[1]), 'a', newline='') as outfile:
                writer = csv.writer(outfile, delimiter="|", quoting=csv.QUOTE_NONE, quotechar='')
                writer.writerow([row[0]])

    finish = time.time()
    print('\n\tDone! ({time:.2})'.format(time=finish - start))


def clear_out():
    import os
    import glob

    print('Cleaning output directory..')

    files = glob.glob('out/*')
    for f in files:
        os.remove(f)
    print('Removed {count} files.'.format(count=len(files)))
    time.sleep(2)

if __name__ == '__main__':
    clear_out()
    main()

import csv
import time
from config import *

# Output limiter for removing flood.
MSG_LIMITER = 100


def parser():
    # Startup time
    start = time.time()
    # Results
    dictionary = {}

    # Data loader
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='"')
        current = 0
        data = filter(None, reader)
        for row in data:
            if current % MSG_LIMITER == 0 and current:      # Message limiter
                print('Items', str(current - MSG_LIMITER + 1) + '-' + str(current), '[OK]')
            current += 1

            # Dictionary generator
            if row[1] in dictionary and type(dictionary[row[1]]).__name__ == 'list':
                dictionary[row[1]].append(row[0])
            else:
                dictionary[row[1]] = [row[0]]
    print('Generated {count} records.'.format(count=len(dictionary)))

    # Saving data
    current = 0
    for item in dictionary:
        with open(out_format.format(key=item), 'a', newline='') as outfile:
            writer = csv.writer(outfile, delimiter="|", quoting=csv.QUOTE_NONE, quotechar='')
            writer.writerow(get_header(item))
            for line in dictionary[item]:
                writer.writerow([dictionary[item][dictionary[item].index(line)]])
                if current % MSG_LIMITER == 0 and current:
                    print('Objects', str(current - MSG_LIMITER + 1) + '-' + str(current), '[SAVED]')
                current += 1
            # Print statistic
    print('Saved {count} object(s).'.format(count=len(dictionary)))
    finish = time.time()
    print('\n\tDone! ({time:.2f})'.format(time=finish - start))


def get_header(key):
    result = []
    for field in out_header:
        result.append(out_header[out_header.index(field)].format(key=key))
    return result


def clear_out():
    import os
    import glob

    print('Cleaning output directory..')

    # scan output folder
    files = glob.glob(out_dir + '/*.' + file_type)
    for f in files:
        os.remove(f)
    print('Removed {count} files.'.format(count=len(files)))
    time.sleep(2)

if __name__ == '__main__':
    clear_out()
    parser()

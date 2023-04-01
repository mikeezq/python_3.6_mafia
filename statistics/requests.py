import psycopg2
import csv


def regression():
    with open('../participants_merged.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            print(row)
            if line_count == 0:
                print(f'Column names are {"; ".join(row)}')
                line_count += 1

regression()
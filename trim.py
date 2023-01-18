import csv
import subprocess


def main():
    with open('meditation_cuts.csv') as f:
        csv_reader = csv.reader(f, delimiter=',')


if __name__ == "__main__":
    main()

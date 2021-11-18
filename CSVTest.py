import csv


def getCalls(path):
    rows = []

    try:
        with open(path, 'r') as fl:
            csvr = csv.reader(fl)
            rows = []
            for row in csvr:
                rows.append(row)
    except IOError as e:
        print(e)

    return rows


def answer(path, data):
    for i in data:
        i.append('2')

    try:
        with open(path, 'w') as fl:
            csvw = csv.writer(fl)
            csvw.writerows(data)
    except IOError as e:
        print(e)


if __name__ == '__main__':
    Path = r"C:\Users\S\OneDrive\Desktop\Ex1_input\Ex1_Calls_case_2_b.csv"
    answer(Path, getCalls(Path))

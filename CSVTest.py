import csv

def getCalls(Path):
    rows = []

    try:
        with open(Path, 'r') as fl:
            csvr = csv.reader(fl)
            rows = []
            for row in csvr:
                rows.append(row)
    except IOError as e:
        print(e)

    return rows

def answere(Path, data):

    for i in data:
        i.append('2')

    try:
        with open(Path, 'w') as fl:
            csvw = csv.writer(fl)
            csvw.writerows(data)
    except IOError as e:
        print(e)







if __name__ == '__main__':
    Path = r"C:\Users\ישראל\Downloads\computer sincse\OOP\Assignments\Ex1\data\Ex1_Calls_case_2_b.csv"
    answere(Path, getCalls(Path))
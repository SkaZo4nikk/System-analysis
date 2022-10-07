import csv
from io import StringIO

def csv_to_array(datafile):
    result = []
    reader = csv.reader(datafile, delimiter=",")
    for row in reader:
        result.append(row)
    return result

def read_csv(string_data):
    string_stream = StringIO(string_data)
    return csv_to_array(string_stream)

def task(csv_str):
    grh = read_csv(csv_str)

    r1_n = {}
    r2_n = {}
    r3_n = {}
    r4_n = {}
    r5_n = {}

    for [r1, r2] in grh:
        r1_n[r1] = r1
        r2_n[r2] = True

    for [l, r] in grh:
        for [i, j] in grh:
            if r == i:
                r3_n[l] = True
                r4_n[j] = True
            if (l == i) & (r != j):
                r5_n[r] = True

    l_1 = list(r1_n.keys())
    l_2 = list(r2_n.keys())
    l_3 = list(r3_n.keys())
    l_4 = list(r4_n.keys())
    l_5 = list(r5_n.keys())

    print("r1 nodes", l_1)
    print("r2 nodes", l_2)
    print("r3 nodes", l_3)
    print("r4 nodes", l_4)
    print("r5 nodes", l_5)
    return [l_1, l_2, l_3, l_4, l_5]

print(task("1,2\n1,3\n2,4"))

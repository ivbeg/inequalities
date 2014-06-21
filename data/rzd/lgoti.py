# -*- coding: utf8 -*-
import csv


def extract_unique(arr, n=0):
    items = {}
    for r in arr:
        s = r[n].decode('windows-1251', 'replace')
        v = items.get(s, 0)
        items[s] = v + 1
    return sorted(items.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)

def extract_unique_persons(arr, n=0):
    items = {}
    for r in arr:
        s = r[n].decode('windows-1251', 'replace').split(u' - ')[0].strip().split(u' – ')[0].strip()
        v = items.get(s, 0)
        items[s] = v + 1
    return sorted(items.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)


def main():
    f = open("lgoti_rzd.txt", 'r')
    r = csv.reader(f, delimiter='\t')
    all = extract_unique(r, 3)
    for row in all:
        print row[0].encode('utf8', 'ignore'), row[1]


if __name__ == "__main__":
    main()
	

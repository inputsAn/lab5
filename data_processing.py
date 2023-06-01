import csv


def reading_csv_file():
    dictionary = {}
    with open('data.csv') as r:
        next(r)
        for line in r:
            (number, data, fio, grant, destination) = line.replace("\n", "").split(",")
            dictionary.update({int(number): {"data": data, "fio": fio, "grant": int(grant),"destination": destination}})
    return dictionary

def fio_sorting(d):
    return sorted(d.items(), key=lambda f: f[1]["fio"])

def grant_sorting(d):
    return sorted(d.items(), key=lambda f: f[1]["grant"], reverse=True)

def grant_more_than_sorting(d, value):
    return dict((k, v) for k, v in d.items() if v["grant"] > value)

def add_new_data(d,data,fio,grant,destination):
    with open("data.csv", "a") as f:
        f.write(f"{list(d.items())[-1][0] + 1},{data},{fio},{grant},{destination}\n")

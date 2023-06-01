import os


def processing():
    DIR = 'test_data'
    count_of_files =len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print(f"Количество файлов в директории: {count_of_files}")

class row():
    number = 0

    def __init__(self, number: int):
        self.number = number

    def get_number(self):
        return self.number

    def set_number(self, val):
        self.number = val

class model(row):
    number = 0
    data = ""
    fio = ""
    grant = ""
    destination = ""

    def __init__(self, number: int, data: str, fio: str, grant: int, destination: str):
        super().__init__(number)
        self.number = number
        self.data = data
        self.fio = fio
        self.grant = grant
        self.destination = destination

    def __str__(self):
        return f"Запись №{self.number}: дата = {self.data}, ФИО студента = {self.fio}, размер стипендия = {self.grant}, куда выдается справка = {self.destination}"

    def __repr__(self):
        return f"model(number={self.number},date={self.data},fio={self.fio},grant={self.grant},destination={self.destination})"

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value
class Data():
    file_path = ""
    data = {}
    pointer = 0

    def __init__(self, file):
        self.file_path = file
        self.data = self.parse(file)

    def __str__(self):
        d_str = '\n'.join([str(rm) for rm in self.data])
        return f"Содержимое:\n{d_str}"

    def __repr__(self):
        return f"Data({[repr(rm) for rm in self.data]})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer >= len(self.data):
            self.pointer = 0
            raise StopIteration
        else:
            self.pointer += 1
            return self.data[self.pointer - 1]

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом.")
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс.")

    def as_generator(self):
        self.pointer = 0
        while self.pointer < len(self.data):
            yield self.data[self.pointer]
            self.pointer += 1

    @staticmethod
    def parse(file):
        parsed = []
        with open(file, "r", encoding='utf-8') as raw_csv:
            for line in raw_csv:
                (number, data, fio, grant, destination) = line.replace("\n", "").split(",")
                parsed.append(model(int(number), data, fio, int(grant), destination))
        return parsed

    def fio_sorting(self):
        return sorted(self.data, key=lambda f: f.fio)

    def grant_sorting(self):
        return sorted(self.data, key=lambda f: f.grant, reverse=True)

    def value(self, value):
        r = []
        for d in self.data:
            if (d.grant > value):
                r.append(d)
        return r

    def add_new(self, data, fio, grant, destination):
        self.data.append(model(len(self.data) + 1, data, fio, grant, destination))
        self.save(self.file_path, self.data)

    @staticmethod
    def save(file, new_data):
        with open(file, "w", encoding='utf-8') as f:
            for r in new_data:
                f.write(f"{r.number},{r.data},{r.fio},{r.grant},{r.destination}\n")

    def print(self):
        for r in self.data:
            print(f"№{r.number}. дата: {r.data}, ФИО студента: {r.fio}, размер стипендии: {r.grant}, куда выдается справка: {r.destination}")

    def printd(self, d):
        for r in d:
            print(f"№{r.number}. дата: {r.data}, ФИО студента: {r.fio} размер стипендии: {r.grant}, куда выдается справка: {r.destination}")

def get_files_count_in_directory(file):
        (loc, dirs, files) = next(os.walk(file))
        return len(files)

data = Data("data.csv")

# __repr__()
print(repr(data), "\n")

# __str__()
print(data, "\n")

# Итератор
print("-" * 64)
for item in iter(data):
    print(item)

print("-" * 64)

# Генератор
for item in data.as_generator():
    print(item)

print("-" * 64)


print("\n")
data.printd(data.grant_sorting())  # сортировка по стипе
print("\n")
data.printd(data.fio_sorting())  # сортировка по имени
print("\n")
data.printd(data.value(2000))  # стипендия больше 2000

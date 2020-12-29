# Подсчитать статистику по буквам в файле с текстом.
# Входные параметры: файл для сканирования

import operator
import zipfile
from tabulate import tabulate
from collections import defaultdict


class LetterStatistics:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = defaultdict(int)

    def unzip(self):
        zip_file = zipfile.ZipFile(self.file_name, 'r')
        filename = zip_file.namelist()[-1]
        zip_file.extract(filename)
        self.file_name = filename

    def collect_data(self):
        if self.file_name.endswith('.zip'):
            self.unzip()

        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for letter in line:
                    if letter.isalpha():
                        self.stat[letter] += 1
        return self.sorting()

    def print_info(self):
        print(tabulate(sort.collect_data(), headers=['БУКВА', 'ЧАСТОТА'], tablefmt='grid', stralign='center'))
        total = [('ВСЕГО', sort.total())]
        print(tabulate(total, tablefmt='grid', stralign='center'))

    def sorting(self):
        pass

    def total(self):
        return sum(self.stat.values())


# Различное упорядочивание статистики. С использованием наследования класса
class SortingDescending(LetterStatistics):
    def sorting(self):
        return sorted(self.stat.items(), key=operator.itemgetter(1), reverse=True)


class SortingGrowth(LetterStatistics):
    def sorting(self):
        return sorted(self.stat.items(), key=operator.itemgetter(1))


class SortingAlphabet(LetterStatistics):
    def sorting(self):
        return sorted(self.stat.items(), key=operator.itemgetter(0))


class SortingEndAlphabet(LetterStatistics):
    def sorting(self):
        return sorted(self.stat.items(), key=operator.itemgetter(0), reverse=True)


sort = SortingDescending(file_name='voyna-i-mir.txt')
sort.print_info()

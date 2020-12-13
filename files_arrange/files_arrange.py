# -*- coding: utf-8 -*-
import shutil
import time
import os
from abc import ABC, abstractmethod


# Скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт расскладывает файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg


# Использовал шаблонный метод
class OrganizeFiles(ABC):
    def __init__(self, path_where_copy):
        self.path_where_copy = path_where_copy

    def organize(self):
        for file_path in self.get_files():
            tm_year, tm_mon = self.collect_time(file_path)
            path_for_dir_month = os.path.join(self.path_where_copy + '_by_year', tm_year + ' год', tm_mon + ' месяц')
            self.creating_folders(destination_path=path_for_dir_month, file_path=file_path)
            self.copying_files(destination_path=path_for_dir_month, path_file=file_path)

    @abstractmethod
    def copying_files(self, path_file, destination_path):
        pass

    @abstractmethod
    def collect_time(self, file_path):
        pass

    @abstractmethod
    def creating_folders(self, destination_path, file_path):
        pass

    @abstractmethod
    def get_files(self):
        pass


class SortFolder(OrganizeFiles):
    def collect_time(self, file_path):
        secs = os.path.getmtime(file_path)
        file_time = time.gmtime(secs)
        return str(file_time.tm_year), str(file_time.tm_mon)

    def creating_folders(self, destination_path, file_path):
        os.makedirs(destination_path, exist_ok=True)

    def get_files(self):
        path_normalized = os.path.normpath(self.path_where_copy)
        list_path_file = []
        for dirpath, dirnames, filenames in os.walk(path_normalized):
            for file in filenames:
                list_path_file.append(os.path.join(dirpath, file))
        return list_path_file

    def copying_files(self, path_file, destination_path):
        shutil.copy2(path_file, destination_path)


path = 'icons'
sort = SortFolder(path_where_copy=path)
sort.organize()


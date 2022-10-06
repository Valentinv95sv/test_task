import os
import pandas as pd

# Задача:
# Ваш питон скрипт (который должен быть создан внутри папки testtask) должен пробежаться по содержимому папки и папок
# внутри папок, и сохранить в excel файл "result.xlsx" список лежащих там файлов в формате:
# Номер строки | Папка в которой лежит файл | название файла | расширение файла

class Filepath_test_assignment():
    # Генератор, формирующий список всех файлов, лежащих в исходной директории и в поддиректориях
    def generator(self):
        for root, dirs, files in list(os.walk(os.getcwd())):
            for file in files:
                if len(file.split(".")[0]) == 0:
                    file = " " + file
                yield os.path.join(root, file)

    #Формируем удобный для дальнейшего использования список, содержащий название папки, имя файла и его расширение
    def lister_maker(self, gen):
        mylist = list()
        iterator = 1
        for i in gen:
            if not os.path.isdir(i):
                mylist.append((iterator, i.split("\\")[-2], os.path.splitext(i.split("\\")[-1])[0], os.path.splitext(i.split("\\")[-1])[-1]))
            else:
                lister_maker(i)
            iterator += 1
        return mylist

    # Формируем dataframe и сохраняем его в Excel файле в заданном формате
    def make_Excel_file(self, datalist: list()):
        df = pd.DataFrame(datalist, columns=["Номер строки", "Папка в которой лежит файл", "название файла", "расширение файла"] )
        try:
            with pd.ExcelWriter("myfile.xlsx", engine="xlsxwriter", ) as writer:
                df.to_excel(writer, index=False, )
        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    b = Filepath_test_assignment()
    b.make_Excel_file(b.lister_maker(b.generator()))






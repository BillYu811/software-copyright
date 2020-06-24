# coding=UTF-8
# !/usr/bin/python


import os
import linecache

class Rz:
    with_file_name = True
    output_file_name = 'out.txt'
    allow_files_suffix = ['.js', '.jsx', '.rb', '.ts', '.tsx']

    __files_count = 0
    __output_lines = 0

    def __init__(self, path):
        self.__walk_path = path
        self.output_file = open(self.output_file_name, 'a+')

    def walk_all(self):
        self.walk_dir(self.__walk_path)

    def set_and_print_counts(self, files=0, lines=0):
        self.__files_count += files
        self.__output_lines += lines
        print('F:{} L:{}'.format(self.__files_count, self.__output_lines))

    def walk_dir(self, path):
        files = os.listdir(path)  # 得到文件夹下的所有文件名称

        for file in files:  # 遍历文件夹
            if os.path.isdir(path + '/' + file):
                # 递归
                self.walk_dir(path + "/" + file)
            else:
                if not (os.path.splitext(file)[-1] in self.allow_files_suffix):
                    return

                f = open(path + "/" + file)
                iter_f = iter(f)

                self.output_file.write('#{}\n'.format(file))
                for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                    if line[0] in ['#', '!', '\n', '\r']:
                        continue
                    self.output_file.write(line)
                    self.set_and_print_counts(0, 1)
                self.set_and_print_counts(1, 0)



path = '~/'
rz = Rz(path)
rz.walk_all()

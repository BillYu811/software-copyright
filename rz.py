# coding=UTF-8
# !/usr/bin/python


import os, sys, time, json


class Rz:
    with_file_name = True

    __files_count = 0
    __output_lines = 0
    __file_in_line = []

    def __init__(self, config):
        self.__output_filename = config.get('output_filename', "") or 'out.txt'
        self.__walk_path = config.get('walk_dir', "") or '~/projects'
        self.__allow_files_suffix = config.get('allow_files_suffix', []) or ['.js', '.jsx', '.rb', '.ts', '.tsx']
        self.__skip_when = config.get('skip_when_character', []) or ['#', '!', '\n', '\r']

        self.__with_filepath = config.get('with_filepath?', False) or False
        self.__with_filename = config.get('with_filename?', True) or True

        self.output_file = open(self.__output_filename, 'a+')

    def walk_all(self):
        start = time.time()
        self.walk_dir(self.__walk_path)
        self.export_result_json_file()
        end = time.time()
        print("\nFiles:{}, Lines:{}, Times:{:.3f}s ".format(self.__files_count, self.__output_lines, end - start))

    def export_result_json_file(self):
        if self.__file_in_line:
            with open('opt_result.json', 'w') as f:
                f.write(json.dumps(self.__file_in_line, indent=1))

    def set_and_print_counts(self, files=0, lines=0):
        self.__files_count += files
        self.__output_lines += lines
        sys.stdout.write('\rF:{} L:{}'.format(self.__files_count, self.__output_lines))
        sys.stdout.flush()

    def walk_dir(self, path):
        files = os.listdir(path)  # 得到文件夹下的所有文件名称

        for file in files:  # 遍历文件夹
            if os.path.isdir(path + '/' + file):
                # 递归
                self.walk_dir(path + "/" + file)
            else:
                if not (os.path.splitext(file)[-1] in self.__allow_files_suffix):
                    return

                f = open(path + "/" + file)
                iter_f = iter(f)

                self.__file_in_line.append({'file_path': path + "/" + file, 'line': self.__output_lines + 1})

                if self.__with_filename:
                    self.output_file.write('#{}\n'.format(file))
                    self.__output_lines += 1
                elif self.__with_filepath:
                    self.output_file.write('#{}\n'.format(path + "/" + file))
                    self.__output_lines += 1

                for line in iter_f:  # 遍历文件，一行行遍历，读取文本
                    if (line[0] in self.__skip_when) or (line[0:1] in self.__skip_when):
                        continue
                    self.output_file.write(line)
                    self.set_and_print_counts(0, 1)
                self.set_and_print_counts(1, 0)


if __name__ == '__main__':
    from config import Config

    rz = Rz(Config().get_configs())
    rz.walk_all()

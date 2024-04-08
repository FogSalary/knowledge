import os
import sys
import re
import shutil


def get_all_files(directory, type=None):
    file_list = []
    for file_name in os.listdir(directory):
        if type is not None:
            if type in file_name:
                # print(file_name)
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path):
                    file_list.append(file_path)
    return file_list


def extract_numbers(s):
    return [int(num) for num in re.findall(r'\d+', s)]


if __name__ == '__main__':
    file_list = get_all_files(os.path.dirname(__file__), '.png')
    for file in file_list:
        file_name = os.path.basename(file)
        file_path = os.path.dirname(file)
        png_index = extract_numbers(file_name)[0]
        refilename = os.path.join(file_path, "geek_image-%d.png" % (png_index+8))
        print(refilename, "   geek_image-%d.png" % (png_index+8))
        try:
            # 调用os模块的rename()函数进行文件重命名
            os.rename(file, refilename)
            print("文件重命名成功！")
        except FileNotFoundError:
            print("未找到指定的文件或目录！")
        except Exception as e:
            print("发生错误：", str(e))
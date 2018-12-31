import os
import shutil

if __name__ == '__main__':
    path = '/Users/alpha/dl/project/traffic_light/data/yellow'
    train_path = '/Users/alpha/dl/project/traffic_light/data/light/train/yellow'
    test_path = '/Users/alpha/dl/project/traffic_light/data/light/test/yellow'
    train_ratio = 9
    file_name_list = os.listdir(path)
    num = 0
    for index, file in enumerate(file_name_list):
        if num%train_ratio==0:
            read_path = os.path.join(path, file)
            write_path = os.path.join(test_path, file)
            shutil.copy(read_path, write_path)
        else:
            read_path = os.path.join(path, file)
            write_path = os.path.join(train_path, file)
            shutil.copy(read_path, write_path)
        num += 1
import os

if __name__ == '__main__':
    write_path_train = '/Users/alpha/dl/project/traffic_light/data/Main/train.txt'
    write_path_val = '/Users/alpha/dl/project/traffic_light/data/Main/val.txt'
    read_path = '/Users/alpha/Pictures/learn/light_img'
    path_list = os.listdir(read_path)
    index = 0
    with open(write_path_train, 'w') as train_w:
        with open(write_path_val, 'w') as val_w:
            for path in path_list:
                new_path = path.split('.jpg')[0]+'\n'
                if index%9 == 0:
                    val_w.writelines(new_path)
                else:
                    train_w.writelines(new_path)
                index += 1

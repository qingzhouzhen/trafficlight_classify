import shutil
import os
if __name__ == '__main__':
    label_path = '/Users/alpha/Pictures/learn/light_label/'
    img_path = '/Users/alpha/Pictures/learn/light_img/'
    img_list = os.listdir(img_path)
    label_list = os.listdir(label_path)
    for path in img_list:
        path = path.replace('.jpg', '.xml')
        if path in label_list:
            continue
        path = path.replace('.xml', '.jpg')
        abs_path = os.path.join(img_path, path)
        os.remove(abs_path)
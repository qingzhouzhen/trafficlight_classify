import os
import cv2
import xml.dom.minidom
if __name__ == '__main__':
    root = '/Users/alpha/Pictures/learn/light_label/'
    image = '/Users/alpha/Pictures/learn/light_img/'
    image_write = '/Users/alpha/Pictures/learn/light_crop/'
    for file in os.listdir(root):
        path_without_dot = file.split('.xml')[0]
        image_path = os.path.join(image, path_without_dot+'.jpg')
        img = cv2.imread(image_path)
        path = os.path.join(root, file)
        if not path.endswith('.xml'):
            continue
        dom_tree = xml.dom.minidom.parse(path)
        annotation = dom_tree.documentElement
        objects = annotation.getElementsByTagName("object")
        for index, object in enumerate(objects):
            name = object.getElementsByTagName("name")[0]
            name_data = name.childNodes[0].data
            bndbox = object.getElementsByTagName("bndbox")[0]
            xmin = bndbox.getElementsByTagName("xmin")[0]
            xmin_data = xmin.childNodes[0].data
            ymin = bndbox.getElementsByTagName("ymin")[0]
            ymin_data = ymin.childNodes[0].data
            xmax = bndbox.getElementsByTagName("xmax")[0]
            xmax_data = xmax.childNodes[0].data
            ymax = bndbox.getElementsByTagName("ymax")[0]
            ymax_data = ymax.childNodes[0].data
            print("xmin,ymin,xmax,ymax", xmin_data, ymin_data, xmax_data,ymax_data)
            #cv2.rectangle(img, (int(xmin_data), int(ymin_data)), (int(xmax_data), int(ymax_data)), (0,0,224),2)
            light_buble = img[int(ymin_data):int(ymax_data),int(xmin_data):int(xmax_data)]
            write_path = os.path.join(image_write, path_without_dot)+'_'+str(index)+'_.jpg'
            cv2.imwrite(write_path, light_buble)
        #cv2.namedWindow("test", cv2.WINDOW_NORMAL)
        # cv2.resizeWindow("test", img.shape[1], img.shape[0])
        #cv2.imshow("test", img)
        #cv2.waitKey(0)
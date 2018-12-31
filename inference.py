from mxnet.gluon import data as gdata, model_zoo
from mxnet import image

if __name__ == '__main__':
    color_dict = ['green', 'red', 'yellow']
    im_fname = '/Users/alpha/dl/project/traffic_light/data/IMG_20181124_125757_0_.jpg'
    img = image.imread(im_fname)
    normalize = gdata.vision.transforms.Normalize(
        [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    transform_fn = gdata.vision.transforms.Compose([
        gdata.vision.transforms.RandomResizedCrop(224),
        gdata.vision.transforms.RandomFlipLeftRight(),
        gdata.vision.transforms.ToTensor(),
        normalize])
    img = transform_fn(img)
    model_wight = '/Users/alpha/dl/project/traffic_light/model/trafficlight-epoch-100.8488372093023255.params'
    net = model_zoo.vision.resnet18_v2(classes=3)
    net.load_parameters(model_wight)
    result = net(img.expand_dims(axis=0))
    index = result.argmax(axis=1)
    class_result = color_dict[int(index.asnumpy()[0])]
    print('classify result:', class_result)
import gluonbook as gb
from mxnet import gluon, init, nd
from mxnet.gluon import data as gdata, loss as gloss, model_zoo
import os

def train_fine_tuning(net, learning_rate, batch_size=128, num_epochs=40):
    train_iter = gdata.DataLoader(
        train_imgs.transform_first(train_augs), batch_size, shuffle=True)
    test_iter = gdata.DataLoader(
        test_imgs.transform_first(test_augs), batch_size)
    ctx = gb.try_all_gpus()
    net.collect_params().reset_ctx(ctx)
    net.hybridize()
    loss = gloss.SoftmaxCrossEntropyLoss()
    trainer = gluon.Trainer(net.collect_params(), 'sgd', {
        'learning_rate': learning_rate, 'wd': 0.001})
    gb.train(train_iter, test_iter, net, loss, trainer, ctx, num_epochs)

if __name__ == '__main__':
    data_dir = 'data'

    train_imgs = gdata.vision.ImageFolderDataset(
        os.path.join(data_dir, 'light/train'))
    test_imgs = gdata.vision.ImageFolderDataset(
        os.path.join(data_dir, 'light/test'))

    # 指定 RGB 三个通道的均值和方差来将图像通道归一化。
    normalize = gdata.vision.transforms.Normalize(
        [0.485, 0.456, 0.406], [0.229, 0.224, 0.225])

    train_augs = gdata.vision.transforms.Compose([
        gdata.vision.transforms.RandomResizedCrop(224),
        gdata.vision.transforms.RandomFlipLeftRight(),
        gdata.vision.transforms.ToTensor(),
        normalize])

    test_augs = gdata.vision.transforms.Compose([
        gdata.vision.transforms.Resize(256),
        gdata.vision.transforms.CenterCrop(224),
        gdata.vision.transforms.ToTensor(),
        normalize])

    pretrained_net = model_zoo.vision.resnet18_v2(pretrained=True)

    finetune_net = model_zoo.vision.resnet18_v2(classes=3)
    finetune_net.features = pretrained_net.features
    finetune_net.output.initialize(init.Xavier())
    # output 中的模型参数将在迭代中使用 10 倍大的学习率。
    finetune_net.output.collect_params().setattr('lr_mult', 10)
    train_fine_tuning(finetune_net, 0.01)


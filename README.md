### 红绿灯分类
环境：mxnet, gluon, mac,基于ImageNet预训练模型transfer learning, finetunning
##### 训练
```python train.py```
测试结果：
```
epoch 1, loss 5.7411, train acc 0.468, test acc 0.651, time 123.7 sec
epoch 2, loss 4.6547, train acc 0.517, test acc 0.860, time 119.4 sec
epoch 3, loss 0.7964, train acc 0.769, test acc 0.884, time 123.1 sec
epoch 4, loss 0.9767, train acc 0.725, test acc 0.872, time 142.4 sec
epoch 5, loss 0.5056, train acc 0.806, test acc 0.802, time 120.0 sec
epoch 6, loss 0.8685, train acc 0.711, test acc 0.884, time 126.5 sec
```
##### 推理
```python inference.py```
测试结果：```classify result: red```
数据太少，精确度不是很高

##### 参考

http://zh.gluon.ai/chapter_computer-vision/fine-tuning.html?highlight=hotdog

https://gluon-cv.mxnet.io/build/examples_classification/demo_cifar10.html
import numpy as np
import torch
import pandas as pd

from torch import nn
#delimiter指定读取文件中数据的分割符 文件中的分割符是空格 就用空格
# xy = np.loadtxt('../datasets/diabetes.csv',delimiter=',',dtype=np.float32)
xy = pd.read_csv('../datasets/diabetes.csv',delimiter=',',dtype=np.float32).values
x_data = torch.from_numpy(xy[:,:-1]) #这里本来就是矩阵
y_data = torch.from_numpy(xy[:, [-1]])# 这里是提取最后1维的数据，如果加上【】那么就是矩阵，不加就是向量


x=torch.tensor([1,2,3,4,5,6])
print(x.shape) # torch.Size([6])
y=x.view(-1,3)
print(y.size()) # torch.Size([2, 3])




class Model(torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = torch.nn.Linear(8, 6)
        self.linear2 = torch.nn.Linear(6, 4)
        self.linear3 = torch.nn.Linear(4, 1)  # 搭建一下每一层的线性结构
        # self.s = torch.nn.Sigmoid()  # 这里的Sigmoid是一个模块
        self.s = torch.nn.ReLU()

    def forward(self, x):
        x = self.s(self.linear1(x))  # 用每一层的线性结构进行非线性输出
        x = self.s(self.linear2(x))  # !!!!这里不能用 self.sigmoid命名 会发生冲突报错
        x = self.s(self.linear3(x))
        return x


model = Model()  # 实例化一个模型

criterion = torch.nn.BCELoss(reduction = 'sum')    #创建损失函数实例
optimizer = torch.optim.SGD(model.parameters(),lr=0.001)  #创建优化器实例 model.parameters()方法会把model中所有需要优化的参数找出来

from PIL import Image

# creating a object
im = Image.open(r"3H7A0197.jpg")

im.show()
for epoch in range(1500):
    # Forward
    y_pred = model(x_data)  # model内部有用call函数的类，所以可以直接调用实例对象
    # (这里是把所有的数据都扔进来了，并没有进行mini-batch运算)
    loss = criterion(y_pred, y_data)  # 构造损失函数实例
    print(epoch, loss.item())  # 去掉格式，直接输出数据

    # Backward
    optimizer.zero_grad()  # 将梯度置零 如果不删除相当于batch的累加，每次求的梯度就会累加，比如上一次计算的梯度
    # 为a，那么下一次的梯度就是a+b（b是下一次的梯度，但是最终的结果会累加）
    loss.backward()  # 计算当前loss对权重的梯度

    # Update
    optimizer.step()
    # 结果为什么不收敛 而且loss很大?  之前的reduction设定的是所有样本的误差



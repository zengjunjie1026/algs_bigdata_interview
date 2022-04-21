import torch
import torch.nn as nn

m = nn.Conv2d(2, 2, 3, stride=2)

''' 定义二维卷积Conv2d,输入通道数in_channels，输出通道数out_channels(间接定义了卷积的个数)，卷积的大小kernel_size（3*3）,
stride=2 卷积移动的步长。
'''

# Torch.nn.Conv2d(in_channels，out_channels，kernel_size，stride=1，padding=0，dilation=1，groups=1，bias=True)


input = torch.randn(1, 2, 5, 7)  # 输入为 大小（宽为5，高为7）5*7，深度为2（也可理解为通道数）

'''
综上可以推算出  输出的featuremap :2*3,深度为2。
'''
output = m(input)

print("输入图片(2张)：")
print(input)
print("卷积的权重：")
print(m.weight)
print("卷积的偏重：")
print(m.bias)

print("二维卷积后的输出：")
print(output)
print("输出的尺度：")
print(output.size())

convBlockOne = 0
convBlockTwo = 0

convBlockOne1 = 0
convBlockTwo1 = 0
for i in range(3):
    for j in range(3):
        # 第一个卷积核与图片对应相乘
        convBlockOne += m.weight[0][0][i][j] * input[0][0][i][j] \
                        + m.weight[0][1][i][j] * input[0][1][i][j]

        # 第二个卷积核与图片对应相乘
        convBlockTwo += m.weight[1][0][i][j] * input[0][0][i][j] \
                        + m.weight[1][1][i][j] * input[0][1][i][j]

#         # 第一个卷积核与图片对应相乘
#         convBlockOne1 += m.weight[0][0][i][j] * input[0][0][i][j]+ m.weight[0][1][i][j] * input[0][1][i][j]
#         # 第二个卷积核与图片对应相乘
#         convBlockTwo1 += m.weight[1][0][i][j] * input[0][0][i][j]+ m.weight[1][1][i][j] * input[0][1][i][j]
convBlockOne += m.bias[0]
convBlockTwo += m.bias[1]

# convBlockOne1 += m.bias[0]
# convBlockTwo1 += m.bias[1]

print("第一个卷积核的输出：")
print(convBlockOne)

print("输出的大小", type(convBlockOne), convBlockOne.shape)
print("第二个卷积核的输出：")
print(convBlockTwo)

# print("去掉斜杠后", convBlockOne1)
# print("去掉斜杠后", convBlockTwo1)
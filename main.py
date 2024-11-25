# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import torch


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    xx = torch.arange(4, dtype=torch.float)
    xx.requires_grad_(True)
    print(xx.grad)

    y = xx ** 2 + 3 * xx
    print(y)
    y=y.sum()
    print(y)

    y.backward()
    print(xx.grad)
    return
    xx = xx.reshape(5, -1)
    print(xx)
    print(torch.mv(xx, torch.ones(4, dtype=torch.long)))
    print(torch.ones(20))
    print(torch.dot(torch.arange(20.), torch.ones(20)))
    # print(xx.sum(axis=[0,1]))
    # print(xx.T)

    x = torch.tensor([[1., 0.], [-1., 1.]], requires_grad=True)
    z = x.pow(2).sum()
    z.backward()
    print(x.grad)
    print(torch.cuda.is_available())
    print(f'Hi, {name}')  # 按 ⌘F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

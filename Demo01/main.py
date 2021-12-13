# 这是一个示例 Python 脚本。
# 给定商品列表，和可用余额，输入商品名称购买商品，如果余额不住提示余额不足，若余额充足则购买成功

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Double Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def showGoods(tmp_goods):
    # print(goods)  直接打印主流程变量可以正常输出
    for tmp_index in range(len(tmp_goods)):
        print('商品：' + tmp_goods[tmp_index]['name'] + '  价格：' + str(tmp_goods[tmp_index]['price']))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    total = 2000
    price = 0
    file = ''
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
    ]
    # print(goods[0]['name'])
    while 1:
        if total < 0:
            break
        print('\n余额：'+str(total))
        showGoods(goods)
        file = input('\n请输入购买的商品：')
        for index in range(len(goods)):
            if file == goods[index]['name']:
                print('该商品['+goods[index]['name']+']价格为：'+str(goods[index]['price']))
                price = goods[index]['price']
                break

        if price <= 0:
            print("没有找到该商品！")
            continue

        if total - price < 0:
            print("余额不足,请重新选择！")
            continue

        total = total - price
        print("购买["+file+"]成功，支付["+str(price)+"],余额["+str(total)+"]！\n")






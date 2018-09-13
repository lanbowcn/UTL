import random
#通常做机器学习问题时，需要准备训练数据，通常会把样本数据和标签存放于2个list中，比如train_x = [x1,x2,...,xN]，
# train_y = [y1,y2,...,yN]. 有时候是需要将数据shuffle后再做处理的（比如，批量梯度下降算法，需要数据是打乱的）。
# 这时就需要以相同的顺序打乱两个list，那么在python中如何实现呢？可以通过设置相同的随机种子，再shuffle的方式来实现。
# 代码如下：
randnum = random.randint(0,100)
random.seed(randnum)
random.shuffle(train_x)
random.seed(randnum)
random.shuffle(train_y)
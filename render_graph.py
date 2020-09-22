import matplotlib.pyplot as plt
 
# 対象データ
x = [1, 2, 3]
y = [2, 4, 6]
 
# figureを生成する
fig = plt.figure()
 
# axをfigureに設定する
ax = fig.add_subplot(1, 1, 1)
 
# axesに散布図を設定する
ax.scatter(x, y, c='b')
 
# 表示する
plt.savefig("graph.jpg")
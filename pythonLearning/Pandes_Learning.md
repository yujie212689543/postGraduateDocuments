# Numpy 数组

## ndarray

```python
import numpy as np
```

```python
arr = np.array(5)  # 创建一个0维的NDAYRRAY数组
print(type(arr))
print(arr)

print("arr的维度：",arr .ndim)  # 数组的维度number of dimensions
```

```
<class 'numpy.ndarray'>
5
arr的维度： 0
```

```python
arr = np.array([1,2,3,5])  # 创建一个1维的NDAYRRAY数组
print(type(arr))
print(arr)

print("arr的维度：",arr .ndim)  # 数组的维度number of dimensions
```

```
<class 'numpy.ndarray'>
[1 2 3 5]
arr的维度： 1
```

```python
arr = np.array([[1,2,3],[4,5,6]])  # 创建一个2维的NDAYRRAY数组
print(type(arr))
print(arr)

print("arr的维度：",arr .ndim)  # 数组的维度number of dimensions
```

```
<class 'numpy.ndarray'>
[[1 2 3]
 [4 5 6]]
arr的维度： 2
```

## ndarray 同质性

```python
arr = np.array([1,"batman"])  # 不同的数据类型会被强制转换成相同的数据类型
print(arr)
```

```
['1' 'batman']
```

```python
arr = np.array([1,2.5])  # 不同的数据类型会被强制转换成相同的数据类型
print(arr)
```

```
[1.  2.5]
```

## 2. ndarray的属性

```python
arr= np.array(1)
print(arr)
print("数组的形状：",arr.shape)
print("数组的维度：",arr .ndim)
print("元素的个数：",arr.size)
print("元素的数据类型：",arr .dtype)
print("元素的转置：",arr .T)
```

```
1
数组的形状： ()
数组的维度： 0
元素的个数： 1
元素的数据类型： int64
元素的转置： 1
```

```python
arr= np.array([1,2.5,3])
print(arr)
print("数组的形状：",arr.shape)
print("数组的维度：",arr .ndim)
print("元素的个数：",arr.size)
print("元素的数据类型：",arr .dtype)
print("元素的转置：",arr .T)
print(" ")


arr= np.array([[1,2,3],[4,5,6]])
print(arr)
print("数组的形状：",arr.shape)
print("数组的维度：",arr .ndim)
print("元素的个数：",arr.size)
print("元素的数据类型：",arr .dtype)
print("元素的转置：",arr .T)
```

```
[1.  2.5 3. ]
数组的形状： (3,)
数组的维度： 1
元素的个数： 3
元素的数据类型： float64
元素的转置： [1.  2.5 3. ]
 
[[1 2 3]
 [4 5 6]]
数组的形状： (2, 3)
数组的维度： 2
元素的个数： 6
元素的数据类型： int64
元素的转置： [[1 4]
 [2 5]
 [3 6]]
```

## 3. ndarray 的创建

![image.png](attachment:c3c2424c-e778-488d-9bc9-f724848760b1.png)

```python
# 基础的创建方法
list1=[4,5,6]
arr= np. array(list1,dtype=np.float64)

print(arr.ndim)
print(arr)
```

```
1
[4. 5. 6.]
```

```python
# copy
arr1=np.copy(arr) # 元素和原始的数组相同，但是不是1个数组
print(arr1)
print("")
arr1[0]=8
print(arr1)
```

```
[4. 5. 6.]

[8. 5. 6.]
```

```python
# 预定义形状
# 全0 全1 未初始化  固定值
# 全0
arr= np.zeros((2,3)) # 2行3列, 完整写法：arr=np.zeros(shape=(2,3))
print(arr)
print(arr .dtype)
```

```
[[0. 0. 0.]
 [0. 0. 0.]]
float64
```

```python
arr= np.zeros((2,0)) # 1维,2个元素

print(arr)
```

```
[0. 0.]
```

```python
# 全1 
arr= np.ones((2,3),dtype=int)# 2行3列
print(arr)
```

```
[[1 1 1]
 [1 1 1]]
```

```python
# 未初始化
arr= np.empty((2,4)) # 2行3列
print(arr)
```

```
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
```

```python
# 未初始化
arr= np.empty((4,5)) # 2行3列
print(arr)
```

```
[[0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0.]]
```

```python
arr=np.full((3,4),2026)
print(arr)
```

```
[[2026 2026 2026 2026]
 [2026 2026 2026 2026]
 [2026 2026 2026 2026]]
```

```python
arr1=np.zeros_like(arr)  ## 创建一个与现有数组形状相同、但值全为零的新数组 
print(arr1)
print("")
arr1= np.empty_like(arr)
print(arr1)
print("")
arr1=np.full_like(arr,2027)
print(arr1)
```

```
[[0. 0. 0.]
 [0. 0. 0.]]

[[0. 0. 0.]
 [0. 0. 0.]]

[[2027. 2027. 2027.]
 [2027. 2027. 2027.]]
```

# 等差数列

```python
arr= np.arange(1,10,2) # start end(不包含) step
print(arr)
```

```
[1 3 5 7 9]
```

## 等间隔数列

```python
arr= np.linspace(0,100,5) #start end（不包含） NUM
print(arr)
```

```
[  0.  25.  50.  75. 100.]
```

```python
arr=np.arange(0,100,25)
print(arr)
```

```
[ 0 25 50 75]
```

# 对数间隔数列

```python
arr=np.logspace(0,4,3,base=2)
print(arr)
```

```
[ 1.  4. 16.]
```

# 单位矩阵

```python
arr=np. eye(3,dtype=int)
print(arr)
```

```
[[1 0 0]
 [0 1 0]
 [0 0 1]]
```

```python
arr1=np.eye(3,4,dtype=int)
print(arr1)
```

```
[[1 0 0 0]
 [0 1 0 0]
 [0 0 1 0]]
```

# 对角矩阵 ：主对角线上是非0，其他数字为0

```python
arr =np.diag([1,2,3,4])
print(arr)
```

```
[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
```

# 随机数组的生成
## 生成0-1之间的随机浮点数（均匀分布）

```python
arr=np.random.rand(2,3)  # 2行3列
print(arr)
```

```
[[0.2723164  0.71860593 0.78300361]
 [0.85032764 0.77524489 0.03666431]]
```

## 生成指定范围区间的随机浮点数

```python
arr=np.random.uniform(3,6,(2,3))。# low high size
print(arr)
```

```
[[3.03398307 3.38006394 5.79570386]
 [4.1008195  4.51807825 5.87672491]]
```

# 生成指定范围区间的随机整数

```python
arr=np.random.randint(3,6,(2,3))
print(arr)
```

```
[[4 3 4]
 [4 4 3]]
```

# 生成随机数列（正态分布）

```python
arr=np.random.randn(2,3)
print(arr)
```

```
[[-0.41079151  0.296111    0.30850584]
 [-0.23715071 -0.31351515  0.24021046]]
```

# 设置随机种子

```python
np.random.seed(200) 
arr=np.random.randint(1,10,(2,5))
print(arr)
```

```
[[1 5 8 7 9]
 [2 8 4 2 8]]
```

# ndarray 的数据类型
布尔类型 
整数类型
浮点数类型
复数 complex

```python
arr =np.array([1,0,2000,0],dtype=int)
print(arr)
```

```
[   1    0 2000    0]
```

# 5. 索引与切片

```python
## 一维数组的索引与切片
arr= np.random.randint(1,100,30)
print(arr)
```

```
[86 25  8 23 55 78 17 71 36 32 33 46 60 46 62 21 86  1  4 56 96 57  4 34
 73  1 53 91 62 71]
```

```python
print(arr[0])
print()
print(arr[:])
print()
print(arr[2:5])  # 2-4的元素（左包右不包）
print(arr[slice(2,5)])
print()
print(arr[(arr>10)&(arr<70)])  # 布尔索引,大于10小于70的值
```

```
86

[86 25  8 23 55 78 17 71 36 32 33 46 60 46 62 21 86  1  4 56 96 57  4 34
 73  1 53 91 62 71]

[ 8 23 55]
[ 8 23 55]

[25 23 55 17 36 32 33 46 60 46 62 21 56 57 34 53 62]
```

```python

## 二维数组的索引与切片
arr= np.random.randint(1,100,(4,8))
print(arr)
```

```
[[79 77 59 69 63 53  7 83]
 [97 28 69 65 90 69 51 95]
 [98 30 89 23  8 34 31 58]
 [98 24  6 41 27 66 98 82]]
```

```python
print(arr[1,4])。# 取第二行第五列的值
print()
print(arr[1:3,3:5])  # 切片
print()
print(arr[arr>50])  # arr>50 先产生1个BOOL数组
print()
print(arr[2][arr[2]>50])
print(arr[2,arr[2]>50])
```

```
90

[[65 90]
 [23  8]]

[79 77 59 69 63 53 83 97 69 65 90 69 51 95 98 89 58 98 66 98 82]

[98 89 58]
[98 89 58]
```

# 5. adarray的运算

```python
# 算数运算,多维数组也能运算，运算尽量形状一样
a =np.array([1,2,3])
b=np.array([4,5,6])
print(b+a)
print(a*b)
```

```
[5 7 9]
[ 4 10 18]
```

```python
# 数组与数字之间的算术运算
c= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c+3)
print()
print(c*3)
```

```
[[ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

[[ 3  6  9]
 [12 15 18]
 [21 24 27]]
```

```python
# 广播机制: 填充成3*3 进行运算
a= np.array([1,2,3])
b=np.array([[4],[5],[6]])
print(a*b)

 # 1 2 3
 # 1 2 3
 # 1 2 3

 # 4 4 4
 # 5 5 5
 # 6 6 6

print()
print(a@b) # 数组乘法（线代运算）
```

```
[[ 4  8 12]
 [ 5 10 15]
 [ 6 12 18]]

[32]
```

```python
# 无法广播
a= np.array([1,2,3]) # 1*3
b=np.array([[4],[5]) # 2*1
print(a*b)
```

```python
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[2,3,4],[3,4,5],[4,5,6]])
print(a@b)
```

```
[[ 20  26  32]
 [ 47  62  77]
 [ 74  98 122]]
```

# 2.3 NUMPY中的常用函数
## 1. 基本数学函数

```python
# 计算平方根
print(np.sqrt(9))
print(np.sqrt([1,4,9]))  # 数组
print()
arr=np.array([1,25,100])
print(np.sqrt(arr))
```

```
3.0
[1. 2. 3.]

[ 1.  5. 10.]
```

```python
# 计算指数
print(np.exp(1)) # 指数底为e, e^x
```

```
2.718281828459045
```

```python
# 计算自然对数
print(np.log(2))  # 底为e
```

```
0.6931471805599453
```

```python
# 计算正弦值，余弦值
a = np.array([0,30,45,60,90])
print ('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度  
print (np.sin(a*np.pi/180))
print ('\n')
print ('数组中角度的余弦值：')
print (np.cos(a*np.pi/180))
print ('\n')
print ('数组中角度的正切值：')
print (np.tan(a*np.pi/180))
```

```
不同角度的正弦值：
[0.         0.5        0.70710678 0.8660254  1.        ]


数组中角度的余弦值：
[1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01
 6.12323400e-17]


数组中角度的正切值：
[0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00
 1.63312394e+16]
```

```python
# 计算绝对值
arr=np.array([-1,1,2,-3])
print(np.abs(arr))
```

```
[1 1 2 3]
```

```python
# 计算A的B次幂 
print(np.power(arr,2))
```

```
[1 1 4 9]
```

```python
# 四舍五入
print(np.round([3.2,4,8.1]))
```

```
[3. 4. 8.]
```

```python
# 向上取整，向下取整
arr=np.array([1.6,2.7,3.1])
print(np.ceil(arr))
print()
print(np.floor(arr))
```

```
[2. 3. 4.]

[1. 2. 3.]
```

```python
# 检测缺失值
np.isnan([1,2,3,np.nan])
```

# 2. 统计函数
求和 计算平均值 计算中位数 标准差 方差
查找最大值 最小值
计算分位数 累计和 累积差

```python
arr=np. random.randint(1,20,8)
print(arr)
```

```
[10  6 19  9 13 10 14 10]
```

```python
# 求和
print(np.sum(arr))
```

```
91
```

```python
# 计算平均值
print(np.mean(arr))
```

```
11.375
```

```python
# 计算中位数
print(np.median([4,1,2])) # 奇数：先排序，再取中间值
print(np.median([1,2,4,8]))# 偶数：中间的两个数的平均值
```

```
2.0
3.0
```

```python

```

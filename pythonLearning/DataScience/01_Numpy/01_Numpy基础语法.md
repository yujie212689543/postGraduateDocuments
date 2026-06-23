#  Numpy基础语法

本练习覆盖课堂第二章 `NumPy` 的基础语法部分。请直接在每道题下方的代码单元中作答。

## 第1题：创建不同维度的 `ndarray`

请分别创建：
1. 一个 0 维数组，值为 `5`
2. 一个 1 维数组，值为 `[10, 20, 30, 40]`
3. 一个 2 维数组，值为 `[[1, 2, 3], [4, 5, 6]]`

要求输出每个数组以及它们的 `ndim`。

```python
import numpy as np

# 创建题目要求的数组
arr1 = np.array(5)
arr2 = np.array([10, 20, 30, 40])
arr3 = np.array([[1, 2, 3], [4, 5, 6]])

# 要求输出每个数组以及它们的 `ndim`
print(arr1)
print("arr1的维度为:%d" % arr1.ndim)
print(arr2)
print("arr2的维度为:%d" % arr2.ndim)
print(arr3)
print("arr3的维度为:%d" % arr3.ndim)

```

## 第2题：理解同质性和 `dtype`

请完成下面任务：
1. 创建数组 `[1, 2.5, 3]`，输出数组和 `dtype`
2. 创建数组 `[1, 'hello']`，输出数组和 `dtype`
3. 用一句注释说明：为什么数组中的元素类型会统一

```python
# 创建数组
arr1 = np.array([1, 2.5, 3])
arr2 = np.array([1, 'hello'])
# 输出数组和dtype
print(arr1)
print(arr1.dtype)
print(arr2)
print(arr2.dtype) # U11:Unicode字符串，每个元素最多存11个字符
# 数组中元素类型必须统一为了方便后续数据处理，符合实际应用场景

```

## 第3题：查看 `ndarray` 常用属性

已知数组：

```python
arr = np.array([[2, 4, 6], [8, 10, 12]])
```

请输出该数组的：
- `shape`
- `ndim`
- `size`
- `dtype`
- `T`
- `itemsize`
- `nbytes`

```python
# shape:尺寸，例如本题为(2,3)
# ndim:维度
# size:元素个数
# dtype:数据类型
# T: 转置
# itemsize:每个元素占字节数
# nbytes:数组总内存占用量
arr = np.array([[2, 4, 6], [8, 10, 12]])
print(arr.shape, arr.ndim)
print(arr.size, arr.dtype)
print(arr.T)
print(arr.itemsize, arr.nbytes)

```

## 第4题：数组创建方法练习

请分别创建下列数组：
1. 形状为 `(3, 4)` 的全 0 整数数组
2. 形状为 `(2, 5)` 的全 1 数组
3. 形状为 `(2, 3)`，所有元素都是 `2025` 的数组
4. 使用 `np.copy()` 复制第 3 小题的数组，并验证它和原数组不是同一个对象

```python
# np.zeros默认数据类型是float64，因此需要指定dtype=int
arr1 = np.zeros((3, 4), dtype=int)
arr2 = np.ones((2, 5))
arr3 = np.full((2, 3), 2025)
arr4 = np.copy(arr3)
print(arr4 is arr3)
# 拷贝后的数组和原数组不是一个对象

```

## 第5题：数值范围生成

请分别使用以下函数完成创建，并输出结果：
1. `np.arange()` 生成 `1` 到 `20` 的整数序列
2. `np.linspace()` 在 `0` 到 `100` 之间生成 `6` 个等间隔数
3. `np.logspace()` 以 `2` 为底，在指数 `0` 到 `4` 之间生成 `3` 个数

```python
# `np.arange()` 生成 `1` 到 `20` 的整数序列
arr1 = np.arange(1, 21, 1) # arange(array range):生成等差数列(start, end, step)
print(arr1)
# `np.linspace()` 在 `0` 到 `100` 之间生成 `6` 个等间隔数
arr2 = np.linspace(0, 100, 6) # linspace(liner space):生成等间距的数组
print(arr2)
# `np.logspace()` 以 `2` 为底，在指数 `0` 到 `4` 之间生成 `3` 个数
arr3 = np.logspace(0, 4, num=3, base=2)
print(arr3)

```

## 第6题：特殊矩阵与随机数组

请完成下面任务：
1. 创建一个 `3 x 3` 单位矩阵
2. 创建一个主对角线元素为 `[5, 1, 2, 3]` 的对角矩阵
3. 固定随机种子为 `20`
4. 生成一个形状为 `(2, 4)`、取值范围在 `[1, 10)` 的随机整数数组

```python
# 创建一个 `3 x 3` 单位矩阵
identity_matrix = np.eye(3)
print(identity_matrix)
# 创建一个主对角线元素为 `[5, 1, 2, 3]` 的对角矩阵
diag_matrix = np.diag([5, 1, 2, 3])
print(diag_matrix)
# 固定随机种子为 `20`
# 生成一个形状为 `(2, 4)`、取值范围在 `[1, 10)` 的随机整数数组
np.random.seed(20)
randint_matrix = np.random.randint(1, 10, size=(2, 4))
print(randint_matrix)

```

## 第7题：修改数据类型

请完成下面任务：
1. 创建数组 `[1, 0, 127, 0]`，数据类型指定为 `np.int8`
2. 再创建数组 `[1, 2, 3]`，数据类型指定为 `'i8'`
3. 分别输出两个数组及其 `dtype`

```python
# 创建数组 `[1, 0, 127, 0]`，数据类型指定为 `np.int8`
arr1 = np.array([1, 0, 127, 0], dtype='int8')
# 再创建数组 `[1, 2, 3]`，数据类型指定为 `'i8'`
arr2 = np.array([1, 2, 3], dtype='i8') # i8 = integer 8个字节
# 分别输出两个数组及其 `dtype`
print(arr1, ' ', arr1.dtype)
print(arr2, ' ', arr2.dtype)

```

## 第8题：一维数组索引与切片

已知数组：

```python
arr = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
```

请完成：
1. 取出索引为 `4` 的元素
2. 取出前 5 个元素
3. 取出索引 `2` 到 `6` 之间的元素
4. 取出步长为 `2` 的切片结果

```python
arr = np.array([11, 22, 33, 44, 55, 66, 77, 88, 99])
# 取出索引为 `4` 的元素
print(arr[4])
# 取出前 5 个元素
print(arr[0: 5])
# 取出索引 `2` 到 `6` 之间的元素
print(arr[2: 7])
# 取出步长为 `2` 的切片结果
print(arr[::2])

```

## 第9题：二维数组索引、切片、布尔索引

已知数组：

```python
arr = np.array([
    [12, 25, 38, 41],
    [56, 67, 78, 89],
    [15, 35, 55, 75]
])
```

请完成：
1. 取出第 `2` 行第 `3` 列的元素
2. 取出第 `1` 行中索引 `1:4` 的元素
3. 取出第 `3` 行中大于 `40` 的所有元素
4. 使用布尔索引筛选整个数组中所有大于 `50` 的元素

```python
arr = np.array([
    [12, 25, 38, 41],
    [56, 67, 78, 89],
    [15, 35, 55, 75]
])
# 取出第 `2` 行第 `3` 列的元素
print(arr[1][2])
# 取出第 `1` 行中索引 `1:4` 的元素
print(arr[0,1:4])
# 取出第 `3` 行中大于 `40` 的所有元素
print(arr[2][arr[2] > 40])
# 使用布尔索引筛选整个数组中所有大于 `50` 的元素
print(arr[arr > 50])

```

## 第10题：算术运算与广播机制

请完成下面任务：
1. 创建 `a = np.array([1, 2, 3])`
2. 创建 `b = np.array([4, 5, 6])`
3. 分别输出 `a + b`、`a * b`
4. 输出 `a + 10`
5. 创建二维数组 `c = np.array([[1, 2, 3], [4, 5, 6]])`，再输出 `c + a`
6. 用注释说明第 5 小题为什么可以直接相加

```python
# 创建二维数组a, b
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# 输出a + b, a * b, a + 10
print(a + b)
print(a * b)
print(a + 10)
# 创建二维数组c
# 为什么能直接相加？因为a数组是1*3大小的，通过广播扩充成和c同样尺寸（2*3），即([1,2,3],[1,2,3])
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c + a)
```

## 第11题：矩阵运算与形状调整

请完成下面任务：
1. 创建数组 `np.arange(1, 13)`
2. 将其重塑为 `3 x 4` 的二维数组
3. 再将它重塑为 `2 x 2 x 3` 的三维数组
4. 创建两个矩阵：

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
```

5. 分别输出 `a @ b` 和 `np.dot(a, b)` 的结果

```python
# 创建数组 `np.arange(1, 13)`
arr1 = np.arange(1, 13)
print(arr1)
# 将其重塑为 `3 x 4` 的二维数组
arr2 = np.reshape(arr1, (3, 4))
print(arr2)
# 再将它重塑为 `2 x 2 x 3` 的三维数组
arr3 = np.reshape(arr1, (2, 2, 3))
print(arr3)

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# 计算矩阵定义中的乘法(两种方法: @ / np.dot)
print(a @ b)
print(np.dot(a, b))

```

## 第12题：基础函数热身

已知数组：

```python
arr = np.array([-4, -1, 0, 1, 4, 9])
```

请分别输出：
1. `np.abs(arr)`
2. `np.sqrt(np.array([1, 4, 9, 16]))`
3. `np.power(np.array([1, 2, 3, 4]), 3)`
4. `np.round([3.2, 4.5, 8.1, 9.6])`
5. `np.ceil([1.6, 25.1, 81.7])`
6. `np.isnan([1, 2, np.nan, 3])`

```python
arr = np.array([-4, -1, 0, 1, 4, 9])
# 取数组的绝对值
print(np.abs(arr))
# 开根号
print(np.sqrt(np.array([1, 4, 9, 16])))
# 幂运算
print(np.power(np.array([1, 2, 3, 4]), 3))
# 四舍五入(注意在Numpy中采用银行家舍入，即“四舍六入五成双”，例如4.5->4.0 5.5->6.0)
print(np.round([3.2, 4.5, 8.1, 9.6]))
# 向上取整
print(np.ceil([1.6, 25.1, 81.7]))
# 判断是否为空值(Numpy中为NaN),每个元素用True/False表示
print(np.isnan([1, 2, np.nan, 3]))
```
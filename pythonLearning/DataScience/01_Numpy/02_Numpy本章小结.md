# Numpy本章小结

本练习偏向章节综合应用，覆盖课堂中提到的常用函数、统计计算、排序去重、条件筛选和简单案例。

## 第1题：基本数学函数

请使用 `numpy` 完成下面计算，并输出结果：
1. `np.exp(1)`
2. `np.log(2.71)`
3. `np.sin(np.pi / 2)`
4. `np.cos(np.pi)`
5. `np.sqrt([1, 4, 9, 16])`

```python
import numpy as np

# `np.exp(1)`
print(np.exp(1))
# `np.log(2.71)`
print(np.log(2.71))
# `np.sin(np.pi / 2)`
print(np.sin(np.pi / 2))
# `np.cos(np.pi)`
print(np.cos(np.pi))
# `np.sqrt([1, 4, 9, 16])`# 在这里作答
print(np.sqrt([1, 4, 9, 16]))

```

## 第2题：统计函数综合

已知成绩数组：

```python
scores = np.array([85, 90, 78, 92, 88, 95, 73, 90])
```

请计算并输出：
1. 总和
2. 平均值
3. 中位数
4. 标准差
5. 方差
6. 最大值与最小值
7. 最大值所在的索引

```python
scores = np.array([85, 90, 78, 92, 88, 95, 73, 90])
# 总和
print("总和sum=%d" %np.sum(scores))
# 平均值
print("平均值mean=%.2f" %np.mean(scores))
# 中位数
print("中位数median=%d" %np.median(scores))
# 标准差
print("标准差std=%.2f" %np.std(scores))
# 方差
print("方差var=%.2f" %np.var(scores))
# 最大值与最小值
print("最大值max=%d, 最小值min=%d" %(np.max(scores), np.min(scores)))
# 最大值所在的索引
print("最大值所在的索引=%d" %np.argmax(scores))
```

## 第3题：分位数、累计和、累计积

已知数组：

```python
arr = np.array([2, 4, 6, 8, 10])
```

请输出：
1. 25 分位数
2. 50 分位数
3. 75 分位数
4. 累计和
5. 累计积

```python
arr = np.array([2, 4, 6, 8, 10])
# 25分位数
print(f"25分位数={np.percentile(arr, 25)}")
# 50分位数
print(f"50分位数={np.percentile(arr, 50)}")
# 75分位数
print(f"75分位数={np.percentile(arr, 75)}")
# 累计和、累计积
print(f"累计和={np.cumsum(arr)}, 累计积={np.cumprod(arr)}")
```

## 第4题：比较、条件筛选与 `where`

已知数组：

```python
arr = np.array([12, 35, 48, 66, 79, 83, 95])
```

请完成：
1. 判断哪些元素大于 `60`
2. 判断哪些元素小于 `50`
3. 使用逻辑运算筛选出 `50` 到 `90` 之间的元素
4. 使用 `np.where()` 将大于等于 `60` 的元素标记为 `'及格'`，否则标记为 `'待提高'`

```python
arr = np.array([12, 35, 48, 66, 79, 83, 95])
# 判断哪些元素大于 60
print(arr[arr>60])
# 判断哪些元素小于 50
print(arr[arr<50])
# 筛选50 到 90之间的元素
print(arr[(arr >= 50) & (arr <= 90)])
# 使用 np.where()将大于等于 `60` 的元素标记为 '及格'，否则标记为 '待提高'
arr = np.where(arr >= 60, '及格', '待提高')
print(arr)
```

## 第5题：排序、去重、索引排序

已知数组：

```python
arr = np.array([7, 3, 9, 3, 5, 7, 1, 9, 2])
```

请完成：
1. 输出升序排序后的结果
2. 输出去重后的结果
3. 输出原数组排序后对应的索引位置（`argsort`）

```python
# 原始数组
arr = np.array([7, 3, 9, 3, 5, 7, 1, 9, 2])
# 升序排序后的结果(np.sort默认升序)
print(f"升序排序后的结果:{np.sort(arr)}")
# 去重后的结果
print(f"去重后的结果:{np.unique(arr)}")
# 原数组排序后的索引位置
print(f"原数组排序后的索引位置:{np.argsort(arr)}")
```

## 第6题：拼接、拆分、重塑

请完成下面任务：
1. 创建 `a = np.array([1, 2, 3])`
2. 创建 `b = np.array([4, 5, 6])`
3. 将两个数组拼接为一个新数组
4. 把拼接后的结果重塑为 `2 x 3` 的数组
5. 按行将该二维数组拆分成两个子数组

```python
# 创建数组a, b
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
# 两个数组拼接为一个新数组
concat_arr = np.concatenate([a, b])
# 拼接后结果重塑为2*3的数组
reshaped_arr = np.reshape(concat_arr, (2, 3))
# 按行拆成两个子数组(2表示分成两份，axis=0代表按行来分)
split_res = np.split(reshaped_arr, 2, axis=0)
```

## 第7题：成员判断与缺失值检测

请完成下面任务：
1. 定义 `a = np.array([1, 3, 5, 7, 9])`
2. 定义 `b = np.array([3, 4, 7, 8])`
3. 使用 `np.in1d(a, b)` 判断 `a` 中哪些元素也出现在 `b` 中
4. 定义数组 `c = np.array([1, np.nan, 3, np.nan, 5])`
5. 检测 `c` 中哪些位置是缺失值

```python
# 新建数组a, b
a = np.array([1, 3, 5, 7, 9])
b = np.array([3, 4, 7, 8])
# 判断a中哪些元素出现在b中
print(a[np.in1d(a, b)])
# 新建数组c
c = np.array([1, np.nan, 3, np.nan, 5])
# 检测c中缺失值的位置
print(np.isnan(c))

```

## 第8题：课堂案例综合练习

某班 6 位同学三门课程成绩如下：

```python
scores = np.array([
    [88, 76, 90],
    [92, 85, 87],
    [75, 79, 83],
    [96, 91, 89],
    [64, 72, 70],
    [85, 88, 84]
])
```

请完成：
1. 计算每位同学的总分
2. 计算每位同学的平均分
3. 找出总分最高的同学索引
4. 找出数学成绩（第 1 列）大于等于 `85` 的同学编号
5. 计算每门课程的平均分
6. 将平均分低于 `80` 的同学标记为 `'重点关注'`，其余标记为 `'表现稳定'`

```python
scores = np.array([
    [88, 76, 90],
    [92, 85, 87],
    [75, 79, 83],
    [96, 91, 89],
    [64, 72, 70],
    [85, 88, 84]
])
# 每位学生的总分、平均分(axis=1沿着行求和，即竖着求和/平均分)
print(f"每个学生的总分：{np.sum(scores, axis=1)}")
mean_arr = np.mean(scores, axis=1)
print("每个学生的平均分:", [f"{x:.2f}" for x in mean_arr])
# 找到总分最高同学索引
print("总分最高同学索引:", np.argmax(np.sum(scores, axis=1)))
# 数学成绩>=85分的同学编号(np.where返回是元组，所以需要加[0])
math_score = scores[:, 1]
print("数学成绩>=85分的同学编号:", np.where(math_score >= 85)[0])
# 计算每门课程的平均分
subj_mean = np.mean(scores, axis=0)
print("每门课程的平均分:", [f"{x:.2f}"for x in subj_mean])
# 平均分低于80分的学生标记为"重点关注"，其他为表现稳定
stu_mean_score = np.mean(scores, axis=1)
print(np.where(stu_mean_score < 80, "重点关注", "表现稳定"))
```

## 第9题：综合应用题

已知数组：

```python
scores = np.array([
    [78, 82, 91],
    [88, 76, 85],
    [92, 90, 89],
    [65, 70, 72]
])
```

请完成：
1. 计算每位同学的总分
2. 计算每门课程的平均分
3. 找出总分最高的同学索引
4. 找出英语成绩（第 3 列）大于等于 `85` 的同学索引
5. 将总分按升序排序后输出
6. 将平均分低于 `80` 的同学标记为“待提升”，否则标记为“良好”

```python
# 新建二维数组-学生分数
scores = np.array([
    [78, 82, 91],
    [88, 76, 85],
    [92, 90, 89],
    [65, 70, 72]
])
# 计算每个学生的总分
stu_sum_scores = np.sum(scores, axis=1)
print(stu_sum_scores)
# 计算每门课程的平均分
subj_mean_arr = np.mean(scores, axis=0)
print([f"{x:.2f}" for x in subj_mean_arr])
# 总分最高的同学索引
print(np.argmax(np.sum(scores, axis=1)))
# 英语成绩>=85的同学索引
eng_scores = scores[:,2]
print(np.where(eng_scores >= 85)[0])
# 总分按升序输出
print(np.sort(stu_sum_scores))
# 平均分低于80的学生标记为“待提升”，否则标记为“良好”
stu_mean_scores = np.mean(scores, axis=1)
print(np.where(stu_mean_scores < 80, '待提升', '良好'))
```
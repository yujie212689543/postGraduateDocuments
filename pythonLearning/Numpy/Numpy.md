# NumPy 核心知识点整理 (CISC 7204 Tutorial 03) - 完整版

> [!INFO] 概述
> **NumPy (Numerical Python)** 是 Python 科学计算的基础库。其核心是 `ndarray` (N-dimensional array)，一种同质（homogeneous）、多维的数组对象。
> - **优势**：比 Python 原生列表快得多，内存占用更少，支持向量化运算。
> - **核心机制**：Strided Memory View (步长内存视图)，所有元素类型相同，访问连续。

---

## 1. 数组创建与加载 (Creation & Loading)

### 从文件加载
在处理真实数据时，通常需要从 CSV 文件加载数据。

| 方法 | 描述 | 示例代码 |
| :--- | :--- | :--- |
| `np.genfromtxt` | 加载文本/CSV 文件，处理缺失值能力强 | `data = np.genfromtxt('file.csv', delimiter=',')` |
| `np.loadtxt` | 加载格式整齐的文本文件，速度稍快 | `data = np.loadtxt('file.txt')` |

> [!EXAMPLE] 作业案例 (Ex 1.01)
> 加载 `normal_distribution.csv`：
> ```python
> dataset = np.genfromtxt('../Datasets/normal_distribution.csv', delimiter=',')
> ```

### 基础属性
- `.shape`: 返回数组维度 `(rows, columns)`。
- `.dtype`: 返回数据类型 (如 `float64`)。
- `.ndim`: 返回维度数量。
- `.size`: 返回元素总数。

---

## 2. 索引与切片 (Indexing & Slicing)

NumPy 的索引语法基于 Python 列表，但支持多维操作。

### 基础索引
- **正向索引**: `dataset[0]` (第一行), `dataset[0, 0]` (第一个元素)。
- **反向索引**: `dataset[-1]` (最后一行), `dataset[-1, -1]` (最后一个元素)。

### 切片 (Slicing)
语法：`[start:stop:step]`
- **行切片**: `dataset[1:3]` (第 2 到第 3 行)。
- **列切片**: `dataset[:, 0]` (所有行的第 1 列)。
- **组合切片**: `dataset[1:3, 1:3]` (2 x 2 子矩阵)。
- **步长切片**: `dataset[4, ::2]` (第 5 行，每隔一个元素)。
- **反向切片**: `dataset[-1, ::-1]` (最后一行，元素反转)。

> [!EXAMPLE] 作业案例 (Ex 1.02)
> - 获取最后三列：`dataset[:, -3:]`
> - 获取最后两行和前两列的交集：`dataset[-2:, :2]`

### 花哨索引 (Fancy Indexing)
使用整数数组或布尔数组进行索引。

> [!NOTE] 什么是花哨索引？
> **花哨索引（Fancy Indexing）** 是指使用整数数组或布尔数组作为索引来访问或重新排列数组元素的技术。
> 
> **核心理解**：花哨索引就是"按照索引数组指定的顺序，从原数组中提取数据"。
> 
> ```python
> # 示例：argsort 排序索引
> data = np.array([8, 3, 9, 1, 5])
> index_sorted = np.argsort(data)  # 返回 [3, 1, 4, 0, 2]
> sorted_data = data[index_sorted]  # 花哨索引！得到 [1, 3, 5, 8, 9]
> ```
> 
> ** `np.argsort()` 的含义**：
> - 返回**排序后的索引位置**，不是排序后的值
> - `[3, 1, 4, 0, 2]` 表示：最小的数在位置 3，第二小的在位置 1，以此类推
> 
> **验证排序是否正确**：
> ```python
> # 检查是否升序排列（每个元素都不大于它后面的元素）
> np.all(sorted_data[:-1] <= sorted_data[1:])  # True 表示已排序
> ```
> 
> ** `np.all()` 的工作原理**：
> - `sorted_data[:-1]`：除最后一个外的所有元素
> - `sorted_data[1:]`：除第一个外的所有元素
> - 对应位置比较：检查 `当前元素 <= 下一个元素` 是否全部成立
> - 全部为 True → 数组已升序排列 ✅

---

## 3. 统计运算 (Statistical Operations)

NumPy 提供了高效的向量化统计函数。大多数函数支持 `axis` 参数。

| 函数 | 描述 | Axis 参数说明 |
| :--- | :--- | :--- |
| `np.mean()` | 平均值 | `axis=0`: 每列均值; `axis=1`: 每行均值 |
| `np.median()` | 中位数 | 同上 |
| `np.var()` | 方差 (Variance) | 衡量数据离散程度 |
| `np.std()` | 标准差 (Std Dev) | 方差的平方根，单位与数据一致 |
| `np.sum()` | 求和 | 同上 |
| `np.min()` / `np.max()` | 最小/最大值 | 同上 |

> [!EXAMPLE] 作业案例 (Ex 1.01 & Activity 1.01)
> ```python
> # 整体均值
> np.mean(dataset)
> # 每列的方差
> np.var(dataset, axis=0)
> # 每行的标准差
> np.std(dataset, axis=1)
> ```

> [!TIP] Axis 记忆法
> - **Axis 0**: 跨行操作 (Cross Rows) → 结果压缩了行，保留列 (Column-wise)。
> - **Axis 1**: 跨列操作 (Cross Columns) → 结果压缩了列，保留行 (Row-wise)。
> - *口诀：Axis 是"被压扁"的那个维度。*
> 
> **更直观的理解**：
> - `axis=0` → 沿着"行"方向移动 → 每列求平均 → 结果数量 = 列数
> - `axis=1` → 沿着"列"方向移动 → 每行求平均 → 结果数量 = 行数

---

## 4. 高级操作 (Advanced Operations)

### 4.1 过滤 (Filtering)
使用布尔掩码 (Boolean Masking) 筛选数据。

- **布尔索引**: `data[data > 10]` (返回所有大于 10 的值，展平为一维)。

> [!NOTE] `dataset[dataset > 105]` 是什么意思？
> 
> 这是 **NumPy 布尔索引（Boolean Indexing）** 的核心语法，分两步执行：
> 
> **第 1 步：比较运算**
> ```python
> dataset > 105
> # 返回一个布尔数组（True/False），标记每个位置是否满足条件
> ```
> 
> **第 2 步：布尔索引**
> ```python
> dataset[dataset > 105]
> # 用布尔数组作为索引，选出所有为 True 的位置对应的值
> ```
> 
> **可视化理解**：
> ```
> dataset:        [100, 102, 108,  95, 110, 103, 107]
>                    ↓    ↓    ↓    ↓    ↓    ↓    ↓
> dataset > 105:  [False, False, True, False, True, False, True]
>                    ↓    ↓    ↓    ↓    ↓    ↓    ↓
> 结果:           [             108,       110,       107]
> ```
> 
> **常见用法**：
> ```python
> # 选择第一列大于100的所有行
> dataset[dataset[:, 0] > 100]
> 
> # 多个条件组合（必须用 &，不能用 and）
> dataset[(dataset > 90) & (dataset < 95)]
> ```

- **复杂条件**: 必须使用 `&` (与), `|` (或), `~` (非)，且每个条件加括号。
  - 例：`(data > 90) & (data < 95)`
- **np.extract**: `np.extract(condition, data)` (功能同布尔索引)。

> [!NOTE] `np.extract()` vs 布尔索引
> ```python
> # 两者完全等价，只是写法不同
> result = dataset[condition]        # 布尔索引（更常用）
> result = np.extract(condition, dataset)  # np.extract（功能相同）
> ```
> 
> **推荐**：在实际工作中，更常用 `dataset[condition]`，因为它更简洁直观。

- **np.where**: 返回满足条件的**索引** `(row_indices, col_indices)`。

> [!EXAMPLE] 作业案例 (Ex 1.03)
> 找出与 100 差值小于 1 的坐标：
> ```python
> rows, cols = np.where(np.abs(dataset - 100) < 1)
> indices_list = [[rows[i], cols[i]] for i in range(len(rows))]
> ```
> 
> ** `np.where()` 的工作原理**：
> - 对于二维数组，返回**两个数组**：
>   - 第一个数组：所有满足条件的**行索引**
>   - 第二个数组：所有满足条件的**列索引**
> - `rows = [0, 1, 3]` 表示第 0 行、第 1 行、第 3 行满足条件
> - `cols = [0, 2, 1]` 表示第 0 列、第 2 列、第 1 列满足条件
> 
> **组合索引的方法**：
> ```python
> # 方法1：列表推导式（你用的方法）
> indices = [[rows[i], cols[i]] for i in range(len(rows))]
> 
> # 方法2：使用 zip（更 Pythonic）
> indices = [[r, c] for r, c in zip(rows, cols)]
> 
> # 方法3：使用 np.argwhere（最简洁！⭐）
> indices = np.argwhere(np.abs(dataset - 100) < 1)
> ```
> 
> **验证筛选结果**：
> ```python
> # 检查第一个点是否正确
> if len(indices) > 0:
>     r, c = indices[0]
>     val = dataset[r, c]
>     print(f"验证：坐标 {r},{c} 的值为 {val}, 差值为 {np.abs(val-100)}")
> ```
> 
> **类型转换问题**：`np.where()` 返回的是 `np.int64` 类型，显示时会带有 `np.int64()` 包装。
> ```python
> # 转换为 Python 原生 int，显示更干净
> indices = [[int(rows[i]), int(cols[i])] for i in range(len(rows))]
> # 或直接使用 .tolist()
> indices = np.argwhere(condition).tolist()
> ```

### 4.2 排序 (Sorting)
- `np.sort(data, axis=1)`: 返回排序后的数组副本 (默认沿最后一轴，即行内排序)。
- `np.argsort(data)`: 返回**排序后的索引**。常用于保持原始数据结构的同时获取顺序。

> [!EXAMPLE] 作业案例 (Ex 1.03)
> 获取第一行排序后的值：
> ```python
> sorted_indices = np.argsort(dataset[0])
> sorted_values = dataset[0][sorted_indices]  # 花哨索引
> ```

### 4.3 分割与合并 (Splitting & Combining)

#### 分割 (Splitting)
- `np.hsplit(data, N)`: 水平分割 (按列切分)，要求列数能被 N 整除。
- `np.vsplit(data, N)`: 垂直分割 (按行切分)，要求行数能被 N 整除。

#### 合并 (Stacking)

> [!NOTE] `np.vstack()` 和 `np.hstack()` 的图形理解
> 
> **垂直堆叠 `np.vstack()` —— 上下拼接（叠罗汉）**
> ```
> ┌─────────────┐     ┌─────────────┐
> │  数组 A      │     │  数组 B      │
> │  [1 2 3]     │     │  [4 5 6]     │
> │  [7 8 9]     │  →  │  [0 1 2]     │
> └─────────────┘     └─────────────┘
>       ↓ vstack (上下拼接)
> ┌─────────────┐
> │  数组 A      │  ← 先放 A
> │  [1 2 3]     │
> │  [7 8 9]     │
> │  数组 B      │  ← 再放 B
> │  [4 5 6]     │
> │  [0 1 2]     │
> └─────────────┘
> 要求：列数必须相同！
> ```
> 
> **水平堆叠 `np.hstack()` —— 左右拼接（排队）**
> ```
> ┌─────────────┐     ┌─────────────┐
> │  数组 A      │     │  数组 B      │
> │  [1 2 3]     │  →  │  [4 5 6]     │
> │  [7 8 9]     │     │  [0 1 2]     │
> └─────────────┘     └─────────────┘
>       ↓ hstack (左右拼接)
> ┌─────────────────────┐
> │  数组 A  │ 数组 B    │
> │  [1 2 3  │  4 5 6]   │
> │  [7 8 9  │  0 1 2]   │
> └─────────────────────┘
> 要求：行数必须相同！
> ```
> 
> **语法注意**：
> ```python
> # ❌ 错误：传入了两个独立的参数
> np.vstack(A, B)
> 
> # ✅ 正确：传入一个包含所有数组的元组或列表
> np.vstack((A, B))  # 注意双重括号！
> np.vstack([A, B])
> ```
> **错误信息**：`vstack() takes 1 positional argument but 2 were given` 表示参数数量错误。

> [!EXAMPLE] 作业案例 (Ex 1.02 & 1.03)
> 重构数据流程：
> 1. `thirds = np.hsplit(dataset, 3)` (分成左中右三份)
> 2. `halves = np.vsplit(thirds[0], 2)` (将左边那份再分成上下两份)
> 3. `restored = np.vstack((halves[0], halves[1]))` (恢复左边那份)
> 4. `full = np.hstack([restored, thirds[1], thirds[2]])` (完全恢复原数据)

**图形化完整流程**：
```
原始数据 (100行×9列)
┌─────────────────────────────────────────────┐
│ 列0 列1 列2 │ 列3 列4 列5 │ 列6 列7 列8   │
│  a   b   c  │  d   e   f  │  g   h   i    │
│  j   k   l  │  m   n   o  │  p   q   r    │
│  ...        │  ...        │  ...          │
└─────────────────────────────────────────────┘
      ↓ hsplit(3) 水平分割成3份
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  thirds[0]   │ │  thirds[1]   │ │  thirds[2]   │
│  列0 列1 列2 │ │  列3 列4 列5 │ │  列6 列7 列8 │
│  a   b   c   │ │  d   e   f   │ │  g   h   i   │
│  j   k   l   │ │  m   n   o   │ │  p   q   r   │
│  ...         │ │  ...         │ │  ...         │
└──────────────┘ └──────────────┘ └──────────────┘
      ↓ vsplit(2) 将第一部分垂直分成上下两份
┌──────────────┐
│  上半部分     │ ← halfed_first[0] (50行×3列)
│  a   b   c   │
│  j   k   l   │
├──────────────┤
│  下半部分     │ ← halfed_first[1] (50行×3列)
│  ...         │
│  x   y   z   │
└──────────────┘
      ↓ vstack 垂直堆叠恢复
┌──────────────┐
│  恢复的      │ ← first_col (100行×3列)
│  thirds[0]   │
└──────────────┘
      ↓ hstack 水平堆叠恢复完整数据
┌─────────────────────────────────────────────┐
│  完整恢复的数据 (100行×9列)                  │
└─────────────────────────────────────────────┘
```

### 4.4 重塑 (Reshaping)
改变数组形状，但元素总数不变。

- `data.reshape(rows, cols)`
- **使用 `-1` **: 让 NumPy 自动计算该维度的大小。
  - `data.reshape(1, -1)`: 展平为单行。
  - `data.reshape(-1, 2)`: 变为多行 2 列。

> [!NOTE] `reshape` 的详细解释
> 
> **核心概念**：重塑 = 重新排列数据，**元素总数不变**。
> 
> ** `(1, -1)` 中的 `1` 代表什么？**
> - `(1, -1)` = 目标形状是 **(1 行, 列数自动计算)**
> - `1` 表示：**我要把数据压缩成只有 1 行**
> - `-1` 表示：列数自动计算（总元素数 ÷ 1）
> 
> **类比理解**：900 个学生可以排成 100 行×9 列，也可以排成 1 行×900 列（超级长队），学生数量不变！
> 
> **对比不同重塑方式**：
> ```python
> # 假设有 8 个元素
> data = np.array([1, 2, 3, 4, 5, 6, 7, 8])
> 
> data.reshape(1, -1)   # → (1, 8)  1行8列
> data.reshape(2, -1)   # → (2, 4)  2行4列
> data.reshape(4, -1)   # → (4, 2)  4行2列
> data.reshape(-1, 1)   # → (8, 1)  8行1列
> data.reshape(-1, 2)   # → (4, 2)  4行2列
> ```
> 
> **验证元素总数守恒**：
> ```python
> single_list = data.reshape(1, -1)
> # shape[0] = 1 (行数)
> # shape[1] = 900 (列数，即元素个数)
> # dataset.size = 900 (总元素数)
> 
> # 验证：列数应等于总元素数
> print(f"元素总数检查：{single_list.shape[1]} == {dataset.size}")
> # 输出：元素总数检查：900 == 900 ✅
> ```
> 
> ** `shape[0]` vs `shape[1]` **：
> - `shape[0]` = 行数（在 (1, 900) 中 = 1）
> - `shape[1]` = 列数（在 (1, 900) 中 = 900）
> - 检查元素总数要用 `shape[1]`（列数），因为只有 1 行

> [!WARNING] 注意事项
> `reshape` 操作不会复制数据，只是改变视图 (View)。如果新形状的元素总数与原数组不匹配，会报错。

---

## 5. 迭代 (Iterating)

虽然向量化运算优于循环，但有时仍需遍历。

- `np.nditer(data)`: 高效遍历每个元素 (扁平化遍历)。

  ```python
  for x in np.nditer(dataset):
      print(x)
  ```

- `np.ndenumerate(data)`: 遍历并获取 **(索引，值)** 对。

  ```python
  for index, value in np.ndenumerate(dataset):
      print(f"Index: {index}, Value: {value}")
      # index 是一个元组，例如 (0, 1) 代表第 0 行第 1 列
  ```

> [!NOTE] 迭代时的常见错误
> 
> **错误 1：变量名混淆**
> ```python
> # ❌ 错误：第二个循环用了第一个循环的计数器
> count1 = 0
> for x in np.nditer(dataset):
>     if count1 < 5:
>         print(x)
>         count1 += 1
> 
> count2 = 0
> for index, value in np.ndenumerate(dataset):
>     if count1 < 5:  # ❌ 应该用 count2，不是 count1
>         print(index, value)
> ```
> 
> **错误 2：缩进错误**
> ```python
> # ❌ 错误：print 和 count += 1 缩进不对
> for x in np.nditer(dataset):
>     if count < 5:
>     print(x)      # ❌ 缩进错误
>     count += 1    # ❌ 缩进错误
> 
> # ✅ 正确
> for x in np.nditer(dataset):
>     if count < 5:
>         print(x)  # ✅ 正确缩进
>         count += 1
> ```

---

## 6. f-string 格式化字符串

> [!NOTE] f-string 详解
> 
> **基本语法**：
> ```python
> print(f"字符串 {变量或表达式} 字符串")
> ```
> 
> **示例**：
> ```python
> single_list.shape = (1, 900)
> dataset.size = 900
> 
> print(f"总元素数检查：{single_list.shape[1]} == {dataset.size}")
> # 输出：总元素数检查：900 == 900
> ```
> 
> **执行过程**：
> 1. 计算 `{single_list.shape[1]}` → 900
> 2. 计算 `{dataset.size}` → 900
> 3. 替换到字符串中
> 4. 输出结果
> 
> **更多用法**：
> ```python
> # 计算表达式
> print(f"10 + 20 = {10 + 20}")  # 10 + 20 = 30
> 
> # 调用函数
> print(f"长度：{len('Python')}")  # 长度：6
> 
> # 格式化数字
> pi = 3.14159
> print(f"π ≈ {pi:.2f}")  # π ≈ 3.14
> 
> # 对齐
> name = "Alice"
> print(f"|{name:10}|")  # |Alice     |
> ```

---

## 7. 常用代码速查表 (Cheat Sheet)

```python
import numpy as np

# 1. 加载
data = np.genfromtxt('data.csv', delimiter=',')

# 2. 统计
mean_val = np.mean(data)          # 整体均值
col_means = np.mean(data, axis=0) # 列均值
std_dev = np.std(data, axis=1)    # 行标准差

# 3. 索引与切片
first_row = data[0]
last_col = data[:, -1]
sub_matrix = data[1:3, 1:3]       # 2 x 2 子集
reversed_row = data[-1, ::-1]     # 最后一行反转

# 4. 过滤
filtered = data[data > 100]       # 大于 100 的值
indices = np.where(data > 100)    # 大于 100 的索引
argwhere_indices = np.argwhere(data > 100)  # 直接返回坐标列表

# 5. 排序
sorted_data = np.sort(data, axis=0)
sort_indices = np.argsort(data)

# 6. 变形
split_cols = np.hsplit(data, 3)
combined = np.vstack([data, data])
reshaped = data.reshape(-1, 2)

# 7. 验证
is_sorted = np.all(sorted_data[:-1] <= sorted_data[1:])  # 检查是否升序
is_equal = np.array_equal(original, restored)            # 检查两个数组是否完全相同
```

---

## 8. 常见陷阱 (Pitfalls)

1. **逻辑运算符错误**: 在 NumPy 中组合条件时，必须使用 `&`, `|`, `~`，**不能**使用 Python 的 `and`, `or`, `not`。
    - ❌ `data[(data > 10) and (data < 20)]`
    - ✅ `data[(data > 10) & (data < 20)]`

2. **Axis 混淆**: 记不清 axis 是行还是列？记住 `axis=0` 是沿着行向下走（操作列），`axis=1` 是沿着列向右走（操作行）。

3. **视图 vs 副本**: 切片操作通常返回**视图 (View)**，修改切片会影响原数组。如果需要副本，请使用 `.copy()`。

4. **分割限制**: `hsplit` 和 `vsplit` 要求维度必须能被整除，否则抛出 `ValueError`。

5. **vstack/hstack 参数错误**: 
    - ❌ `np.vstack(A, B)` (两个独立参数)
    - ✅ `np.vstack((A, B))` (一个元组/列表)

6. **变量名混淆**: 多个循环使用独立计数器变量，不要混用。

7. **文件路径错误**: 
    - 使用 `os.getcwd()` 检查当前工作目录
    - 使用 `os.listdir('.')` 查看目录内容
    - 使用 `os.path.exists(path)` 检查文件是否存在
    - Mac 系统**区分大小写**：`Dataset` ≠ `Datasets`

8. ** `np.int64` 显示问题**: 
    - `np.where()` 和 `np.argwhere()` 返回 `np.int64` 类型
    - 使用 `.tolist()` 或 `int()` 转换为 Python 原生类型，显示更干净

---

> [!SUMMARY] 核心要点
> 1. **NumPy 数组** = 同质、多维、高效
> 2. **布尔索引** = 用条件筛选数据 `data[condition]`
> 3. ** `np.where` ** = 返回满足条件的索引位置
> 4. ** `np.argwhere` ** = 直接返回坐标列表（最简洁）
> 5. ** `np.argsort` ** = 返回排序后的索引（配合花哨索引）
> 6. ** `np.hstack/vstack` ** = 水平/垂直拼接（注意参数要用元组）
> 7. ** `reshape` ** = 改变形状，元素总数守恒
> 8. ** `axis` ** = 被压缩的维度（axis=0 压缩行，axis=1 压缩列）
> 9. **f-string** = `f"变量值：{variable}"` 格式化字符串
> 10. **验证数据** = 始终检查操作结果是否正确（`np.array_equal`, `np.all`）
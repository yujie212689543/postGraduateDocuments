# NumPy 核心知识点整理 (CISC 7204 Tutorial 03)

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
- **Argsort 索引**: `data[np.argsort(data)]` (获取排序后的值)。

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
> - **Axis 0**: 跨行操作 (Cross Rows) $\rightarrow$ 结果压缩了行，保留列 (Column-wise)。
> - **Axis 1**: 跨列操作 (Cross Columns) $\rightarrow$ 结果压缩了列，保留行 (Row-wise)。
> - *口诀：Axis 是“被压扁”的那个维度。*

---

## 4. 高级操作 (Advanced Operations)

### 4.1 过滤 (Filtering)
使用布尔掩码 (Boolean Masking) 筛选数据。

- **布尔索引**: `data[data > 10]` (返回所有大于 10 的值，展平为一维)。
- **复杂条件**: 必须使用 `&` (与), `|` (或), `~` (非)，且每个条件加括号。
  - 例：`(data > 90) & (data < 95)`
- **np.extract**: `np.extract(condition, data)` (功能同布尔索引)。
- **np.where**: 返回满足条件的**索引** `(row_indices, col_indices)`。

> [!EXAMPLE] 作业案例 (Ex 1.03)
> 找出与 100 差值小于 1 的坐标：
> ```python
> rows, cols = np.where(np.abs(dataset - 100) < 1)
> indices_list = [[rows[i], cols[i]] for i in range(len(rows))]
> ```

### 4.2 排序 (Sorting)
- `np.sort(data, axis=1)`: 返回排序后的数组副本 (默认沿最后一轴，即行内排序)。
- `np.argsort(data)`: 返回**排序后的索引**。常用于保持原始数据结构的同时获取顺序。

> [!EXAMPLE] 作业案例 (Ex 1.03)
> 获取第一行排序后的值：
> ```python
> sorted_indices = np.argsort(dataset[0])
> sorted_values = dataset[0][sorted_indices]
> ```

### 4.3 分割与合并 (Splitting & Combining)

#### 分割 (Splitting)
- `np.hsplit(data, N)`: 水平分割 (按列切分)，要求列数能被 N 整除。
- `np.vsplit(data, N)`: 垂直分割 (按行切分)，要求行数能被 N 整除。

#### 合并 (Stacking)
- `np.vstack([a, b])`: 垂直堆叠 (增加行数)，要求列数相同。
- `np.hstack([a, b])`: 水平堆叠 (增加列数)，要求行数相同。
- `np.stack([a, b], axis=0)`: 沿新轴堆叠 (增加维度)。

> [!EXAMPLE] 作业案例 (Ex 1.02 & 1.03)
> 重构数据流程：
> 1. `thirds = np.hsplit(dataset, 3)` (分成左中右三份)
> 2. `halves = np.vsplit(thirds[0], 2)` (将左边那份再分成上下两份)
> 3. `restored = np.vstack(halves)` (恢复左边那份)
> 4. `full = np.hstack([restored, thirds[1], thirds[2]])` (完全恢复原数据)

### 4.4 重塑 (Reshaping)
改变数组形状，但元素总数不变。
- `data.reshape(rows, cols)`
- **使用 `-1` **: 让 NumPy 自动计算该维度的大小。
  - `data.reshape(1, -1)`: 展平为单行。
  - `data.reshape(-1, 2)`: 变为多行 2 列。

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


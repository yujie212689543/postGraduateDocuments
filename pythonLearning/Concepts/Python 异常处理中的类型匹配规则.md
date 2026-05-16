## 1. 例子中发生了什么？
代码是这样的：

```python

try:
    f = open("C:/code/study.txt", "r")   # 文件不存在
except NameError as e:
    print('文件不存在')
```    

- 因为 `C:/code/study.txt` 这个文件不存在，`open()` 会抛出一个 ** `FileNotFoundError` ** 异常。
- 但是 `except` 后面写的是 ** `NameError` **（变量未定义的错误）。
- `FileNotFoundError` 和 `NameError` 是两种完全不同的异常类型，它们之间没有继承关系。
- 所以 Python 认为这个 `except` 不适用于当前发生的异常，于是**忽略这个 `except` **，继续向上层抛出异常，最终导致程序终止并显示红色的错误信息（你截图中的 `Traceback ... FileNotFoundError`）。

---

## 2. “异常类型不一致，无法捕获”是什么意思？

- 每个异常都有一个具体的类型，比如：
    
    - `FileNotFoundError`（文件不存在）
    - `NameError`（变量未定义）
    - `ZeroDivisionError`（除以零）
    - `ValueError`（值错误）
        
- `try` 块中发生的异常类型，必须和 `except` 后面写的类型**相同或者是它的子类**，才能被那个 `except` 捕获。
    
**类比**：  
你准备了一个专门抓“老鼠”的笼子（`except NameError`），结果来了一只“猫”（`FileNotFoundError`）。笼子不认识猫，当然抓不住，猫就会继续乱跑（程序崩溃）。

---

## 3. 正确的写法应该是什么？

既然要捕获“文件不存在”这个异常，应该使用：

```python

try:
    f = open("C:/code/study.txt", "r")
except FileNotFoundError as e:
    print('文件不存在')
```
或者更通用一点，捕获所有与文件/IO 相关的异常（`OSError` 是 `FileNotFoundError` 的父类）：

```python

except OSError as e:
    print('文件操作出错，可能是不存在或权限问题')
```

---

## 4. “同样的代码却无法捕获”是什么意思？

截图中说的“同样的代码”可能是指：**在别的场景下，同样的 `try-except` 结构能正常工作**，但在这里不行。  
这是因为**之前可能发生的异常正好是 `NameError` **（比如变量名写错），而现在发生的是 `FileNotFoundError`。  
代码没有变，但**实际出现的异常类型变了**，所以原来的 `except` 不再适用。

这就是为什么写异常处理时，要**明确知道可能发生什么异常**，并写出对应的类型。

---

## 5. 怎么知道一个操作会抛出哪些异常？

- 查文档：比如 `open()` 的文档会说明可能抛出 `FileNotFoundError`、`PermissionError` 等。
    
- 或者先不写 `try`，让程序崩溃，看错误信息里写的异常类型是什么，然后把它写到 `except` 后面。
    

---

## 总结一句话

> ** `except` 只能捕获与它指定的异常类型匹配（相同或是父类）的异常；类型不匹配时，`except` 被忽略，程序照样报错。**  
> 你截图中的例子就是用 `NameError` 去捕获 `FileNotFoundError`，所以失败了。
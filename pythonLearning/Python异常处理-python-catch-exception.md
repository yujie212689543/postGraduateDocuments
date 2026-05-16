
> python学习之旅(七)
> 
> 学习汇总入口[【Python】学习汇总(3万字+思维导图)](https://blog.csdn.net/m0_66570338/article/details/128714062)
> 
> 笔记PDF下载：[知识笔记：Python异常处理(七)](https://download.csdn.net/download/m0_66570338/90058591)
> 
> 文末附带全文概览思维导图
> 
> 写作不易，如果您觉得写的不错，欢迎给博主来一波点赞、收藏~让博主更有动力吧！

### 一.什么是异常

> 程序运行的过程中出现了错误

-   定义：在程序运行中,检测到一个错误，程序中止运行并且出现了一些错误的提示,也称作`BUG`
    
-   例如：读取一个不存在的文件`f = open("C:/code/观止.txt", "r")`
    

![[63a1b9381a05d1a48b4895db28aefaa6.png]]

### 二.为什么要捕获异常

> 避免程序中止，提前准备处理可能出现的异常

-   在真实工作中, 我们肯定不能因为一个小的BUG就让整个程序全部奔溃，而是对BUG进行提醒, 整个程序继续运行

### 三.如何捕获异常

> 在可能出现异常的地方,做好提前准备,当真的出现异常的时候,可以有后续手段。

#### (1) 捕获常规异常

-   基本语法：

```python
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码
    

```

<mark class="eme-highlight eme-h-pink" data-id="a57615a1-3f65-4030-b859-6a5dacf9541a">未发生错误try全部代码都会执行</mark>
<mark class="eme-highlight eme-h-pink" data-id="ab2dd955-8de5-4f2b-a62a-3ab40b385728">未发生错误不会执行except中的代码</mark>
<mark class="eme-highlight eme-h-pink" data-id="7eb35fa9-58e7-4f8a-82cc-4e0c376d261a">发生错误try中只会执行到报错行为止的代码</mark>
<mark class="eme-highlight eme-h-pink" data-id="7a627974-9dcf-4afc-810c-ecd786f99f08">发生错误会执行except中的代码</mark>


-   使用示例:
    
    -   首次执行,文件不存在,程序未报错中止，而是转而执行`except`中代码，创建文件
    
    ```python
    try:
        print("r模式打开") # 执行
        f = open("C:/code/观止.txt", "r") # 报错
        print("r模式打开") # 不执行
    except:
        print("w模式打开") # 执行
        f = open("C:/code/观止.txt", "w") # 执行
        print("w模式打开") # 执行
    ```
    

![[4e3b929dff280dc5d0f6123563600bbc.png]]

-   第二次执行，文件存在，程序无异常，只执行try中代码

```python
try:
    print("r模式打开") # 执行
    f = open("C:/code/观止.txt", "r") # 执行
    print("r模式打开") # 执行
except:
    print("w模式打开") # 不执行
    f = open("C:/code/观止.txt", "w") # 不执行
    print("w模式打开") # 不执行
```

![[aed85eb65a9cd7048caf65c4457a3469.png]]

#### (2) 捕获特定异常

-   <mark class="eme-highlight eme-h-pink" data-id="35fc3cc4-4317-4e72-9daa-1cef592ecde1">如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常。</mark>
-   基本语法：

```python
try:
    可能发生错误的代码
except 待捕获异常名 as 别名:
    如果出现异常执行的代码
```

-   例如:
    
    -   捕获未定义变量产生的错误
    
    ```python
    try:
        print(name) # 未定义变量，报错
    except NameError as e:
        print('name变量名称未定义错误')
    ```
    

![[36da20e61a303a750232248178911d9d.png]]

-   同样的代码却无法捕获处理找不到文件异常

```python
try:
    f = open("C:/code/study.txt", "r") # 文件不存在，报错
except NameError as e:
    print('文件不存在')			
```

![[cb865cb859fc61a1a4617ced32e19f26.png]]

- 小知识点： [[Python 异常处理中的类型匹配规则]]

#### (3) 捕获多个异常

-   格式一：当待捕获异常名为`Exception`可以捕获所有类型异常，作用与(1)一致
    
    -   例如：
    
    ```python
    try:
        f = open("C:/code/study.txt", "r")
    except Exception as e:
        print('文件不存在')
    ```
    

![[e193cdfaaf772c036202162f41df4d83.png]]

-   <mark class="eme-highlight eme-h-pink" data-id="5f5876bf-3af1-404c-be9c-3f9104cb6110">格式二:把要捕获的异常类型的名字，放到except 后，并使用元组的方式进行书写。</mark>
    
-   基本格式：

<mark class="eme-highlight eme-h-pink" data-id="ae19f97c-a220-401f-a2e2-27af1030511d">- 场景：你想对几种已知的、可预见的异常做统一处理</mark>

```python
try:
    可能发生错误的代码
except (异常名1,异常名2) as 别名:
    如果出现异常执行的代码
```

-   使用示例:

```python
try:
    with open("config.txt") as f:
        data = f.read()
except (FileNotFoundError, PermissionError) as e:
    print(f"无法读取配置文件：{e}")
    # 然后使用默认配置
```

 为什么不用 `except Exception`？

`except Exception` 会捕获**所有**继承自 `Exception` 的异常（几乎你遇到的所有异常）。这很方便，但也很危险：

- 它会掩盖**编程错误**，比如变量名拼写错误、传入 `None` 导致属性错误等。
    
- 当你看到程序没有崩溃而是打印了“文件不存在”，你会误以为是文件问题，实际却是代码逻辑错误，导致浪费大量调试时间。
    
**工程原则**：**只捕获你预期会发生的异常，让其他异常自然崩溃**（或者记录日志后重新抛出）。这样程序出问题时，你能立刻看到真实的错误堆栈。


#### (4) 其他用法

##### (4.1) 打印异常 信息

-   <mark class="eme-highlight eme-h-pink" data-id="f85c58d9-7a1a-43e6-b98a-edce41fcbb7f">异常描述信息存贮在别名中，可以通过打印别名获取</mark>
-   使用示例：

```python
try:
    print(num) # 未定义，报错
except (NameError, ZeroDivisionError) as e:
    print(e) # 打印 name 'num' is not defined
```

![[e8d69227b3f3ef7ef02730bd96cb8201.png]]

##### (4.2) 异常else

-   else表示的是如果没有异常要执行的代码。
    
-   使用示例：
    
    -   出现异常，打印结果与(4.2)一致
    
    ```python
    try:
        print(num) # 未定义，报错
    except (NameError, ZeroDivisionError) as e:
        print(e) # 打印 name 'num' is not defined
    else:
        print("无异常") # 有异常，不执行
    ```
    
    -   无异常

```python
try:
    print("正常") # 不报错
except (NameError, ZeroDivisionError) as e:
    print(e) # 不执行
else:
    print("无异常") # 执行
```

![[5a67c3535ec235f9c6c2d76bbc82bd27.png]]

##### (4.3) 异常finally

-   finally表示的是无论是否异常都要执行的代码
    
-   使用示例：
    
    -   之前提过，如果open文件却一直未close且程序未中止，将一直占用文件无法操作
    -   如果打开文件后发生异常，未close也将导致一直占用，因此可选择在finally中close
    
    ```python
    global f
    try:
        f = open("C:/code/aaa.txt", "r")
    except Exception as e:
        print(e)  
    finally:
        f.close() # 一定会执行close操作
    ```
    



### 四. 异常的 传递

> 异常是具有传递性的(向上一级抛出)

-   当函数调用链中出现异常，如果所有函数都没有捕获异常的时候, 程序就会报错

![[262241a8439a390c4b4610476fc8ecec.png]]

-   利用异常具有传递性的特点, 当我们想要保证程序不会因为异常崩溃的时候, 就可以在主函数中设置异常捕获, 由于无论在整个程序哪里发生异常, 最终都会传递到主函数中, 这样就可以确保所有的异常都会被统一捕获

### 五.全文概览

![[cac9d2c3f3cd28acc42f77d48c2d058c.png]]
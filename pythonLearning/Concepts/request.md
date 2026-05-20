## 核心技巧

以后遇到任何 `response.json()` 拿到的数据，三步走：

```python
print(type(数据))        # dict？list？str？
print(数据.keys())       # 如果是 dict，有哪些 key？
print(len(数据))         # 如果是 list，有多少条？
```
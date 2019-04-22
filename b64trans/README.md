## base64码表转换

用来将非正常base64转换表编码的信息转换为正确编码的信息。

#### 使用方法

修改`yourList`为你遇到的非正常码表，运行即可。

#### Example

假设遇到的异常码表为`IJLMNOPKABDEFGHCQRTUVWXSYZbcdefa45789+/6ghjklmnioprstuvqwxz0123y`

运行：
```
$ python3 trans.py
RVYtG85NQ9OPHU4uQ8AuFM+MHVVrFMJMR8FuF8WJQ8Y= # 输入异常码表编码的串
RUY0NjhEQkFGOTg1QjI1MDlDOUUyMDBDRjM1MjVBQjY= # 恢复正常编码
```
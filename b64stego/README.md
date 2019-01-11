## base64隐写工具

根据[base64](https://en.wikipedia.org/wiki/Base64)的填充规则，向填充位写入或从中读出隐藏信息。

>deStego(stegoFile)

从隐写文件stegoFile提取字符串

>enStego(sourceFile,setgoFile,message)

根据源文件sourceFile隐写字符串message,base64保存到stegoFile

~~如果遇到最后一个字符显示不正常，建议在`stego.txt`尾添加空格。~~

想了想让用户做额外操作是不人道的，修改了代码，应该不会遇到显示不正常的问题了。


##### Example:
```
In [249]: %run b64EnStego.py
0101001101101001011011010111000001101100011001010100110101100101011100110111001101100001011001110110010100001010
Remaining 0 bits!

In [250]: %run b64DeStego.py
SimpleMessage
```

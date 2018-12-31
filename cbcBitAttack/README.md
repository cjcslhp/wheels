## cbc_bit_attack

根据[CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operationer_mode_of_operation)的工作模式，在已知一个分组明文和密文的情况下，可以修改上一分组密文使得此分组正常解密后明文为任意值。

```
def cbc_bit_attack_mul(c:原始密文(base64编码),m:明文,position:改变的位,target:改变的内容)
    return r生成密文:(base64编码)
```
##### Example:

```
$./cbc_bit_attack.py
c(base64):bMPWOsg+YH0eSwchPY6HTEvf3ESETSrEQ3/M1d0lUm0=
m:token=5t43g5g2j1;admin=0;group=0
position(exp: 1 2 3):31
target(exp: A B C)1
bMPWOsg+YH0eSwchPY6HTUvf3ESETSrEQ3/M1d0lUm0=
```
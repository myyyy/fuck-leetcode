> [字符串匹配的KMP算法](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)

**3个关键点**
1. 匹配表 p （可以用list）
2. 标记匹配项->匹配值 （从1->n 在表p填写没匹配上时写0，匹配成功依次+1）
3. 移动位数 = 已匹配的字符数个数 - 对应的部分匹配值
![picture 1](../images/3432a114976554ddf4d83feaf77f0b90af675f4ecd0d37f87ccffc60825a726c.png)  

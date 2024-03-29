### 大O表示法

假设列表包含n个元素，简单查找需要检查每个元素，因此需要n次操作，大O表示法----O(n)

大O表示法指的并非以秒为单位的速度，它指出了算法运行时间的增速

大O表示法指出了最糟糕情况下的运行时间

一些常见的大O运行时间
* O(logn)，也叫对数时间，这样的算法包括二分查找法
* O(n)，也叫线性时间，这样的算法包括简单查找
* O(n * logn)，这样的算法包括快速排序---一种速度较快的排序算法
* O(n^2)，选择排序---一种速度较慢的排序算法
* O(n!)


大O表示法主要启示：
* 算法的速度指的并非时间，而是操作数的增速
* 谈论算法的速度时，我们说的随着输入的增加，其运行时间将以什么样的速度增加
* 算法的运行时间用大O表示法表示
* O(logn)比O(n)快，当需要搜索的元素越多时，前者比后者快的越多
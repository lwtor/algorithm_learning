### 排序算法
#### 常见的排序算法
- 冒泡排序
- 插入排序
- 选择排序
- 归并排序
- 快速排序
- 计数排序
- 基数排序
- 桶排序

#### 衡量性能的标准
- 最好情况、最坏情况、平均情况的时间复杂度
- 时间复杂度的系数、常数、低阶
- 比较次数和交换（或移动）次数
- 是否为 `原地排序` ，即空间复杂度为 `O(1)`
-  `稳定性`  （如果一个序列中包含相同的元素，在排序之后如果相同的元素的位置关系没有发生改变，则该排序算法为稳定的排序算法）

#### 有序度 和 逆序度
数组中具有有序关系的元素对的个数。  
既 当 i < j 时，如果 a[i] < a[j] ，则i，j为有序元素对。  

例：2, 4, 3, 1, 5, 6 这个数组的有序度为11。  
(2,4), (2,3), (2,5), (2,6)  
(4,5), (4,6)  
(3,5), (3,6)  
(1,5), (1,6)  
(5,6)  

完全有序的数组，如 1, 2, 3, 4, 5 ，的有序度为10。也叫 `满有序度`  
倒序排列的数组，如 5, 4, 3, 2, 1 ，的有序度为0。  
所以一个包含 n 个元素的数组，满有序度为 `(n * n - 1) / 2`  

逆序度的定义与有序度相反。  
既 当 i < j 时，如果 a[i] > a[j] ，则i，j为逆序元素对。  

数组 1, 2, 3, 4, 5 ，的逆序度为10。  
数组 5, 4, 3, 2, 1 ，的逆序度为0。  

所以可以得出 逆序度 = 满有序度 - 有序度  

所以在排序过程中，其实就是增加有序度，减少逆序度。  

#### 问题
- **为什么插入排序比冒泡排序好**  
  虽然两个排序算法的时间复杂度都是 **$O(n^2)$** ，都是原地排序算法，且都移动元素的次数都是原始序列的逆序度。  
  从代码上看，由于冒泡排序需要交换两个元素的位置，需要3个赋值语句来实现，而插入排序只需要1个。  
  所以插入排序的执行效率比冒泡排序高。

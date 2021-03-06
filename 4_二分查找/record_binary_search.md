### 二分查找
对于有序序列，每次判断中间值与目标数值是否相等。如果大于目标数值，表示目标数值可能在左半边的序列中，则对左半边的序列进行二分查找。否则表示目标数值可能在右半边的序列中，则对右边的序列进行二分查找。不断重复进行查找，直到找到目标数值或者查找失败即目标数值不存在序列中。  

**时间复杂度**  
被查找区间的大小变化：n, n/2, n/4, n/8, .. , n/2^k  
时间复杂度： **$O(logn)$**

**限制：**  
数组，由于需要每次找到中间值进行比较，所以需要使用数组来存储数据  
有序序列  
数据量：太小了，无法发挥二分查找的优势；太大了有序需要使用数组，所以会占据大量的连续内存

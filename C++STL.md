# Standard Templete Libary (STL)
## Table of Contents
- 1. Vector
- 2. Map
- 3. Set
- 4. Stack
- 5. Queue
- 6. Priority_Queue
- 7. Deque
- 8. Array

## Vector
Vector คือ Data structure ที่สามารถขยายขนาดได้ จะใช้ต้อง `#include <vector>` ก่อน ประกาศได้ดังนี้
```
vector<type> name;
```

```cpp
vector<int> v1;
vector<int> v2(5); // กําหนดขนาดเวกเตอร์เป็น 5
vector<int> v3(5, 10) // กําหนดขนาดเวกเตอร์เป็น 5 เซตให้ทุกตัวเป็น 10
vector<int> v4[3] // กําหนดเป็น vector 2 มิติที่มีขนาด 3 
```
การเพิ่มค่าลบค่าทําได้ดังนี้
```cpp
// add element
v1.push_back(5);
v2[0] = 5;
// delete element from back
v3.pop_back();
```
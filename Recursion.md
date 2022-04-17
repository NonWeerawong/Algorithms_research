# Recursion in C++
ความหมายของ recursion คือฟังชันที่มีการเรียกตัวเองซํ้า คล้ายฟังก์ชันเวียนเกิด

- ตัวอย่าง recursion ที่พบเจอบ่อยเช่น หา แฟคทอเรียล
```cpp
int factorial(int n) {
    if (n == 0) return 1;
    return n * factorial(n - 1);
}
```

ขั้นตอนที่เกิดขึ้นแสดงได้ดังนี้ สมมุติให้ factorial(5)
1. `5 * factorial(4)`
2. `5 * (4 * factorial(3))`
3. `5 * (4 * (3 * factorial(2)))`
4. `5 * (4 * (3 * (2 * factorial(1))))`
5. `5 * (4 * (3 * (2 * (1 * factorial(0)))))`
6. `5 * (4 * (3 * (2 * (1 * 1))))`
7. `5 * (4 * (3 * (2 * 1))`
8. `5 * (4 * (3 * 2)`
8. `5 * (4 * 6)`
9. `5 * 24`
10. `120`

- เราสามารถใช้ Recursive แทนการลูปได้เช่น
การปริ้น `ๅ` ถึง `n` ถ้าใช้ for loop เขียนได้ดังนี้
```cpp
for (int i = 1; i <= n; i++) 
	cout << i << " ";
```

เขียนโดยใช้ Recursive
```cpp
void print(int n) {
    if (n == 0)
        return;
    print(n - 1);
    cout << n << " ";
}
```

จาก `n` ถึง `1`

```cpp
void print(int n) {
    if (n == 0)
        return
    cout << n << " ";
    print(n - 1);
}
```
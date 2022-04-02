


# C/C++ Notes
# Table of Contents
1. Getting Started
2. Types Operators and Expressions
3. Input / Output
4. Control Flow
5. Array and String
6. Function
7. Pointers, References, and Dynamic Allocation
8. Struct
9. Linked list
10. Class and Object	
 ## Getting Started
 ## Types Operators and Expressions
 ### Types
 - Intergers `int` `short` `long long` `char` `bool`
 - Floating point `float` `double` `long double`
 - characters `char` 

Size of each type in Byte
| type | byte | range | format |
|------|----|---------|--------| 
| char | 1 | -128 to 127 | %c |
| unsigned char | 1 | 0 to 255 | %c |
| short | 2 | -32,768 to 32767 | %d |
| unsigned short | 2 | 0 to 65535 | %u |
| int | 4 | 2,147,483,648 to 2,147,483,647 | %d |
| unsigned int | 4 | 0 to 4,294,967,295 | %d |
| float | 4 | 1.2E-38 to 3.4E+38 | %f |
| double | 8 | 2.3E-308 to 1.7E+308 | %lf |
| long double | 10 | 3.4E-4932 to 1.1E+4932 | %Lf |
| long long | 8 | -9223372036854775808 to 9223372036854775807 | %ld |
| unsigned long long | 8 | 0 to 18446744073709551615 | %lu |
 ### Operators
**C++ Operators Precedence**
 ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6ab22d69-82f5-4797-ac13-bee5b05cfaeb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220401T212406Z&X-Amz-Expires=86400&X-Amz-Signature=b15f20ccb7b7a3f60da1c653a018095e1ecdbbdb5f32df4b578017b8e5addcb2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject =1000x)
  
  ## Input / Output
  จะใช้คําสั่งได้ต้อง Include Libary มาก่อนโดยใน C กับ C++ จะใช้ต่างกันโดย
  In C:
```c
  #include <stdio.h>
  ```
  In C++:
```c++
  #include <iostream>
  #include <cstdio> // same thing as <stdio.h> in C
  using namespace std;
  ```
  คําสั่งที่ใช้รับ Input
```
  fgets();
  gets() // not safe to use
  scanf();
  cin >> x;
  ```
  คําสั่งที่ใช้ print ออกไปหน้าจอ
```
  printf();
  cout << x;
  ```

## Control flow
### If-else
```
if (condition1) {
  // do something
} else if (condition2) {
  // do something
} else {
 // do something
}
```


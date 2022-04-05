


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
| type             | byte | range                                    | format |
|--------------------|----|---------------------------------------------|-----| 
| char               | 1  | -128 to 127                                 | %c  |
| unsigned char      | 1  | 0 to 255                                    | %c  |
| short              | 2  | -32,768 to 32767                            | %d  |
| unsigned short     | 2  | 0 to 65535                                  | %u  |
| int                | 4  | 2,147,483,648 to 2,147,483,647              | %d  |
| unsigned int       | 4  | 0 to 4,294,967,295                          | %d  |
| float              | 4  | 1.2E-38 to 3.4E+38                          | %f  |
| double             | 8  | 2.3E-308 to 1.7E+308                        | %lf |
| long double        | 10 | 3.4E-4932 to 1.1E+4932                      | %Lf |
| long long          | 8  | -9223372036854775808 to 9223372036854775807 | %ld |
| unsigned long long | 8  | 0 to 18446744073709551615                   | %lu |
 ### Operators
**C++ Operators Precedence**
 ![](/images/Precedence)
  
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
### Conditional
**If-Else, Else if**
```
if (condition1) {
  // statements
} else if (condition2) {
  // statements
} else {
  // statements
}
```
Example: โปรแกรมคํานวณหาเกรด
```cpp
#include <iostream>
using namespace std;

int main() {
  int score;
  char grade;
  cin >> score;
  if (score >= 80)
    grade = 'A';
  else if (score >= 75)
    grade = 'B+'
  else if (score >= 70)
    grade = 'B'
  else if (score >= 65)
    grade = 'C+'
  else if (score >= 60)
    grade = 'C'
  else if (score >= 55)
    grade = 'D+'
  else if (score >= 50)
    grade = 'D'
  else
    grade = 'F'

  cout << grade << endl;
}
```
**switch-case**
มีได้หลาย case ถ้าไม่ตรงกับ case ไหนเลยให้ทําคําสั่งใน default
```
switch (var) {
  case 1:
    // statements
	break;
  case 2:
	// ..
  default:
	// statements
}
```
Example : โปรแกรมเครื่องคิดเลข
```cpp
#include <iostream>
using namespace std;

int main() {
  int num1, num2, result;
  char op;
  cin >> num1 >> op >> num2;
  switch (op) {
    case '+':
	  result = num1 + num2;
	  break;
    case '-':
      result = num1 - num2;
      break;
    case '*':
	  result = num1 * num2;
      break;
    case '/':
      result = num1 / num2;
      break;
    default:
      result = 0;
      break;
  }
  cout << result << endl;
}
```
### Loops
ข้อดีของลูปคือลดการเขียนโค้ดซํ้าๆ ซึ่งใน C++ ใช้ได้หลายแบบ ดังนี้

**while**
```
while (condition) {
  // statements
}
```
**do-while**
```
do {
  // statements
} while (condition)
```
**for-loop**
```
for (init; condition; end) {
  // statements
}
```
**for-each**
```
for (init : array or vector) {
  // statements
}
```

Example : ใช้ลูปปริ้นสูตรคูณแม่ 12
```cpp
#include <cstdio>

int main() {
  for (int i = 1; i <= 12; i++)
    printf("12 * %d = %d", i, 12 * i);
}
```

### Array and String
Array ใช้เก็บข้อมูลประเภทเดียวกันหลายๆตัว
```cpp : Array 1D
int arr[5] = {1, 2, 3, 4, 5}; // index of array start with 0
int zero[10] = {}; // initialize all data to 0
char s[3] = {'a', 'b', 'c'};
```

String ก็คือ Character array 
```cpp
char str[6] = {'H', 'E', 'L', 'L', 'O', '\0'};
cout << str << endl;
// output : HELLO
```

Array 2D
```cpp
int arr[5][5] = 
{
	{1, 2, 3, 4, 5},
	{6, 7, 8, 9, 0},
	{1, 3, 5, 7 ,9},
	{0, 1, 5, 3, 2},
	{1, 1, 5, 5, 2}

}
```

เวลาจะเรียกใช้ ให้ใช้ nested loop
```cpp
for (int i = 0; i < 5; i++) {
  for (int j = 0; j < 5; j++) {
    cout << arr[i][j] << " ";
  }
  cout << "\n";
}
```

### Function
มีประโยชน์เพื่อช่วยลดการเขียนโค้ดซํ้าโดยโค้ดในใช้บ่อยก็สร้างเป็นฟังก์ชั่นขึ้นมา
- Type : `void` คือไม่ return อะไร ถ้าไม่ใช่ก็คือมีการ return
- Paremeter : มีหรือไม่มีก็ได้
- Function Name

ตัวอย่างการประกาศ function คือ
- เขียนเป็นฟังก์ชันเลย
```
type FunctionName(Parameter1, Parameter2, ...) {
	// statements
}
```
- หรือประกาศเป็น **Function Prototype** แล้วค่อยเขียนทีหลัง
```
type FunctionName(Parameter1, Parameter2, ...);
```

### Pointer References and Dynamic Allocation
**Pointer** คือตัวแปรที่ใช้เก็บ Address ของข้อมุล วิธีการประกาศใช้ `*` เขียนนําหน้าชื่อตัวแปรใช้ `&`เพื่อเรียกตําแหน่งของข้อมูลตัวแปร pointer จะชี้ไปที่ตําแหน่งของ data 
```cpp
int data = 5;
int *ptr = &data;
```
ถ้าเปลี่ยนค่า `*ptr` ตัวแปร `data` ก็จะเปลี่ยนด้วย
```cpp
*ptr = 10;
cout << data << endl;
// output : data = 10
```

จะเก็บตําแหน่งของ Pointer ให้ใช้ Pointer to Pointer `**ptr`
```cpp
int **ptr2 = &ptr;
```

### Struct

### Linked list
การเก็บข้อมูลที่เชื่อมติดกันจะเรียกได้ต้องเรียกจาก หัว ไป หาง เท่านั้น
![](images/LinkedList)
- เราสามารถกําหนดโหนดที่ใช้เก็บข้อมูลได้โดยใช้ Struct
```cpp
struct Node {
  int val; // for storing data
  struct *Node next; // access next node
} 
```
- จะนําข้อมูลจาก array มาเป็น linked list ทําได้ดังนี้
```cpp
void insertNode(struct Node **head, int val) {
  struct Node *tail;
  struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->val = val;
  newNode->next = NULL;
  if (*head == NULL) {
    *head = newNode;
  } 
  else {
    tail->next = newNode;
  }
  tail = newNode;
}
```

- Sorted Linked list 
เรียงจากน้อยไปมาก
```cpp
void insertOrderedList(struct Node **head, int val) {
  struct Node *tmp = *head;
  struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
  newNode->val = val;
  newNode->next = NULL;
  if (*head == NULL) {
    *head = newNode;
  }
  else if (newNode->val <= (*head)->val) {
    newNode->next = *head;
    *head = newNode;
  }
  else {
    while (tmp->next != NULL && (tmp->next)->val < newNode->val) {
      tmp = tmp->next;
    }
    newNode->next = tmp->next;
    tmp->next = newNode;
  }
}
```
- Delete Node
```cpp
void deleteNode(struct Node **Head, int val) {
  struct Node *tmp = *head, *prev;
  if (tmp != NULL && tmp->val == val) {
    *head = tmp->next;
    free(tmp);
  }
  while (tmp != NULL && tmp->val != val) {
    prev = tmp;
    tmp = tmp->next;
  }
  if (tmp != NULL) {
    prev->next = tmp->next;
    free(tmp);
  }
}

```

- Print Linked list
```cpp
void printList(struct Node *tmp) {
  for (; tmp != NULL; tmp = tmp->next) {
    cout << tmp->data << " ";
  }
  cout << "\n";
}
```

- In main
```cpp
int main() {
  struct Node *pList1, *pList2;
  int arr[5] = {2, 3, 1, 5, 4};
  for (int i = 0; i < 5; i++)
    insertNode(&pList1, arr[i]);
  for (int i = 0; i < 5; i++)
    insertOrderedList(&pList2, arr[i]);

  printList(pList1);
  printList(pList2);
}
```
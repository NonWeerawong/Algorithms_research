# java

01418211 Software Construction class's note by Weerawong Vonggatunyu.

## Table of Contents

- 1 Instrallation
- 2 Introduction to Java
  - 2.1 Data Type, Statement, Expression
  - 2.2 Input/Output
- 3 ipsum

## Instrallation

- [Java JDK 17 (LTS)](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloa)
- [Intellij IDEA](https://www.jetbrains.com/idea/download/) (Communitiy version)

## Run java file

- use command `javac file.java` to complie `.java` file you will got `file.class` as a result
- use command `java file.class` to run `.class` file your code result will appear in terminal

## Get to know about Java

Java has a main concept which is _write once run everywhere_ created by a guy name James Gosling in 1991. The original name was 'Oak' and was rename to 'java' in 1994 which is a name of coffee

### Sample code

```java
public class main {
  public static void main(String[] args) {
    System.out.println("Hello World");
  }
}
```

In java class name need to match with file name for example code above has class name `main` so in file need to name `main.java` as well

## Data Type, Statement, Expression

### Data Type

Java is a strongly typed language and divided into two categories

- Primitive Types
  - boolean
  - numeric
    - interger -> `byte`, `short` `int` `long` `char`
    - floating point `float` `double`
- Reference Types
  - class
  - interface
  - Array
  - String

> note: if the type start with uppercase e.g. `Char` it is a reference not primitive

```java
public class Type {
  public static void main(String[] args) {
    int x = 0; // ok
    int y = 0.0; // error because 0.0 is double can't assign to int
    double k = 0; // ok because int is subtype of  double
    float f = 2.5; // error because 2.5 is double can't assing to float
    float f = 2.5f; // ok because `f` behind number mean we convert it into float
    double d = 2.5;
    float dd = d/2; // error because `d/2` return double, can't assing to float
  }
}
```
**type casting**

```java
public class Type {
  public static void main(String[] args) {
    // convert double to integer
    int x = (int)2.5; // 2
  }
}
```



### Statement 
- Each statement usually ends with semicolon `;`
- such as variable declarations and assignments

### Expression
- Everything is a expression if it return a value back

```java
public class Example {
  public static void main(String[] args) {
    int i, j; // statement
    j = 5; // both expression and statement
    j += (i = (j-3)); // i = 2 -> j = 7
    System.out.println("j = " + j); // 7
  }
}
```

## Input/Output

```java
import java.util.Scanner; // use to get input from stdin

public class main {
  public static void main(String[] args) {
    // input
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(); // take input as Integer
    // output
    System.out.println(n);
  }
}
```

## Inheritance

use keyword `extends` to inherit from another class.

```java
public static class Person {
  private String name;
  private int age;
  Person(String name, int age) {
    this.name = name;
    this.age = age;
  }
  String getName() {
    return this.name;
  }
  int getAge() {
    return this.age;
  }
  String greet() {
    return "Hello my name is " + this.name +
           " I'm " + this.age + " years old";
  }
}

public static class Student extends Person {
  private int score;
  Student(String name, int age) {
    super(name, age);
    this.score = 0;
  }
  void setScore(int score) {
    // score between 0-100
    this.score = Math.max(Math.min(this.score + score, 100), 0);
  }
}

public static void main(String[] args) {
  Student s = new Student("Non", 19);
  System.out.println(s.greet());
}
```

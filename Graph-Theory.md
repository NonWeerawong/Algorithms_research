# Graph theory
## Table of Contents
1 Graph
- 1.1  Graph definitions
- 1.2 Special Simple graphs
	- 1.2.1 Line Graph
	- 1.2.2 Cycle Graph
	- 1.2.3 Wheel Graph
	- 1.2.4 Complete Graph
	- 1.2.5 Bipartite Graph
	- 1.2.6 Complete Bipartite Graph
- 1.3 Graph Representations
	- 1.3.1 Adjacency Matrices
	- 1.3.2 Adjacency List
- 1.4 Paths Cycles and Connectivity
	- 1.4.1 Paths
	- 1.4.2 Cycles
	- 1.4.3 Connectivity
	- 1.4.4 Euler Paths and Cycles
	- 1.4.5 Hamilton Paths and Cycles
- 1.5 Graph Application
	- 1.5.1 Planar Graph
	- 1.5.2 Graph Coloring
	- 1.5.3 Graph Traversal
2. Trees
- 2.1 Introduction to Trees
- 2.2 Properties of Trees
- 2.3 Application of Trees
	- 2.3.1 Binary Search Trees
	- 2.3.2 Huffman Coding
	- 2.3.3 Game Trees
- 2.4 Tree Traversal
- 2.5 Spanning Trees


## Graphs Definitions
ประเภทของกราฟ 
- Undirected graph กราฟไร้ทิศทาง
- Directed graph กราฟมีทิศทาง
- Weighted graph การฟมีนํ้าหนักจะเป็น directed หรือ undirected ก็ได้

ลักษณะของกราฟ
- Simple graph -> no self loop and muti edges
- Mutigraph -> have muti edges
- pseudograph -> have self loop or muti edges

คําศัพท์ที่เจอในกราฟ
- vertex or node -> จุดยอด
- edge -> เส้นเชื่อมระหว่างจุดยอด
- degree -> จํานวน edge ที่เชื่อมกับจุดยอดเขียนได้ด้วย $deg(v)$
	vertex of degree zero is called `isolated`
	vertex of degree one is called `pendant`
	- degree of undirected graph นับตามเส้นที่เชื่อมโหนดได้เลย
	- degree of directed  graph แยกเป็น 2 แบบคือ
		- in-degree เขียนด้วย $`deg^-(v)`$ นับจํานวนที่ลูกศรชี้เข้าหาตัวเอง
		- out-degree เขียนด้วย $`deg^+(v)`$ นับจํานวนที่ลูกศรชี้ออกตัวเอง
	$$`\sum_{v\in{V}}{deg^-(v)}=\sum_{v\in{V}}{deg^+(v)}=|E|`$$
	
	The Handshaking theorem
	ทฎษฤีที่ใช้หาจํานวนดีกรีทั้งหมดของ undirected graph
	$$`2|E|=\sum_{v\in{V}}{deg(v)}`$$
	จะเห็นว่ากราฟจะเป็นจริงได้ต้องมี ดีกรีไม่เป็นคู่ทั้งหมด ก็ต้องมีโหนดคู่ตัวมีดีกรีเป็นคี่
	
- adjacent โหนดเชื่อมติดกัน
- neighborhood โหนดเชื่อมติดกัน เขียนได้เป็น $`N(u)`$

## Special Simple Graphs
- Line Graph
	กราฟเส้น $n$ node มี $n-1$ edge
- Cycle Graph
	กราฟวงกลม $C_n$ โดยที่ $n>=3$ หลักการคือเริ่มจากโหนด u แล้วเดินไปยังโหนดที่ติดกันของ u แล้วกลับมาจบทีได้
- Wheel Graph
	กราฟวงล้อ เพิ่มโหนดมา 1 โหนดจากกราฟวงกลมทําให้กราฟเชื่อมถึงกันหมด
- Complete Graph 
	มี edge เชื่อมต่อครบทุกโหนด เขียนแทนด้วย $K_n$ มีจํานวน edge $$\sum^{n-1}_{i=1}i={\frac{n(n-1)}{2}}\space edges$$ 
- Bipartite Graph
	กราฟที่แบ่งเป็นสองส่วน โดยการที่จะเป็น bipartite graph ได้ต้องไม่มีกราฟที่เป็น $C_3$
- Complete Bipartite Graph
	กราฟสองส่วนสมบูรณ์ $K_{m,n}$ กราฟที่แบ่งเป็นสองส่วนแต่ละโหนดเชื่อมถึงกันหมด

## Graph Representations
- Adjacency Matrices
<<<<<<< HEAD
	ใน c++ คือการกําหนด Array 2d ขนาด `N*N` โดย N จํานวนโหนดของกราฟทั้งหมด
	```cpp
	int adj[N][N];
	// set all element in adj equal to 0

	// to input a node in to graph you do like so.
	adj[u][v] = 1;
	adj[v][u] = 1; // remove this line if a graph is an directed graph
	// if graph is a weighted graph we change 1 to w
	adj[u][v] = w;	
	``` 
- Adjacency Lists
	ใน c++ ใช้ array of vector
	```cpp
	vector<int> adj[N];

	adj[u].push_back(v);
	adj[v].push_back(u); // remove this line if a graph is an directed graph
	```
	ถ้ากราฟมี weight ให้ใช้เป็น pair ของ (v, w)
	```cpp
	vector<pair<int, int>> adj[N];

	adj[u].push_back(make_pair(v, w));
	adj[v].push_back(make_pair(u, w)); // remove this line if a graph is a directed 
								       // graph 
	```
	เวลาเรียกหา node ให้ทําแบบนี้
	```cpp
	for (auto v: adj[u]) {
	    // do whatever you want
	}
	```

## Paths Cycles and Connectivity
### Paths
 - เส้นทางที่ใช้ในการเดินจากโหนด u ไป v
### Cycles
 - ทางเดินที่วนกลับมาที่เดิม
### Connectivity
- Undirected graph
	กราฟจะเรียกว่า connected ถ้ามีเส้นทางในการเดินจาก u ไป v เสมอ 
- Directed graph
	กราฟจะเรียกว่า strongly connected ถ้ามีเส้นทางในการเดินจาก u ไป v เสมอ และเรียกว่า
	weakly connected ถ้าไม่มี
- Connected components
	กราฟย่อยที่เชื่อมถึงกันหมดและเชื่อมด้วยโหนดสองโหนดของกราฟย่อย

## Euler Paths and Cycles
- การเดินให้ครบทุก edge โดยไม่ผ่าน edge ที่ผ่านไปแล้ว
- A graph is Euler path if and only if it has exactly two vertices of odd degree.
- A graph is Euler cycles if and only every vertex has a even degree.
## Hamilton Paths and Cycles
- การเดินให้ครบทุกโหนด โดยไม่ผ่านโหนดที่ผ่านไปแล้ว
- Dirac's Theorem 
> if $G$ is a simple graph with n vertices with $n>=3$ and degree of every vertex in $G$, $deg(u) >= \frac{n}{2}$ then G has a Hamilton cycle
- Ore's Theorem
> if $G$ is a simple graph with n vertices and $n>=3$ such that $deg(u) + deg(v) >= n$ for every pair of nonadjacent vertices $u$ and $v$ in G,
> then $G$ has a Hamiton cycle.

## Graph Application
### Planar Graphs
- กราฟจะถูกเรียกว่า กราฟระนาบถ้าสามารถวาดให้กราฟไม่ตัดกันได้
- Euler's formula
> $r+v-e=2$
### Graph coloring
- การระบายสีโหนดในกราฟ โดยโหนดที่ติดกันจะระบายสีต่างกัน
### Graph traversal
- Depth First Search
	เดินให้ลึกที่สุดถ้าเจอทางตัดแล้ว backtrack กลับมาที่โหนดก่อนหน้า
```cpp
// find order of tarversal using dfs
#include <iostream>
#include <vector>
using namespace std;

const int mxN = 1e5+1; // maximum value of input
int N = 10;
int visited[mxN];
vector<int> adj[mxN]; // node start from 0, 1, 2, ..., N

void dfs(int u) {
    visited[u] = 1;
    cout << u << " ";
    for (auto v: adj[u]) {
        if (!visited[v])
            dfs(v);
    }
}

int main() {
    for (int i = 0, u, v; i < 9; i++) {
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    
    for (int u = 0; u < N; u++) {
        if (!visited[u])
            dfs(u);
    }
}

/* testcase
0 1
0 2
0 3
1 4
1 5
1 6
2 7
2 8
4 9
output : 0 1 4 9 5 6 2 7 8 3
*/
```
	

- Breadth First Search
	เดินไปทีละชั้นโดยเดินตามโหนด neighbor ของโหนดแรกก่อน
	- นิยมใช้หา Shortest path
	- การ Implement ใน c++ ให้ใช้ queue ช่วย โดยใช้ queue เก็บลําดับที่จะสํารวจ
```cpp
// find order of traversal in graph using bfs
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int mxN = 1e5+1; // maximum value of input
int N = 10;
int visited[mxN];

int main() {
    vector<int> adj[N]; // node start from 0, 1, 2, ..., N
    queue<int> q;
    for (int i = 0, u, v; i < 9; i++) {
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    q.push(0); // push start node to queue
    
    while (!q.empty()) {
        int u = q.front();
        visited[u] = 1;
        cout << u << " ";
        q.pop();
        for (auto v: adj[u]) {
            if (!visited[v])
                q.push(v);
        }
    }
}

/* testcase
0 1
0 2
0 3
1 4
1 5
1 6
2 7
2 8
4 9

output : 0 1 2 3 4 5 6 7 8 9
*/
```

# Trees
=======
- Adjacency Lists
>>>>>>> dbdac0b71eb32f3db95dd5ec835bc33c4ace0768

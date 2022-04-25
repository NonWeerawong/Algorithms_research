# Graph theory
## Table of Contents
- 1.  Graph definitions
- 2. Special Simple graphs

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
		- in-degree เขียนด้วย `$deg^-(v)$` นับจํานวนที่ลูกศรชี้เข้าหาตัวเอง
		- out-degree เขียนด้วย `$deg^+(v)$` นับจํานวนที่ลูกศรชี้ออกตัวเอง
	`$$\sum_{v\in{V}}{deg^-(v)}=\sum_{v\in{V}}{deg^+(v)}=|E|$$`
	
	The Handshaking theorem
	ทฎษฤีที่ใช้หาจํานวนดีกรีทั้งหมดของ undirected graph
	`$$2|E|=\sum_{v\in{V}}{deg(v)}$$`
	จะเห็นว่ากราฟจะเป็นจริงได้ต้องมี ดีกรีไม่เป็นคู่ทั้งหมด ก็ต้องมีโหนดคู่ตัวมีดีกรีเป็นคี่
	
- adjacent โหนดเชื่อมติดกัน
- neighborhood โหนดเชื่อมติดกัน เขียนได้เป็น $N(u)$

## Special Simple Graphs
- Line Graph
- Cycle Graph
- Wheel Graph
- Complete Graph
- Bipartite Graph
- Complete Bipartite Graph

## Graph Representations
- Adjacency Matrices
- Adjacency Lists

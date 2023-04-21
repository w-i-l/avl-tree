<h1>AVL tree</h1>
<h2>A Python implementation of a AVL data structure</h2>
<img src='https://user-images.githubusercontent.com/65015373/233707201-65fa25a7-24ad-42ea-9f83-b713a689d401.png'>



<br>
<hr>
<h2>About it</h2>

<p>The curent project represents an implementation for an AVL, that mainly serves to solves 6 tasks:</p>

<ol>
    <li>Insert a node</li>
    <li>Delete a node</li>
    <li>Search for a node</li>
    <li>Show the biggest number, smaller than a given number</li>
    <li>Show the smallest number, bigger than a given number</li>
    <li>Show all nodes, sorted, in a given range</li>
</ol>

<br>
<hr>
<h2>How to use it</h2>

<p>In the <a href='https://github.com/w-i-l/avl-tree/blob/main/main.py'>main</a> file is an example for each task from above.</p>

<br>
<hr>
<h2>How it works</h2>

<p>For a deeper understanding about AVL trees, but also beeing my references, I recommend watching this videos:</p>

<a hreaf='https://www.youtube.com/watch?v=jDM6_TnYIqE&ab_channel=AbdulBari'>10.1 AVL Tree - Insertion and Rotations</a> 

<a hreaf='https://www.youtube.com/watch?v=vRwi_UcZGjU&ab_channel=BackToBackSWE'>AVL Trees & Rotations (Self-Balancing Binary Search Trees)</a> 

<a hreaf='https://www.youtube.com/watch?v=kD_xn7mZ6v8&ab_channel=LalithaNatraj'>AVL Tree - Deletion</a> 

<p>Along with this article:</p><a href='https://www.geeksforgeeks.org/count-bst-nodes-that-are-in-a-given-range/'>Count BST nodes that lie in a given range</a>

<br>
<hr>
<h2>Tech specs</h2>


<p>For my implementation those are the time complexities:</p>
<table>
    <tr>
        <th>Insertion</th>
        <th>Deletion</th>
        <th>Search</th>
        <th>Biggest</th>
        <th>Smallest</th>
        <th>Range Numbers</th>
    </tr>
    <tr>
        <td>log(N)</td>
        <td>log(N)</td>
        <td>log(N)</td>
        <td>log(N)</td>
        <td>log(N)</td>
        <td>height + numbers_in_range</td>
    </tr>
</table>

<hr/>
<br/>

<h3>Functions documentation</h3>
<br/>

<b><h3><a href='https://github.com/w-i-l/avl-tree/blob/main/node.py'>Node</a> class</h3></b>
<u><h4>Attributes</h4></u>
<ul>
    <li><code>key</code> : int - node's value</li>
    <li><code>right</code> : Node | None - right child, None if it doesn't have one</li>
    <li><code>left</code> : Node | None - left child, None if it doesn't have one</li>
    <li><code>parent</code> : Node | None - parent node, None for the root node</li>

</ul>

<u><h4>Methods:</h4></u>
<ul>
    <li><code>__init__((self, key:int = 0, left:Node|None = None, right:Node|None = None))</code> - has an auto-increment for key if unspecified </li>
    <li><code>_get_height() -> int</code> - returns the node's height </li>
    <li><code>get_balance() -> int</code> - returns the node's balance factor
        <ul>
            <li>a <code>negative</code> one - means more elements on the <code>right</code> side</li>
            <li>a <code>positive</code> one - means more elements on the <code>left</code> side</li>
            <li>a <code>0</code> - means that is <code>balanced </code></li>
        </ul>
    </li>
</ul>

<br/>

<b><h3><a href='https://github.com/w-i-l/avl-tree/blob/main/avl.py'>AVL</a> class</h3></b>
<u><h4>Attributes</h4></u>
    <ul>
        <li><code>nodes</code> : list[Node] - a list with all nodes, based on insertion order</li>
        <li><code>root</code> : Node - root node</li>    
    </ul>
    
<u><h4>Methods:</h4></u>
<ul>
    <li><code>insert(node:Node)</code> - insert a given node, and rebalance the tree</li>
    <li><code>remove(node:Node)</code> - removes a given node from tree, if not found raise a <code>ValueError</code></li>
    <li><code>search(node:Node) -> bool</code> - returns True if the node is in tree</li>
    <li><code>get_node(key:int) -> Node|None</code> - return the node if the given tree, or if not found None</li>
    <li><code>smallest_element() -> Node</code> - returns the smallest node from tree</li>
    <li><code>biggest_element() -> Node</code> - returns the biggest node from tree</li>
    <li><code>biggest_element_smaller_than(node:Node)</code> - returns the biggest Y such that <code>Y <= node</code></li>
    <li><code>smallest_element_bigger_than(node:Node)</code> - returns the smallest Y such that <code>Y >= node</code></li>
    <li><code>dfs() -> list[Node]</code> - returns the nodes found in the BFS order</li>
    <li><code>get_numbers_in_range(curent_node:Node, from_node:Node, to_node:Node, nodes:list[Node] = []) -> list[Node]</code> - returns a list with
        all numbers in the given range, curent_node should be set as <code>self.root</code></li>
    <li><code>is_balanced() -> bool</code> - returns True if all nodes balances are either -1, 0 or 1</li>    </li>
    <li><code>display()</code> - shows details about each node in tree</li>
    <li><code>display_tree()</code> - shows the nodes in a tree style</li>
    <li><code>balance(parent:Node, curent:Node)</code> - rebalance the tree from the curent node and parent</li>
    <li><code>_final_balance()</code> - balance all unbalanced nodes in tree</li>
    <li><code>_left_left</code>, <code>_left_right</code>, <code>_right_right</code>, <code>_right_left</code> - are used to tree's rotations</li>
</ul>

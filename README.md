# Leetcode

Solutions for Leetcode in Python. For formatting solutions. I use [autopep8](https: // pypi.org / project / autopep8 / ). Run

```sh
autopep8 - -in-place - -aggressive - -aggressive *
```

## Todo / Redo

- Merge Two Sorted List
- Iterative

- Merge k Sorted List
- Use Priority Queue

- Binary Tree Level Order Traversal
- Iterative

- Binary Tree Zigzag Level Order Traversal
- Iterative

- Delete Node in a Linked List
- A shorter approach is possible

- Pascal Triangle II
- Recursive O(k) space

- Reverse Linked List
Iterative

- Same Tree
- Recursive

- Symmetric Tree
- Iterative

- Implement Trie

- Target Sum
- Bottom up

- Open the Lock

# Useful Patterns
# ASCII

- '0' is 48
- 'A' is 65
- 'a' is 97

# Sort
# Merge Sort

```python


def merge_sort(nums):
    # bottom cases: empty or list of a single element.
    if len(nums) <= 1:
        return nums

    pivot = int(len(nums) / 2)
    left_list = merge_sort(nums[0:pivot])
    right_list = merge_sort(nums[pivot:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    left_cursor = right_cursor = 0
    ret = []
    while left_cursor < len(left_list) and right_cursor < len(right_list):
        if left_list[left_cursor] < right_list[right_cursor]:
            ret.append(left_list[left_cursor])
            left_cursor += 1
        else:
            ret.append(right_list[right_cursor])
            right_cursor += 1

    # append what is remained in either of the lists
    ret.extend(left_list[left_cursor:])
    ret.extend(right_list[right_cursor:])

    return ret


```

# Sliding Window

```go
func findSomeWindow(nums[]int) {
    i: = 0
    for j: = 0
    j < len(nums)
    j + + {
        // some logic

        for condition() {
            i += 1
        }

        // logic to check max or min
    }
}
```

# Two Pointer

# Binary Search
# Pattern I

```go
func binarySearch(nums[]int, target int) int {
    if len(nums) == 0 {
        return -1
    }

    left: = 0
    right: = len(nums) - 1

    for left <= right {
        mid: = left + (right - left) / 2
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return -1
}
```

Description:
- Most basic and elementary form of Binary Search
- For accessing a single index in the array.
- Search condition can be determined without comparing to the element's neighbors(or use specific elements around it)
- No post - processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found.

Distinguishing syntax:
- Initial condition: `left = 0, right = length - 1`
- Termination `left > right`
- Searching left `right = mid - 1`
- Searching righ `left = mid + 1`

# Pattern II

```go
func binarySearch(nums[]int, target int) int {
    if len(nums) == 0 {
        return -1
    }

    left: = 0
    right: = len(nums) - 1

    for left < right {
        mid: = left + (right - left) / 2
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }

    if left != nums.length & & nums[left] == target {
        return left
    }

    return -1
}
```

Description:
- An advanced way to implement Binary Search.
- Search condition needs to access element's immediate right neighbor
- Use element's right neighbor to determine if condition is met and decide whether to go left or right
- Guarantees search space is at least 2 in size at each step
- Post - processing required. Loop / recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

Distinguishing syntax:
- Initial condition: `left = 0, right = length`
- Termination `left == right`
- Searching left `right = mid`
- Searching righ `left = mid + 1`

# Pattern II

```go
func binarySearch(nums[]int, target int) int {
    if len(nums) == 0 {
        return -1
    }

    left: = 0
    right: = len(nums) - 1

    for left + 1 < right {
        mid: = left + (right - left) / 2
        if nums[mid] == target {
            return mid
        } else if nums[mid] < target {
            left = mid
        } else {
            right = mid
        }
    }

    if nums[left] == target {
        return left
    }

    if nums[right] == target {
        return right
    }

    return -1
}
```

Description:
- An alternative way to implement Binary Search
- Search Condition needs to access element's immediate left and right neighbors
- Use element's neighbors to determine if condition is met and decide whether to go left or right
- Guarantees Search Space is at least 3 in size at each step
- Post - processing required. Loop / Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

Distinguishing syntax:
- Initial Condition: left = 0, right = length - 1
- Termination: left + 1 == right
- Searching Left: right = mid
- Searching Right: left = mid

# Tree Traversal
# In Order
# Iterative

```go
func iterativeInorder(root * TreeNode)[]int {
    result: = []int{}

    if root == nil {
        return result
    }

    current: = root
    stack: = [] * TreeNode{}

    for current != nil | | len(stack) > 0 {
        for current != nil {
            stack = append(stack, current)
            current = current.Left
        }

        current = stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]

        result = append(result, current.Val)
        current = current.Right
    }

    return result
}
```

# Recursive

```go
func recursiveInOrder(root * TreeNode)[]int {
    result: = []int{}

    if root == nil {
        return result
    }

    recurse(root, & result)

    return result
}

func recurse(root * TreeNode, result * []int) {
    if root == nil {
        return
    }

    recurse(root.Left, result)
    * result = append(*result, root.Val)
    recurse(root.Right, result)
}
```

# Pre Order
# Iterative

```go
func iterativePreOrder(root * TreeNode)[]int {
    result: = []int{}

    if root == nil {
        return result
    }

    stack: = [] * TreeNode{root}

    for len(stack) > 0 {
        node: = stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]

        result = append(result, node.Val)

        if node.Right != nil {
            stack = append(stack, node.Right)
        }

        if node.Left != nil {
            stack = append(stack, node.Left)
        }
    }

    return result
}
```

# Recursive

```go
func recursivePreOrder(root * TreeNode)[]int {
    result: = []int{}

    if root == nil {
        return result
    }

    recurse(root, & result)

    return result
}

func recurse(root * TreeNode, result * []int) {
    if root == nil {
        return
    }

    * result = append(*result, root.Val)
    recurse(root.Left, result)
    recurse(root.Right, result)
}
```

# Post Order
# Iterative

```go
func iterativePostOrder(root * TreeNode)[]int {
    result: = []int{}

    if root == nil {
        return result
    }

    stack: = [] * TreeNode{root}

    for len(stack) > 0 {
        node: = stack[len(stack) - 1]
        stack = stack[:len(stack) - 1]

        result = append(result, node.Val)

        if node.Left != nil {
            stack = append(stack, node.Left)
        }

        if node.Right != nil {
            stack = append(stack, node.Right)
        }
    }

    reverse(result)

    return result
}
```

# Recursive

```go
func recursivePostOrder(root * TreeNode)[]int {
    result: = []int{}

    if root == nil {
        return result
    }

    recurse(root, & result)

    return result
}

func recurse(root * TreeNode, result * []int) {
    if root == nil {
        return
    }

    recurse(root.Left, result)
    recurse(root.Right, result)
    * result = append(*result, root.Val)
}
```

# Level Order
# Iterative

```go
func iterativeLevelOrder(root * TreeNode)[][]int {
    result: = [][]int{}

    if root == nil {
        return result
    }

    queue: = [] * TreeNode{root}

    for len(queue) > 0 {
        level: = []int{}
        qLen: = len(queue)

        for i: = 0
        i < qLen
        i + + {
            node: = queue[0]
            queue = queue[1:]

            level = append(level, node.Val)

            if node.Left != nil {
                queue = append(queue, node.Left)
            }

            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }

        result = append(result, level)
    }

    return result
}
```

# Recursive

Warning! This is not really BFS because by nature recursion is DFS. See GeeksforGeeks for more.

```go
func recursiveLevelOrder(root * TreeNode)[][]int {
    result: = [][]int{}

    if root == nil {
        return result
    }

    level: = 0
    recurse(root, level, & result)

    return result
}

func recurse(root * TreeNode, level int, result * [][]int) {
    if root == nil {
        return
    }

    if len(*result) - 1 < level {
        newLevel: = []int{}
        * result = append(*result, newLevel)
    }

    (*result)[level] = append((*result)[level], root.Val)
    recurse(root.Left, level + 1, result)
    recurse(root.Right, level + 1, result)
}
```

# Graph Cloning
# Recursive

```go
func cloneGraph(node * GraphNode) * GraphNode {
    if node == nil {
        return nil
    }

    visited: = map[*GraphNode] * GraphNode{}
    return recurse(node, visited)
}

func recurse(node * GraphNode, visited map[*GraphNode] * GraphNode) * GraphNode {
    if node == nil {
        return nil
    }

    if cloned, ok: = visited[node]
    ok {
        return cloned
    }

    cloned: = &GraphNode{Val: node.Val}
    visited[node] = cloned

    for _, neighbor: = range node.Neighbors {
        clonedNeighbor: = recurse(neighbor, visited)
        cloned.Neighbors = append(cloned.Neighbors, clonedNeighbor)
    }

    return cloned
}
```

# Graph Coloring
# Recursive

```go
func coloring(graph[][]int) bool {
    colors: = make([]int, len(graph))
    for i: = 0
    i < len(colors)
    i + + {
        colors[i] = -1
    }

    for i: = 0
    i < len(colors)
    i + + {
        if colors[i] == -1 & & !colorGraph(i, 0, & colors, graph) {
            return false
        }
    }

    return true
}

func colorGraph(node, color int, colors * []int, graph[][]int) bool {
    if (*colors)[node] != -1 {
        if (*colors)[node] == color {
            return true
        }

        return false
    }

    (*colors)[node] = color

    neighbors: = graph[node]
    for _, n: = range neighbors {
        if color == 0 {
            if !colorGraph(n, 1, colors, graph) {
                return false
            }
        } else {
            if !colorGraph(n, 0, colors, graph) {
                return false
            }
        }
    }

    return true
}
```

# Iterative

```go
func coloring(graph[][]int) bool {
    colors: = make([]int, len(graph))
    for i: = 0
    i < len(colors)
    i + + {
        colors[i] = -1
    }

    for i: = 0
    i < len(colors)
    i + + {
        if colors[i] == -1 {
            stack: = []int{i}
            colors[i] = 0

            for len(stack) > 0 {
                node: = stack[len(stack) - 1]
                stack = stack[:len(stack) - 1]

                neighbors: = graph[node]
                for _, neighbor: = range neighbors {
                    if colors[neighbor] == -1 {
                        stack = append(stack, neighbor)

                        if colors[node] == 0 {
                            colors[neighbor] = 1
                        } else {
                            colors[neighbor] = 0
                        }
                    } else {
                        if colors[neighbor] == colors[node] {
                            return false
                        }
                    }
                }
            }
        }
    }

    return true
}
```

# Permutation

```go
func generatePermutation(choices[]int)[][]int {
    result: = [][]int{}

    if len(nums) == 0 {
        return result
    }

    permutation: = []int{}

    recurse(nums, & permutation, & result)

    return result
}

func recurse(choices[]int, permutation * []int, result * [][]int) {
    if len(choice) == 0 {
        *result = append(*result, createCopy(permutation))
        return
    }

    for i: = 0
    i < len(choices)
    i + + {
        newChoices: = createNewChoicesExceptCurrent(choices, i)

        * permutation = append(permutation, choices[i])
        recurse(newChoices, permutation, result)
        * permutation = (*permutation)[:len(*permutation) - 1]
    }
}
```

# Subset

```go
func generateSubsets(set[]int)[][]int {
    result: = [][]int{}

    if len(nums) == 0 {
        return result
    }

    subset: = []int{}
    startIndex: = 0

    recurse(set, startIndex, & subset, & result)

    return result
}

func recurse(set[]int, index int, subset * []int, result * [][]int) {
    if index == len(nums) {
        *result = append(*result, createCopy(*subset))
        return
    }

    recurse(nums, index + 1, subset, result)

    * subset = append(*subset, nums[index])
    recurse(nums, index + 1, subset, result)
    * subset = (*subset)[:len(*subset) - 1]
}
```

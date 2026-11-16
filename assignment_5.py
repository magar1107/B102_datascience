import heapq
from collections import OrderedDict, deque


"""
Python Coding Interview Questions

1. Find the second-largest unique element in an array without using sort() or max().
"""


def second_largest_unique(arr):
    first = None
    second = None
    for num in arr:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
    return second


print(second_largest_unique([4, 8, 8, 1, 9, 9, 6]))


"""
2. Find all pairs in an array whose sum equals a given target.
"""


def find_pairs(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        if target - num in seen:
            pairs.append((target - num, num))
        seen.add(num)
    return pairs


print(find_pairs([1, 5, 7, -1, 5, 3, 4], 6))


"""
3. Move all zeros to the end of an array without changing the order of other elements.
"""


def move_zeros(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    return arr


print(move_zeros([0, 1, 0, 3, 12, 0, 5]))


"""
4. Find the missing number from an array containing numbers from 1 to N.
"""


def find_missing(arr):
    n = len(arr) + 1
    expected = n * (n + 1) // 2
    return expected - sum(arr)


print(find_missing([1, 2, 4, 5, 6]))


"""
5. Find all duplicate elements in a list without using nested loops.
"""


def find_duplicates(arr):
    seen = set()
    duplicates = []
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    return duplicates


print(find_duplicates([1, 2, 3, 2, 4, 3, 5, 1]))


"""
6. Find the first non-repeating character in a string.
"""


def first_non_repeating(s):
    count = {}
    for ch in s:
        count[ch] = count.get(ch, 0) + 1
    for ch in s:
        if count[ch] == 1:
            return ch
    return None


print(first_non_repeating("swiss"))
print(first_non_repeating("aabb"))


"""
7. Check whether two strings are anagrams without using sorted().
"""


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1
    for ch in s2:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1
    return True


print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))


"""
8. Merge two sorted arrays without using sort().
"""


def merge_sorted(a, b):
    result = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result


print(merge_sorted([1, 3, 5, 7], [2, 4, 6, 8, 10]))


"""
9. Rotate an array to the right by K positions.
"""


def rotate_right(arr, k):
    if not arr:
        return arr
    k = k % len(arr)
    if k == 0:
        return arr[:]
    return arr[-k:] + arr[:-k]


print(rotate_right([1, 2, 3, 4, 5, 6, 7], 3))


"""
10. Find the intersection of two arrays, including duplicate occurrences.
"""


def intersect(a, b):
    count = {}
    for num in a:
        count[num] = count.get(num, 0) + 1
    result = []
    for num in b:
        if count.get(num, 0) > 0:
            result.append(num)
            count[num] -= 1
    return result


print(intersect([1, 2, 2, 1, 3], [2, 2, 3, 3]))


"""
11. Find the maximum sum of a contiguous subarray.
"""


def max_subarray_sum(arr):
    best = arr[0]
    current = arr[0]
    for num in arr[1:]:
        current = max(num, current + num)
        best = max(best, current)
    return best


print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


"""
12. Find the longest substring without repeating characters.
"""


def longest_unique_substring(s):
    last_seen = {}
    start = 0
    best_start = 0
    best_len = 0
    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        if i - start + 1 > best_len:
            best_len = i - start + 1
            best_start = start
    return s[best_start:best_start + best_len]


print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("pwwkew"))


"""
13. Find the longest common prefix among multiple strings.
"""


def longest_common_prefix(words):
    if not words:
        return ""
    prefix = words[0]
    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "car", "race"]))


"""
14. Group a list of strings into anagram groups.
"""


def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


"""
15. Find the Kth largest element in an unsorted array.
"""


def kth_largest(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


print(kth_largest([3, 2, 1, 5, 6, 4], 2))


"""
16. Check whether a given string contains balanced parentheses using a stack.
"""


def is_balanced(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0


print(is_balanced("{[()]}"))
print(is_balanced("{[(])}"))


"""
17. Find all subarrays whose sum equals a given target.
"""


def subarrays_with_sum(arr, target):
    result = []
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            if total == target:
                result.append(arr[i:j + 1])
    return result


print(subarrays_with_sum([1, 2, 3, 4, 5, -2, 2], 5))


"""
18. Merge overlapping intervals in a list.
"""


def merge_intervals(intervals):
    if not intervals:
        return []
    intervals = sorted(intervals, key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18], [17, 20]]))


"""
19. Search for an element in a rotated sorted array.
"""


def search_rotated(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 3))


"""
20. Find the longest consecutive sequence in an unsorted array.
"""


def longest_consecutive(arr):
    nums = set(arr)
    best = 0
    for num in nums:
        if num - 1 not in nums:
            current = num
            length = 1
            while current + 1 in nums:
                current += 1
                length += 1
            best = max(best, length)
    return best


print(longest_consecutive([100, 4, 200, 1, 3, 2]))


"""
21. Find the trapped rainwater between elevation bars.
"""


def trapped_water(heights):
    left = 0
    right = len(heights) - 1
    left_max = 0
    right_max = 0
    water = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= left_max:
                left_max = heights[left]
            else:
                water += left_max - heights[left]
            left += 1
        else:
            if heights[right] >= right_max:
                right_max = heights[right]
            else:
                water += right_max - heights[right]
            right -= 1
    return water


print(trapped_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


"""
22. Find the median of two sorted arrays in O(log(m+n)) time.
"""


def find_median(a, b):
    if len(a) > len(b):
        a, b = b, a
    m = len(a)
    n = len(b)
    low = 0
    high = m
    half = (m + n + 1) // 2
    while low <= high:
        i = (low + high) // 2
        j = half - i
        left_a = a[i - 1] if i > 0 else float("-inf")
        right_a = a[i] if i < m else float("inf")
        left_b = b[j - 1] if j > 0 else float("-inf")
        right_b = b[j] if j < n else float("inf")
        if left_a <= right_b and left_b <= right_a:
            if (m + n) % 2 == 1:
                return max(left_a, left_b)
            return (max(left_a, left_b) + min(right_a, right_b)) / 2
        elif left_a > right_b:
            high = i - 1
        else:
            low = i + 1


print(find_median([1, 3], [2]))
print(find_median([1, 2], [3, 4]))


"""
23. Find the maximum product of a contiguous subarray.
"""


def max_product_subarray(arr):
    best = arr[0]
    cur_max = arr[0]
    cur_min = arr[0]
    for num in arr[1:]:
        candidates = (num, cur_max * num, cur_min * num)
        cur_max = max(candidates)
        cur_min = min(candidates)
        best = max(best, cur_max)
    return best


print(max_product_subarray([2, 3, -2, 4]))
print(max_product_subarray([-2, 3, -4]))


"""
24. Find the smallest missing positive integer from an unsorted array.
"""


def smallest_missing_positive(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            j = arr[i] - 1
            arr[i], arr[j] = arr[j], arr[i]
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1


print(smallest_missing_positive([3, 4, -1, 1]))
print(smallest_missing_positive([1, 2, 0]))


"""
25. Count the number of subarrays whose sum equals K.
"""


def count_subarrays_sum_k(arr, k):
    prefix_count = {0: 1}
    total = 0
    count = 0
    for num in arr:
        total += num
        count += prefix_count.get(total - k, 0)
        prefix_count[total] = prefix_count.get(total, 0) + 1
    return count


print(count_subarrays_sum_k([1, 1, 1], 2))
print(count_subarrays_sum_k([1, 2, 3, -3, 3], 3))


"""
26. Find the longest increasing subsequence in an array.
"""


def longest_increasing_subsequence(arr):
    if not arr:
        return []
    n = len(arr)
    length = [1] * n
    parent = [-1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i] and length[j] + 1 > length[i]:
                length[i] = length[j] + 1
                parent[i] = j
    end = length.index(max(length))
    result = []
    while end != -1:
        result.append(arr[end])
        end = parent[end]
    return result[::-1]


print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))


"""
27. Solve the Coin Change problem using dynamic programming.
"""


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))


"""
28. Solve the Word Break problem using dynamic programming.
"""


def word_break(s, word_dict):
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]


print(word_break("leetcode", ["leet", "code"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))


"""
29. Find the minimum number of jumps required to reach the last index.
"""


def min_jumps(arr):
    if len(arr) <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(len(arr) - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= len(arr) - 1:
                break
    if current_end < len(arr) - 1:
        return -1
    return jumps


print(min_jumps([2, 3, 1, 1, 4]))


"""
30. Find the maximum profit from buying and selling stocks with multiple transactions.
"""


def max_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))


"""
31. Implement an LRU Cache with O(1) time complexity for get() and put().
"""


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))


"""
32. Implement a Min Stack that supports push(), pop(), top() and getMin() in O(1).
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(3)
print(ms.getMin())
ms.pop()
print(ms.getMin())
ms.pop()
print(ms.top())
print(ms.getMin())


"""
33. Find the number of islands in a 2D matrix using DFS or BFS.
"""


def count_islands(grid):
    if not grid:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == 0 or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                dfs(r, c)
                islands += 1
    return islands


print(count_islands([
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
]))


"""
34. Find the shortest path in a weighted graph using Dijkstra's algorithm.
"""


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return distances


weighted_graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 5)],
    "C": [("B", 1), ("D", 8)],
    "D": [],
}
print(dijkstra(weighted_graph, "A"))


"""
35. Detect a cycle in a directed and undirected graph.
"""


def has_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False


def has_cycle_directed(graph):
    state = {node: 0 for node in graph}

    def dfs(node):
        state[node] = 1
        for neighbor in graph[node]:
            if state[neighbor] == 1:
                return True
            if state[neighbor] == 0 and dfs(neighbor):
                return True
        state[node] = 2
        return False

    for node in graph:
        if state[node] == 0:
            if dfs(node):
                return True
    return False


print(has_cycle_undirected({0: [1, 2], 1: [0, 2], 2: [0, 1]}))
print(has_cycle_undirected({0: [1], 1: [0, 2], 2: [1]}))
print(has_cycle_directed({0: [1], 1: [2], 2: [0]}))
print(has_cycle_directed({0: [1], 1: [2], 2: []}))


"""
36. Implement topological sorting for a directed acyclic graph.
"""


def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    queue = deque([node for node in graph if in_degree[node] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    if len(order) != len(graph):
        return []
    return order


print(topological_sort({5: [2, 0], 4: [0, 1], 2: [3], 3: [1], 0: [], 1: []}))


"""
37. Solve the N-Queens problem using backtracking.
"""


def solve_n_queens(n):
    solutions = []
    cols = set()
    diag1 = set()
    diag2 = set()
    board = []

    def backtrack(row):
        if row == n:
            solutions.append(["." * c + "Q" + "." * (n - c - 1) for c in board])
            return
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board.append(col)
            backtrack(row + 1)
            board.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return solutions


queens_solutions = solve_n_queens(4)
print(len(queens_solutions))
for row in queens_solutions[0]:
    print(row)


"""
38. Generate all permutations of a given string or array without duplicates.
"""


def unique_permutations(data):
    items = sorted(data)
    used = [False] * len(items)
    result = []
    current = []

    def backtrack():
        if len(current) == len(items):
            if isinstance(data, str):
                result.append("".join(current))
            else:
                result.append(current[:])
            return
        for i in range(len(items)):
            if used[i]:
                continue
            if i > 0 and items[i] == items[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            current.append(items[i])
            backtrack()
            current.pop()
            used[i] = False

    backtrack()
    return result


print(unique_permutations("aab"))
print(unique_permutations([1, 1, 2]))


"""
39. Serialize and deserialize a binary tree.
"""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def serialize(root):
    result = []

    def preorder(node):
        if node is None:
            result.append("#")
            return
        result.append(str(node.value))
        preorder(node.left)
        preorder(node.right)

    preorder(root)
    return ",".join(result)


def deserialize(data):
    values = iter(data.split(","))

    def build():
        value = next(values)
        if value == "#":
            return None
        node = TreeNode(int(value))
        node.left = build()
        node.right = build()
        return node

    return build()


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)

encoded = serialize(tree)
print(encoded)
print(serialize(deserialize(encoded)) == encoded)


"""
40. Find the lowest common ancestor of two nodes in a binary tree.
"""


def lowest_common_ancestor(root, p, q):
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    if left:
        return left
    return right


lca = lowest_common_ancestor(tree, tree.right.left, tree.right.right)
print(lca.value)
lca = lowest_common_ancestor(tree, tree.left, tree.right.right)
print(lca.value)

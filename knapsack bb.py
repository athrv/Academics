class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def knapsack_branch_and_bound(items, capacity):
    def bound(i, weight, value):
        if weight > capacity:
            return 0
        bound_value = value
        j = i
        total_weight = weight
        while j < n and total_weight + items[j].weight <= capacity:
            total_weight += items[j].weight
            bound_value += items[j].value
            j += 1
        if j < n:
            bound_value += (capacity - total_weight) * (items[j].value / items[j].weight)
        return bound_value

    def knapsack_recursive(i, weight, value):
        nonlocal max_value
        if weight <= capacity and value > max_value:
            max_value = value
        if i < n:
            if weight + items[i].weight <= capacity:
                knapsack_recursive(i + 1, weight + items[i].weight, value + items[i].value)
            if bound(i + 1, weight, value) > max_value:
                knapsack_recursive(i + 1, weight, value)

    n = len(items)
    max_value = 0
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    knapsack_recursive(0, 0, 0)
    return max_value

# Example usage
if __name__ == "__main__":
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    capacity = 50

    max_value = knapsack_branch_and_bound(items, capacity)
    print("Maximum value in the knapsack:", max_value)
    
    
    '''
    Sure, let's walk through the code with an example to illustrate how it works. We have a list of items with their weights and values and a knapsack with a capacity. The goal is to find the combination of items to maximize the total value within the knapsack's capacity.

Example:
Suppose we have the following items:
- Item 1: Weight = 10, Value = 60
- Item 2: Weight = 20, Value = 100
- Item 3: Weight = 30, Value = 120

And the knapsack has a capacity of 50.

1. Sorting items:
   First, the items are sorted in descending order of their value-to-weight ratios. This step helps prioritize items that provide the most value relative to their weight.

   The sorted order becomes:
   - Item 3 (Value-to-Weight Ratio: 120/30 = 4)
   - Item 2 (Value-to-Weight Ratio: 100/20 = 5)
   - Item 1 (Value-to-Weight Ratio: 60/10 = 6)

2. The `knapsack_recursive` function is called with the following initial parameters:
   - i = 0 (starting from the first item)
   - weight = 0 (initial weight in the knapsack)
   - value = 0 (initial value in the knapsack)
   - max_value = 0 (initial maximum value)

3. Recursive exploration:
   The algorithm explores various combinations of items, including and excluding them. It considers Item 1 (weight = 10, value = 60) first. It checks if adding this item to the knapsack is feasible (weight + 10 <= capacity) and explores both possibilities (adding it or not). This process continues for other items.

   - At each step, it checks if the current value is greater than the `max_value`. If so, it updates `max_value` with the current value.

   In this example, the recursion tree would look like this:

   ```
               (0,0,0)
               /     \
          (1,10,60) (1,0,0)
           /   \     /   \
      (2,30,160) (2,10,60) ...
      ...
   ```

4. Pruning:
   During exploration, the `bound` function is used to estimate the maximum value that can be achieved from the remaining items. If the estimated maximum value is less than the current `max_value`, the branch of the tree is pruned, as it won't lead to a better solution.

5. Backtracking:
   The algorithm backtracks when it reaches a point where no more items can be included without exceeding the capacity. It explores alternative paths in the search tree.

6. Finally, the algorithm returns the maximum value found in the knapsack. In this example, the algorithm would find the combination of items that maximizes the total value, and the result would be printed.

In this case, the algorithm would return a maximum value of 220, achieved by including Item 2 and Item 3 in the knapsack. Item 1 is not included because adding it would exceed the knapsack's capacity. This demonstrates how the Branch and Bound algorithm efficiently explores the solution space to find the optimal solution to the 0/1 Knapsack problem.
    '''
Day 6 of my DSA Journey 🚀
Solved: Min Stack (LeetCode #155)

Today’s problem was a step up—designing a stack that can return the minimum element in constant time. It was a great mix of data structure design and optimization.

🔹 Key Learning:
To achieve O(1) for getMin(), we need to track minimums efficiently:

* Maintain an additional stack to store the current minimum at each step
* This avoids recalculating the minimum every time

🔹 Approach:
Used two stacks:

* Main stack → stores all elements
* Min stack → keeps track of the minimum value corresponding to each element

🔹 Complexity:
Push: O(1)
Pop: O(1)
Top: O(1)
GetMin: O(1)
Space: O(n)

💡 This problem reinforced how auxiliary data structures can help optimize operations and meet strict constraints.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

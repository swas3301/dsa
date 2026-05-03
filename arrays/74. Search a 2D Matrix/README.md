Day 11 of my DSA Journey 🚀
Solved: Search a 2D Matrix (LeetCode #74)

Today’s problem combined arrays with binary search logic. It was interesting to see how a 2D matrix can be treated like a sorted 1D array.

🔹 Key Learning:
The matrix properties allow optimization:

* Each row is sorted
* First element of each row > last element of previous row
  ➡️ This means we can apply binary search on the entire matrix

🔹 Approach:
Started with a brute-force approach:

* Traverse all elements and check for the target

Next step:

* Apply binary search by treating the matrix as a flattened array

🔹 Complexity:
Brute Force → Time: O(m × n), Space: O(1)
Optimized (Binary Search) → Time: O(log(m × n)), Space: O(1)

💡 This problem showed how recognizing patterns in constraints can unlock more efficient solutions.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

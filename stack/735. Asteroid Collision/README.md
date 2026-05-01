Day 8 of my DSA Journey 🚀
Solved: Contains Duplicate II (LeetCode #219)

Today’s problem was a nice mix of arrays and hashing. It focused on efficiently checking duplicates within a given range.

🔹 Key Learning:
Instead of comparing every pair, we can track elements using a hashmap or set:

* Store the last seen index of each number
* Check if the current index difference is ≤ k

🔹 Approach:
Used a hashmap (dictionary):

* If a number is already seen and the index difference ≤ k → return True
* Otherwise, update its latest index

🔹 Complexity:
Time: O(n)
Space: O(n)

💡 This problem reinforced how hashing helps reduce time complexity and makes duplicate checks efficient.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

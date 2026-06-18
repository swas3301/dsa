Day 7 of my DSA Journey 🚀
Solved: Trapping Rain Water (LeetCode #42)

Today’s problem was a challenging one and really pushed my understanding of array traversal and optimization techniques.

🔹 Key Learning:
Water trapped at any index depends on the minimum of the maximum heights on both sides:

* Water = min(left_max, right_max) − height[i]
* Brute force works, but optimization is key

🔹 Approach:
Used the two-pointer technique:

* Maintain left and right pointers
* Track left_max and right_max dynamically
* Move the pointer with the smaller height inward and calculate trapped water on the go

🔹 Complexity:
Time: O(n)
Space: O(1)

💡 This problem reinforced how powerful the two-pointer approach can be in reducing space complexity and improving efficiency.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

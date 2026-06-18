Day 25 of my DSA Journey 🚀
Solved: Assign Cookies (LeetCode #455)

Today’s problem was a nice introduction to greedy algorithms—making the best local choice to achieve the optimal overall result.

🔹 Key Learning:
To maximize the number of content children:

* Sort both the greed factors and cookie sizes
* Try to satisfy the least greedy child first
* Use the smallest possible cookie that works

🔹 Approach:
Used sorting + two pointers:

* Sort both arrays in ascending order
* Compare the current child’s greed with the current cookie size
* If the cookie satisfies the child, move to the next child
* Always move to the next cookie

🔹 Complexity:
Time: O(n log n + m log m) *(due to sorting)*
Space: O(1) *(excluding sorting space)*

💡 This problem reinforced how greedy strategies can lead to elegant and efficient solutions when making optimal local decisions.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

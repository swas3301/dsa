Day 24 of my DSA Journey 🚀
Solved: Simplify Path (LeetCode #71)

Today’s problem was a great stack + string parsing challenge that simulated navigating through a Unix file system.

🔹 Key Learning:
Path simplification is all about handling directory navigation correctly:

* `"."` → stay in the current directory
* `".."` → move to the parent directory
* Multiple `/` → treat as a single separator
* Valid folder names → push into the path stack

🔹 Approach:
Used a stack-based approach:

* Traverse the path character by character
* Build directory names dynamically
* Process each segment when a `/` is encountered
* Use the stack to simulate moving forward/backward in directories
* Join the final stack to construct the canonical path

🔹 Complexity:
Time: O(n)
Space: O(n)

💡 This problem reinforced how stacks are excellent for simulating navigation/history-based operations.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

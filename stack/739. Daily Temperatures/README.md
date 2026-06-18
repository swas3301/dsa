Day 12 of my DSA Journey 🚀
Solved: Daily Temperatures (LeetCode)

Today’s problem was a great example of using a monotonic stack to solve next greater element–type questions efficiently.

🔹 Key Learning:
Instead of checking every future day (which is inefficient), we can use a stack:

* Store indices of temperatures
* Maintain a decreasing stack
* When a warmer temperature is found, resolve previous days

🔹 Approach:
Used a stack to keep track of unresolved indices:

* Traverse the array
* While current temperature > stack top → calculate days difference
* Push current index onto the stack

🔹 Complexity:
Time: O(n)
Space: O(n)

💡 This problem reinforced how monotonic stacks help optimize problems that involve “next greater element” patterns.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

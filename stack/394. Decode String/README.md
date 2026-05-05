Day 13 of my DSA Journey 🚀
Solved: Decode String (LeetCode #394)

Today’s problem was a fun mix of strings and stacks. It really tested how to handle nested patterns and build results step by step.

🔹 Key Learning:
Stacks are perfect for handling nested structures:

* When encountering `"["`, start a new context
* When encountering `"]"`, resolve the current encoded string
* Build the result from inside out

🔹 Approach:
Used a stack to process the string:

* Push characters until `"]"` is found
* Extract the encoded string inside brackets
* Get the repeat count `k`
* Push the decoded substring back onto the stack

🔹 Complexity:
Time: O(n)
Space: O(n)

💡 This problem reinforced how stacks can simplify complex string decoding, especially with nested patterns.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

Day 5 of my DSA Journey 🚀
Solved: Implement Queue using Stacks (LeetCode #232)

Today’s problem was the reverse of yesterday’s—implementing a FIFO queue using LIFO stacks. It really tested my understanding of how data flow can be controlled using two stacks.

🔹 Key Learning:
Two stacks can simulate queue behavior efficiently:

* One stack for incoming elements
* One stack for outgoing elements (reverses order)

🔹 Approach:
Used two stacks:

* Push elements into the input stack
* For pop/peek, transfer elements to the output stack only when needed

🔹 Complexity:
Amortized Time: O(1)
Space: O(n)

💡 This problem reinforced the concept of amortized analysis and how reversing order twice restores FIFO behavior.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

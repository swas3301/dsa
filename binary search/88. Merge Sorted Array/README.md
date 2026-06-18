Day 22 of my DSA Journey 🚀
Solved: Merge Sorted Array (LeetCode #88)

Today’s problem was a neat two-pointer problem that emphasized in-place array manipulation and optimization.

🔹 Key Learning:
Since both arrays are already sorted:

* Start filling from the end to avoid overwriting values in `nums1`
* Compare the largest remaining elements from both arrays
* Place the bigger one at the current position

🔹 Approach:
Used the two-pointer technique from the back:

* One pointer for the valid part of `nums1`
* One pointer for `nums2`
* One pointer for the final insertion position
* Merge elements in-place without using extra space

🔹 Complexity:
Time: O(m + n)
Space: O(1)

💡 This problem reinforced how thinking from the end instead of the beginning can make in-place operations much cleaner and more efficient.

Consistency is the key. Showing up every day, one problem at a time.

#DSA #LeetCode #Python #CodingJourney #1000DaysOfCode #SoftwareEngineering #ProblemSolving

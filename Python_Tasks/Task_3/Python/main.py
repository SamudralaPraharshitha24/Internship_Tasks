# Q1. Find the Frequency of Each Word in a Sentence
from solutions import q1_word_frequency
sentence = "python is easy and python is powerful"
result = q1_word_frequency(sentence)
print("Q1 Output:")
print(result)

# Q2. Find the Frequency of Each Character in a Word
from solutions import q2_character_frequency
word = "banana"
print("\nQ2 Output:")
print(q2_character_frequency(word))

# Q3. Find the First Non-Repeating Character in a Word
from solutions import q3_first_non_repeating
word = "swiss"
print("Q3 Output:")
print(q3_first_non_repeating(word))

# Q4. Check Whether Two Strings Are Anagrams
from solutions import q4_are_anagrams
s1 = "listen"
s2 = "silent"
print("Q4 Output:")
print(q4_are_anagrams(s1, s2))

# Q5. Find the First Repeating Character in a String
from solutions import q5_first_repeating_char
string = "programming"
print("Q5 Output:")
print(q5_first_repeating_char(string))

# Q6. Move All Zeros to the End of a List
from solutions import q6_move_zeros
numbers = [0, 3, 0, 1, 2, 0, 4]
print("Q6 Output:")
print(q6_move_zeros(numbers))

# Q7. Find the Second Highest Distinct Number in a List
from solutions import q7_second_highest
numbers = [10, 20, 40, 30, 40, 20]
print("Q7 Output:")
print(q7_second_highest(numbers))

# Q8. Remove Duplicates Without Changing the Original Order
from solutions import q8_remove_duplicates
numbers = [4, 2, 4, 5, 2, 7, 5]
print("Q8 Output:")
print(q8_remove_duplicates(numbers))

# Q9. Find the Missing Number from 1 to N
from solutions import q9_missing_number
nums = [1, 2, 4, 5, 6]
N = 6
print("Q9 Output:")
print(q9_missing_number(nums, N))

# Q10. Find Two Numbers Whose Sum Equals a Target
from solutions import q10_two_sum
nums = [2, 7, 11, 15]
target = 9
print("Q10 Output:")
print(q10_two_sum(nums, target))

# Q11. Find the Number Closest to Zero
from solutions import q11_closest_to_zero
nums = [-8, -3, 2, 5, -2]
print("Q11 Output:")
print(q11_closest_to_zero(nums))

# Q12. Find Common Elements Between Two Lists
from solutions import q12_common_elements
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print("Q12 Output:")
print(q12_common_elements(list1, list2))

# Q13. Rotate a List to the Right by K Positions
from solutions import q13_rotate_right
nums = [1, 2, 3, 4, 5]
K = 2
print("Q13 Output:")
print(q13_rotate_right(nums, K))

# Q14. Find the Maximum Sum of Two Consecutive Elements
from solutions import q14_max_consecutive_sum
nums = [4, 7, 2, 9, 5]
print("Q14 Output:")
print(q14_max_consecutive_sum(nums))

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target
from solutions import q15_all_pairs
nums = [2, 4, 3, 5, 7, 8, 1]
target = 9
print("Q15 Output:")
print(q15_all_pairs(nums, target))
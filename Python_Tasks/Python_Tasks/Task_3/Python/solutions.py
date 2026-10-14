
# Q1. Find the Frequency of Each Word in a Sentence

def q1_word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency

# Q2. Find the Frequency of Each Character in a Word

def q2_character_frequency(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    return frequency


# Q3. Find the First Non-Repeating Character in a Word

def q3_first_non_repeating(word):
    frequency = {}

    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in word:
        if frequency[char] == 1:
            return char

    return None


# Q4. Check Whether Two Strings Are Anagrams

def q4_are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)


# Q5. Find the First Repeating Character in a String

def q5_first_repeating_char(string):
    seen = set()

    for char in string:
        if char in seen:
            return char
        else:
            seen.add(char)

    return None


# Q6. Move All Zeros to the End of a List

def q6_move_zeros(numbers):
    non_zeros = []
    zeros = []

    for num in numbers:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)

    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number in a List

def q7_second_highest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


# Q8. Remove Duplicates Without Changing the Original Order

def q8_remove_duplicates(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)

    return unique_numbers


# Q9. Find the Missing Number from 1 to N

def q9_missing_number(nums, N):
    expected_sum = N * (N + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum


# Q10. Find Two Numbers Whose Sum Equals a Target

def q10_two_sum(nums, target):
    seen = []

    for num in nums:
        complement = target - num

        if complement in seen:
            return [complement, num]

        seen.append(num)

    return []


# Q11. Find the Number Closest to Zero

def q11_closest_to_zero(nums):
    if not nums:
        return None

    closest = nums[0]

    for num in nums:
        if abs(num) < abs(closest):
            closest = num
        elif abs(num) == abs(closest) and num > closest:
            closest = num

    return closest


# Q12. Find Common Elements Between Two Lists

def q12_common_elements(list1, list2):
    common = []

    for num in list1:
        if num in list2 and num not in common:
            common.append(num)

    return common

# Q13. Rotate a List to the Right by K Positions

def q13_rotate_right(nums, K):
    if not nums:
        return []

    K = K % len(nums)

    return nums[-K:] + nums[:-K] if K != 0 else nums.copy()


# Q14. Find the Maximum Sum of Two Consecutive Elements

def q14_max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Q15. Find All Pairs of Numbers Whose Sum Equals a Target

def q15_all_pairs(nums, target):
    pairs = []
    seen = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            pair = sorted([num, complement])

            if pair not in pairs:
                pairs.append(pair)

        seen.add(num)

    pairs.sort(key=lambda pair: pair[0])

    return pairs

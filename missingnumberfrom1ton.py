total_list = [1, 2, 3, 4, 6, 7, 8, 9, 10]  
#Sum of 1 to n is (n * (n + 1)) // 2
expected_sum = (10 * 11) // 2
actual_sum = sum(total_list)
missing_number = expected_sum - actual_sum
print(f"The missing number is: {missing_number}")

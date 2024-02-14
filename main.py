'''
First Solution *** 

Time Complexity: 
O(nlogn), dominated by the sorting operations for finding the most common elements and potentially sorting the tied even elements.

Space Complexity: 
O(n) in the worst case, due to the storage requirements for counting occurrences and handling the list of most frequent even elements.

Second Solution *** 

Time Complexity: 
O(n) - The function needs to iterate through the list once for counting, and the operation to find the maximum is linear with respect to the number of unique even numbers.

Space Complexity: 
O(n) in the worst case - This is due to the space required to store the counts of the even numbers, which, in the worst case scenario, could be as many as the total number of items in the input list if they are all unique and even.
'''
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        # nums_counter = Counter(nums) # Returns a list of tuples containing each number with its count
        # most_frequent_elements = nums_counter.most_common() # Returns a list of tuples with most common frequency
        # most_frequent_count = 0
        # most_frequent_even_elements = [] # For Handling Ties we store all ties

        # for element in most_frequent_elements:
        #     if element[0]%2 == 0: # Even
        #         if most_frequent_count == 0: # Storing most_frequent_count for only one time
        #             most_frequent_count = element[1]
        #             most_frequent_even_elements.append(element[0])
        #         elif most_frequent_count == element[1]:
        #             most_frequent_even_elements.append(element[0])
        
        # # Sort ascending so we get smaller ones first
        # most_frequent_even_elements.sort()
        
        # return most_frequent_even_elements[0] if most_frequent_even_elements else -1       
        
        # Count and filter even numbers
        even_nums_counter = Counter(num for num in nums if num%2 == 0)

        if not even_nums_counter:
            return -1
        
        ''' Find the most frequent even number
        x[1] is the count of occurrences of the number, so maximizing based on this value prioritizes numbers with higher frequencies.
        -x[0] is the negated even number itself, which means that among numbers with equal frequencies, the smaller number is prioritized. 
        default=(-1, -1): This argument specifies a default value to return if even_counts.items() is empty (which would happen if there are no even numbers in the original list).
        most_frequent_even, _ =: This part uses tuple unpacking to extract the most frequent even number from the (key, value) pair returned by max(). The underscore _ is used to ignore the second element of the pair (the count), as it's not needed for the final result.
        '''
        most_frequent_even, _ = max(even_nums_counter.items(), key=lambda x: (x[1], -x[0]), default=(-1, -1))
        
        return most_frequent_even 

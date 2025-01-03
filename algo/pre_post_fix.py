def productExceptSelf(nums):
    n = len(nums)
    
    # Initialize two arrays to store prefix and suffix products
    prefix = [1] * n
    suffix = [1] * n
    result = [0] * n
    
    # Compute prefix products
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
        # print(prefix[])
    # Compute suffix products
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
        print(suffix[i])
    
    # Compute result using prefix and suffix products
    for i in range(n):
        result[i] = prefix[i] * suffix[i]
    
    return result

# Example usage
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]

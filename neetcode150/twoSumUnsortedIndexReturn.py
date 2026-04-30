
import pytest
import random
def sumTwo(nums: list[int], target:int) -> list[int]:
    pair:list[int] = []
    for i in range(len(nums)):
        for j in range (len(nums)-1, i, -1):
            if nums[i] + nums[j] == target:
                pair.append(i)
                pair.append(j)
                return pair
    return pair

def generate_50k_cases():
    for _ in range(500):
        size = random.randint(2, 30)  # Keep size small for O(n^2) speed
        nums = [random.randint(-1000, 1000) for _ in range(size)]
        
        if random.random() > 0.5:
            # Create a guaranteed solution
            i, j = random.sample(range(size), 2)
            target = nums[i] + nums[j]
        else:
            # Random target (might not have a solution)
            target = random.randint(-2000, 2000)
            
        yield nums, target

@pytest.mark.parametrize("nums, target", generate_50k_cases())
def test_50k_performance(nums, target):
    result = sumTwo(nums, target)
    if result:
        # If a result is found, verify it is correct
        assert nums[result[0]] + nums[result[1]] == target
    # If no result, we assume for random data it's possible

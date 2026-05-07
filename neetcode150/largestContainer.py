from typing import List
import pytest

def largest_container(heights: List[int]) -> int:
    # Write your code here
    left, right = 0, len(heights)-1
    
    maxWater = 0
    for left in range(len(heights)-1):
        maxWater = min(heights[left], heights[right]) * (right-left)
        if heights[right-left]>heights[left]:
            continue
        elif heights[right-left]<heights[left]:
            continue
        
            
    return maxWater
     
  




@pytest.mark.parametrize("heights, expected", [
    [[],0],
    [[1], 0],
    [[0,1,0], 0],
    [[3,3,3,3,3], 12],
    [[1, 2, 3], 2],
    [[3, 2, 1], 2],
    [[4,4,4,4], 12],
    [[1,1,4,4], 4],
    [[2, 7, 8, 3, 7, 6], 24]

])

def test_largest_container(heights, expected):
    assert largest_container(heights) == expected

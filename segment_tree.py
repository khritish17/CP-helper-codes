'''
Segment Tree is used when we need to find something within
a range in a list. e.g. given a list find the maximum element
between a given valid range

This class represents a Segment Tree data structure.

Attributes:
    nums (list): The original list of numbers.
    segment_tree (list): The segment tree representation of the list.
    default_conditional_value (float): 
        The default value used when a range doesn't overlap with the current node.
        (For finding maximum, it's set to negative infinity.)

'''
class SegmentTree:
    def __init__(self, nums) -> None:
        self.nums = nums
        self.segment_tree = [None] * 4 * (len(self.nums))
        self.default_conditional_value = -float('inf')
        self.build_tree()
    
    def condition(self, recursive_call1, recursive_call2):
        return max(recursive_call1, recursive_call2)
    
    def build_tree(self):
        
        def recursive(index, l_range, r_range):
            if l_range == r_range:
                self.segment_tree[index] = self.nums[l_range]
                return self.segment_tree[index]
            mid = l_range + (r_range - l_range)//2
            self.segment_tree[index] = self.condition(recursive((2 * index) + 1, l_range, mid), recursive((2 * index) + 2, mid + 1, r_range) )
            return self.segment_tree[index]

        recursive(0, 0, len(self.nums) - 1)
    
    def find(self, l_range, r_range):
        if l_range > r_range:
            print("Error: In find(l_range, r_range):\n\texpected: l_range <= r_range but received l_range > r_range")
            exit()
    
        def recursive(index, l_curRange, r_curRange):
            if l_range <= l_curRange <= r_curRange <= r_range:
                # completely lies inside
                return self.segment_tree[index]
            elif (l_curRange <= r_curRange < l_range <= r_range) or (l_range <= r_range < l_curRange <= r_curRange):
                # it does not lie
                return self.default_conditional_value
            else:
                # it overlaps
                mid = l_curRange + (r_curRange - l_curRange)//2
                return self.condition(recursive((2*index)+ 1, l_curRange, mid), recursive((2*index)+ 2, mid + 1, r_curRange))

        return recursive(0, 0, len(self.nums) - 1)
    
# # example
# S = SegmentTree([3,9,6,2,5,1,0])
# print(S.find(5, 6))
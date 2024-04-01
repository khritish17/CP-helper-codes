
class FenwickTree:
    def __init__(self, nums):
        self.nums = nums
        self.fenwick = [0]*(len(nums) + 1)
        self.length = len(self.fenwick)
        # write the initiate the fenwick tree
        for i, ele in enumerate(self.nums):
            index = i + 1
            while index < self.length:
                self.fenwick[index] += ele
                index  = index + (index & (-index))

    def update(self, index, ele):
        diff = ele - self.nums[index]
        self.nums[index] = ele
        index += 1
        while index < self.length:
            self.fenwick[index] += diff
            # go to its next index
            index  = index + (index & (-index))

    def prefix_sum(self, index):
        index += 1
        pre_sum = 0
        while index > 0:
            pre_sum += self.fenwick[index]
            # go to its parent index
            index -= index & (-index)
        return pre_sum

    def range_sum(self, left_index, right_index):
        return self.prefix_sum(right_index) - self.prefix_sum(max(0, left_index - 1))

# example:
# F = FenwickTree([1, 2, 3, 4, 5])
# print(F.prefix_sum(4))
# F.update(1, 4)
# print(F.prefix_sum(4))
# print(F.range_sum(1, 4))
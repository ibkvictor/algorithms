    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        postfix = []
        for i in range(len(nums)):
            j = - i - 1
            if i == 0:
                prefix.append(nums[i])
                postfix.append(nums[j])
            else:
                prefix.append(nums[i] * prefix[i - 1])
                postfix = [nums[j] * postfix[j + 1]] + postfix
            
        for val in range(len(nums)):
            if val == 0:
                res.append(postfix[val + 1])
            elif val == len(nums) - 1:
                res.append(prefix[val - 1])
            else:
                res.append(prefix[val - 1] * postfix[val + 1])
        return res

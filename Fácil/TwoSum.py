class Solution(object):
    def twoSum(self, nums, target):
        for indice,n1 in enumerate(nums):
            for indice2,n2 in enumerate(nums):
                if n1 + n2 == target and indice != indice2:
                    return [indice,indice2]
        
exemplo01 = Solution()
exemplo01.twoSum([-3,4,3,90],0)

#Complexidade O(n)
class Solution02(object):
    def twoSum(self, nums, target):
        mapa = {} 
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in mapa:
                return [mapa[complemento], i]
            mapa[num] = i

exemplo02 = Solution()
exemplo02.twoSum([-3,4,3,90],0)
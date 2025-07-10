class Solution(object):
    def maximumWealth(self, accounts):
        rico = 0
        for clientes in accounts:
            valor = 0
            for conta in clientes:
                valor+=conta
                if valor >= rico:
                    rico = valor
        return rico
        
exemplo = Solution()
print(exemplo.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

exemplo = Solution()
print(exemplo.maximumWealth([[1,5],[7,3],[3,5]]))

exemplo = Solution()
print(exemplo.maximumWealth([[1,2,3],[3,2,1]]))


"""
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(acc) for acc in accounts])

"""
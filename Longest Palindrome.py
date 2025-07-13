class Solution(object):
    def longestPalindrome(self, s):
        letras = {}
        for letra in s:
            if letra in letras:
                letras[letra] +=1
            else:
                letras[letra] = 1
        tamanho = 0
        impar = False
        for chave,valor in letras.items():
            if valor % 2 == 0:
                tamanho+=valor
            else:
                tamanho+=valor
                if not impar:
                    impar = True
                else:
                    tamanho -=1
        return print(tamanho)

        
teste = Solution()
teste.longestPalindrome("aaaabbbbcccc")
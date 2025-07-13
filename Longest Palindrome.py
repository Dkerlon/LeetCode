class Solution():
    def longest_palindrome(self,s):
        tamanho = {}
        for letra in s:
            if letra in tamanho:
                tamanho[letra]+=1
            else:
                tamanho[letra] = 1
        impar = False
        maior_palindromo =  0

        for chave,valor in tamanho.items():
            if valor / 2 == 0:
                maior_palindromo+=valor
            else:
                impar == True
                maior_palindromo+=valor

                if impar:
                    maior_palindromo-=1
        print(maior_palindromo)

exemplo = Solution()
exemplo.longest_palindrome("lalaklalabla")
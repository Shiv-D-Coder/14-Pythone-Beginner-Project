'''
PROJECT 14 : Roman to decimal convetar

Remember that the base numbers are not the numbers that are used by the Romans 
as they have count values such as 
     I: 1, V: 5, X: 10, C: 100, D: 500, M: 1000

'''

#  C  O  D  E

class Solition:
    def convert(self,str):
        containar={"I":1 ,"V":5 ,"X":10 ,"L":50 ,'C':100 ,"D":500 ,"M":1000}
        
        res = 0
        for i in range(len(str)):
            if i + 1< len(str) and containar[str[i]] > containar[str[i + 1]]:
                res -= containar[str[i]]
                
            else:
                res += containar[str[i]] 
                
            return res
        
obj = Solition()
print(obj.convert("CM"))          
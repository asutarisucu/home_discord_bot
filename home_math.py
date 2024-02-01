from discord import Interaction
async def Math(interaction,num1:int,text:str,num2:int):
    ans:int={
        '+':num1+num2,
        '-':num1-num2,
        '*':num1*num2,
        '/':num1/num2
    }
    if ans in text:
        return ans
    else:
        return "null"
    
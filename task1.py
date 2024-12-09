def strict(func):
    def wrapped_one(*args, **kwargs):
        #agrs assurance
        checker_args = tuple(func.__annotations__.values())
        for i in range(len(args)):
            if type(args[i]) != checker_args[i]:
                raise TypeError
            
        #output assurance    
        result = func(*args)
        if type(result) != checker_args[-1]:
            raise TypeError
        return result
    return wrapped_one

@strict
def summ(a:int, b:int) -> int:
    return a + b 

@strict
def inverse_bool(t:bool) -> bool:
    if t == True:
        return False
    return True

@strict
def trunc_down(number:float) -> int:
    return int(number)

@strict
def concetinate(first_str:str, second_str:str) -> str:
    return first_str + second_str

@strict
def something(a:bool, b:int, c:str) -> float:
    return 2.28

#не уверен, как pythonic way тестить декораторы
#пока просто прогоню все функции и првоверю, что ошибок нет

print(summ(2,3))
print(inverse_bool(True))
print(trunc_down(2.5))
print(concetinate("aba", "brrrrr"))
print(something(False, 8, "arara"))
def suma(num1: int, num2: int) -> int:
    return num1 + num2


def resta(num1: int, num2: int) -> int:
    return num1 - num2

def gato(animal:str):
    if animal == 'cat':
        return True
    else:
        return False


if __name__ == '__main__':
    print(suma(num1=2, num2=4))
    print(resta(num1=2, num2=4))
    print(gato(animal='cat'))


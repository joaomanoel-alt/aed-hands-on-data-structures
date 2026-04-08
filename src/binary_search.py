from src.my_array import MyArray


def binary_search(array: MyArray, target: int) -> int:
    """
    Realiza busca binária em um array ordenado.

    Deve retornar o índice do elemento ou -1 caso não encontrado.
    """
    esquerda = 0
    direita = len(array) -1
    
    while esquerda <= direita:
        mid = (esquerda + direita) // 2
        
        if array[mid] == target: 
            return mid
        elif array[mid] < target:
            esquerda = mid + 1
        else:
            direita = mid - 1
    return -1

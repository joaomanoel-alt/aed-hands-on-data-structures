from src.array import Array


class MyArray(Array):
    """
    Implementação concreta do TAD Array.
    """

    def __init__(self) -> None:
        self.data: list[int] = []

    def append(self, value: int) -> None:
        self.data.append(value)

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.data):
            raise IndexError("Índice inválido")
        return self.data[index]

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= len(self.data):
            raise IndexError("Índice inválido")
        self.data[index] = value

    def remove(self, value: int) -> None:
        if value not in self.data:
            raise ValueError("Valor não encontrado")
        self.data.remove(value)

    def insert(self, index: int, value: int) -> None:
        if index < 0 or index > len(self.data):
            raise IndexError("Índice inválido")
        self.data.insert(index, value)

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> int:
        return self.get(index)

    def __setitem__(self, index: int, value: int) -> None:
        self.set(index, value)

    def __repr__(self) -> str:
        return repr(self.data)

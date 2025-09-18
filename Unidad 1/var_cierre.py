def crear_contador():
    count = 0

    def icrementar():
        nonlocal count
        count += 1
        return count
    return icrementar
contador = crear_contador()
print(contador())  # Output: 1
print(contador())  # Output: 2
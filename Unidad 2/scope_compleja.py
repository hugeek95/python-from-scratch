x = "global"

def externa():
    x = "enclosing"

    def interna():
        x = "local"
        print("Interna:", x)

    interna()
    print("Externa:", x)

externa()
print("Global:", x)

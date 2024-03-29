from TDA.Cola import Cola
from TDA.Lista import Lista
from TDA.Pila import Pila
from TDA.Nodo import Nodo

ColaBanco = Cola()
PilaLibros = Pila()
ListaInventario = Lista()

Ejemplo = input()
if Ejemplo == 'Pila':
    #Trabajemos con la pila de libros
    print(PilaLibros.Impimir())

    PilaLibros.Push("Harry Potter y el prisionero de Sauron")

    print(PilaLibros.Impimir())

    PilaLibros.Push("Terminator Legacy of Matrix")

    print(PilaLibros.Impimir())

    PilaLibros.Push("Los juegos del hambre en llamas")

    print(PilaLibros.Impimir())

    PilaLibros.Pop()
    print(PilaLibros.Impimir())
    PilaLibros.Pop()
    PilaLibros.Pop()
    print(PilaLibros.Impimir())
    PilaLibros.Pop()
    print(PilaLibros.Impimir())

elif Ejemplo == 'Cola':
    #Trabajaremos con una cola de un banco
    ColaBanco.Insertar('Josue Martinez')
    print(ColaBanco.Impimir())
    ColaBanco.Pop()
    print(ColaBanco.Impimir())
    ColaBanco.Insertar('Josue Martinez')
    print(ColaBanco.Impimir())
    ColaBanco.Insertar('Maria Flores')
    print(ColaBanco.Impimir())
    ColaBanco.Insertar('Marta Sanchez')
    print(ColaBanco.Impimir())
    print("Se va del banco:",ColaBanco.Pop().ObtenerDato())
    print(ColaBanco.Impimir())
    print("Fue atendido ", ColaBanco.Pop().ObtenerDato())
    print(ColaBanco.Impimir())
    ColaBanco.Pop()
    print(ColaBanco.Impimir())
    ColaBanco.Pop()
    print(ColaBanco.Impimir())
elif Ejemplo == 'Lista':
    print(ListaInventario.Impimir())
    ListaInventario.Push('1xTronco')
    print(ListaInventario.Impimir())
    ListaInventario.Pop()
    print(ListaInventario.Impimir())
    ListaInventario.Push('4xMadera')
    print(ListaInventario.Impimir())
    ListaInventario.Pop()
    print(ListaInventario.Impimir())
    ListaInventario.Push('1xMesa de Crafteo')
    print(ListaInventario.Impimir())
    ListaInventario.Push('1xTronco')
    print(ListaInventario.Impimir())
    ListaInventario.Push('1xTronco')
    print(ListaInventario.Impimir())
    ListaInventario.Pop()
    print(ListaInventario.Impimir())
    ListaInventario.Push('4xPalo')
    print(ListaInventario.Impimir())
    ListaInventario.EliminarIndice(1)
    print(ListaInventario.Impimir())
    ListaInventario.Insertar('4xMadera')
    print(ListaInventario.Impimir())
    ListaInventario.EliminarIndice(1)
    print(ListaInventario.Impimir())
    ListaInventario.Pop()
    print(ListaInventario.Impimir())
    ListaInventario.Pop()
    print(ListaInventario.Impimir())
    ListaInventario.Push('2xPalo')
    print(ListaInventario.Impimir())
    ListaInventario.Insertar('1xPico de Madera')
    print(ListaInventario.Impimir())
    ListaInventario.Insertar('1xPiedra')
    print(ListaInventario.Impimir())
    ListaInventario.Push('1xCarbón')
    print(ListaInventario.Impimir())
    ListaInventario.Pop()
    print(ListaInventario.Impimir())
    ListaInventario.Pop()
    print(ListaInventario.Impimir())
    ListaInventario.Push('1xPalo')
    print(ListaInventario.Impimir())
    ListaInventario.Push('4xAntorcha')
    print(ListaInventario.Impimir())
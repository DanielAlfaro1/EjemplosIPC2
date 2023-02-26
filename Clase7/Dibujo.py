from TDA.ColaDibujo import ColaDibujo
import subprocess

def Dibujar(FichasActuales, FichasContrarias, PosComestibles):
    LimiteVertical = FichasActuales.LimiteVertical
    LimiteHorizontal = FichasActuales.LimiteHorizontal

    ListaElementosDibujar = ColaDibujo(LimiteVertical, LimiteHorizontal)
    for rows in range(LimiteVertical):
        for cols in range(LimiteHorizontal):
            #Verificar si en esta posicion hay ficha del que va a comer
            if FichasActuales.BuscarPosicion(rows, cols):
                if cols-1 >= 0 and rows-1 >= 0:
                    ListaElementosDibujar.Insertar(cols-1, rows-1, 'White', 'Black')
                if rows-1 >= 0:
                    ListaElementosDibujar.Insertar(cols, rows-1, 'White', 'Black')
                if rows-1 >= 0 and cols+1 < LimiteHorizontal:
                    ListaElementosDibujar.Insertar(cols+1, rows-1, 'White', 'Black')
                if cols-1 >= 0:
                    ListaElementosDibujar.Insertar(cols-1, rows, 'White', 'Black')

                #Quiero Graficar la ficha
                ListaElementosDibujar.Insertar(cols, rows, FichasActuales.Color, 'Black')

                if cols+1 < LimiteHorizontal:
                    ListaElementosDibujar.Insertar(cols+1, rows, 'White', 'Black')
                if rows+1 < LimiteVertical and cols-1 >= 0:
                    ListaElementosDibujar.Insertar(cols-1, rows+1, 'White', 'Black')
                if rows+1 < LimiteVertical:
                    ListaElementosDibujar.Insertar(cols, rows+1, 'White', 'Black')
                if rows+1 < LimiteVertical and cols+1 < LimiteHorizontal:
                    ListaElementosDibujar.Insertar(cols+1, rows+1, 'White', 'Black')
            elif FichasContrarias.BuscarPosicion(rows, cols):
                if cols-1 >= 0 and rows-1 >= 0:
                    ListaElementosDibujar.Insertar(cols-1, rows-1, 'White', 'Black')
                if rows-1 >= 0:
                    ListaElementosDibujar.Insertar(cols, rows-1, 'White', 'Black')
                if rows-1 >= 0 and cols+1 < LimiteHorizontal:
                    ListaElementosDibujar.Insertar(cols+1, rows-1, 'White', 'Black')
                if cols-1 >= 0:
                    ListaElementosDibujar.Insertar(cols-1, rows, 'White', 'Black')

                #Quiero Graficar la ficha
                if PosComestibles.BuscarPosicion(rows, cols):
                    ListaElementosDibujar.Insertar(cols, rows, FichasContrarias.Color, 'Green')
                else:
                    ListaElementosDibujar.Insertar(cols, rows, FichasContrarias.Color, 'Black')

                if cols+1 < LimiteHorizontal:
                    ListaElementosDibujar.Insertar(cols+1, rows, 'White', 'Black')
                if rows+1 < LimiteVertical and cols-1 >= 0:
                    ListaElementosDibujar.Insertar(cols-1, rows+1, 'White', 'Black')
                if rows+1 < LimiteVertical:
                    ListaElementosDibujar.Insertar(cols, rows+1, 'White', 'Black')
                if rows+1 < LimiteVertical and cols+1 < LimiteHorizontal:
                    ListaElementosDibujar.Insertar(cols+1, rows+1, 'White', 'Black')
    ListaElementosDibujar.GenerarDibujo()
    cmd_str = "dot -Tsvg -O ./Clase7/Dibujo.dot"
    subprocess.run(cmd_str, shell=True)
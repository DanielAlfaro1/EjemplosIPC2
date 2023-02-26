from .NodoDibujo import NodoDibujo

class ColaDibujo:

    def __init__(self, LimiteVertical, LimiteHorizontal):
        self.LimiteVertical = LimiteVertical
        self.LimiteHoritontal = LimiteHorizontal
        self.Cabeza = None
        self.Cola = None

    def Insertar(self, Columna, Fila, Color, Borde):
        NuevoNodo = NodoDibujo(Columna, Fila, Color, Borde)
        if self.Cabeza == None:
            self.Cabeza = NuevoNodo
            self.Cola = NuevoNodo
        else:
            Auxiliar = self.Cabeza
            while Auxiliar != None:
                if Auxiliar.ObtenerColumna() == Columna and Auxiliar.ObtenerFila() == Fila:
                    #Si entramos acá, quiere decir que existe la posicon almacenada
                    if Color != 'White':
                        #Solo quiero el color si es negro o rojo
                        Auxiliar.setColor(Color)
                    if Auxiliar.ObtenerBorde() == 'Black':
                        #Solo si el borde es negro, quiero cambiarlo, si el borde es verde se queda igual
                        Auxiliar.setBorde(Borde)
                    return
                Auxiliar = Auxiliar.Siguiente
            #Si llegamos acá quiere decir que no existe ninguna ficha en la posicion ingresada
            self.Cola.Siguiente = NuevoNodo
            self.Cola = NuevoNodo
    
    def GenerarDibujo(self):
        Texto = "digraph {\n"
        Texto = Texto + "\ttbl [\n"
        Texto = Texto + "\t\tshape=plaintext\n"
        Texto = Texto + "\t\tlabel=<\n"
        Texto = Texto + "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
        ContFilaVacia = 0
        for i in range(self.LimiteVertical):
            ListaFila = self.ObtenerTodaLaFila(i)
            if ListaFila.Cabeza != None:
                if ContFilaVacia > 0:
                    Texto = Texto + "\t\t\t\t<tr>\n"
                    Texto = Texto + "\t\t\t\t\t<td colspan='"+str(self.LimiteHoritontal)+"'>...</td>\n"
                    Texto = Texto + "\t\t\t\t</tr>\n"
                ContFilaVacia = 0
                Texto = Texto + "\t\t\t\t<tr>\n"
                ContColumnaVacia = 0
                for j in range(self.LimiteHoritontal):
                    Auxilar = ListaFila.ObtenerEnColumna(j)
                    if Auxilar != None:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        ContColumnaVacia = 0
                        if Auxilar.ObtenerBorde() == 'Green':
                            Texto = Texto + "\t\t\t\t\t<td bgcolor='"+str(Auxilar.ObtenerColor())+"'><font color='lightblue'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='Green'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>"+str(Auxilar.ObtenerFila())+","+str(Auxilar.ObtenerColumna())+"</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        else:
                            Texto = Texto + "\t\t\t\t\t<td bgcolor='"+str(Auxilar.ObtenerColor())+"'><font color='lightblue'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='"+str(Auxilar.ObtenerColor())+"'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>"+str(Auxilar.ObtenerFila())+","+str(Auxilar.ObtenerColumna())+"</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                    else:
                        ContColumnaVacia = ContColumnaVacia + 1
                    if j+1 == self.LimiteHoritontal:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                Texto = Texto + "\t\t\t\t</tr>\n"
            else:
                ContFilaVacia = ContFilaVacia + 1
                if i + 1 == self.LimiteVertical:
                    if ContFilaVacia > 0:
                        Texto = Texto + "\t\t\t\t<tr>\n"
                        Texto = Texto + "\t\t\t\t\t<td colspan='"+str(self.LimiteHoritontal)+"'>...</td>\n"
                        Texto = Texto + "\t\t\t\t</tr>\n"
        Texto = Texto + "\t\t\t</table>\n"
        Texto = Texto + "\t\t>];\n"
        Texto = Texto + "}\n"
        Destino = open('./Clase7/Dibujo.dot', 'w')
        Destino.write(Texto)
        Destino.close()
    
    def ObtenerTodaLaFila(self, Fila):
        ListaFila = ColaDibujo(self.LimiteVertical, self.LimiteHoritontal)
        Aux = self.Cabeza
        while Aux != None:
            if Aux.ObtenerFila() == Fila:
                ListaFila.Insertar(Aux.ObtenerColumna(), Aux.ObtenerFila(), Aux.ObtenerColor(), Aux.ObtenerBorde())
            Aux = Aux.Siguiente
        return ListaFila
    
    def ObtenerEnColumna(self, Columna):
        Aux = self.Cabeza
        while Aux != None:
            if Aux.ObtenerColumna() == Columna:
                return Aux
            Aux = Aux.Siguiente
        return None
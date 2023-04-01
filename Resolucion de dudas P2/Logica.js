clase nodo {
    constructor();

    imprimirContenido(){
        return self.Texto;
    }
}

clase Lista {
    constructor();

    insertar();

    imprimirTexto(){
        aux = self.devolverInicio();
        texto = "";
        while (aux != null){
            texto = texto + aux.imprimirContenido();
            texto = texto + "\n";
            aux = aux.siguiente;
        }
        return texto;
    }

    devolverInicio(){
        return inicio;
    }
}




class ventana{

    

    root = Tk()
    root.resizable(False, False)
    root.title("Text Widget Example")

    text = Text(root, height=8)

    TextoTxt = Lista.imprimirTexto();

    text.insert('1.0', TextoTxt);

    text.pack()


    root.mainloop()


    

    nombre = ['Computadora1', 'Servidor', 'Computadora portátil']
    ipcode = ['10.13.71.223','10.25.61.186','10.25.11.163']
    MiLista = Lista();
    i = 0; 
    aux = MiLista.devolverInicio();
    while (aux != None) {
        treeview.insert('', i, vales = (aux.nombre, aux.ipcode))
        aux = aux.siguiente;
        i++;
    }

    para i en rango (min (len (nombre), len (ipcode))): # escribir datos
    treeview.insert('', i, values=(name[i], ipcode[i]))
    root.mainloop () # ingrese el bucle de 
}

Ando trabado con los de analizar los compuestos y los pines, pero pues es algo mas logico no se si podrias darme una idea 

class ListaMaquina{
    constructor(){
        self.Inicio = null
        self.Final = null
    };

    insertar(valorx){
        Maquinita = new Maquina(valorx);
        aux = self.Inicio; 
        if (aux == null){
            self.Inicio = Maquinita
            self.Final = Maquinita
            return;
        }
        while (aux.Siguiente != null){
            aux = aux.Siguiente
        }
        aux.Siguiente = Maquinita;
        self.Final = Maquinita
    }

    insertarPin(numero){
        if (self.Final != null) {
            self.Final.insertarPin(numero)
        }
    }
    
    insertarElementoEnPin(Simbolo){
        if (self.Final != null){
            self.Final.insertarElementoEnPin(Simbolo)
        }
    }
}

class Maquina{
    constructor(valorx){
        Nombre = valorx;
        self.Siguiente = None;
        self.ListaPines = new ListaPin()
    };

    insertarPin(numero) {
        self.ListaPines.insertar(numero);
    }

    insertarElementoEnPin(Simbolo) {
        self.ListaPines.insertarElementoEnPin(Simbolo);
    }

    Fusionar(ListaElementos){
        //Revisar Si la lista de elementos contiene solo elementos que pueda analizar esta máquina
            //si no descartar
        //Recorrer ListaElementos
            //CrearLista de trabajo para pines (Elementos que puede trabajar x pin)
            //Colnar ListaElmentos en Trabajo
        //while true
            //Terminamos el trabajo? Trabajo.inicio == null
                //break;
            //Elemento a trabajar = Trabajo.inicio
            //Recorrer pines
                //Preguntar que pin tiene este elemento.
                //PReguntar si el pin está listo para fusionar
                    //Fusionar
                    //Sino Desplazar
                //recorrer ListaTrabajoPines
                    //PinX tienees el elemento ListaTrabajoPin.Inicio
                        //Lo tienes listo?
                            //Esperar
                            //Desplazar

    }

}

class ListaPin{
    constructor(){
        self.Inicio = null;
        self.Final = null;
    };

    insertar(numero){
        Pinito = new Pin(numero);
        aux = Inicio; 
        if (aux == null){
            self.Inicio = Pinito
            self.Final = Pinito
            return;
        }
        while (aux.Siguiente != null){
            aux = aux.Siguiente
        }
        aux.Siguiente = Pinito
        self.Final = Pinito;
    }

    insertarElementoEnPin(Simbolo){
        if self.Final != null {
            self.Final.insertarElemento(Simbolo);
        }
    }
}

class Pin{
    constructor(numero){
        self.numero = numero
        self.Siguiente = null
        self.ListaElementos = new ListaElementoPin();
    }


    insertarElemento(Simbolo) {
        self.ListaElementos.insertar(Simbolo);
    }

}

class ListaElementoPin{
    constructor(){
        self.Inicio = null
    }

    insertar(Simbolo){
        Elementito = new Elemento(Simbolo)

        aux = self.Inicio
        if aux == null{
            aux = Elementito
        } else {
            while (aux.Siguiente != null){
                aux = aux.Siguiente
            }
            aux.Siguiente = Elementito
            Elementito.Anterior = aux           
        }
    }
}

class Elemento {
    constructor(Simbolo){
        self.Simbolo = Simbolo //Li, He, H
        self.Siguiente = null
        self.Anterior = null
    }
}

MiListaMaqinas = new ListaMaquina()

MiListaMaqinas.insertar("Maquina1");
MiListaMaqinas.insertarPin(1);
MiListaMaqinas.insertarElementoEnPin("He")
MiListaMaqinas.insertarElementoEnPin("H")
MiListaMaqinas.insertarElementoEnPin("O")
MiListaMaqinas.insertarElementoEnPin("As")
MiListaMaqinas.insertarPin(2);
MiListaMaqinas.insertarElementoEnPin("Fe")
MiListaMaqinas.insertarElementoEnPin("C")
MiListaMaqinas.insertarElementoEnPin("Mg")
MiListaMaqinas.insertarElementoEnPin("Cu")

MiListaMaqinas.insertar("Maquina2");
MiListaMaqinas.insertarPin(1);
MiListaMaqinas.insertarElementoEnPin("He")
MiListaMaqinas.insertarElementoEnPin("C")
MiListaMaqinas.insertarElementoEnPin("O")
MiListaMaqinas.insertarElementoEnPin("Mg")
MiListaMaqinas.insertarPin(2);
MiListaMaqinas.insertarElementoEnPin("Fe")
MiListaMaqinas.insertarElementoEnPin("H")
MiListaMaqinas.insertarElementoEnPin("As")
MiListaMaqinas.insertarElementoEnPin("Cu")

MiListaCompuestos = new ListadeCompuesto()
MiListaCompuestos.insertar("Feralio")
MiListaCompuestos.insertarElemento("He")
MiListaCompuestos.insertarElemento("H")
MiListaCompuestos.insertarElemento("Mg")
MiListaCompuestos.insertarElemento("Mg")
MiListaCompuestos.insertarElemento("He")

ListaAAnalizar = MiListaCompuestos.DevolverListaElementos_Compuesto("Feralio")




class ListadeCompuesto{
    constructor(){
        self.Inicio = null
    }

    insertar(Nombre){
        Compuestito = new Compuesto(Nombre)
        aux = self.Inicio
        if (aux == null){
            self.Inicio = Compuestito
        } else {
            while (aux.Siguiente != null){
                aux = aux.Siguiente
            }
            aux.Siguiente = Compuestito
        }
    }

    insertarElemento(Simbolo){
        aux = self.Inicio
        if (aux != null){
            while(aux.siguiente != null){
                aux = aux.siguiente
            }
            aux.insertarElemento(Simbolo)
        }
    }

    DevolverListaElementos_Compuesto(Nombre){
        aux = self.Inicio
        if (aux == null){
            return null
        } else {
            while(aux!=null){
                if (aux.Nombre == Nombre) {
                    aux.DevolverListaElementos()
                }
                aux = aux.Siguiente
            }
            return null
        }
    }
}

class Compuesto{
    constructor(Nombre){
        self.Nombre= Nombre;
        self.Siguiente = null
        self.ListaElementos = ListaElementosDeCompuesto()
    }

    insertarElemento (Simbolo){
        self.ListaElementos.insertar(Simbolo)
    }

    DevolverListaElementos(){
        return self.ListaElementos;
    }
}


class ListaElementosDeCompuesto {
    constructor(){
        self.Inicio = null
    }

    insertar(Simbolo){
        if RevisarExistencia(Simbolo) == true{
            //YA EXISTE
            return
        }
        Elementito = new Elemento(Simbolo)
        aux = self.Inicio
        if (aux == null){
            self.Inicio = Elementito
        } else {
            while (aux.Siguiente != null){
                aux = aux.Siguiente
            }
            aux.Siguiente = Elementito
            Elementito.Anterior = aux
        }
    }

    RevisarExistencia(Simbolo){
        aux = self.Inicio
        while (aux != null){
            if (aux.Simbolo == Simbolo){
                return true
            }
            aux = aux.Siguiente
        }
        return false
    }
}




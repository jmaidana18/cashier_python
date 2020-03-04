# Testing - Doc Tests()

from decimal import *
import numpy as np
import doctest

class Product():
    """ Clase que ayuda a estructurar un producto en venta 
    
    Atributos:
    
    Desc-> Descripcion
    Price-> Precio
    Tax-> Valor de impuesto.
    Imported -> Variable booleana que informa la calidad de importado o no.
    Exen - > Booleano que informa sobre  la calidad de exento de impuesto o no.
    
    """
    def __init__(self, desc, price,ip_boolean,ex_boolean):
        self.desc = desc
        self.price = Decimal(price)
        self.tax = 0
        self.imported = ip_boolean
        self.exen = ex_boolean
            
    def cal_tax(self):
        """Calcula el Impuesto para Cada instancia de Product()"""
        if self.imported:
            self.tax += self.price* Decimal(0.05)
        if self.exen:
            self.tax += 0
        else:
            self.tax += self.price * Decimal(0.1)
        # la siguiente linea evita lidiar con casos complejos con valores Decimal() en la subrutina
        if self.tax-int(self.tax) > 0 :
            self.tax = round_up(self.tax-int(self.tax)) + int(self.tax)
        return(self.tax)
    
    
            
    def __str__(self):
        return ("Objeto de Tipo Producto")
            
class Register():
    """ Clase que permite registrar movimientos en Caja 
    
    Atributos:
    
    Quantity -> Cantidad
    Product -> Instancia de Objeto de Tipo Producto
    Line_Total -> Subtotal en Euros de Boleta Comercial Emitida por Linea
    
    """
    
    def __init__(self,quantity,product):
        self.quantity = quantity
        self.product = product
        self.line_total = Decimal(self.quantity) * Decimal(product.cal_tax())
    
    def __str__(self):
        return("Objeto de Tipo Registro")


######### Auxiliar Methods #########

def sale_print(entrada):
    """Metodo regular que imprime las ventas generadas 
    
    total_tax -> variable que acumula total de impuestos por registro de venta.
    sumal_total-> total de venta con impuestos.
    
    entrada : Coleccion de Objetos de Tipo Register()
    
    """
    
    total_tax = 0
    suma_total = 0
    try:
        for item in entrada:
            print (item.quantity,item.product.desc, ":", format(item.product.price + item.line_total, '.2f'))
            total_tax  += item.line_total
            suma_total +=  item.product.price + item.line_total
        print ("Impuestos:", format(total_tax, '.2f'))
        print("Total:", format(suma_total, '.2f'))
    except (TypeError):
        print("ERROR: Por favor ingrese una coleccion de Registros o factura[limite inferior:superior] para imprimir "+
              "un solo Registro()")

    
def round_up(valor):
        """Metodo regular: Ajusta los valores impositivos al 0.05% hacia arriba
        
        valor -> Variable con un valor decimal
        valores -> lista de valores 0, 0.05, 0.1, ...1
        
        retorno: valor decimal ajustado a 0.05%
        
        """
        valores = np.arange(0,1, 0.05).tolist()
        valor = round(valor, 2)
        for elemento in valores:
            if valor == elemento:
                return valor
            if valor < elemento:
                return (elemento)

######### Harcoded Data Set #########
def main():
    """Punto de Entrada del Programa 
        ----DocTest----
    >>> libro = Product("libro",12.49, False , True)
    >>> pelicula = Product("pelicula en DVD", 14.99, False, False)
    >>> factura = []
    >>> factura.append( Register('1', libro))
    >>> factura.append( Register('1', pelicula))
    >>> sale_print(factura[:1])
    1 libro : 12.49
    Impuestos: 0.00
    Total: 12.49
    >>> sale_print(factura[1])
    ERROR: Por favor ingrese una coleccion de Registros o factura[limite inferior:superior] para imprimir un solo Registro()
    """
    
    libro = Product("libro",12.49, False , True)
    pelicula = Product("pelicula en DVD", 14.99, False, False)
    chocolate = Product("barrita de chocolate", 0.85, False, True)
    bombones = Product("caja de bombones de importación",10, True , True)
    perfume = Product("frasco de perfurme de importación", 47.50, True, False)
    perfume_import = Product("frasco de perfume de importación",27.99, True , False)
    perfume_local = Product("frasco de perfurme ", 18.99 , False, False)
    pastillas = Product("caja de pastillas para el estómago ", 9.75 , False, True)
    bombones_import = Product("caja de bombones importados",11.25, True , True)
    
    factura = []
    factura.append( Register('1', libro))
    factura.append( Register('1', pelicula))
    factura.append( Register('1', chocolate))
    factura.append( Register('1', bombones))
    factura.append( Register('1', perfume))
    factura.append( Register('1', perfume_import))
    factura.append( Register('1', perfume_local))
    factura.append( Register('1', pastillas))
    factura.append( Register('1', bombones_import))
    
    ######### OUTPUT 1 #########
    sale_print(factura[:3])
    ######### OUTPUT 2 #########
    print("")
    sale_print(factura[3:5])
    ######### OUTPUT 3 #########
    print("")
    sale_print(factura[5:9])
    
    
    doctest.testmod()
main()

######### Comentario sobre Estructuras Usadas #########
""" Para referir una coleccion de objetos Register() es mas sencillo escribir
    una coleccion list(), en terminos de legibilidad.
    
    Escribir codigo para dict() se complica al iterar la estructura en las distintas subrutinas
    probadas, al hacer referencias, se necesitan muchos accesos ilegibles en codigo.
    
    Sin embargo, al ejecutar tests, una factura podria consistir de un solo objeto lista de Register(),
    y las estructuras de datos que lidian en las subrutinas con los objetos, esperan una lista.
    
    Un simple elemento de lista se puede referir asi: lista[0], sin embargo, esto envia a las subrutinas
    una copia del contenido (en nuestro caso, un objeto de tipo Register()).
    
    Adicionalmente, un diccionario tiene mejor rendimiento que una lista, computacionalmente.
    
    El sacrificio hecho en el codigo, es de rendimiento por legibilidad.
    
    """
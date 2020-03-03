# Corregir Lista por Dict() hecho
# Usar metodo estatico calc_tax (probado)
# Corregir salida redondeada. 
# Testing
from decimal import *
import numpy as np

class Product():
    def __init__(self, desc, price,ip_boolean,ex_boolean):
        self.desc = desc
        self.price = Decimal(price)
        self.tax = 0
        self.imported = ip_boolean
        self.exen = ex_boolean
    def cal_tax(self):
        if self.imported:
            self.tax += self.price* Decimal(0.05)
        if self.exen:
            self.tax += 0
        else:
            self.tax += self.price * Decimal(0.1)
        if self.tax-int(self.tax) > 0 :
            self.tax = round_up(self.tax-int(self.tax)) + int(self.tax)
        return(self.tax)
    
    def __str__(self):
        return ("Objeto de Tipo Producto")
            
class Register():
    def __init__(self,quantity,product):
        self.quantity = quantity
        self.product = product
        self.line_total = Decimal(self.quantity) * Decimal(product.cal_tax())
        
    def __str__(self):
        return("Objeto de Tipo Registro")


def round_up(valor):
    valores = np.arange(0,1, 0.05).tolist()
    valor = round(valor, 2)
    for elemento in valores:
        if valor == elemento:
            return valor
        if valor < elemento:
            return (elemento)


def sale_print(entrada):
    total_tax = 0
    suma_total = 0
    for item in entrada:
#        print("Valor Prod", item.product.price)
#        print("Valor Tax", item.line_total)
#        print("Valor de Linea", item.product.price+item.line_total)
        print (item.quantity,item.product.desc, ":", format(item.product.price + item.line_total, '.2f'))
        total_tax  += item.line_total
        suma_total +=  item.product.price + item.line_total
    print ("Impuestos:", format(total_tax, '.2f'))
    print("Total:", format(suma_total, '.2f'))
#    print ("Impuestos:", total_tax)
#    print("Total:", suma_total)
    
# rutina ingrese productos CRUD Database

######### Harcoded Data Set #########
def main():
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
    
    # Register.sale_print = staticmethod(Register.sale_print)
    ######### OUTPUT 1 #########
    sale_print(factura[:3])
    ######### OUTPUT 2 #########
    print("")
    sale_print(factura[3:5])
    ######### OUTPUT 3 #########
    print("")
    sale_print(factura[5:9])

main()

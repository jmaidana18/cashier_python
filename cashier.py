# Corregir Lista por Dict()
# Usar metodo estatico calc_tax
# Corregir salida redondeada.
# Testing

class product():
    def __init__(self, desc, price,ip_boolean,ex_boolean):
        self.desc = desc
        self.price = price
        self.tax = 0
        self.imported = ip_boolean
        self.exen = ex_boolean
    def cal_tax(self):
        if self.imported:
            self.tax = self.tax + self.price* 0.05
        if self.exen:
            self.tax = self.tax + 0
        else:
            self.tax = self.tax + self.price*0.1

    def tax(self):
        return self.tax
    
    def __str__(self):
        return ("Objeto de Tipo Producto")
            
class register():
    def __init__(self,quantity,product):
        self.quantity = quantity
        self.product = product
#        self.subtotal = self.quantity*self.product + (product.tax())
        
def sale_printer(entrada):
    [item[1].product.cal_tax() for item in entrada.items()]
    total_tax = 0
    suma_total = 0
    for item in entrada.items():
        print (item[1].quantity,item[1].product.desc, ":", item[1].product.price + item[1].product.tax )
        total_tax = total_tax + item[1].product.tax
        suma_total = suma_total +  item[1].product.price + item[1].product.tax
    print ("Impuestos:", format(total_tax, '.2f'))
    print("Total:", format(suma_total, '.2f'))
# alternative do it with a dict:

# rutina ingrese productos CRUD Database

######### Harcoded Data Set #########

libro = product("libro",12.49, False , True)
pelicula = product("pelicula en DVD", 14.99, False, False)
chocolate = product("barrita de chocolate", 0.85, False, True)

######### INPUT 1 #########

entrada_1 = dict()
entrada_1[0] = register('1', libro)
entrada_1[1] = register('1', pelicula)
entrada_1[2] = register('1', chocolate)

# entrada es un dict() con keys = 0,1,2,..,n  y values = objeto "register"

######### Harcoded Data Set #########

bombones = product("caja de bombones de importación",10, True , True)
perfume = product("frasco de perfurme de importación", 47.50, True, False)

######### INPUT 2 #########

entrada_2 = dict()
entrada_2[0] = register('1', bombones)
entrada_2[1] = register('1', perfume)

######### Harcoded Data Set #########

perfume_import = product("frasco de perfume de importación",27.99, True , False)
perfume_local = product("frasco de perfurme ", 18.99 , False, False)
pastillas = product("caja de pastillas para el estómago ", 9.75 , False, True)
bombones_import = product("caja de bombones importados",11.25, True , True)
######### INPUT 3 #########

entrada_3 = dict()
entrada_3[0] = register('1', perfume_import)
entrada_3[1] = register('1', perfume_local)
entrada_3[2] = register('1', pastillas)
entrada_3[3] = register('1', bombones_import)

######### OUTPUT 1 #########
sale_printer(entrada_1)

######### OUTPUT 2 #########
print("")
sale_printer(entrada_2)

print("")
sale_printer(entrada_3)
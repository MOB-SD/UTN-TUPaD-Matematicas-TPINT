# ingresamos el dni de cada integrante

documentos = {
    "A": "42710740",
    "B": "45692114",
    "C": "44350946",
    "D": "47128149"
}
# ingresamos el año de nacimiento de cada integrante
años_nacimiento = {
    "A": 2000,
    "B": 2002,
    "C": 2005,
    "D": 2006
}

# creamos un diccionario para los conjuntos
conjuntos = {}
for clave, documento in documentos.items():
     # Convertimos cada dígito del documento a entero y se guarda en un set para eliminar que se repita
    conjuntos[clave] = set(int(digito) for digito in documento)
print("----------- Conjuntos de dígitos: -----------")
for clave, conjunto in conjuntos.items():
    print(f"{clave}: {conjunto}") 
    print("--------------------------------------------")
# asignamos variables para ingresar a los conjuntos
a = conjuntos["A"]
b = conjuntos["B"]
c = conjuntos["C"]
d = conjuntos["D"]
print("----------- Operaciones entre conjuntos A y B: -----------")
print ("dni: 42710740")
print ("dni: 45692114")
print("Unión entre conjuntos (A U B):", a | b)
print("Intersección entre conjuntos (A ∩ B):", a & b)
print("Diferencia entre conjuntos (A - B):", a - b)
print("Diferencia simétrica entre conjuntos (A Δ B):", a ^ b)
print("--------------------------------------------")
print("Operaciones entre conjuntos B y C:")
print ("dni: 45692114")
print ("dni: 44350946")
print("Unión entre conjuntos (B U C):", b | c)
print("Intersección entre conjuntos (B ∩ C):", b & c)
print("Diferencia entre conjuntos (B - C):", b - c)
print("Diferencia simétrica entre conjuntos (B Δ C):", b ^ c)
print("--------------------------------------------")
print("Operaciones entre conjuntos A y C:")
print ("dni: 42710740")
print ("dni: 44350946")
print("Unión entre conjuntos (A ∪ C):", a | c)
print("Intersección entre conjuntos (A ∩ C):", a & c)
print("Diferencia entre conjuntos (A - C):", a - c)
print("Diferencia simétrica entre conjuntos (A Δ C):", a ^ c)
print("--------------------------------------------")
print("Operaciones entre conjuntos A y D:")
print ("dni: 42710740")
print ("dni: 47128149")
print("Unión entre conjuntos (D U C):", a | d)
print("Intersección entre conjuntos (D ∩ C):", a & d)
print("Diferencia entre conjuntos (D - C):", a - d)
print("Diferencia simétrica entre conjuntos (D Δ C):", a ^ d)
print("--------------------------------------------")
print("Operaciones entre conjuntos D y C:")
print ("dni: 47128149")
print ("dni: 44350946")
print("Unión entre conjuntos (D U C):", d | c)
print("Intersección entre conjuntos (D ∩ C):", d & c)
print("Diferencia entre conjuntos (D - C):", d - c)
print("Diferencia simétrica entre conjuntos (D Δ C):", d ^ c)
print("--------------------------------------------")
print("Operaciones entre conjuntos D y B:")
print ("dni: 47128149")
print ("dni: 45692114")
print("Unión entre conjuntos (D U C):", d | b)
print("Intersección entre conjuntos (D ∩ C):", d & c)
print("Diferencia entre conjuntos (D - C):", d - c)
print("Diferencia simétrica entre conjuntos (D Δ C):", d ^ c)
print("--------------------------------------------")
print("Frecuencia y suma de dígitos por DNI:")
# Recorre el diccionario documentos
for clave, documento in documentos.items():
    frecuencia = {} 
    # inicializamos la variable suma
    suma = 0
    for digito in documento:
        # convierte el digito a entero
        suma += int(digito)
        # actualiza el conteo
        frecuencia[digito] = frecuencia.get(digito, 0) + 1 
    print(f"{clave} - Frecuencia: {frecuencia}, Suma total: {suma}") 

# calcula que digiTos estan compartidos entre los conjuntos
print ("--------------------------------------------")
digito_comun = set.intersection(*conjuntos.values())
if digito_comun:
    print("Si, estos digito esta compartido entre todos los conjuntos:", digito_comun)
else:
    print("No hay ningún dígito compartido entre los 4 conjutnos.")
print ("--------------------------------------------")
for clave, conjunto in conjuntos.items():
    print(f"{clave}: {conjunto} → {len(conjunto)} elementos")
# Recorre cada conjunto de dígitos y muestra cuáles son y cuántos elementos (dígitos únicos) tiene
    if len(conjunto) > 6:
        print(f"{clave} tiene Diversidad numérica alta.")
    else: 
        print("El conjuntos tienen Diversidad numérica baja.")
        
print ("------------------PARTE B---------------------")
# guarda los años de nacimiento en una lista
años = list(años_nacimiento.values())
# calcula las edades de cada integrante
edades = [2025 - año for año in años]

pares = sum(1 for a in años if a % 2 == 0)
# Cuenta cuántos años son pares y cuántos impares.
impares = len(años) - pares
print(f"La cantidad de años pares son: {pares}")
print ("--------------------------------------------")
print(f"La cantidad de años impares son: {impares}")
print ("--------------------------------------------")
# si son mayores a 2000 imprime Z
if (año > 2000 for año in años):
    print("Grupo Z")
    print ("--------------------------------------------")
for año in años:
    # Recorre la lista de años para verificar si alguno es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("Tenemos un año especial.")
        break
print ("--------------------------------------------")
print("Producto cartesiano entre años y edades:")
for año in años:
    for edad in edades:
# Imprime el producto cartesiano entre la lista de años y la lista de edades
        print(f"({año}, {edad})")
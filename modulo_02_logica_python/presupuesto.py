print("Presupuesto Mensual")

# Solicitar al usuario que ingrese su nombre, ingresos y gastos
nombre = input("Ingrese su nombre: ")
ingresos = float(input("Ingrese sus ingresos mensuales: "))
gastos_fijos = float(input("Ingrese sus gastos fijos mensuales: "))
gastos_variables = float(input("Ingrese sus gastos variables mensuales: "))

# Calcular el presupuesto mensual
total_gastos = gastos_fijos + gastos_variables
ahorro = ingresos - total_gastos
porcentaje_ahorro = (ahorro / ingresos) * 100

# Mostrar los resultados al usuario
print("\nResumen del Presupuesto Mensual")
print(f"Hola {nombre}, tus gastos totales en el mes son: ${total_gastos}")
print(f"Te queda disponible para ahorrar: ${ahorro}")
print(f"Tu porcentaje de ahorro respecto a tus ingresos es: {porcentaje_ahorro:.2f}%")

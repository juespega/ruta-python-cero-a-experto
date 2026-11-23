print("Evlauador Financiero")

# Solicitar al usuario que ingrese su nombre, ingresos y gastos
nombre = input("Ingrese su nombre: ")
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))
gastos_fijos = float(input("Ingrese sus gastos fijos mensuales: "))
gastos_variables = float(input("Ingrese sus gastos variables mensuales: "))

# Validación inicial de ingresos y gastos
if ingresos_mensuales <= 0:
    print("Error: Los ingresos mensuales deben ser mayores a cero.")
else:
    # Calcular el presupuesto mensual
    total_gastos = gastos_fijos + gastos_variables
    ahorro = ingresos_mensuales - total_gastos
    porcentaje_ahorro = (ahorro / ingresos_mensuales) * 100

    # Diagnostico
    if ahorro < 0:
        print(
            f"DEFICIT: Tus gastos superan tus ingresos en ${ahorro:,.2f}. Debes reducir tus gastos o aumentar tus ingresos."
        )
    elif porcentaje_ahorro < 10:
        print(
            f"AHORRO BAJO: Tu porcentaje de ahorro es del {porcentaje_ahorro:.2f}%. debes reducir tus gastos variables."
        )
    elif porcentaje_ahorro >= 10 and porcentaje_ahorro < 20:
        print(
            f"FINANZAS ESTABLES: Tu porcentaje de ahorro es del {porcentaje_ahorro:.2f}%. Mantén tus hábitos financieros."
        )
    else:
        print(
            f"SALUD FINANCIERA OPTIMA: Tu porcentaje de ahorro es del {porcentaje_ahorro:.2f}%. ¡Excelente trabajo!"
        )

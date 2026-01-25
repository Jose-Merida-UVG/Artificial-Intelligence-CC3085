import math

# Define values (from assignment)
y_real = [100, 150, 200, 250, 300]
y_pred = [110, 140, 210, 240, 500]


# RMSE Function
def rmse(y_real, y_pred):
    sum = 0
    n = len(y_real)
    for i in range(n):
        sum += (y_pred[i] - y_real[i]) ** 2

    avg = sum / n

    return math.sqrt(avg)


# MAE Function
def mae(y_real, y_pred):
    sum = 0
    n = len(y_real)
    for i in range(n):
        sum += abs(y_pred[i] - y_real[i])

    return sum / n


res_mae = mae(y_real, y_pred)
res_rmse = rmse(y_real, y_pred)

# Prints

# --- Todo el análisis en un solo print ---
analisis = f"""
- Resultados
  MAE: {res_mae:.1f}, RMSE: {res_rmse:.2f}

- ¿Cuál de las dos métricas penalizó más el error del último dato?

  El RMSE, definitivamente. Esto se debe a la manera que se realizan las mediciones,
  dónde el MAE todos los errores se tratan por igual. Mientras que en el RMSE,
  los errores más grandes se ven más penalizados. Podemos tomar también como ejemplo,
  digamos que tenemos una lista con 10 observaciones. Bajo el MAE, es equivalente que
  todas nuestras predicciones tuvieran un error de 50 a que una sola predicción tuviera
  un error de 500. Mientras que el RMSE, similar a como fue en los resultados de este
  código, penalizaría más la predicción absurda con un error de 500.

- ¿Por qué esto es importante si estamos prediciendo, por ejemplo, dosis de medicamentos?

  En el caso de la dosis de medicamentos, las predicciones muy poco certeras pueden
  llegar a tener repercusiones sobre la salud del paciente. Es un caso dónde es
  completamente diferente tener 10 casos con un error pequeño, en comparación a
  9 casos perfectos y un caso dónde la dosis es letal. Siguiendo el ejemplo del inciso
  anterior, las dosis se mantienen en valores alrededor de 250mg. Con todos los errores 
  alrededor de 50mg, todos los pacientes estarían recibiendo +/- 50mg (20% de una 
  dosis promedio) en comparación a su dosis adecuada. 
  
  Por otro lado, tendríamos 9 pacientes con su dosis perfecta pero uno de ellos recibió 
  500mg extra. Es decir, alrededor de 3x la dosis promedio de medicamento que deberían 
  recibir los pacientes. Claramente, deberíamos penalizar más los errores catastróficos 
  utilizando métricas como RMSE.

  Como nota adicional, también tenemos diferentes métricas que podemos utilizar.
  MAE utiliza la norma L1, mientras que RMSE la norma L2. Existen normas Lk (que no voy
  a definir por brevedad), dónde mientras k aumenta se penalizan aún más los valores
  extremos. Aquí podría ser una buena idea utilizar la Norma de Chebyshev (L-infinito),
  dónde se ignora completamente el promedio y únicamente se enfoca en el peor caso posible.
"""

print(analisis)

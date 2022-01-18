
# Conversion SAT a 3SAT

Trabajo de Complejidad Computacional de pasar el problema SAT al 3SAT.

### Autores:
##### ADRIÁN FLEITAS DE LA ROSA <alu0101024363@ull.edu.es>
##### THADDAUS HAASE <alu0101016733@ull.edu.es>
##### FRANCISCO JESUS MENDES GOMEZ <alu0101163970@ull.edu.es>
##### SERGIO TABARES HERNÁNDEZ <alu0101124896@ull.edu.es>

## Como se usa:

Para usar el programa hace falta tener instalado Python 3.

Ejecutando el main pasando el fichero de SAT.json como primer argumento y el nombre del fichero en donde se quiere guardar el problema 3SAT resultante como segundo argumento.

### Ejemplo:
queremos convertir el problema SAT en examples/SAT.json a 3SAT:

```bash
ubuntu@ubutnu:~/SAT-to-3SAT$ python3 main.py examples/SAT.json examples/3SAT.json
```
Como resultado de lo anterior obtenemos en el terminal:

```bash 
U: {u1, u2, u3, u4}
C: {[u1, !u2], [!u1, u2, u1], [u3], [!u3, u2, u1, u4]}
The SAT problem has been loaded.

U: {u1, u2, u3, u4, T0_0, T2_0, T2_1, T3_0}
C: {[u1, !u2, T0_0], [u1, !u2, !T0_0], [!u1, u2, u1], [u3, T2_0, T2_1], [u3, T2_0, !T2_1], [u3, !T2_0, T2_1], [u3, !T2_0, !T2_1], [!u3, u2, T3_0], [!T3_0, u1, u4]}
The 3SAT problem has been generated.

The examples/3SAT.json has been exported.
Both problems are satisfiable with:
{'u1': False, 'u2': False, 'u3': True, 'u4': True, 'T0_0': False, 'T2_0': False, 'T2_1': False, 'T3_0': True}
{'u1': True, 'u2': False, 'u3': True, 'u4': False, 'T0_0': False, 'T2_0': False, 'T2_1': False, 'T3_0': True}
{'u1': True, 'u2': False, 'u3': True, 'u4': True, 'T0_0': False, 'T2_0': False, 'T2_1': False, 'T3_0': True}
{'u1': True, 'u2': True, 'u3': True, 'u4': False, 'T0_0': False, 'T2_0': False, 'T2_1': False, 'T3_0': False}
{'u1': True, 'u2': True, 'u3': True, 'u4': True, 'T0_0': False, 'T2_0': False, 'T2_1': False, 'T3_0': False}
```
Y el resultado de la conversion es guardado en examples/3SAT.json: 

## Ficheros:

### main.py

Este programa es el programa principal, espera dos argumentos, el primero es el fichero del problem SAT en formato json, el segundo es el nombre del fichero en el cual se va a guardar el problema 3SAT, también en formato json.

### SAT.py

Este fichero contiene la clase para representar el problema SAT.

### SAT_3.py

Este fichero contiene la clase para representar el problema 3SAT.

### SAT2SAT_3.py

Esta clase contiene todos los métodos para transformar una clausula SAT a 3SAT. Estos métodos son estáticos para permitir el acceso directo a ellos.

### checkResult.py

Este programa comprueba si un problema SAT y 3SAT son iguales.


## Ejemplos

En la carpeta examples podemos encontrar algunos ficheros de ejemplo de problemas SAT y 3SAT convertido por el programa.

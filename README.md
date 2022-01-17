
# Conversion SAT a 3SAT

Trabajo de Complejidad Computacional de pasar el problema SAT al 3SAT.

### Autores:
##### ADRIÁN FLEITAS DE LA ROSA <alu0101024363@ull.edu.es>
##### THADDAUS HAASE <alu0101016733@ull.edu.es>
##### FRANCISCO JESUS MENDES GOMEZ <alu0101163970@ull.edu.es>
##### SERGIO TABARES HERNÁNDEZ <alu0101124896@ull.edu.es>

## Como se usa:

Ejecutando el main pasando el fichero de SAT.json como primer argumento y el nombre del fichero en donde se quiere guardar el problema 3SAT resultante.

## Ficheros:

### main.py

Este programa es el programa principal, espera dos argumentos, el primero es el fichero del problem SAT en formato json. El segundo el el nombre del fichero en el cual se va a guardar el problema 3SAT, también en formato json.

### SAT.py

Este fichero contiene la clase para representar el problema SAT.

### SAT_3.py

Este fichero contiene la clase para representar el problema 3SAT.

### SAT2SAT_3.py

Esta clase contiene todos los metodos para transformar una clausula SAT a 3SAT. Estos methodos son estaticos para permitir el acceso directo a ellos.

### checkResult.py

Este programa comprueba si un problema SAT y 3SAT son iguales.

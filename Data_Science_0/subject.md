### Capítulo I: Reglas Generales

- Debes renderizar tus módulos desde una computadora en el clúster, ya sea usando una máquina virtual:
  - Puedes elegir el sistema operativo a utilizar en tu máquina virtual.
  - Tu máquina virtual debe tener todo el software necesario para realizar tu proyecto. Este software debe estar configurado e instalado.
  
- O puedes usar la computadora directamente en caso de que las herramientas estén disponibles:
  - Asegúrate de tener el espacio en tu sesión para instalar todo lo que necesitas para todos los módulos (utiliza el espacio en *goinfre* si tu campus lo tiene).
  - Debes tener todo instalado antes de las evaluaciones.

- Tus funciones no deben finalizar inesperadamente (fallos de segmentación, errores de bus, liberación de memoria doble, etc.), aparte de comportamientos indefinidos. Si esto sucede, tu proyecto será considerado no funcional y recibirá un 0 durante la evaluación.

- Te animamos a crear programas de prueba para tu proyecto, aunque este trabajo no tendrá que ser entregado ni será calificado. Esto te dará la oportunidad de probar fácilmente tu trabajo y el de tus compañeros. Encontrarás estas pruebas especialmente útiles durante tu defensa. De hecho, durante la defensa, puedes usar tus propias pruebas y/o las pruebas del compañero que estés evaluando.

- Sube tu trabajo al repositorio git asignado. Solo el trabajo en el repositorio git será evaluado. Si *Deepthought* está asignado para calificar tu trabajo, se hará después de las evaluaciones de tus compañeros. Si ocurre un error en alguna sección de tu trabajo durante la evaluación de *Deepthought*, la evaluación se detendrá.

- ¡Por Odin, por Thor! ¡Usa tu cerebro!

---

### Capítulo II: Introducción

En los próximos dos módulos, verás el papel de un ingeniero de datos.  
Este segundo paso es importante de entender: el ingeniero de datos "limpia" los datos y los transforma para que estén listos para ser analizados por analistas o científicos de datos.

El próximo módulo implica la limpieza de datos. Este segundo paso es crucial para comprender cómo el ingeniero de datos "limpia" y transforma la información. El objetivo es tener los datos listos para ser analizados por analistas o científicos de datos.

Nos encontramos a finales de febrero de 2022, y es tu primer día en una empresa que vende artículos en Internet. Antes de irse de viaje, tu jefe te entrega las ventas de los últimos 4 meses. Tendrás que analizarlas y proponer soluciones para aumentar los ingresos de la empresa.

Ten cuidado con esta "piscina". Incluso si logras validar un módulo, podrías quedarte atascado más adelante si no has limpiado o almacenado correctamente tus datos.


### Capítulo III: Introducción
#### Exercise 00

### Capítulo IV: 
#### Exercise 01

Funciones permitidas: pgadmin, Postico, dbeaver o lo que quieras para ver la base de datos fácilmente

• Busque una forma de visualizar la base de datos fácilmente con un software
• El software elegido debe ayudarlo a encontrar y manipular fácilmente los datos utilizando su ID correspondiente

### Capítulo V: 
#### Exercise 02

• Cree una tabla de Postgres utilizando los datos de un CSV de la carpeta "cliente". Nombre las tablas según el nombre del CSV pero sin la extensión del archivo, por ejemplo: "data_2022_oct"
• El nombre de las columnas debe ser el mismo que el de los archivos CSV y tener el tipo apropiado, tenga cuidado, debe tener al menos 6 tipos de datos diferentes
• Es obligatorio incluir una DATETIME como primera columna

### Capítulo VI: 
#### Exercise 03

• Estamos a finales de febrero de 2022, deberías poder crear tablas con datos extraídos de un CSV.
• Ahora, además, recupera todos los CSV de la carpeta 'cliente' automáticamente y nombra las tablas según el nombre del CSV pero sin la extensión del archivo, por ejemplo: "data_2022_oct"
A continuación, se muestra un ejemplo de la estructura de directorio esperada
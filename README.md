# obligatorio-p1-2023
Este es el obligatorio hecho por Geronimo Reyes y Kevin Wiens.
En este obligatorio podremos ver una simulacion de carrra de Formula 1 donde participan equipos, los cuales tiene un nombre, país de origen y año de fundación. Dicho equipo es una clase que contiene a la clase Empleados y Auto. La primera es una clase madre que es abstracta la cual tiene distintos atributos los cuales son compartidos por todas sus clase hijas. Estos atributos son cedula, nombre, fecha de nacimineto, salario, nacionalidad y edad. Por otro lado como mencionamos anteriormente la clase Equipo tiene distintas clases hijas las culaes son Piloto que tiene coomo atributos a score, numero de auto, puntaje y lesion. Por otro lado esta la clase PilotoSuplente la cual comparte las atributos de Piloto y es activa cuando el atributo lesion(boolean) de Piloto es igual a True. Cada equipo tiene dos Pilotos y un PilotoSuplente. Ademas de estas dos clases el Equipo se compone de 8 Mecaninos la cual es otra clase hija que tiene como atributo score. Por ultimo la otra clase hija es DirectorDeEquipo, y con estas cuatro clases hijas queda compuesta la clase Empleado. Para terminar de componer el equipo hay que asignarle la clase Auto la cual tiene como atributos modelo, año y score.

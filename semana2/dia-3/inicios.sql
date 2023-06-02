-- DDL (DATA DEFITION LANGUAGE)
-- CREATE   > Crear DB o Tablas o Columna o Indices, etc.
-- ALTER    > Modificar las tablas, DB, columnas, etc
-- DROP     > Eliminar tablas, Db, Columnas, etc
-- TRUCANTE > Eliminar todos los registros de una tabla
-- COMMENT  > Agregar comentarios a diccionario de datos
-- RENAME   > Renombrar Tablas, Columnas, ETC
CREATE DATABASE prueba


CREATE TABlE alumnos (
    id SERIAL             NOT NULL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido_paterno TEXT NULL,
    apellido_materno TEXT NULL,
    correo TEXT NOT NULL UNIQUE,
    fecha_nacimiento DATE,
    habilitado BOOLEAN DEFAULT true
)

-- DML (DATA MANIPULATION LANGUAGE)
-- INSERT > Insertar data a las tablas
-- SELECT > Seleccionar la data de las tablas
-- UPDATE > Actualizar la informacion contenida en las tablas
-- DELETE > Eliminar la informacion de las tablas

INSERT INOT alumnos (id, nombre, apellido_paterno, apellido_materno, correo, fecha_nacimiento, habilitado)
(DEFAULT, 'Eduardo', 'De Rivero', 'Manrique', 'edeman@hc', '1992-02-02', 'false')

INSERT INTO alumnos (id, nombre, apellido_paterno, apellido_materno, correo, fecha_nacimiento, habilitado) VALUES
(DEFAULT, 'Juana', 'Martinez', 'Manrique', 'jmartinez@gmail.com', '1992-11-01', DEFAULT),
(DEFAULT, 'Pedro', 'Choquehuanca', 'Gil', 'pchoquehuanca@gmail.com', '200
0-05-15', false),
(DEFAULT, 'Martin', 'Ancco', 'Perez', 'mancco@gmail.com', '1998-09-25', DEFAULT),
(DEFAULT, 'Roxana', 'Juarez', 'Rodriguez', 'rjuarez@gmail.com', '2005-02-09', false);

SELECT nombre FROM alumnos;

-- Si queremos seleccionar todas las columnas de nuestra tabla
SELECT * FROM alumnos;

SELECT * FROM alumnos
WHERE habilitado = true AND apellido_materno = 'Manrique',

-- Listar los nombres y fecha_nacimiento de los alumnos que su nombre sea Roxana o Pedro

SELECT * FROM alumnos
WHERE nombre = 'Roxana' OR nombre = 'Pedro'


-- Devolvera todos los alumnos cuyo nombre tenga la letra e pero sensible a mayusculas y minusculas
SELECT nombre FROM alumnos WHERE nombre LIKE '%e%';

-- Devolvera todos los alumnos con la letra e pero no se respetara si es mayus o minus
SELECT nombre FROM alumnos WHERE nombre ILIKE '%e%';

-- Mostrarme todos los alumnos (todas las columnas) cuyo correo sea hotmail o gmail

SELECT * FROM alumnos WHERE correo LIKE '%hotmail%' OR correo LIKE '%gmail';





--
CREATE TABLE direcciones (
    -- una columna llamada id que sea primary key y autoincrementable
    id  SERIAL PRIMARY KEY,
    -- calle  y tiene que ser text y no puede ser nula
    calle TEXT NOT NULL,
    -- numero numeral y no puede ser nulo
    numero INT NOT NULL,
    -- referencia tiene que ser text y puede ser nulo
    referencia TEXT NULL,
    -- alumno_id tiene que ser un numero y no puede ser nulo
    alumno_id INT NOT NULL,
    -- RELACIONES
    CONSTRAINT fk_direcciones_alumnos FOREIGN KEY(alumno_id) 
    REFERENCES alumnos(id)
);


INSERT INTO direcciones (id, calle, numero, referencia, alumno_id) VALUES
(DEFAULT, 'Av Ejercito', 1050, 'Al frente del Hospital', 1),
(DEFAULT, 'Av Tulipanes', 123, NULL, 1),
(DEFAULT, 'Calle Jose Olaya', 333, NULL, 2),
(DEFAULT, 'Giron Los Girasoles', 576, 'Al frente del parque', 3),
(DEFAULT, 'Pje. B', 8664, 'Al lado del periodiquero', 2),
(DEFAULT, 'Calle Los Martires', 123, NULL, 4),
(DEFAULT, 'Av Las condes', 252, 'En la esquina la casa blanca', 3);

-- Para poder visualizar columnas que sean NULAS, se utiliza el operador IS, no el = ya que haremos uso de una asignacion
SELECT * FROM direcciones WHERE referencia IS NULL;
SELECT * FROM direcciones WHERE referencia IS NOT NULL;

-- Mostrar todas las direcciones que sean Av o Calle y que no tengan referencias

SELECT * FROM direcciones WHERE calle LIKE 'Av' OR calle LIKE 'Calle' AND referencia IS NULL










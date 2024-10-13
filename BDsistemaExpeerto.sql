CREATE DATABASE SistemaExperto;
USE SistemaExperto;
GRANT ALL PRIVILEGES ON SistemaExperto.* TO 'root'@'localhost';
FLUSH PRIVILEGES;

-- Crear la tabla de objeto == enfermedades
CREATE TABLE IF NOT EXISTS enfermedades (
    id_enfermedad INT AUTO_INCREMENT PRIMARY KEY,
    nombre_objeto VARCHAR(255) NOT NULL,
    descripcion TEXT,
    imagen_path VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
#Modificar id por id_enfermedad
ALTER TABLE enfermedades CHANGE id id_enfermedad INT NOT NULL AUTO_INCREMENT;

#Agregar el campo de suma_peso inicializado en 0
ALTER TABLE enfermedades
ADD COLUMN suma_peso INT DEFAULT 0;

#Reiniciar suma_peso a 0
UPDATE enfermedades
SET suma_peso = 0;

#Mostrar datos de la tabla
select * from enfermedades;

#Contar total de registros
SELECT COUNT(*) AS total_registros
FROM enfermedades;


-- Paso 1: Crear la tabla 'sintomas'
CREATE TABLE sintomas (
    id_sintoma INT AUTO_INCREMENT PRIMARY KEY,
    sintoma VARCHAR(255) NOT NULL,
    imagen_path VARCHAR(255) NOT NULL
);
#Modificar id por id_sintoma
ALTER TABLE sintomas CHANGE id id_sintoma INT NOT NULL AUTO_INCREMENT;

#Agregar columna bandera inicializada en 0
ALTER TABLE sintomas
ADD COLUMN bandera TINYINT DEFAULT 0;

#Mostrar los dintomas de la tabla
select * from sintomas;

#Contar total de registros
SELECT COUNT(*) AS total_registros
FROM sintomas;

# Este trigger se activará después de que se elimine un síntoma 
# y actualizará los registros en cuadro_relacion para eliminar las referencias a ese síntoma. 
DELIMITER $$
CREATE TRIGGER actualizar_cuadro_relacion_delete
AFTER DELETE ON sintomas
FOR EACH ROW
BEGIN
    DELETE FROM cuadro_relacion
    WHERE id_sintoma = OLD.id_sintoma;
END$$

DELIMITER ;

#Insertar los sintomas
INSERT INTO sintomas (sintoma, imagen_path) VALUES
('Fiebre', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/fiebre.jpg'),
('Dolor de cabeza', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor_cabeza.jpg'),
('Dolor detrás de los ojos', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor_detras_de_los_ojos.jpg'),
('Dolor muscular', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor_muscular.jpg'),
('Dolor articular', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor_articular.jpg'),
('Náuseas', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/nauseas.jpg'),
('Vómitos', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/vomito.jpg'),
('Erupción cutánea', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/erupcion_cutanea.jpg'),
('Sangrado leve (encías o nariz)', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Sangrado leve (encías o nariz).jpg'),
('Dolor abdominal', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor_abdominal.png'),
('Letargo', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/letargo.jpg'),
('Dolor de garganta', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor_garganta.jpg'),
('Fatiga', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/fatiga.jpg'),
('Tos seca', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/tos_seca.jpg'),
('Escalofríos', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/escalofrios.jpg'),
('Dolor en los oídos', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor_oidos.jpg'),
('Aumento de la sed', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Aumento de la sed.jpg'),
('Micción frecuente', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/miccion frecuente.jpg'),
('Visión borrosa', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/vision borrosa.jpg'),
('Pérdida de peso inexplicable', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/perdida de peso inexplicable.jpg'),
('Hambre extrema', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/hambre extrema.jpg'),
('Infecciones frecuentes (piel o encías)', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Infecciones frecuentes (piel o encías).jpg'),
('Hormigueo en las manos o pies', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Hormigueo en las manos o pies.jpg'),
('Mareos', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/mareo.jpg'),
('Dificultad para respirar', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Dificultad para respirar.jpg'),
('Palpitaciones cardíacas', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/palpitaciones_cardiacas.jpg'),
('Hemorragias nasales', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/hemorragia nasal.jpg'),
('Enrojecimiento facial', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/enrojecimiento.jpg'),
('Dolor o ardor en el estómago', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Ardor en el estomago.jpg'),
('Pérdida de apetito', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/perdida de apetito.jpg'),
('Hinchazón', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/hinchazon.jpg'),
('Indigestión', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/indigestion.jpg'),
('Sangrado gastrointestinal', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/sangrado gastrointestinal.jpg'),
('Tos con flema', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/tos con flema.jpg'),
('Dolor en el pecho', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/dolor en el pecho.jpg'),
('Sudoración excesiva', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/sudoracion excesiva.jpg'),
('Ganglios linfáticos inflamados', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Ganglios linfáticos inflamados.jpg'),
('Manchas blancas o pus en las amígdalas', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Manchas blancas o pus en las amígdalas.jpg'),
('Mal aliento', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/mal aliento.jpg'),
('Voz apagada o ronca', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Voz apagada o ronca.jpg'),
('Pérdida del olfato o gusto', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Pérdida del olfato o gusto.jpg'),
('Diarrea', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Diarrea.jpg'),
('Sibilancias', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/sibilancias.jpg'),
('Opresión en el pecho', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Opresión en el pecho.jpg'),
('Aumento del ritmo cardíaco', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Aumento del ritmo cardíaco.jpg'),
('Respiración rápida o superficial', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Respiración rápida o superficial.jpg'),
('Piel pálida', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/piel_palida.jpg'),
('Problemas de concentración', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/problemas_concentracion.jpg'),
('Manos y pies fríos', 'C:/Users/Alfre/SistemaEnfermedades/sintomas/Manos y pies fríos.jpg');

#crear tabla cuadro-relacion, ON DELETE CASCADE PARA ELIMINAR DESDE SINTOMAS O ENFERMEDAD
CREATE TABLE cuadro_relacion (
    id_cuadro_relacion INT PRIMARY KEY AUTO_INCREMENT,
    id_enfermedad INT,
    id_sintoma INT,
    peso INT,
    FOREIGN KEY (id_enfermedad) REFERENCES enfermedades(id_enfermedad) ON DELETE CASCADE,
    FOREIGN KEY (id_sintoma) REFERENCES sintomas(id_sintoma) ON DELETE CASCADE
);

#drop table cuadro_relacion;
#Mostrar los datos de la tabla
SELECT * FROM cuadro_relacion;

#Contar total de registros
SELECT COUNT(*) AS total_registros
FROM cuadro_relacion;



#Ya no moverle 
#Trigger para inserciones
DELIMITER $$

CREATE TRIGGER actualizar_suma_peso
AFTER INSERT ON cuadro_relacion
FOR EACH ROW
BEGIN
    UPDATE enfermedades
    SET suma_peso = (
        SELECT SUM(peso) 
        FROM cuadro_relacion 
        WHERE id_enfermedad = NEW.id_enfermedad
    )
    WHERE id_enfermedad = NEW.id_enfermedad;
END$$

DELIMITER ;

#Trigger para actualizaciones
DELIMITER $$

CREATE TRIGGER actualizar_suma_peso_update
AFTER UPDATE ON cuadro_relacion
FOR EACH ROW
BEGIN
    UPDATE enfermedades
    SET suma_peso = (
        SELECT SUM(peso) 
        FROM cuadro_relacion 
        WHERE id_enfermedad = NEW.id_enfermedad
    )
    WHERE id_enfermedad = NEW.id_enfermedad;
END$$

DELIMITER $$
CREATE TRIGGER actualizar_suma_peso_delete_relacion
AFTER DELETE ON cuadro_relacion
FOR EACH ROW
BEGIN
    UPDATE enfermedades e
    SET e.suma_peso = COALESCE((
        SELECT SUM(cr.peso) 
        FROM cuadro_relacion cr
        WHERE cr.id_enfermedad = e.id_enfermedad
    ), 0)
    WHERE e.id_enfermedad = OLD.id_enfermedad;
END$$
DELIMITER ;

UPDATE enfermedades
SET suma_peso = (
    SELECT SUM(peso) 
    FROM cuadro_relacion 
    WHERE id_enfermedad = 1
)
WHERE id_enfermedad = 1;

 #Actualiza los valores de suma_peso para los registros ya existentes: SET SQL_SAFE_UPDATES = 0;

UPDATE enfermedades e
JOIN (
    SELECT id_enfermedad, SUM(peso) AS suma_peso
    FROM cuadro_relacion
    GROUP BY id_enfermedad
) cr ON e.id_enfermedad = cr.id_enfermedad
SET e.suma_peso = cr.suma_peso;



#CONSULTAS id_enfermedad y muestra la suma del peso
SELECT id_enfermedad, SUM(peso) AS suma_peso
FROM cuadro_relacion
GROUP BY id_enfermedad;



SELECT s.sintoma, cr.peso
FROM cuadro_relacion cr
JOIN sintomas s ON cr.id_sintoma = s.id_sintoma
WHERE cr.id_enfermedad = 1; 
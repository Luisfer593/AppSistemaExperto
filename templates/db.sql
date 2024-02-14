-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 14-02-2024 a las 18:45:56
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 7.3.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sistema_experto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reglas_heuristicas`
--

CREATE TABLE `reglas_heuristicas` (
  `id` int(11) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL,
  `tipo` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `reglas_heuristicas`
--

INSERT INTO `reglas_heuristicas` (`id`, `descripcion`, `tipo`) VALUES
(1, 'Si el solicitante tiene un historial crediticio sin problemas, con pagos puntuales y bajos niveles de deuda, entonces es más probable que sea aprobado para el crédito.', 'Aprobado'),
(2, 'Si el solicitante tiene múltiples retrasos en los pagos o incumplimientos anteriores, entonces se le podría asignar una calificación crediticia más baja.', 'Reprobado'),
(3, 'Si la relación entre los ingresos del solicitante y sus deudas actuales es alta, entonces es más probable que sea aprobado para el crédito.', 'Aprobado'),
(4, 'Si la deuda existente del solicitante es significativamente mayor que sus ingresos, entonces se podría considerar un riesgo crediticio y asignar una calificación más baja.', 'Reprobado'),
(5, 'Si el solicitante tiene un historial de empleo estable y ha vivido en la misma residencia durante un período prolongado, entonces es más probable que sea aprobado.', 'Aprobado'),
(6, 'Si hay indicios de inestabilidad laboral o frecuentes cambios de residencia, se podría considerar un factor de riesgo y afectar la aprobación.', 'Reprobado'),
(7, 'Si el monto solicitado es razonable en relación con los ingresos y la capacidad de pago del solicitante, entonces es más probable que sea aprobado.', 'Aprobado'),
(8, 'Si el monto solicitado es desproporcionadamente alto en comparación con la situación financiera del solicitante, podría aumentar el riesgo crediticio.', 'Reprobado'),
(9, 'Si el solicitante tiene una edad y experiencia crediticia considerable, es más probable que se le otorgue crédito.', 'Aprobado'),
(10, 'Los solicitantes más jóvenes o aquellos sin historial crediticio previo podrían requerir una mayor verificación y podrían tener límites de crédito más bajos.', 'Reprobado'),
(11, 'Cumplir con las regulaciones locales y normativas es crucial. Si el solicitante no cumple con ciertos requisitos legales, se le podría denegar el crédito.', 'Reprobado'),
(12, 'Si el solicitante cumple con todos los requisitos anteriores y tiene una calificación crediticia alta, se aprueba automáticamente.', 'Aprobado'),
(13, 'Si hay evidencia de riesgo crediticio significativo en múltiples áreas (historial crediticio, relación ingresos-deudas, estabilidad laboral, etc.), se podría requerir una revisión más detallada o incluso denegar el crédito.', 'Reprobado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitudes_credito`
--

CREATE TABLE `solicitudes_credito` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `historial_crediticio` varchar(50) DEFAULT NULL,
  `ingresos_deudas` varchar(50) DEFAULT NULL,
  `tiempo_empleo_actual` int(11) DEFAULT NULL,
  `tiempo_residencia_actual` int(11) DEFAULT NULL,
  `monto_solicitado` decimal(10,2) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `experiencia_crediticia` int(11) DEFAULT NULL,
  `cumple_normativas` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `solicitudes_credito`
--

INSERT INTO `solicitudes_credito` (`id`, `nombre`, `apellido`, `historial_crediticio`, `ingresos_deudas`, `tiempo_empleo_actual`, `tiempo_residencia_actual`, `monto_solicitado`, `edad`, `experiencia_crediticia`, `cumple_normativas`) VALUES
(0, 'Pedro', 'Torrez Camacho', 'Bueno', 'Cumple', 5, 3, '4000.00', 36, 4, 0),
(0, 'Emiliana Félix', 'Larrañaga Luís', 'Regular', 'Cumple', 1, 3, '37000.00', 53, 8, 1),
(0, 'Clara Rogelio', 'Garcia Barrera', 'Regular', 'No Cumple', 9, 5, '39000.00', 44, 7, 0),
(0, 'Manu Carmela', 'Gonzalo Sevilla', 'Malo', 'No Cumple', 8, 2, '50000.00', 53, 5, 0),
(0, 'Paulina Amando', 'Luz Pintor', 'Regular', 'Cumple', 2, 2, '3000.00', 57, 2, 0),
(0, 'Primitiva Ramón', 'Aragonés Coello', 'Regular', 'No Cumple', 2, 10, '31000.00', 34, 1, 0),
(0, 'Flor Ildefonso', 'Donaire Bueno', 'Malo', 'Cumple', 1, 1, '31000.00', 58, 5, 0),
(0, 'Benjamín Marisa', 'Vallejo Valverde', 'Bueno', 'No Cumple', 9, 9, '30000.00', 33, 3, 1),
(0, 'Marisa Daniel', 'Peñas Salmerón', 'Regular', 'Cumple', 7, 9, '26000.00', 20, 3, 0),
(0, 'Crescencia Anunciación', 'Galan Linares', 'Regular', 'Cumple', 3, 6, '9000.00', 62, 9, 0),
(0, 'Lalo Eutimio', 'Revilla Salvador', 'Malo', 'Cumple', 6, 10, '6000.00', 50, 4, 1),
(0, 'Julio César Haydée', 'Bernal Pino', 'Regular', 'No Cumple', 2, 9, '37000.00', 64, 9, 1),
(0, 'Casemiro Ismael', 'Murcia Pi', 'Regular', 'Cumple', 9, 5, '6000.00', 57, 8, 1),
(0, 'Alejo Noemí', 'Cuadrado Jover', 'Malo', 'Cumple', 2, 7, '29000.00', 23, 2, 0),
(0, 'Guiomar Nico', 'Paniagua Iñiguez', 'Regular', 'Cumple', 2, 4, '30000.00', 53, 5, 1),
(0, 'Rosenda Elisa', 'Gimeno Nebot', 'Malo', 'No Cumple', 3, 10, '44000.00', 56, 6, 0),
(0, 'Maricruz Gilberto', 'Garmendia Valverde', 'Malo', 'Cumple', 3, 5, '45000.00', 56, 2, 1),
(0, 'Felicidad Eladio', 'Llabrés Espada', 'Malo', 'No Cumple', 3, 9, '2000.00', 63, 3, 0),
(0, 'Dionisio Jordi', 'Bermúdez Hernando', 'Regular', 'No Cumple', 2, 7, '41000.00', 42, 3, 1),
(0, 'Esteban Baldomero', 'Adadia León', 'Malo', 'No Cumple', 2, 1, '21000.00', 45, 3, 1),
(0, 'Juan Bautista Manolo', 'Armengol Sanabria', 'Malo', 'Cumple', 2, 3, '32000.00', 30, 1, 1),
(0, 'Cristian Ruy', 'Barranco Pellicer', 'Regular', 'No Cumple', 10, 6, '38000.00', 34, 1, 0),
(0, 'Chus Melisa', 'Arévalo Garcia', 'Regular', 'Cumple', 8, 5, '13000.00', 42, 7, 0),
(0, 'Martin Renata', 'Redondo Moles', 'Regular', 'Cumple', 2, 7, '7000.00', 58, 1, 0),
(0, 'Wilfredo Dani', 'Alfaro Millán', 'Regular', 'Cumple', 5, 8, '24000.00', 23, 6, 1),
(0, 'Nieves Florencio', 'Ortega Pineda', 'Regular', 'No Cumple', 9, 3, '11000.00', 49, 4, 0),
(0, 'Dalila Viviana', 'Boada Barrera', 'Regular', 'No Cumple', 2, 2, '45000.00', 26, 6, 0),
(0, 'Baudelio Paola', 'Carranza Pereira', 'Malo', 'No Cumple', 8, 4, '15000.00', 36, 1, 0),
(0, 'Cloe Ascensión', 'Feliu Vila', 'Bueno', 'No Cumple', 9, 2, '25000.00', 27, 5, 0),
(0, 'Gonzalo Itziar', 'Piña Pavón', 'Regular', 'Cumple', 7, 1, '38000.00', 62, 10, 0),
(0, 'Sarita Irma', 'Cases Ribera', 'Malo', 'Cumple', 7, 10, '39000.00', 43, 9, 0),
(0, 'Juan Francisco Dorotea', 'Huertas Gálvez', 'Malo', 'Cumple', 2, 4, '49000.00', 29, 4, 0),
(0, 'Francisca Edelmira', 'Belmonte Garriga', 'Regular', 'Cumple', 7, 4, '10000.00', 21, 6, 1),
(0, 'Eva Julieta', 'Bastida Carnero', 'Bueno', 'Cumple', 4, 5, '14000.00', 41, 5, 0),
(0, 'Severiano Angelino', 'Rozas Ferrán', 'Malo', 'Cumple', 1, 3, '6000.00', 59, 5, 1),
(0, 'Carlos Jordán', 'Torrecilla Canals', 'Malo', 'Cumple', 9, 2, '21000.00', 42, 6, 0),
(0, 'Joaquín Herminio', 'Rico Nogueira', 'Regular', 'No Cumple', 3, 6, '31000.00', 49, 6, 1),
(0, 'Victoria Piedad', 'Vigil Blazquez', 'Malo', 'No Cumple', 4, 5, '41000.00', 49, 2, 1),
(0, 'Gerardo Amancio', 'Núñez Corral', 'Bueno', 'Cumple', 4, 7, '46000.00', 60, 9, 0),
(0, 'Angelina Teobaldo', 'Blanch Diaz', 'Bueno', 'Cumple', 4, 10, '26000.00', 52, 2, 1),
(0, 'María Manuela Xavier', 'Uriarte Garay', 'Bueno', 'Cumple', 10, 6, '22000.00', 51, 6, 1),
(0, 'Cornelio Tiburcio', 'Baeza Puga', 'Regular', 'Cumple', 5, 10, '39000.00', 33, 5, 1),
(0, 'Wilfredo Carmelita', 'Jimenez Batalla', 'Malo', 'No Cumple', 10, 1, '48000.00', 44, 9, 0),
(0, 'Ismael Demetrio', 'Daza Ureña', 'Regular', 'No Cumple', 3, 3, '38000.00', 26, 8, 1),
(0, 'Jessica Soraya', 'Casado Acero', 'Malo', 'Cumple', 7, 2, '11000.00', 31, 10, 1),
(0, 'Abril Antonio', 'Alonso Landa', 'Malo', 'No Cumple', 8, 5, '19000.00', 42, 7, 0),
(0, 'Conrado Roberta', 'Nieto Moya', 'Malo', 'Cumple', 10, 7, '41000.00', 56, 10, 0),
(0, 'Eva María Elena', 'Morata Río', 'Bueno', 'No Cumple', 8, 1, '49000.00', 52, 8, 1),
(0, 'Inmaculada Ema', 'Velasco Rosselló', 'Malo', 'No Cumple', 9, 8, '14000.00', 44, 9, 0),
(0, 'Bibiana Baltasar', 'Domingo Pujadas', 'Regular', 'No Cumple', 8, 10, '4000.00', 30, 2, 1),
(0, 'Emiliano Inmaculada', 'Echevarría Llamas', 'Bueno', 'Cumple', 2, 4, '29000.00', 19, 1, 0),
(0, 'Apolinar Teófila', 'Gabaldón Figuerola', 'Malo', 'No Cumple', 3, 4, '43000.00', 45, 1, 0),
(0, 'Adoración Clementina', 'Carpio Malo', 'Bueno', 'No Cumple', 2, 5, '27000.00', 43, 9, 0),
(0, 'Cándido Catalina', 'Gallego Blasco', 'Regular', 'No Cumple', 10, 8, '46000.00', 21, 2, 0),
(0, 'Verónica Quique', 'Gómez Alarcón', 'Bueno', 'No Cumple', 8, 10, '20000.00', 24, 5, 0),
(0, 'Abraham Alfredo', 'Barranco Bonet', 'Regular', 'Cumple', 2, 5, '37000.00', 39, 4, 1),
(0, 'Marcio Eleuterio', 'Caro Oller', 'Regular', 'No Cumple', 2, 9, '16000.00', 23, 10, 0),
(0, 'Eusebia Aroa', 'Royo Ojeda', 'Regular', 'Cumple', 9, 7, '9000.00', 39, 8, 0),
(0, 'África Felix', 'Asenjo Blanco', 'Regular', 'Cumple', 1, 1, '8000.00', 34, 10, 0),
(0, 'Jonatan Ximena', 'Vargas Bosch', 'Bueno', 'Cumple', 10, 9, '37000.00', 25, 4, 0),
(0, 'Flavia Raúl', 'Ricart Pizarro', 'Regular', 'Cumple', 1, 9, '4000.00', 30, 4, 1),
(0, 'Fabián José Luis', 'Avilés Gisbert', 'Regular', 'No Cumple', 1, 2, '26000.00', 63, 4, 1),
(0, 'Mar Yolanda', 'Cuadrado Espejo', 'Malo', 'Cumple', 8, 10, '6000.00', 39, 6, 0),
(0, 'Chus Dora', 'Ripoll Alegria', 'Regular', 'Cumple', 8, 7, '23000.00', 18, 1, 0),
(0, 'Jacinta Constanza', 'Torrecilla Adán', 'Regular', 'No Cumple', 1, 1, '24000.00', 18, 1, 0),
(0, 'Ramiro Ale', 'Fabra Amores', 'Regular', 'Cumple', 4, 6, '17000.00', 52, 9, 1),
(0, 'Melisa Alberto', 'Valenzuela Quirós', 'Malo', 'Cumple', 1, 9, '45000.00', 42, 9, 0),
(0, 'Haydée Julián', 'Folch Berenguer', 'Bueno', 'No Cumple', 3, 6, '42000.00', 47, 4, 1),
(0, 'Che Lalo', 'Perales Gutiérrez', 'Malo', 'Cumple', 1, 8, '46000.00', 34, 7, 1),
(0, 'César Sara', 'Amaya Boix', 'Bueno', 'No Cumple', 10, 6, '38000.00', 23, 5, 0),
(0, 'Daniela Fulgencio', 'Melero Agullo', 'Bueno', 'Cumple', 8, 4, '2000.00', 35, 6, 0),
(0, 'Agustín Adela', 'Arce Pagès', 'Regular', 'Cumple', 1, 8, '48000.00', 49, 9, 0),
(0, 'Elías Maxi', 'Tejera Fernandez', 'Regular', 'Cumple', 6, 1, '44000.00', 33, 3, 1),
(0, 'Flora Mirta', 'Santana Portero', 'Malo', 'Cumple', 5, 2, '30000.00', 19, 9, 0),
(0, 'Javiera Carlito', 'Losada Bartolomé', 'Bueno', 'No Cumple', 3, 8, '46000.00', 32, 2, 0),
(0, 'Rómulo Reyna', 'Aroca Blanca', 'Bueno', 'No Cumple', 3, 6, '21000.00', 28, 9, 1),
(0, 'Martín Juanito', 'Ortuño Moreno', 'Regular', 'No Cumple', 8, 4, '17000.00', 48, 7, 1),
(0, 'Hugo Tamara', 'Díaz Pombo', 'Regular', 'No Cumple', 6, 6, '16000.00', 18, 5, 1),
(0, 'Pía Sebastián', 'Cano Gallego', 'Bueno', 'No Cumple', 5, 3, '4000.00', 51, 7, 0),
(0, 'Alex Diego', 'Madrigal Angulo', 'Bueno', 'Cumple', 3, 7, '26000.00', 62, 6, 0),
(0, 'Teobaldo Dionisio', 'Rico Ferrer', 'Bueno', 'Cumple', 5, 9, '12000.00', 64, 4, 1),
(0, 'Itziar Aurelio', 'Acero Lasa', 'Bueno', 'Cumple', 4, 2, '18000.00', 48, 4, 1),
(0, 'Dora Aránzazu', 'Gonzalo Costa', 'Bueno', 'No Cumple', 2, 3, '10000.00', 58, 8, 0),
(0, 'Cesar Benita', 'García Benet', 'Regular', 'Cumple', 7, 5, '46000.00', 62, 6, 1),
(0, 'Noé Valeria', 'Tello Giner', 'Malo', 'Cumple', 5, 4, '28000.00', 59, 3, 1),
(0, 'Cebrián Renata', 'Revilla Meléndez', 'Bueno', 'Cumple', 8, 2, '19000.00', 64, 2, 0),
(0, 'Cleto Zaida', 'Echevarría Bas', 'Malo', 'No Cumple', 2, 4, '33000.00', 47, 7, 0),
(0, 'Santos Josué', 'Mir Pujadas', 'Malo', 'Cumple', 10, 1, '46000.00', 45, 1, 1),
(0, 'Fabricio Isabel', 'Mancebo Moya', 'Regular', 'Cumple', 1, 2, '17000.00', 45, 2, 1),
(0, 'Gisela Sol', 'Verdugo Rosado', 'Regular', 'No Cumple', 1, 10, '17000.00', 45, 3, 1),
(0, 'Reynaldo Reyes', 'Fabregat Cánovas', 'Malo', 'Cumple', 3, 8, '18000.00', 51, 5, 0),
(0, 'Maite Nidia', 'Cuevas Portero', 'Malo', 'No Cumple', 4, 6, '45000.00', 47, 6, 0),
(0, 'Joaquín Heliodoro', 'Hidalgo Falcón', 'Bueno', 'No Cumple', 8, 1, '23000.00', 47, 1, 1),
(0, 'Tiburcio Lucho', 'Águila Alcolea', 'Bueno', 'No Cumple', 2, 5, '35000.00', 61, 5, 0),
(0, 'Nacio Ofelia', 'Machado Córdoba', 'Bueno', 'Cumple', 8, 1, '41000.00', 38, 9, 0),
(0, 'Amaro Rosalinda', 'Pelayo Rosales', 'Malo', 'No Cumple', 4, 1, '35000.00', 55, 3, 0),
(0, 'Mirta Jafet', 'Gras Mora', 'Bueno', 'Cumple', 1, 10, '40000.00', 57, 8, 1),
(0, 'Horacio Pascuala', 'Costa Riera', 'Regular', 'No Cumple', 5, 3, '27000.00', 44, 7, 0),
(0, 'Salvador Lupe', 'Quirós Moll', 'Bueno', 'Cumple', 5, 3, '38000.00', 23, 9, 1),
(0, 'Rolando Patricia', 'Orozco Segarra', 'Bueno', 'Cumple', 6, 1, '10000.00', 62, 2, 0),
(0, 'Álvaro Mireia', 'Español Aramburu', 'Regular', 'No Cumple', 3, 8, '36000.00', 63, 5, 1),
(0, 'Pedro', 'Torrez Camacho', 'Malo', 'Cumple', 5, 7, '10000.00', 21, 2, 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
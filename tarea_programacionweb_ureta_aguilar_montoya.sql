-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.1.36-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win32
-- HeidiSQL Versión:             9.5.0.5196
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para pooweb
CREATE DATABASE IF NOT EXISTS `pooweb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `pooweb`;

-- Volcando estructura para tabla pooweb.grupo
CREATE TABLE IF NOT EXISTS `grupo` (
  `idgrupo` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`idgrupo`),
  UNIQUE KEY `descripcion` (`descripcion`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla pooweb.grupo: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `grupo` DISABLE KEYS */;
INSERT INTO `grupo` (`idgrupo`, `descripcion`) VALUES
	(1, 'activos'),
	(4, 'ingresos'),
	(2, 'pasivo'),
	(3, 'patrimonio');
/*!40000 ALTER TABLE `grupo` ENABLE KEYS */;

-- Volcando estructura para tabla pooweb.plan_cuenta
CREATE TABLE IF NOT EXISTS `plan_cuenta` (
  `idplancuenta` int(11) NOT NULL AUTO_INCREMENT,
  `grupo` int(11) DEFAULT NULL,
  `codigo` varchar(50) DEFAULT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `naturaleza` char(1) DEFAULT NULL,
  `estado` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`idplancuenta`),
  KEY `FK_plan_cuenta_grupo` (`grupo`),
  CONSTRAINT `FK_plan_cuenta_grupo` FOREIGN KEY (`grupo`) REFERENCES `grupo` (`idgrupo`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla pooweb.plan_cuenta: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `plan_cuenta` DISABLE KEYS */;
INSERT INTO `plan_cuenta` (`idplancuenta`, `grupo`, `codigo`, `descripcion`, `naturaleza`, `estado`) VALUES
	(1, 1, '02', 'bancos', 'a', 0),
	(2, 1, '03', 'cuentas por cobrar', 'a', 1),
	(3, 3, '07', 'equipos de oficina', 'a', 1),
	(4, 4, '04', 'ventas', 'a', 0),
	(5, 3, '05', 'edificios', 'd', 0),
	(6, 2, '02', 'sueldos', 'd', 1),
	(7, 3, '06', 'llates', 'a', 1),
	(8, 1, '001', 'caja chica ', 'a', 1);
/*!40000 ALTER TABLE `plan_cuenta` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

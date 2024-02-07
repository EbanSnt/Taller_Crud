CREATE DATABASE  IF NOT EXISTS `taller_database` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `taller_database`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: taller_database
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `main_customers`
--

DROP TABLE IF EXISTS `main_customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_customers` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(70) NOT NULL,
  `telephone_number` bigint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_customers`
--

LOCK TABLES `main_customers` WRITE;
/*!40000 ALTER TABLE `main_customers` DISABLE KEYS */;
INSERT INTO `main_customers` VALUES (1,'Esteban Gomez',340912389),(3,'Juana Roman',12558203241),(4,'Pamela Alvarez',18710091281),(5,'Antonio Marcos Nuñez',77129013451);
/*!40000 ALTER TABLE `main_customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_deliveredproducts`
--

DROP TABLE IF EXISTS `main_deliveredproducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_deliveredproducts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `ticket_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_deliveredproducts_ticket_id_id_cbd5f77f_fk_main_tickets_id` (`ticket_id_id`),
  CONSTRAINT `main_deliveredproducts_ticket_id_id_cbd5f77f_fk_main_tickets_id` FOREIGN KEY (`ticket_id_id`) REFERENCES `main_tickets` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_deliveredproducts`
--

LOCK TABLES `main_deliveredproducts` WRITE;
/*!40000 ALTER TABLE `main_deliveredproducts` DISABLE KEYS */;
INSERT INTO `main_deliveredproducts` VALUES (1,'2024-02-07',2);
/*!40000 ALTER TABLE `main_deliveredproducts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_tickets`
--

DROP TABLE IF EXISTS `main_tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_tickets` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ticket_number` bigint NOT NULL,
  `product` varchar(30) NOT NULL,
  `trademark` varchar(30) NOT NULL,
  `version` varchar(30) NOT NULL,
  `serial_number` varchar(40) NOT NULL,
  `failure` varchar(40) NOT NULL,
  `product_image1` varchar(100) NOT NULL,
  `product_image2` varchar(100) NOT NULL,
  `product_image3` varchar(100) NOT NULL,
  `description` varchar(300) NOT NULL,
  `local` tinyint(1) NOT NULL,
  `customer_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_tickets_customer_id_id_6a92e609_fk_main_customers_id` (`customer_id_id`),
  CONSTRAINT `main_tickets_customer_id_id_6a92e609_fk_main_customers_id` FOREIGN KEY (`customer_id_id`) REFERENCES `main_customers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_tickets`
--

LOCK TABLES `main_tickets` WRITE;
/*!40000 ALTER TABLE `main_tickets` DISABLE KEYS */;
INSERT INTO `main_tickets` VALUES (1,100002345,'Batidora','Peabody','PE-BM190R','29DOP2391JDP','No gira','products_images/352429_3.jpg','products_images/1903.jpg','','Tienes algunos rayones al costado',1,4),(2,34273,'Microondas','Atma','MR1720NPI','TJ291ND','No calienta','products_images/D_NQ_NP_804133-MLU72611785165_112023-F.jpg','products_images/microondas-atma-easy-cook-20-litros-mr-1720-npi-rotativo-700-w.jpg','products_images/microondas-atma-easy-cook-20-litros-mr-1720-npi-rotativo-700-w_1.jpg','Necesita Limpieza',0,3);
/*!40000 ALTER TABLE `main_tickets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_warrantyproducts`
--

DROP TABLE IF EXISTS `main_warrantyproducts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `main_warrantyproducts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `description` varchar(300) NOT NULL,
  `local` tinyint(1) NOT NULL,
  `ticket_id_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_warrantyproducts_ticket_id_id_2bd99b2b_fk_main_tickets_id` (`ticket_id_id`),
  CONSTRAINT `main_warrantyproducts_ticket_id_id_2bd99b2b_fk_main_tickets_id` FOREIGN KEY (`ticket_id_id`) REFERENCES `main_tickets` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_warrantyproducts`
--

LOCK TABLES `main_warrantyproducts` WRITE;
/*!40000 ALTER TABLE `main_warrantyproducts` DISABLE KEYS */;
INSERT INTO `main_warrantyproducts` VALUES (1,'Misma falla que la vez anterior',1,1);
/*!40000 ALTER TABLE `main_warrantyproducts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-07 20:02:06

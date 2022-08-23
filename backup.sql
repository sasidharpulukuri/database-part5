-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.9.1-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table teaproject.customer_details
CREATE TABLE IF NOT EXISTS `customer_details` (
  `customer_id` varchar(25) DEFAULT NULL,
  `customer_name` varchar(25) DEFAULT NULL,
  `customer_address` varchar(25) DEFAULT NULL,
  `phone_number` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table teaproject.customer_details: ~3 rows (approximately)
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
REPLACE INTO `customer_details` (`customer_id`, `customer_name`, `customer_address`, `phone_number`) VALUES
	('c1', 'john', 'stree vb', '4343434'),
	('c2', 'mitchel', 'street fd', '4554546'),
	('c3', 'tom', 'street gh', '565577');
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;

-- Dumping structure for table teaproject.order_details
CREATE TABLE IF NOT EXISTS `order_details` (
  `order_id` varchar(50) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `quantity` int(15) DEFAULT NULL,
  `price` int(15) DEFAULT NULL,
  `customer_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table teaproject.order_details: ~3 rows (approximately)
/*!40000 ALTER TABLE `order_details` DISABLE KEYS */;
REPLACE INTO `order_details` (`order_id`, `order_date`, `quantity`, `price`, `customer_id`) VALUES
	('o1', '2022-01-01', 1, 100, 'c1'),
	('o2', '2022-01-01', 2, 200, 'c2'),
	('o3', '2022-01-01', 3, 300, 'c3');
/*!40000 ALTER TABLE `order_details` ENABLE KEYS */;

-- Dumping structure for table teaproject.order_status
CREATE TABLE IF NOT EXISTS `order_status` (
  `order_status_id` varchar(25) DEFAULT NULL,
  `order_id` varchar(25) DEFAULT NULL,
  `process` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table teaproject.order_status: ~9 rows (approximately)
/*!40000 ALTER TABLE `order_status` DISABLE KEYS */;
REPLACE INTO `order_status` (`order_status_id`, `order_id`, `process`) VALUES
	('os1', 'o1', 'delivered'),
	('os2', 'o2', 'on the way'),
	('os3', 'o3', 'delivered'),
	('os4', 'o4', 'Shipped'),
	('os5', 'o5', 'Resolved'),
	('os6', 'o6', 'Cancelled'),
	('os7', 'o7', 'On Hold'),
	('os8', 'o8', 'Disputed'),
	('os9', 'o9', 'In Process');
/*!40000 ALTER TABLE `order_status` ENABLE KEYS */;

-- Dumping structure for table teaproject.payment
CREATE TABLE IF NOT EXISTS `payment` (
  `payment_id` varchar(25) DEFAULT NULL,
  `method` varchar(25) DEFAULT NULL,
  `pay_status` varchar(25) DEFAULT NULL,
  `amount` float DEFAULT NULL,
  `customer_id` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table teaproject.payment: ~3 rows (approximately)
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
REPLACE INTO `payment` (`payment_id`, `method`, `pay_status`, `amount`, `customer_id`) VALUES
	('p1', 'online', 'full paid', 100, 'c1'),
	('p2', 'offline', 'half paid', 100.2, 'c2'),
	('p3', 'online', 'full paid', 50, 'c3');
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;

-- Dumping structure for table teaproject.review
CREATE TABLE IF NOT EXISTS `review` (
  `review_id` varchar(54) DEFAULT NULL,
  `Customer_name` varchar(45) DEFAULT NULL,
  `comment` varchar(43) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table teaproject.review: ~3 rows (approximately)
/*!40000 ALTER TABLE `review` DISABLE KEYS */;
REPLACE INTO `review` (`review_id`, `Customer_name`, `comment`) VALUES
	('r1', 'ricky', 'good'),
	('r2', 'tom', 'worst'),
	('r3', 'json', 'good');
/*!40000 ALTER TABLE `review` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

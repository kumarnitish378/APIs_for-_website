-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 11, 2021 at 11:49 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jivans`
--

-- --------------------------------------------------------

--
-- Table structure for table `credential`
--

CREATE TABLE `credential` (
  `userName` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `token` varchar(30) DEFAULT NULL,
  `sat` varchar(30) DEFAULT NULL,
  `emailOTP` varchar(30) DEFAULT NULL,
  `phoneOTP` varchar(30) DEFAULT NULL,
  `loginAttempt` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `credential`
--

INSERT INTO `credential` (`userName`, `password`, `token`, `sat`, `emailOTP`, `phoneOTP`, `loginAttempt`, `status`) VALUES
('kumar_nitish', '123456', 'asdfghjklzxcvnm', '456', '5241', '6325', '1', 'done');

-- --------------------------------------------------------

--
-- Table structure for table `employ`
--

CREATE TABLE `employ` (
  `fname` varchar(50) NOT NULL,
  `Lastname` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `streetaddress` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `zipcode` varchar(10) NOT NULL,
  `country` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employ`
--

INSERT INTO `employ` (`fname`, `Lastname`, `email`, `role`, `phone`, `streetaddress`, `city`, `zipcode`, `country`) VALUES
('ABC', 'xyz', 'abc@gmail.com', 'data science', '456321789', 'Kotwa', 'motihari', '85632', 'India'),
('Nitish kumar', 'Sharma', 'nitish.ns377@gmail.com', 'executive engineer', '7004969879', 'Jasauli Patti', 'Motihari', '845437', 'India'),
('ABC', 'xyz', 'abc@gmail.com', 'data science', '456321789', 'Kotwa', 'motihari', '85632', 'India'),
('abc', 'xyz', 'abc@gmail.com', 'data science', '456321789', 'Kotwa', 'motihari', '85632', 'India'),
('Abhishek Kumar', 'Sharma', 'nitish.ns350@gmail.com', 'Researcher', '7631245635', 'Jasauli Patti', 'Motihari', '845439', 'India');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `productid` varchar(10) DEFAULT NULL,
  `pname` varchar(30) DEFAULT NULL,
  `description` varchar(30) DEFAULT NULL,
  `price` varchar(30) DEFAULT NULL,
  `category` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`productid`, `pname`, `description`, `price`, `category`) VALUES
('3', 'mango', 'good food for health', '100/kg', 'food');

-- --------------------------------------------------------

--
-- Table structure for table `sigup`
--

CREATE TABLE `sigup` (
  `firstName` varchar(30) DEFAULT NULL,
  `lastName` varchar(30) DEFAULT NULL,
  `userName` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sigup`
--

INSERT INTO `sigup` (`firstName`, `lastName`, `userName`, `password`) VALUES
('nitish kumar', 'sharma', 'nitish.ns378@gmail.com', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` varchar(30) DEFAULT NULL,
  `userName` varchar(30) DEFAULT NULL,
  `firstName` varchar(30) DEFAULT NULL,
  `lastName` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `role` varchar(30) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL,
  `zipcode` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `userName`, `firstName`, `lastName`, `email`, `phone`, `role`, `address`, `city`, `zipcode`, `status`) VALUES
('0', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE `userdetails` (
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `conformpassword` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`name`, `email`, `password`, `conformpassword`) VALUES
('nitish kumar sharma', 'nitish.ns378@gmail.com', '123456', '123456'),
('nitish kumar', 'nitish.ns377@gmail', '123456', '123456'),
('nitish kumar', 'nitish.ns377@gmail', '123456', '123456'),
('nitish kumar', 'nitish.ns377@gmail', '123456', '123456');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

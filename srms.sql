-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: srms
-- ------------------------------------------------------
-- Server version	8.0.21
CREATE DATABASE IF NOT EXISTS srms;

USE srms;
--
-- Table structure for table `auth_user`
--
CREATE TABLE `auth_user` (
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  UNIQUE KEY `password_UNIQUE` (`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `result`
--

CREATE TABLE `result` (
  `roll_no` int NOT NULL,
  `student_name` varchar(45) DEFAULT NULL,
  `class_name` varchar(45) DEFAULT NULL,
  `subject_name` varchar(45) NOT NULL,
  `marks` int DEFAULT NULL,
  PRIMARY KEY (`subject_name`),
  KEY `class_id_idx` (`class_name`),
  KEY `student_id_idx` (`roll_no`),
  KEY `subject_id_idx` (`subject_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `student_classes`
--

CREATE TABLE `student_classes` (
  `id` int NOT NULL,
  `class_name` varchar(45) DEFAULT NULL,
  `class_name_numric` int DEFAULT NULL,
  `section` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int NOT NULL,
  `student_name` varchar(45) NOT NULL,
  `roll_no` int DEFAULT NULL,
  `student_gender` varchar(45) DEFAULT NULL,
  `student_mobile` varchar(45) DEFAULT NULL,
  `student_class_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Table structure for table `subjects`
--

CREATE TABLE `subjects` (
  `id` int NOT NULL,
  `subject_name` varchar(45) DEFAULT NULL,
  `subject_code` int DEFAULT NULL,
  `class_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `class_id_idx` (`class_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

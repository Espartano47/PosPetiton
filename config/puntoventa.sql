-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 23, 2026 at 02:31 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `puntoventa`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_payable`
--

CREATE TABLE `accounts_payable` (
  `id` int(11) NOT NULL,
  `purchase_id` int(11) DEFAULT NULL,
  `supplier_id` int(11) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `description`, `created_at`, `updated_at`) VALUES
(1, 'Electrónica', 'Productos electrónicos como celulares, computadoras y accesorios', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(2, 'Ropa', 'Todo tipo de ropa para hombres, mujeres y niños', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(3, 'Alimentos', 'Comida, bebidas y productos de supermercado', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(4, 'Hogar', 'Artículos para el hogar, muebles y decoración', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(5, 'Deportes', 'Equipos, ropa y accesorios deportivos', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(6, 'Juguetes', 'Juguetes para niños de todas las edades', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(7, 'Salud y Belleza', 'Productos de cuidado personal y belleza', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(8, 'Automotriz', 'Accesorios, repuestos y mantenimiento de vehículos', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(9, 'Libros y Papelería', 'Libros, cuadernos, material escolar', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(10, 'Electrodomésticos', 'Lavadoras, refrigeradores, microondas y otros', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(11, 'Tecnología', 'Gadgets, smartwatches, auriculares', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(12, 'Mascotas', 'Alimentos, accesorios y productos para mascotas', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(13, 'Ferretería', 'Herramientas, pinturas y materiales de construcción', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(14, 'Jardinería', 'Plantas, semillas y accesorios de jardín', '2026-03-10 01:18:02', '2026-03-10 01:18:02'),
(15, 'Oficina', 'Mobiliario y suministros de oficina', '2026-03-10 01:18:02', '2026-03-10 01:18:02');

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `document` varchar(50) DEFAULT NULL,
  `status` tinyint(4) DEFAULT 1,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`id`, `name`, `phone`, `email`, `address`, `document`, `status`, `created_by`, `updated_by`, `created_at`, `updated_at`) VALUES
(1, 'Juan Pérez', '809-555-1001', 'juan.perez@email.com', 'Santo Domingo', '001-1234567-8', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(2, 'María Rodríguez', '809-555-1002', 'maria.rodriguez@email.com', 'Santiago', '002-2345678-9', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(3, 'Carlos Gómez', '809-555-1003', 'carlos.gomez@email.com', 'La Vega', '003-3456789-0', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(4, 'Ana Martínez', '809-555-1004', 'ana.martinez@email.com', 'San Cristóbal', '004-4567890-1', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(5, 'Luis Fernández', '809-555-1005', 'luis.fernandez@email.com', 'Puerto Plata', '005-5678901-2', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(6, 'Sofía Castillo', '809-555-1006', 'sofia.castillo@email.com', 'San Pedro de Macorís', '006-6789012-3', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(7, 'Pedro Ramírez', '809-555-1007', 'pedro.ramirez@email.com', 'Bonao', '007-7890123-4', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(8, 'Laura Torres', '809-555-1008', 'laura.torres@email.com', 'Moca', '008-8901234-5', 1, 1, NULL, '2026-03-08 21:59:37', '2026-03-08 21:59:37'),
(9, 'Miguel Herreraa', '809-555-1009', 'miguel.herrera@email.com', 'Higüey', '009-9012345-6', 1, 1, 2, '2026-03-08 21:59:37', '2026-03-10 19:49:41'),
(10, 'Daniela Cruz', '809-555-1010', 'daniela.cruz@email.com', 'Baní', '010-0123456-7', 1, 1, 2, '2026-03-08 21:59:37', '2026-03-10 19:52:20'),
(11, 'Yermy', '8092962672', '', NULL, NULL, 1, 2, NULL, '2026-03-10 20:02:35', '2026-03-10 20:02:35');

-- --------------------------------------------------------

--
-- Table structure for table `empresas`
--

CREATE TABLE `empresas` (
  `idnew_table` int(11) NOT NULL,
  `Nombre` varchar(45) DEFAULT NULL,
  `Pais` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `empresas`
--

INSERT INTO `empresas` (`idnew_table`, `Nombre`, `Pais`) VALUES
(1, 'Grupo Popular', 'República Dominicana'),
(2, 'Banreservas', 'República Dominicana'),
(3, 'Cervecería Nacional Dominicana', 'República Dominicana');

-- --------------------------------------------------------

--
-- Table structure for table `inventory_movements`
--

CREATE TABLE `inventory_movements` (
  `id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `type` varchar(20) NOT NULL,
  `quantity` decimal(10,2) NOT NULL,
  `stock_before` decimal(10,2) NOT NULL,
  `stock_after` decimal(10,2) NOT NULL,
  `reference` varchar(100) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `permisos`
--

CREATE TABLE `permisos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `descripcion` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `permisos`
--

INSERT INTO `permisos` (`id`, `nombre`, `descripcion`) VALUES
(1, 'empleados:read', 'Ver empleados'),
(2, 'empleados:create', 'Crear empleados'),
(3, 'empleados:update', 'Editar empleados'),
(4, 'empleados:delete', 'Eliminar empleados'),
(5, 'usuarios:read', 'Ver usuarios del sistema'),
(6, 'usuarios:create', 'Crear usuarios del sistema'),
(7, 'usuarios:update', 'Editar usuarios del sistema'),
(8, 'usuarios:delete', 'Eliminar usuarios del sistema');

-- --------------------------------------------------------

--
-- Table structure for table `permissions`
--

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `permissions`
--

INSERT INTO `permissions` (`id`, `name`, `description`) VALUES
(13, 'productos:read', 'Ver productos'),
(14, 'productos:create', 'Crear productos'),
(15, 'productos:update', 'Editar productos'),
(16, 'productos:delete', 'Eliminar productos'),
(17, 'usuarios:read', 'Ver usuarios'),
(18, 'usuarios:create', 'Crear usuarios'),
(19, 'usuarios:update', 'Editar usuarios'),
(20, 'usuarios:delete', 'Eliminar usuarios'),
(21, 'roles:read', 'Ver roles'),
(22, 'roles:create', 'Crear roles'),
(23, 'roles:update', 'Editar roles'),
(24, 'roles:delete', 'Eliminar roles');

-- --------------------------------------------------------

--
-- Table structure for table `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `cost` decimal(10,2) DEFAULT 0.00,
  `stock` int(11) DEFAULT 0,
  `min_stock` int(11) DEFAULT 0,
  `barcode` varchar(100) DEFAULT NULL,
  `status` tinyint(4) DEFAULT 1,
  `photo` varchar(255) DEFAULT NULL,
  `created_by` int(11) NOT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `description` text DEFAULT NULL,
  `price` decimal(10,2) NOT NULL,
  `stock` int(11) DEFAULT 0,
  `min_stock` int(11) DEFAULT 0,
  `barcode` varchar(100) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `status` tinyint(4) DEFAULT 1,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `cost` decimal(10,2) DEFAULT 0.00
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `name`, `description`, `price`, `stock`, `min_stock`, `barcode`, `image`, `status`, `created_by`, `updated_by`, `created_at`, `updated_at`, `cost`) VALUES
(3, 'test', 'test', 2342.00, 228, 234, '234', NULL, 1, 2, 2, '2026-03-08 00:22:12', '2026-03-10 20:03:18', 34.00),
(4, 'er', 'er', 234.00, 2337, 3423, '4', NULL, 1, 2, NULL, '2026-03-08 00:40:02', '2026-03-10 20:05:11', 234.00),
(5, 'werasdwadwad', 'wer', 2342.00, 9, 1, '234', NULL, 1, 2, 2, '2026-03-08 00:40:18', '2026-03-10 20:03:18', 342.00),
(6, 'Papel de baño premier', 'null', 234.00, 0, 0, NULL, '/uploads/productos/8949ea9d-40ac-461d-baf9-3adeded8a3d9.webp', 1, 2, 2, '2026-03-09 20:41:43', '2026-03-10 20:03:18', 50.00),
(8, 'Jugo Rica Mediano 500Ml', 'Jugo Rica Mediano ', 50.00, 12, 1, NULL, '/uploads/productos/0ccbd73d-2667-4659-8326-92fc148fac99.webp', 1, 2, 2, '2026-03-09 20:45:51', '2026-03-10 20:03:18', 40.00);

-- --------------------------------------------------------

--
-- Table structure for table `purchases`
--

CREATE TABLE `purchases` (
  `id` int(11) NOT NULL,
  `supplier_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `invoice_number` varchar(100) DEFAULT NULL,
  `status` varchar(20) DEFAULT 'paid',
  `total` decimal(10,2) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `purchase_items`
--

CREATE TABLE `purchase_items` (
  `id` int(11) NOT NULL,
  `purchase_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` decimal(10,2) DEFAULT NULL,
  `cost` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `quotations`
--

CREATE TABLE `quotations` (
  `id` int(11) NOT NULL,
  `client_id` int(11) DEFAULT NULL,
  `total` decimal(10,2) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `quotations`
--

INSERT INTO `quotations` (`id`, `client_id`, `total`, `created_at`) VALUES
(1, NULL, 5202.00, '2026-03-10 20:39:37');

-- --------------------------------------------------------

--
-- Table structure for table `quotation_items`
--

CREATE TABLE `quotation_items` (
  `id` int(11) NOT NULL,
  `quotation_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `quotation_items`
--

INSERT INTO `quotation_items` (`id`, `quotation_id`, `product_id`, `name`, `price`, `quantity`, `subtotal`) VALUES
(1, 1, 3, 'test', 2342.00, 1, 2342.00),
(2, 1, 5, 'werasdwadwad', 2342.00, 1, 2342.00),
(3, 1, 4, 'er', 234.00, 1, 234.00),
(4, 1, 6, 'Papel de baño premier', 234.00, 1, 234.00),
(5, 1, 8, 'Jugo Rica Mediano 500Ml', 50.00, 1, 50.00);

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `status` int(11) DEFAULT 1,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`, `description`, `status`, `created_by`, `updated_by`, `created_at`, `updated_at`) VALUES
(1, 'Administrador', 'Acceso total al sistema', 1, NULL, 2, '2026-03-09 22:14:24', NULL),
(2, 'Gerente', 'Puede gestionar operaciones pero no configurar el sistema', 1, NULL, NULL, '2026-03-09 22:14:24', NULL),
(3, 'Empleado', 'Acceso limitado a operaciones diarias', 1, NULL, NULL, '2026-03-09 22:14:24', NULL),
(4, 'Invitado', 'Solo puede visualizar información', 1, NULL, NULL, '2026-03-09 22:14:24', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `role_permissions`
--

CREATE TABLE `role_permissions` (
  `id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `role_permissions`
--

INSERT INTO `role_permissions` (`id`, `role_id`, `permission_id`) VALUES
(4, 1, 13),
(5, 1, 20),
(6, 1, 14),
(7, 1, 15),
(8, 1, 16),
(9, 1, 17),
(10, 1, 18),
(11, 1, 19),
(12, 1, 21),
(13, 1, 22),
(14, 1, 23),
(15, 1, 24),
(16, 2, 13),
(17, 2, 14),
(18, 2, 15),
(19, 2, 16),
(20, 2, 17),
(21, 2, 18),
(22, 2, 19),
(23, 2, 20),
(24, 2, 21),
(25, 2, 22),
(26, 2, 23),
(27, 2, 24),
(28, 4, 13),
(29, 4, 17),
(30, 4, 21),
(31, 3, 13),
(32, 3, 15);

-- --------------------------------------------------------

--
-- Table structure for table `sales`
--

CREATE TABLE `sales` (
  `id` int(11) NOT NULL,
  `invoice_number` varchar(50) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `total` decimal(10,2) NOT NULL,
  `tax` decimal(10,2) DEFAULT 0.00,
  `discount` decimal(10,2) DEFAULT 0.00,
  `tipo` enum('contado','credito') DEFAULT 'contado',
  `status` enum('completada','anulada') DEFAULT 'completada',
  `created_by` int(11) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sales`
--

INSERT INTO `sales` (`id`, `invoice_number`, `customer_id`, `total`, `tax`, `discount`, `tipo`, `status`, `created_by`, `created_at`) VALUES
(1, NULL, NULL, 518.00, 0.00, 0.00, 'contado', 'completada', 2, '2026-03-10 01:43:10'),
(2, NULL, NULL, 2576.00, 0.00, 0.00, 'contado', 'completada', 2, '2026-03-10 01:43:47'),
(3, NULL, NULL, 2576.00, 0.00, 0.00, 'contado', 'completada', 2, '2026-03-10 01:43:56'),
(4, NULL, NULL, 4918.00, 0.00, 0.00, 'contado', 'completada', 2, '2026-03-10 02:08:30'),
(5, NULL, NULL, 4968.00, 0.00, 0.00, 'contado', 'completada', 2, '2026-03-10 02:08:45'),
(6, NULL, 11, 7544.00, 0.00, 0.00, 'credito', 'completada', 2, '2026-03-10 20:03:18'),
(7, NULL, NULL, 234.00, 0.00, 0.00, 'contado', 'completada', 2, '2026-03-10 20:05:11');

-- --------------------------------------------------------

--
-- Table structure for table `sale_items`
--

CREATE TABLE `sale_items` (
  `id` int(11) NOT NULL,
  `sale_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `subtotal` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sale_items`
--

INSERT INTO `sale_items` (`id`, `sale_id`, `product_id`, `quantity`, `price`, `subtotal`) VALUES
(1, 1, 4, 1, 234.00, 234.00),
(2, 1, 6, 1, 234.00, 234.00),
(3, 1, 8, 1, 50.00, 50.00),
(4, 2, 3, 1, 2342.00, 2342.00),
(5, 2, 6, 1, 234.00, 234.00),
(6, 3, 6, 1, 234.00, 234.00),
(7, 3, 3, 1, 2342.00, 2342.00),
(8, 4, 3, 1, 2342.00, 2342.00),
(9, 4, 4, 1, 234.00, 234.00),
(10, 4, 5, 1, 2342.00, 2342.00),
(11, 5, 5, 1, 2342.00, 2342.00),
(12, 5, 4, 1, 234.00, 234.00),
(13, 5, 3, 1, 2342.00, 2342.00),
(14, 5, 8, 1, 50.00, 50.00),
(15, 6, 3, 2, 2342.00, 4684.00),
(16, 6, 6, 1, 234.00, 234.00),
(17, 6, 5, 1, 2342.00, 2342.00),
(18, 6, 4, 1, 234.00, 234.00),
(19, 6, 8, 1, 50.00, 50.00),
(20, 7, 4, 1, 234.00, 234.00);

-- --------------------------------------------------------

--
-- Table structure for table `sale_payments`
--

CREATE TABLE `sale_payments` (
  `id` int(11) NOT NULL,
  `sale_id` int(11) NOT NULL,
  `method` enum('efectivo','tarjeta','transferencia') DEFAULT 'efectivo',
  `amount` decimal(10,2) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sale_payments`
--

INSERT INTO `sale_payments` (`id`, `sale_id`, `method`, `amount`, `created_at`) VALUES
(1, 1, 'efectivo', 518.00, '2026-03-10 01:43:10'),
(2, 2, 'efectivo', 2576.00, '2026-03-10 01:43:47'),
(3, 3, 'efectivo', 2576.00, '2026-03-10 01:43:56'),
(4, 4, 'efectivo', 4918.00, '2026-03-10 02:08:30'),
(5, 5, 'efectivo', 4968.00, '2026-03-10 02:08:45'),
(6, 6, 'efectivo', 7544.00, '2026-03-10 20:03:18'),
(7, 7, 'efectivo', 234.00, '2026-03-10 20:05:11');

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` int(11) NOT NULL,
  `system_name` varchar(150) NOT NULL,
  `currency` varchar(10) DEFAULT 'USD',
  `tax` decimal(5,2) DEFAULT 0.00,
  `business_name` varchar(150) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `system_name`, `currency`, `tax`, `business_name`, `phone`, `email`, `address`, `logo`, `created_at`, `updated_at`) VALUES
(1, 'qweasd', 'USD', 1.00, 'qweasd', '1', NULL, '1', '/static/logos/output-onlinepngtools.png', '2026-03-09 23:54:10', '2026-03-10 00:12:49');

-- --------------------------------------------------------

--
-- Table structure for table `suppliers`
--

CREATE TABLE `suppliers` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `suppliers`
--

INSERT INTO `suppliers` (`id`, `name`, `phone`, `email`, `address`, `created_at`, `updated_at`) VALUES
(7, 'Distribuidora Valdez', '809-123-4567', 'contacto@valdez.com', 'Av. Independencia #123, Santo Domingo', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(8, 'Importadora Caribe', '809-234-5678', 'ventas@caribe.com', 'Calle Duarte #456, Santo Domingo', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(9, 'TecnoMundo', '809-345-6789', 'info@tecnomundo.com', 'Calle 27 de Febrero #789, Santiago', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(10, 'Alimentos RD', '809-456-7890', 'contacto@alimentosrd.com', 'Av. Luperón #321, Santo Domingo', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(11, 'Hogar y Deco', '809-567-8901', 'ventas@hogarydeco.com', 'Calle Salcedo #654, Santo Domingo', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(12, 'Deportes Pro', '809-678-9012', 'info@deportespro.com', 'Av. Independencia #987, Santiago', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(13, 'Libros & Más', '809-789-0123', 'contacto@librosymas.com', 'Calle Comercio #111, Santo Domingo', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(14, 'Electroventas', '809-890-1234', 'ventas@electroventas.com', 'Av. Winston Churchill #222, Santo Domingo', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(15, 'Mascotas Felices', '809-901-2345', 'info@mascotasfelices.com', 'Calle Hostos #333, Santiago', '2026-03-10 01:21:02', '2026-03-10 01:21:02'),
(16, 'Ferretería Central', '809-012-3456', 'contacto@ferreteriacentral.com', 'Av. 27 de Febrero #444, Santo Domingo', '2026-03-10 01:21:02', '2026-03-10 01:21:02');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` enum('admin','user') DEFAULT 'user',
  `estado` enum('Activo','Inactivo') DEFAULT 'Activo',
  `foto` varchar(255) DEFAULT NULL,
  `created` datetime DEFAULT current_timestamp(),
  `createdByName` varchar(255) NOT NULL,
  `createdById` int(11) NOT NULL,
  `empresaId` int(11) NOT NULL,
  `Correo` varchar(255) DEFAULT NULL,
  `Nombre` varchar(255) DEFAULT NULL,
  `LastLogin` datetime DEFAULT NULL,
  `forcePasswordChange` tinyint(1) NOT NULL DEFAULT 1,
  `role_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`, `role`, `estado`, `foto`, `created`, `createdByName`, `createdById`, `empresaId`, `Correo`, `Nombre`, `LastLogin`, `forcePasswordChange`, `role_id`) VALUES
(1, 'juan', '$2b$12$zuHNxDvANw62.LC058jLGemNNsEqmw7YGsjnGV08lA4DkuA6xyFAe', 'user', 'Activo', NULL, '2026-01-23 15:03:18', '', 0, 2, NULL, NULL, NULL, 1, 1),
(2, 'yermy', '$2b$12$dJVz/ZKH2Obzhe90O24Lze1zmt7tj9Qdp4H6p4IbZz/MkWxxsKmr2', 'user', 'Activo', NULL, '2026-01-23 15:03:18', '', 0, 2, 'Yermyvaldezpolanco@gmail.com', 'Yermy Valdez Polanco', '2026-03-23 13:09:08', 0, NULL),
(3, 'yvaldez', '$2b$12$mXcel8nCyebJIDLyJoUyXuXY/6ShPnE4DeYzu2jv228CP5w9yzBZu', 'admin', 'Activo', '/uploads/empleados/4850ff2e-087d-47ad-a4de-4ddd05b3b05e.png', '2026-01-28 16:17:35', 'yermy', 2, 2, 'yermy@email.com', 'Yermy Valdez', NULL, 1, NULL),
(5, 'yevaldez', '$2b$12$C9cCTw0RafoYpqbdj1QjGOuW4Vr7vZMoLFHNEOkriEq/q7AOIkENW', 'admin', 'Activo', '/uploads/empleados/cc8aa337-411d-499d-9f5a-191bf56388dd.png', '2026-01-28 16:20:34', 'yermy', 2, 2, 'yermy@email.com', 'Yermy Valdez', '2026-01-28 22:31:30', 1, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios_permisos`
--

CREATE TABLE `usuarios_permisos` (
  `usuario_id` int(11) NOT NULL,
  `permiso_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios_permisos`
--

INSERT INTO `usuarios_permisos` (`usuario_id`, `permiso_id`) VALUES
(2, 1),
(2, 2),
(2, 3),
(2, 4),
(2, 5),
(2, 6),
(2, 7),
(2, 8);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_payable`
--
ALTER TABLE `accounts_payable`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `empresas`
--
ALTER TABLE `empresas`
  ADD PRIMARY KEY (`idnew_table`),
  ADD UNIQUE KEY `idnew_table_UNIQUE` (`idnew_table`);

--
-- Indexes for table `inventory_movements`
--
ALTER TABLE `inventory_movements`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `permisos`
--
ALTER TABLE `permisos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nombre` (`nombre`);

--
-- Indexes for table `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_products_created_by` (`created_by`),
  ADD KEY `fk_products_updated_by` (`updated_by`);

--
-- Indexes for table `purchases`
--
ALTER TABLE `purchases`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `purchase_items`
--
ALTER TABLE `purchase_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `quotations`
--
ALTER TABLE `quotations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `quotation_items`
--
ALTER TABLE `quotation_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `quotation_id` (`quotation_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `role_permissions`
--
ALTER TABLE `role_permissions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `role_id` (`role_id`),
  ADD KEY `permission_id` (`permission_id`);

--
-- Indexes for table `sales`
--
ALTER TABLE `sales`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `invoice_number` (`invoice_number`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `sale_items`
--
ALTER TABLE `sale_items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sale_id` (`sale_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `sale_payments`
--
ALTER TABLE `sale_payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sale_id` (`sale_id`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `suppliers`
--
ALTER TABLE `suppliers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `role_id` (`role_id`);

--
-- Indexes for table `usuarios_permisos`
--
ALTER TABLE `usuarios_permisos`
  ADD PRIMARY KEY (`usuario_id`,`permiso_id`),
  ADD KEY `permiso_id` (`permiso_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_payable`
--
ALTER TABLE `accounts_payable`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `empresas`
--
ALTER TABLE `empresas`
  MODIFY `idnew_table` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `inventory_movements`
--
ALTER TABLE `inventory_movements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `permisos`
--
ALTER TABLE `permisos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `purchases`
--
ALTER TABLE `purchases`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `purchase_items`
--
ALTER TABLE `purchase_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `quotations`
--
ALTER TABLE `quotations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `quotation_items`
--
ALTER TABLE `quotation_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `role_permissions`
--
ALTER TABLE `role_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `sales`
--
ALTER TABLE `sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `sale_items`
--
ALTER TABLE `sale_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `sale_payments`
--
ALTER TABLE `sale_payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `suppliers`
--
ALTER TABLE `suppliers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `fk_products_created_by` FOREIGN KEY (`created_by`) REFERENCES `usuarios` (`id`),
  ADD CONSTRAINT `fk_products_updated_by` FOREIGN KEY (`updated_by`) REFERENCES `usuarios` (`id`);

--
-- Constraints for table `quotation_items`
--
ALTER TABLE `quotation_items`
  ADD CONSTRAINT `quotation_items_ibfk_1` FOREIGN KEY (`quotation_id`) REFERENCES `quotations` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `role_permissions`
--
ALTER TABLE `role_permissions`
  ADD CONSTRAINT `role_permissions_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  ADD CONSTRAINT `role_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`);

--
-- Constraints for table `sales`
--
ALTER TABLE `sales`
  ADD CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`);

--
-- Constraints for table `sale_items`
--
ALTER TABLE `sale_items`
  ADD CONSTRAINT `sale_items_ibfk_1` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `sale_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`);

--
-- Constraints for table `sale_payments`
--
ALTER TABLE `sale_payments`
  ADD CONSTRAINT `sale_payments_ibfk_1` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`);

--
-- Constraints for table `usuarios_permisos`
--
ALTER TABLE `usuarios_permisos`
  ADD CONSTRAINT `usuarios_permisos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `usuarios_permisos_ibfk_2` FOREIGN KEY (`permiso_id`) REFERENCES `permisos` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

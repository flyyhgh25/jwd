-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 20, 2024 at 07:12 AM
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
-- Database: `lembaga_pelatihan_kerja`
--

-- --------------------------------------------------------

--
-- Table structure for table `pelatihans`
--

CREATE TABLE `pelatihans` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `gambar_pelatihan` varchar(255) NOT NULL,
  `nama_pelatihan` varchar(50) NOT NULL,
  `deskripsi` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pelatihans`
--

INSERT INTO `pelatihans` (`id`, `judul`, `gambar_pelatihan`, `nama_pelatihan`, `deskripsi`) VALUES
(5, 'BNSP', 'teknisi_jaringan.jpeg', 'Teknisi Jaringan', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(6, 'BNSP', 'designerGrafis.jpg', 'Designer Grafis', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(7, 'BNSP', 'teknisi_jaringan.jpeg', 'Teknisi Jaringan', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(8, 'BNSP', 'designerGrafis.jpg', 'Designer Grafis', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(9, 'BNSP', 'Enterprise_Resource_Planning.jpeg', 'Enterprise Resource ', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(10, 'BNSP', 'content_creator.jpeg', 'Content Creator', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(11, 'BNSP', 'animator.jpeg', 'Animator', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(12, 'BNSP', 'androidDeveloper.jpeg', 'Android developer', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(13, 'BNSP', 'dataScientist.jpeg', 'Data Science', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?'),
(14, 'BNSP', 'Pelatihan_Web_Developer.jpg', 'Pelatihan Web Developer', 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Minima, dolorum doloremque eos repellat quibusdam recusandae?');

-- --------------------------------------------------------

--
-- Table structure for table `pendaftarans`
--

CREATE TABLE `pendaftarans` (
  `id` int(11) NOT NULL,
  `id_pelatihan` int(11) NOT NULL,
  `nama_lengkap` varchar(255) NOT NULL,
  `NIK` int(50) NOT NULL,
  `no_whatsapp` varchar(13) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pendaftarans`
--

INSERT INTO `pendaftarans` (`id`, `id_pelatihan`, `nama_lengkap`, `NIK`, `no_whatsapp`, `email`) VALUES
(0, 5, 'Yatinahhjjj', 2147483647, '823564844', 'yatinah@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pelatihans`
--
ALTER TABLE `pelatihans`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pendaftarans`
--
ALTER TABLE `pendaftarans`
  ADD UNIQUE KEY `id_pelatihan` (`id_pelatihan`,`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pelatihans`
--
ALTER TABLE `pelatihans`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

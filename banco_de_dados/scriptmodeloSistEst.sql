-- MySQL Script generated by MySQL Workbench
-- Tue Dec  3 11:05:52 2024
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema sistestbd
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `sistestbd` ;

-- -----------------------------------------------------
-- Schema sistestbd
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `sistestbd` DEFAULT CHARACTER SET utf8 ;
USE `sistestbd` ;

-- -----------------------------------------------------
-- Table `sistestbd`.`Usuarios`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sistestbd`.`Usuarios` ;

CREATE TABLE IF NOT EXISTS `sistestbd`.`Usuarios` (
  `idUsuarios` INT NOT NULL,
  `nome` VARCHAR(300) NOT NULL,
  `cpf` VARCHAR(11) NOT NULL,
  `num_CNH` VARCHAR(15) NULL,
  `validade_CNH` DATE NULL,
  `telefone` VARCHAR(15) NOT NULL,
  `email` VARCHAR(300) NULL,
  PRIMARY KEY (`idUsuarios`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sistestbd`.`Carros`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sistestbd`.`Carros` ;

CREATE TABLE IF NOT EXISTS `sistestbd`.`Carros` (
  `idCarros` INT NOT NULL,
  `placa` VARCHAR(10) NOT NULL,
  `marca_modelo` VARCHAR(50) NOT NULL,
  `cor` VARCHAR(50) NOT NULL,
  `fk_idUsuarios` INT NOT NULL,
  PRIMARY KEY (`idCarros`),
  INDEX `fk_Carros_Usuarios1_idx` (`fk_idUsuarios` ASC) VISIBLE,
  CONSTRAINT `fk_Carros_Usuarios1`
    FOREIGN KEY (`fk_idUsuarios`)
    REFERENCES `sistestbd`.`Usuarios` (`idUsuarios`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `sistestbd`.`Estacionamentos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `sistestbd`.`Estacionamentos` ;

CREATE TABLE IF NOT EXISTS `sistestbd`.`Estacionamentos` (
  `idEstacionamentos` INT NOT NULL,
  `fk_idCarros` INT NOT NULL,
  `data_entrada` DATE NOT NULL,
  `hora_entrada` TIME NOT NULL,
  `data_saida` DATE NULL,
  `hora_saida` TIME NULL,
  PRIMARY KEY (`idEstacionamentos`),
  INDEX `fk_Estacionamentos_Carros1_idx` (`fk_idCarros` ASC) VISIBLE,
  CONSTRAINT `fk_Estacionamentos_Carros1`
    FOREIGN KEY (`fk_idCarros`)
    REFERENCES `sistestbd`.`Carros` (`idCarros`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
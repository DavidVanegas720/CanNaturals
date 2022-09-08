-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cannaturals
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cannaturals
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cannaturals` DEFAULT CHARACTER SET utf8 ;
USE `cannaturals` ;

-- -----------------------------------------------------
-- Table `cannaturals`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(200) NULL,
  `user_type` TINYINT(1) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`products`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`products` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `price` INT NULL,
  `decription` VARCHAR(255) NULL,
  `presentacion` TINYINT(2) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_productos_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_productos_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `cannaturals`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `productos` VARCHAR(45) NULL,
  `total` INT NULL,
  `Direccion` VARCHAR(255) NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_orders_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `cannaturals`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`productos_has_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`productos_has_orders` (
  `productos_id` INT NOT NULL,
  `order_id` INT NOT NULL,
  PRIMARY KEY (`productos_id`, `order_id`),
  INDEX `fk_productos_has_orders_orders1_idx` (`order_id` ASC) VISIBLE,
  INDEX `fk_productos_has_orders_productos1_idx` (`productos_id` ASC) VISIBLE,
  CONSTRAINT `fk_productos_has_orders_productos1`
    FOREIGN KEY (`productos_id`)
    REFERENCES `cannaturals`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_productos_has_orders_orders1`
    FOREIGN KEY (`order_id`)
    REFERENCES `cannaturals`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`orders_has_users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`orders_has_users` (
  `orders_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`orders_id`, `users_id`),
  INDEX `fk_orders_has_users_users1_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_orders_has_users_orders1_idx` (`orders_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_has_users_orders1`
    FOREIGN KEY (`orders_id`)
    REFERENCES `cannaturals`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_has_users_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `cannaturals`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`productos_has_orders_has_users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`productos_has_orders_has_users` (
  `productos_has_orders_productos_id` INT NOT NULL,
  `productos_has_orders_orders_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`productos_has_orders_productos_id`, `productos_has_orders_orders_id`, `users_id`),
  INDEX `fk_productos_has_orders_has_users_users1_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_productos_has_orders_has_users_productos_has_orders1_idx` (`productos_has_orders_productos_id` ASC, `productos_has_orders_orders_id` ASC) VISIBLE,
  CONSTRAINT `fk_productos_has_orders_has_users_productos_has_orders1`
    FOREIGN KEY (`productos_has_orders_productos_id` , `productos_has_orders_orders_id`)
    REFERENCES `cannaturals`.`productos_has_orders` (`productos_id` , `order_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_productos_has_orders_has_users_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `cannaturals`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`orders_has_productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`orders_has_productos` (
  `orders_id` INT NOT NULL,
  `productos_id` INT NOT NULL,
  PRIMARY KEY (`orders_id`, `productos_id`),
  INDEX `fk_orders_has_productos_productos1_idx` (`productos_id` ASC) VISIBLE,
  INDEX `fk_orders_has_productos_orders1_idx` (`orders_id` ASC) VISIBLE,
  CONSTRAINT `fk_orders_has_productos_orders1`
    FOREIGN KEY (`orders_id`)
    REFERENCES `cannaturals`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_orders_has_productos_productos1`
    FOREIGN KEY (`productos_id`)
    REFERENCES `cannaturals`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`users_has_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`users_has_orders` (
  `users_id` INT NOT NULL,
  `orders_id` INT NOT NULL,
  PRIMARY KEY (`users_id`, `orders_id`),
  INDEX `fk_users_has_orders_orders1_idx` (`orders_id` ASC) VISIBLE,
  INDEX `fk_users_has_orders_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_orders_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `cannaturals`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_orders_orders1`
    FOREIGN KEY (`orders_id`)
    REFERENCES `cannaturals`.`orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cannaturals`.`reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cannaturals`.`reviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `comment` TEXT(255) NULL,
  `likes` TINYINT(1) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `product_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_reviews_productos1_idx` (`product_id` ASC) VISIBLE,
  INDEX `fk_reviews_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_reviews_productos1`
    FOREIGN KEY (`product_id`)
    REFERENCES `cannaturals`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reviews_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `cannaturals`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

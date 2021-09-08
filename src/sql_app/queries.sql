CREATE TABLE `wedding_guests`.`families` (
  `family_id` INT NOT NULL AUTO_INCREMENT,
  `family_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`family_id`),
  UNIQUE INDEX `family_name_UNIQUE` (`family_name` ASC));
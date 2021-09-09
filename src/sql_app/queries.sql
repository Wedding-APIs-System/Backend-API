CREATE TABLE `wedding_guests`.`families` (
  `family_id` INT NOT NULL AUTO_INCREMENT,
  `family_name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`family_id`),
  UNIQUE INDEX `family_name_UNIQUE` (`family_name` ASC));

  <<-- Check foreign key relationships
  SELECT   TABLE_NAME,   COLUMN_NAME,   CONSTRAINT_NAME,      REFERENCED_TABLE_NAME,   REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE   REFERENCED_TABLE_NAME = 'families';  
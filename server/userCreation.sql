drop user 'admin'@'localhost';
drop user 'doctor'@'localhost';
drop user 'nurse'@'localhost';


flush privileges;
-- create admin user and giving root access

CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin123';
GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';

-- create doctor user and giving view, insert, update and modify access

CREATE USER 'doctor'@'localhost' IDENTIFIED BY 'doctor123';
GRANT SELECT ON covidVaccine_656.* TO 'doctor'@'localhost';
GRANT INSERT ON covidVaccine_656.* TO 'doctor'@'localhost';
GRANT UPDATE ON covidVaccine_656.* TO 'doctor'@'localhost';


-- create nurse user and giving view, insert, update and modify access

CREATE USER 'nurse'@'localhost' IDENTIFIED BY 'nurse123';
GRANT SELECT ON covidVaccine_656.* TO 'nurse'@'localhost';
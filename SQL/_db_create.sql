
CREATE DATABASE IF NOT EXISTS auth;
CREATE DATABASE IF NOT EXISTS other;
CREATE DATABASE IF NOT EXISTS logs;
CREATE DATABASE IF NOT EXISTS characters;
CREATE DATABASE IF NOT EXISTS laniatracker;

CREATE USER 'newmmo'@'localhost' IDENTIFIED BY 'newmmo';

GRANT SELECT, INSERT, UPDATE, DELETE ON `characters`.* TO 'newmmo'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE ON `logs`.* TO 'newmmo'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE ON `other`.* TO 'newmmo'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE ON `auth`.* TO 'newmmo'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE ON `laniatracker`.* TO 'newmmo'@'localhost';




CREATE DATABASE IF NOT EXISTS tourny_mate;



CREATE TABLE IF NOT EXISTS NOT userInfo(
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(20) UNIQUE,
  fullName VARCHAR(30) NOT NULL,
  email VARCHAR(30) NOT NULL,
  role_id VARCHAR(20) NOT NULL,
  phone VARCHAR(11) NOT NULL,
  dp VARCHAR(100),
  cover VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS player(
  id INT AUTO_INCREMENT PRIMARY KEY,
  sports_type VARCHAR(10) NOT NULL,
  position VARCHAR(10) NOT NULL,
  team_id INT,
  user_id INT,
  Foreign Key (team_id) REFERENCES (team),
  Foreign Key (user_id) REFERENCES (userInfo)
);


CREATE TABLE IF NOT EXISTS team(
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(30) NOT NULL,
  manager_id INT,
  logo VARCHAR(100),
  Foreign Key (manager_id) REFERENCES (manager)
);

CREATE TABLE IF NOT EXISTS match(
  id INT AUTO_INCREMENT PRIMARY KEY,
  team_1_id INT,
  team_2_id INT,
  match_day DATE NOT NULL,
  offical_1_id INT ,
  offical_2_id INT ,
  offical_3_id INT ,
  match_type VARCHAR(10) NOT NULL,
  Foreign Key (team_1_id) REFERENCES (team),
  Foreign Key (team_2_id) REFERENCES (team),    
  Foreign Key (offical_1_id) REFERENCES (userInfo),
  Foreign Key (offical_2_id) REFERENCES (userInfo)
  Foreign Key (offical_3_id) REFERENCES (userInfo),
  
);

CREATE TABLE IF NOT EXISTS score(
  score_id INT AUTO_INCREMENT PRIMARY KEY,
  match_id INT,
  team_1_id INT,
  team_2_id INT,
  team_1_score INT NOT NULL,
  team_2_score INT NOT NULL,
  winner_name VARCHAR(30) NOT NULL,
  Foreign Key (match_id) REFERENCES (match),
  Foreign Key (team_1_id) REFERENCES (team),
  Foreign Key (team_2_id) REFERENCES (team)
);

CREATE TABLE IF NOT EXISTS individual_score(
  match_id INT,
  user_id INT,
  no_of_matches INT,
  odi_runs INT,
  short_pitch_runs INT,
  t20_runs INT,
  total_six INT,
  total_fours INT,
  total_wickets INT,
  total_over FLOAT,
  total_dots INT,
  total_goals INT,
  total_saves INT, 
  total_assists INT,
  total_wins_football INT,
  total_wins_cricket INT,
  total_yellow INT,
  total_red INT,
  positions VARCHAR(10),
  Foreign Key (match_id) REFERENCES (match),
  Foreign Key (user_id) REFERENCES (userInfo),

);

CREATE TABLE IF NOT EXISTS tournament(
  id INT AUTO_INCREMENT PRIMARY KEY,
  creator_id INT,
  venue VARCHAR(40) NOT NULL,
  region VARCHAR(40) NOT NULL,
  district VARCHAR(40) NOT NULL,
  thana VARCHAR(40) NOT NULL,
  area VARCHAR(40) NOT NULL,
  tour_type VARCHAR(10) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  Foreign Key (creator_id) REFERENCES (userInfo)

);

CREATE TABLE IF NOT EXISTS tournament_team(
  id INT AUTO_INCREMENT PRIMARY KEY,
  tournament_id INT,
  team_id INT,
  Foreign Key (tournament_id) REFERENCES (tournament),
  Foreign Key (team_id) REFERENCES (team)
);

CREATE TABLE IF NOT EXISTS tournament_officals(
  id INT AUTO_INCREMENT PRIMARY KEY,
  officals_id INT,
  tournament_id INT,
  Foreign Key (officals_id) REFERENCES (userInfo),
  Foreign Key (tournament_id) REFERENCES (tournament)
);

CREATE TABLE IF NOT EXISTS manager(
  id INT AUTO_INCREMENT PRIMARY KEY,
  team_id INT,
  Foreign Key (team_id) REFERENCES (team)
);
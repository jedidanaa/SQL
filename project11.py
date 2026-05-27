CREATE TABLE Teams (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(100) NOT NULL
);

CREATE TABLE Players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    jersey_number INT UNIQUE,
    age INT CHECK (age >= 16),
    position VARCHAR(50) DEFAULT 'Guard',
    salary DECIMAL(10,2) CHECK (salary > 0),
    team_id INT,
    FOREIGN KEY (team_id) REFERENCES Teams(team_id)
);
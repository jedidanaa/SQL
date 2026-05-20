-- Teams table
CREATE TABLE Teams (
    TeamID INT PRIMARY KEY,
    TeamName VARCHAR(50),
    City VARCHAR(50)
);

-- Players table
CREATE TABLE Players (
    PlayerID INT PRIMARY KEY,
    Name VARCHAR(50),
    Position VARCHAR(20),
    TeamID INT,
    FOREIGN KEY (TeamID) REFERENCES Teams(TeamID)
);

-- Games table
CREATE TABLE Games (
    GameID INT PRIMARY KEY,
    HomeTeamID INT,
    AwayTeamID INT,
    GameDate DATE,
    HomeScore INT,
    AwayScore INT,
    FOREIGN KEY (HomeTeamID) REFERENCES Teams(TeamID),
    FOREIGN KEY (AwayTeamID) REFERENCES Teams(TeamID)
);

-- Query: List each game with its winning team
SELECT g.GameID, g.GameDate, 
       CASE 
         WHEN g.HomeScore > g.AwayScore THEN ht.TeamName
         ELSE at.TeamName 
       END AS Winner
FROM Games g
JOIN Teams ht ON g.HomeTeamID = ht.TeamID
JOIN Teams at ON g.AwayTeamID = at.TeamID;

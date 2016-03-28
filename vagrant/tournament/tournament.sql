-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament
CREATE DATABASE tournament
\c tournament;

CREATE TABLE players(
	
	player_id serial PRIMARY KEY,
	name text NOT NULL
	
	);


CREATE TABLE matches(


	match_id serial PRIMARY KEY NOT NULL,
	winner serial references players (player_id),
	loser serial references players (player_id)

);

CREATE VIEW view_wins AS
SELECT players.player_id AS id, players.name AS name, count(matches.winner) AS wins
FROM players LEFT JOIN matches 
ON players.player_id = matches.winner 
GROUP BY players.player_id;


CREATE VIEW view_matches AS
SELECT players.player_id AS id, count(matches.winner) AS match 
FROM players LEFT JOIN matches 
ON players.player_id = matches.winner OR players.player_id = matches.loser 
GROUP BY players.player_id;
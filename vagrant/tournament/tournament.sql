-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

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
SELECT players.player_id as id, players.name as name, count(matches.winner) as wins
from players left join matches 
on players.player_id = matches.winner 
group by players.player_id;


CREATE VIEW view_matches AS
SELECT players.player_id as id, count(matches.winner) as match 
from players left join matches 
on players.player_id = matches.winner or players.player_id = matches.loser 
group by players.player_id;
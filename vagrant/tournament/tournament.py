#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""

    conn = psycopg2.connect("dbname=tournament")
    c = conn.cursor()
    return conn, c 


def deleteMatches():
    """Remove all the match records from the database."""
    conn, c = connect()
    c.execute("TRUNCATE matches;")
    conn.commit() 
    conn.close()

def deletePlayers():
    """Remove all the player records from the database."""
    conn, c = connect()
    c.execute("TRUNCATE players CASCADE;")
    conn.commit() 
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn, c = connect()
    c.execute("SELECT count(*) AS num FROM players;")
    count = c.fetchall()
    conn.close()
    return count[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """

    conn, c = connect()
    cmd = "INSERT INTO players (name) VALUES(%s);"
    c.execute(cmd, (name,))
    conn.commit() 
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    conn, c = connect()
    cmd = "SELECT win_table.id, win_table.name, win_table.wins, match_table.match FROM view_wins AS win_table LEFT JOIN view_matches AS match_table ON win_table.id = match_table.id ORDER BY win_table.wins DESC;"
    c.execute(cmd)
    standings = c.fetchall()
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn, c = connect()
    cmd = "INSERT INTO matches (winner, loser) VALUES(%s, %s);"
    c.execute(cmd, (winner, loser))
    conn.commit() 
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    conn, c = connect()
    pairings = []
    nPlayers = len(standings)
    if nPlayers % 2 == 0:
        while len(standings) > 0:
            id1 = standings[len(standings)-1][0]
            id2 = 0
            i = 2
            while i<=len(standings):
                id2 = standings[len(standings)-i][0]
                ## Preventing Rematch by checking for previous match data from matches table
                cmd = "SELECT match_id FROM matches WHERE (winner = %s AND loser = %s) OR (winner = %s AND loser = %s)"
                c.execute(cmd, (id1, id2, id2, id1))
                matches = c.fetchall()
                if len(matches) == 0:
                    break
                else:
                    i = i + 1
            name1 = standings.pop()[1]
            name2 = standings.pop(1-i)[1]
            pair = (id2, name2, id1, name1)
            pairings.append(pair)
        conn.close()
        pairings.reverse()
        return pairings
    elif nPlayers % 2 == 1:
        ## For odd no. of players a bye is provided in which the player gets a auto win. He is not provided mpre than 1 byes.
        id1 = 0
        for row in standings.reverse():
            id1 = row[0]
            cmd = "SELECT match_id FROM matches WHERE (winner = %s AND loser = %s)" 
            c.execute(cmd, (id1, id1))
            matches = c.fetchall()
            if len(matches) == 0:
                del row
                break
        reportMatch(id1, id1)
        while len(standings) > 0:
            id1 = standings[len(standings)-1][0]
            id2 = 0
            i = 2
            while i<=len(standings):
                id2 = standings[len(standings)-i][0]
                ## Preventing Rematch by checking for previous match data from matches table
                cmd = "SELECT match_id FROM matches WHERE (winner = %s AND loser = %s) OR (winner = %s AND loser = %s)"
                c.execute(cmd, (id1, id2, id2, id1))
                matches = c.fetchall()
                if len(matches) == 0:
                    break
                else:
                    i = i + 1
            name1 = standings.pop()[1]
            name2 = standings.pop(1-i)[1]
            pair = (id2, name2, id1, name1)
            pairings.append(pair)
        conn.close()
        pairings.reverse()
        return pairings

# Swiss Tournament System

##### Database backed Application to setup a swiss pairing based tournament.         

## QuickStart

Follow these easy steps to set up:

- Clone the repo: `git clone https://github.com/evilc0des/fullstack-nanodegree-vm.git`
- Manual install
    - Install [Python 2.7](https://www.python.org/ftp/python/2.7.11/python-2.7.11.msi)
    - Install [PostgreSQL](http://www.postgresql.org/download/)
- Or just use Vagrant
    - Install [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
    - Install [Vagrant](https://www.vagrantup.com/downloads.html)
    - First `vagrant up`
    - and then `vagrant ssh`
- Go to `~/vagrant/tournament`

### Getting Started

##### Included Files

  - **tournament.sql**  
    This file is used to set up your database schema (the table representation of your data structure).
    - connect to the postgreSQL databse
        
        `$ psql`
        
    - execute the tournament.sql file to create the databse and build the tables
    
        `\i tournament.sql`
  - **tournament.py** 
    This file is used to provide access to your database via a library of functions       which can add, delete or query data in your database to another python program (a     client program). 
    The file should be imported into your python file for using the various functions available. 
    <br>`from tournament import *`
   <br> The functions available are as follows
    <table class="c36"><tbody><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c21 c11 c26"> **tournament.py** </span><span class="c25 c41 c11">function</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c24"><span class="c21 c11 c26"> **tournament_test.py** </span><span class="c25 c11 c41">test function</span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c4"> **connect** </span></p><p class="c18 c7"><span class="c11 c42">Meant to connect to the database. Already set up for you.</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c22"><span class="c5 c21 c33"></span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c5 c4"> **deleteMatches** </span></p><p class="c18 c7"><span class="c2">Remove all the matches records from the database.</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c24"><span class="c4">testDeleteMatches</span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c5 c4"> **deletePlayers** </span></p><p class="c7 c18"><span class="c2">Remove all the player records from the database.</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c24"><span class="c4">testDelete</span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c5 c4"> **countPlayers** </span></p><p class="c18 c7"><span class="c2">Returns the number of players currently registered</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c7"><span class="c4 c5">testCount</span></p><p class="c18 c22"><span class="c5 c21 c28 c33"></span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c4"> **registerPlayer**</span><bR><br><span class="c2">Adds a player to the tournament database.</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c7"><span class="c4">testRegister, testRegisterCountDelete</span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c5 c4"> **playerStandings** </span></p><p class="c18 c7"><span class="c2">Returns a list of the players and their win records, sorted by wins. You can use the player standings table created in your .sql file for reference.</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c24"><span class="c4">testStandingsBeforeMatches</span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c5 c4"> **reportMatch** </span></p><p class="c18 c7"><span class="c2">This is to simply populate the matches table and record the winner and loser as (winner,loser) in the insert statement.</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c24"><span class="c4">testReportMatches</span></p></td></tr><tr class="c10"><td class="c3" colspan="1" rowspan="1"><p class="c18 c7"><span class="c5 c4"> **swissPairings** </span></p><p class="c18 c7"><span class="c5 c2 c31">Returns a list of pairs of players for the next round of a match. Here all we are doing is the pairing of alternate players from the player standings table, zipping them up and appending them to a list with values:</span></p><p class="c18 c7"><span class="c2">(id1, name1, id2, name2)</span></p></td><td class="c30" colspan="1" rowspan="1"><p class="c18 c7"><span class="c5 c4">testPairings</span></p><p class="c18 c22"><span class="c5 c21 c33 c28"></span></p></td></tr></tbody></table>
  
  - **tournament_test.py** 
  
     This is a client program which will test functions written in the tournament.py module and the proper setup of the database.
     Just run it with *Python* from **cmd**
     
     `$ python python_test.py`
     
#### Copyright, Ownership, License etc etc...

This is a project submission for Udacity Full-stack Web Developer Nanodegree. The _**fullstack-nanodegree-vm**_ repository is forked from udacity and changes are introduced as prescribed.
# Database starting 

-- main process
mongod --dbpath ~/data/db


-- child process
from folder: "backend" run: 
mongod --dbpath ~/data/db --fork --logpath ~/data/mongod.log

to stop:
tail -n 10 ~/data/mongod.log

# Database starting 

from folder: "backend" run: 

-- main process
mongod --dbpath ~/data/db


-- child process
mongod --dbpath ~/data/db --fork --logpath ~/data/mongod.log

to stop:
tail -n 10 ~/data/mongod.log


# Server starting
-- WSL / Linux
source venv/bin/activate

-- Windows 
call venv/bin/activate/activate.bat  (unsure needa test)

pip install requirements.txt

python3 app/main.py
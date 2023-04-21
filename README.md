# MySQL + Flask Boilerplate + Local Appsmith Project
# a Mythical Database for the wizards & aristocrats of the lands

jbINC implemented a REST API to facilitate the online processing and transaction of dragon boots. Our databases, bootstrapped with current players and currencies to function, supports an emerging world. Online accounts can customize their characters, whether its daring hunters fighting dragons and taking on quests, brute cobblers forging the tools and boots that run the lands, or sneaky shopkeepers networking and controlling the transactions... there is something for everyone!

## Links

MySQL + Flask Boilerplate Repo: https://github.com/superdarchie/Dragon_Boots_App.git

Appsmith Repo: https://github.com/superdarchie/Dragon_Boots_Appsmith.git

Project Video: https://youtu.be/OsKqFxFWBZo

## How to start the Docker Desktop containers

1. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
2. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

## Accesing the program

1. A MySQL 8 container supports the databases and data models. In Datagrip, this can be connected using the public port and root user with the password found in the db_root_password.txt.
2. A Python Flask container implements our blueprints for two user personas: Hunter (/h) + Wizard (/w).
3. A Local AppSmith Server is the logic side, where customers can interact with the model via GET, PUT, POST, and DELETE commands. In your browser, the user can connect through localhost:8080. Routes through appsmith you can utilize the web port.

## CONTACT

If you have problems, questions, or ideas, please kindly keep them to yourself. Unless your name is Dr. Fontenot, in which case, please redirect all problems, quesitons, or ideas to Dallon Archibald, Javier Vidal, and Tyler King via Slack.
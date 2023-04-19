DROP DATABASE IF EXISTS jbINC_db;

CREATE DATABASE jbINC_db;

grant all privileges on jbINC_db.* to 'webapp'@'%';
flush privileges;

USE jbINC_db;

CREATE TABLE Common_Attributes (
    id_number INTEGER PRIMARY KEY AUTO_INCREMENT,
    crystal_ball_number varchar(25) UNIQUE,
    age INTEGER,
    pay decimal,
    realm varchar(50) NOT NULL,
    username varchar(30) NOT NULL,
    start_date DATETIME DEFAULT current_timestamp
);

CREATE TABLE Shop (
    galactic_port_id INTEGER,
    realm VARCHAR(50),
    description VARCHAR(200) NOT NULL,
    open_time VARCHAR(100) NOT NULL,
    close_time VARCHAR(100) NOT NULL,
    PRIMARY KEY (galactic_port_id, realm)
);

CREATE TABLE Shopkeeper (
    s_id INTEGER AUTO_INCREMENT, 
    id_number INTEGER NOT NULL,
    favor smallint NOT NULL,
    galactic_port_id INTEGER,
    realm VARCHAR(50),
    PRIMARY KEY (s_id),
    FOREIGN KEY (id_number) REFERENCES Common_Attributes(id_number) ON DELETE RESTRICT,
    FOREIGN KEY(galactic_port_id, realm) REFERENCES Shop(galactic_port_id, realm) ON UPDATE CASCADE
);

CREATE TABLE Shopkeeper_Keys (
    s_id INTEGER,
    s_key VARCHAR(50),
    PRIMARY KEY (s_id, s_key),
    FOREIGN KEY (s_id) REFERENCES Shopkeeper(s_id) ON UPDATE CASCADE
);

CREATE TABLE Dragons (
    name VARCHAR(50) PRIMARY KEY,
    age INTEGER,
    hp smallint,
    size VARCHAR(25),
    weakness VARCHAR(50),
    damage_type VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE Quests (
    quest_id INTEGER PRIMARY KEY,
    s_id INTEGER,
    dragon_name VARCHAR(100),
    reward INTEGER NOT NULL,
    difficulty VARCHAR(3) NOT NULL,
    description VARCHAR(200) NOT NULL,
    completion_date VARCHAR(15) NOT NULL,
    FOREIGN KEY (s_id) REFERENCES Shopkeeper(s_id) ON UPDATE CASCADE,
    FOREIGN KEY (dragon_name) REFERENCES Dragons(name) ON UPDATE CASCADE
);

CREATE TABLE Hunters (
    h_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_number int NOT NULL,
    hp smallint NOT NULL,
    damage smallint NOT NULL,
    speed smallint NOT NULL,
    defense smallint NOT NULL,
    quest_id INTEGER,
    quest_date VARCHAR(15),
    FOREIGN KEY (id_number) REFERENCES Common_Attributes(id_number) ON DELETE RESTRICT,
    FOREIGN KEY (quest_id) REFERENCES Quests(quest_id) ON UPDATE CASCADE
);


CREATE TABLE Forge (
    forge_id INTEGER PRIMARY KEY,
    magical_fuel INTEGER NOT NULL,
    realm varchar(50) NOT NULL
);

CREATE TABLE Cobblers (
    c_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_number INTEGER NOT NULL,
    title varchar(50) NOT NULL,
    iq smallint NOT NULL,
    task varchar(100) NOT NULL,
    forge_id INTEGER,
    FOREIGN KEY (id_number) REFERENCES Common_Attributes(id_number) ON DELETE RESTRICT,
    FOREIGN KEY (forge_id) REFERENCES Forge(forge_id) ON UPDATE CASCADE
);

CREATE TABLE Tools (
    t_id INTEGER PRIMARY KEY,
    h_id INTEGER,
    c_id INTEGER,
    name varchar(100) NOT NULL,
    type varchar(50) NOT NULL,
    material varchar(50) NOT NULL,
    FOREIGN KEY (h_id) REFERENCES Hunters(h_id) ON UPDATE CASCADE,
    FOREIGN KEY (c_id) REFERENCES Cobblers(c_id) ON UPDATE CASCADE
);

CREATE TABLE Boots (
    boot_id INTEGER,
    forge_id INTEGER,
    materials varchar(50) NOT NULL,
    name varchar(100) NOT NULL,
    size varchar(3),
    galactic_port_id INTEGER,
    realm varchar(50),
    enchantment_1 varchar(50),
    enchantment_2 varchar(50),
    enchantment_3 varchar(50),
    PRIMARY KEY (boot_id, forge_id),
    FOREIGN KEY (forge_id) REFERENCES Forge(forge_id) ON UPDATE CASCADE,
    FOREIGN KEY (galactic_port_id, realm) REFERENCES Shop(galactic_port_id, realm) ON UPDATE CASCADE
);

CREATE TABLE Scales (
    type varchar(50),
    dragon_name varchar(100),
    damage_bonus smallint,
    durability smallint,
    protection_type smallint,
    color varchar(25) NOT NULL,
    forge_id INTEGER,
    galactic_port_id INTEGER,
    realm varchar(50),
    stock_quantity INTEGER,
    forge_quantity INTEGER,
    PRIMARY KEY (type, dragon_name),
    FOREIGN KEY (dragon_name) REFERENCES Dragons(name),
    FOREIGN KEY (forge_id) REFERENCES Forge(forge_id) ON UPDATE CASCADE,
    FOREIGN KEY (galactic_port_id, realm) REFERENCES Shop(galactic_port_id, realm) ON UPDATE CASCADE
);

CREATE TABLE Potions (
    potion_id INTEGER PRIMARY KEY,
    ingredients TEXT NOT NULL,
    time_to_make decimal NOT NULL,
    damage_bonus smallint,
    protection_type smallint,
    duration decimal,
    galactic_port_id INTEGER,
    realm varchar(50),
    stock_quantity INTEGER,
    FOREIGN KEY (galactic_port_id, realm) REFERENCES Shop(galactic_port_id, realm) ON UPDATE CASCADE
);

CREATE TABLE Wizards (
    id_numb INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    crystal_ball_number VARCHAR(50) UNIQUE,
    address VARCHAR(50),
    realm VARCHAR(50),
    gold_vault_number INTEGER UNIQUE
);

CREATE TABLE Orders (
    order_number INTEGER,
    wizard_id INTEGER,
    address VARCHAR(50) NOT NULL,
    realm VARCHAR(50) NOT NULL,
    gold_vault_number INTEGER NOT NULL,
    s_id INTEGER,
    PRIMARY KEY(order_number, wizard_id),
    FOREIGN KEY(wizard_id) REFERENCES Wizards(id_numb) ON UPDATE CASCADE,
    FOREIGN KEY (s_id) REFERENCES Shopkeeper(s_id) ON UPDATE CASCADE
);

CREATE TABLE Potion_Orders (
    order_number INTEGER,
    potion_id INTEGER,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL NOT NULL,
    PRIMARY KEY (order_number, potion_id),
    FOREIGN KEY (order_number) REFERENCES Orders(order_number),
    FOREIGN KEY (potion_id) REFERENCES Potions(potion_id)
);

CREATE TABLE Boot_Orders (
    order_number INTEGER,
    boot_id INTEGER,
    forge_id INTEGER,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL NOT NULL,
    PRIMARY KEY(order_number, boot_id, forge_id),
    FOREIGN KEY(order_number) REFERENCES Orders(order_number),
    FOREIGN KEY (boot_id, forge_id) REFERENCES Boots(boot_id, forge_id)
);

CREATE TABLE Scale_Orders (
    order_number INTEGER,
    type VARCHAR(50),
    dragon_name VARCHAR(50),
    quantity INTEGER NOT NULL,
    unit_price DECIMAL NOT NULL,
    PRIMARY KEY(order_number, type, dragon_name),
    FOREIGN KEY(order_number) REFERENCES Orders(order_number),
    FOREIGN KEY (type, dragon_name) REFERENCES Scales(type, dragon_name)
);
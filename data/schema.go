package data 

import "github.com/jmoiron/sqlx"




func CreateTables(db *sqlx.DB) error {
    tables := `        
      CREATE TABLE IF NOT EXISTS sessions ();

        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(11) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE
        );
        
        CREATE TABLE IF NOT EXISTS addresses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME,
            is_supplier BOOLEAN NOT NULL DEFAULT FALSE,
            street_1 VARCHAR(200) NOT NULL,
            street_2 VARCHAR(200),
            city VARCHAR(100) NOT NULL,
            state VARCHAR(2),
            zip VARCHAR(10) NOT NULL
        );


        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME,
            name VARCHAR(100) NOT NULL UNIQUE,
            street VARCHAR(200) NOT NULL,
            street_2 VARCHAR(200),
            city VARCHAR(100) NOT NULL,
            state VARCHAR(2) NOT NULL,
            zip VARCHAR(10) NOT NULL
        );

        -- color options are just going to be referenced by foreign key so you can keep track of where
        -- to get specific colors
        
        CREATE TABLE IF NOT EXISTS color_options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            color VARCHAR(100) NOT NULL,
            supplier_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
        );

        -- similar to color options, just going to be accessed as a foreign key refernce to item listings. 
        CREATE TABLE IF NOT EXISTS accessory_options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME
        );

        -- Basically just the coil size or profile
        CREATE TABLE IF NOT EXISTS coil_sizes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            deleted_at DATETIME
        );
    `
    db.MustExec(tables)
    
    return nil 
}



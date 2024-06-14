import quart_db


# When using sqlite3, you can only execute one statement at a time.

async def migrate(connection: quart_db.Connection):
    await connection.execute("""
        create table if not exists company_address(
            id serial primary key,
            street1 varchar(255),
            street2 varchar(255),
            city varchar(255),
            st varchar(2),
            zip varchar(5)
        );
    """)
    await connection.execute("""
        create table if not exists branch(
            id serial primary key,
            branch_name varchar(100),
            address_id integer not null,
            foreign key (address_id) references company_address(id)
        );
    """)
    await connection.execute("""
        create table if not exists warehouse(
            id serial primary key,
            warehouse_name varchar(100),
            address_id integer not null,
            branch_id integer not null,
            foreign key (address_id) references company_address(id),
            foreign key (branch_id) references branch(id)
        );
    """)
    await connection.execute("""    
        create table if not exists loop_program(
            id serial primary key,
            program_name varchar(100),
            operating_branch_id integer not null, -- operatting branch references the branch it is based out of
            foreign key (operating_branch_id) references branch(id)
        );
    """)
    await connection.execute("""    
        -- -- Warehouse location are bins/shelves in the warehosue
        create table if not exists warehouse_location(
            id serial primary key,
            warehouse_id integer not null,
            location varchar(100) not null,
            foreign key (warehouse_id) references warehouse(id)
        );
    """)
    await connection.execute("""    
        -- create table if not exists warehouse_role();
        
        -- create table if not exists warehouse_user();
        
        -- create table if not exists inside_sales_role();
        
        -- create table if not exists inside_sales_user();
        
        -- create table if not exists outside_sales_role();
        
        -- create table if not exists outside_sales_user();
        
        -- create table if not exists credit_role();
        
        -- create table if not exists credit_user();
        
        -- create table if not exists customer_account(); 
        
        -- create table if not exists product_category();
        
        -- create table if not exists product();
        
        create table if not exists status_code (
            id serial primary key, 
            status_name varchar(60) not null,
            status_description varchar(255)
        );
    """)
    await connection.execute("""    
        -- This is the backbone of the application. 
        create table if not exists journal(
            id serial primary key,
            created_at timestamp not null default current_timestamp,
            updated_at timestamp,
            deleted_at timestamp,
            status_code_id integer not null,
        
            foreign key (status_code_id) references status_code(id)
        ); 
    """)
    await connection.execute("""    
        -- create table if not exists order ();
        
        -- create table if not exists note ();
        
        -- create table if not exists task_list ();
        
        create table if not exists checklist(
            id serial primary key,
            created_at timestamp not null default current_timestamp,
            deleted_at timestamp,
            complete boolean not null default false,
            checklist_name varchar(100) not null,
            checklist_description varchar(255)
        );
    """)
    await connection.execute("""    
        create table if not exists checklist_item (
            id serial primary key,
            checklist_id integer not null,
            created_at timestamp not null default current_timestamp,
            deleted_at timestamp,
            complete boolean default false, 
            item_name varchar(100) not null,
            item_description varchar(255),
            foreign key (checklist_id) references checklist(id)
        );
    """)
    await connection.execute("""    
        create table if not exists checklist_item_stipulation (
            id serial primary key,
            checklist_item_id integer not null,
            created_at timestamp not null default current_timestamp,
            deleted_at timestamp,
            completed_at timestamp,
            complete boolean not null default false,
            foreign key (checklist_item_id) references checklist_item(id)
        );
        
        -- create table if not exists issue (); 
        -- for when you have problems with the order, or something they complain about
    """)


async def valid_migration(connection: quart_db.Connection) -> bool:
    return True
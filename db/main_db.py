# main_db.py
import sqlite3
from db import queries


# db = sqlite3.connect('db/registered.sqlite3')
db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def DataBase_create():
    if db:
        print('Database is enabled!')
    cursor.execute(queries.CREATE_TABLE_registered)
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_store_details)
    cursor.execute(queries.CREATE_TABLE_collection_products)

async def sql_insert_registered(fullname, age, gender, email, photo):
    cursor.execute(queries.INSERT_registered_QUERY, (
        fullname, age, gender, email, photo
    ))
    db.commit()

async def sql_insert_store(name_product, size, price, product_id, photo):
    cursor.execute(queries.INSERT_store_QUERY, (
        name_product, size, price, product_id, photo
    ))
    db.commit()

async def sql_insert_store_detail(category, product_id, info_product):
    cursor.execute(queries.INSERT_store_details_QUERY, (
        category, product_id, info_product
    ))
    db.commit()

async def sql_insert_collection_product(product_id, collection):
    cursor.execute(queries.INSERT_collection_products_QUERY, (
        product_id, collection
    ))
    db.commit()

#==================================================
# CRUD
def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM store s
    INNER JOIN store_details sd 
    ON s.product_id = sd.product_id
    """).fetchall()
    conn.close()
    return products

# CRUD - Delete
# =====================================================

def delete_product(product_id):
    conn = get_db_connection()

    conn.execute('DELETE FROM collection_products WHERE product_id = ?', (product_id,))


    conn.execute('DELETE FROM store_details WHERE product_id = ?', (product_id,))


    conn.execute('DELETE FROM store WHERE product_id = ?', (product_id,))

    conn.commit()
    conn.close()

# CRUD -
# =====================================================

def update_product_field(product_id, field_name, new_value):
    store_table = ["name_product", "size", "price", "product_id", "photo"]
    store_details = ["category", "product_id", "info_product"]
    collection_table = ['product_id', 'collection']
    conn = get_db_connection()

    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in store_details:
            query = f'UPDATE store_details SET {field_name} = ? WHERE product_id = ?'
        elif field_name in collection_table:
            query = f'UPDATE collection SET {field_name} = ? WHERE product_id = ?'
        else:
            raise ValueError(f"Invalid field: {field_name}")

        conn.execute(query, (new_value, product_id))
        conn.commit()

    except sqlite3.OperationalError as error:
        print(f"Error: {error}")

    finally:
        conn.close()

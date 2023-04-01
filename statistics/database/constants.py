TABLES_MAP = {
    "companies": {
        "name": "TEXT",
        "supplier_inn": "VARCHAR(12)",
        "supplier_kpp": "VARCHAR(9)",
        "okved": "TEXT",
        "status": "TEXT",
        "count_managers": "INTEGER"
    },
    "contracts": {
        "contract_reg_number": "TEXT",
        "id": "TEXT",
        "price": "DECIMAL(10, 2)",
        "contract_conclusion_date": "DATE"
    },
    "participants": {
        "id": "TEXT",
        "supplier_inn": "TEXT",
        "is_winner": "TEXT"
    },
    "purchases": {
        "id": "TEXT",
        "purchase_name": "TEXT",
        "lot_name": "TEXT",
        "price": "DECIMAL(10, 2)",
        "customer_inn": "VARCHAR(12)",
        "customer_name": "TEXT",
        "delivery_region": "TEXT",
        "publish_date": "TIMESTAMP",
        "contract_category": "TEXT"
    }
}

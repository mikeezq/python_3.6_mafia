from .migrations import create_tables, copy_data

if __name__ == "__main__":
    create_tables()
    copy_data()
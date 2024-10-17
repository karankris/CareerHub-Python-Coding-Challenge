# util/db_property_util.py

import pyodbc

# util/db_property_util.py
class DBPropertyUtil:
    @staticmethod
    def get_property_string():
        # Example values; replace these with your actual configuration retrieval logic
        host = r"DESKTOP-R2UME43\SQLEXPRESS"  # e.g., "localhost" or "192.168.1.1"
        user = "DESKTOP-R2UME43\Lenovo"
        password = "0930"
        database = "CareerHub"
        port = "1433"  # Default SQL Server port
        
        return host, user, password, database, port

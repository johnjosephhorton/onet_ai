import sqlite3
import os

# Set the folder path containing the SQL files
folder_path = 'sql'
# Set the database name
db_name = 'onet.db'

# Connect to the SQLite database
conn = sqlite3.connect(db_name)

# Loop through all files in the folder
for file in os.listdir(folder_path):
    print(file)
    # Check if the file is a SQL file
    if file.endswith('.sql'):
        # Build the file path
        file_path = os.path.join(folder_path, file)
        # Open the SQL file
        with open(file_path, 'r') as sql_file:
            # Read the SQL content
            sql_content = sql_file.read()
            # Execute the SQL commands
            conn.executescript(sql_content)

# Commit the changes and close the connection
conn.commit()
conn.close()

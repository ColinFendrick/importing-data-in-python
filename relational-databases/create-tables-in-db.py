from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///../_datasets/Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

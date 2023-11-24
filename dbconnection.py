import pyodbc

DRIVER = 'SQL Server'
SERVER = 'DESKTOP-MA7OUVV'
DATABASE = 'BDSpotPer'

connectionString = f'DRIVER={{{DRIVER}}};SERVER={SERVER};DATABASE={DATABASE}'
conn = pyodbc.connect(connectionString)
cursor = conn.cursor()

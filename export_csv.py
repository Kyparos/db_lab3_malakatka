# %%
import csv

import psycopg2

# %%

path = 'out_{}.csv'

username = 'sashamalakhatka'
password = '111'
database = 'sashamalakhatka'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(database=database
                        , user=username
                        , password=password
                        , host=host
                        , port=port)

data = {}
TABLES = ['athletes', 'noc', 'disipline']
# %%

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(path.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])


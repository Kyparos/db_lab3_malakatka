# %%
import csv
import psycopg2

# %%

path = 'out.csv'

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

# %%
with conn:
    cur = conn.cursor()

    for table in ('athletes', 'noc', 'disipline'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table] = rows
        with open('data.csv{}'.format(table), 'w') as out_file:
            wrt = csv.writer(out_file)
            wrt.writerow(fields)
            for row in cur:
                wrt.writerow([str(x) for x in row])


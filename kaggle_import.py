# %%
import csv
import psycopg2

# %%
path = 'vgsales.csv'

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

query_delete = '''
DELETE FROM noc  
'''

query = '''
INSERT INTO noc (noc_id, noc_name, g_medal, s_medal, b_medal) VALUES (%d, %s, %d, %d, %d)
'''


#%%
with conn:
    cur = conn.cursor()
    cur.execute(query_delete)
    with open(path, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['Year'] != 'N/A':
                values = (row['Name'], row['Platform'], row['Genre'], row['Year'])
                cur.execute(query, values)

    conn.commit()

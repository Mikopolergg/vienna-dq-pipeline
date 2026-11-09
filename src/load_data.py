import duckdb

CSV_PATH = "data/raw/baumkataster.csv"
DB_PATH = "data/trees.duckdb"

con = duckdb.connect(DB_PATH)
con.sql(f"""
    CREATE OR REPLACE TABLE trees_raw AS
    SELECT * FROM read_csv('{CSV_PATH}', all_varchar = true)
""")
con.sql("SELECT count(*) AS n_rows FROM trees_raw").show()
con.close()
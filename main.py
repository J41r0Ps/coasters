from fastapi import FastAPI
import database
from queries import themepark_queries as queries_themeparks
from queries import coaster_queries as queries_coaster
import config

app = FastAPI(docs_url=config.documentation_url)

@app.get("/createDatabase")
def insert_coasters_from_SQL_file():
    with open('sql_files/coasters.sql', "r", encoding="utf-8") as sql_file:
        sql_queries = sql_file.read()

    success = database.execute_sql_query(sql_queries)
    return {"success": success}

@app.get("/themeparks")
def get_all_themeparks():
    query = queries_themeparks.themeparks_name_query
    themeparks = database.execute_sql_query(query)
    if isinstance(themeparks, Exception):
        return themeparks, 500
    themeparks_to_return = []
    for themepark in themeparks:
        themeparks_to_return.append(themepark[0])
    return {"themeparks":themeparks_to_return}


from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import psycopg2
from psycopg2.extras import RealDictCursor
from config import host, port, db_name, user, password

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# while True:
#     try:
#         # Connect to an existing database
#         conn = psycopg2.connect(
#             host=host,
#             port=port,
#             dbname=db_name,
#             user=user,
#             password=password,
#             cursor_factory=RealDictCursor
#         )
#
#         # Open a cursor to perform database operations
#         cursor = conn.cursor()
#         cursor.execute("select version()")
#         print(f'version: {cursor.fetchone()}')
#         break
#
#     except Exception as error:
#         print('connecting to database unsucessful')
#         print('Error: ', error)
#         # time.sleep(2)


@app.get("/")
def hi():
    return FileResponse('templates/index.html')




# from flask import Flask, render_template
# import psycopg2
# from config import host, user, password, db_name
#
#
# app = Flask(__name__)
#
# pg = psycopg2.connect(
#      host=host,
#      user=user,
#      password=password,
#      database=db_name,
# )
#
# @app.route('/')
# def hello():
#      return render_template('index.html')
#
# if __name__ == "__main__":
#      app.run(host="127.0.0.1", debug=True)
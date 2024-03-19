# RandomQuotes_REST-API

This REST-API was designed for the project [Discord-REST_API-bot](https://github.com/AstronautMarkus/Discord-REST_API-bot), but if you like, you can use it!

# Description

A REST-API with random quotes REST API of random quotes based on a topic, the topics list are:

1. happy
2. inspirational
3. sad
4. love
5. money
6. knowledge

# How to Run Locally

1. Open `create_env.bat` if you're using Windows or `create_env.sh` for bash. The dependencies will install automatically.
2. Start the virtual environment by navigating to `Quotes_REST_API\venv\Scripts\Activate`, and with the environment open, run the `main.py` file.
3. Now, before using the API, you need to create the database table and insert the data. To do this, you need a database browser. I recommend using [DB Browser for SQLite](https://sqlitebrowser.org/). Then, create the table with `script_database.sql` and insert the data with `insert_data.sql`.
4. Write the changes to the database, and everything will be ready!


- If you don't want use an environment you can install the dependencies with the `Requirements.txt` file.

# URL list

you can use `/quote/{topic}` for use the api, ex: `/quote/sad`.

### For now, just that. I hope this API with inspiring phrases is useful to you! Hehe!

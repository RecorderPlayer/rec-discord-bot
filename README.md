# 🤖 RecorderPlayer Bot 

This is source code of RecorderPlayer Bot.


## ⚠️ Prerequisites
<a href="https://www.python.org/downloads/release/python-3100/">Python 3.10.0</a><br>
<a href="https://www.postgresql.org/download/">PostgreSQL 14.1</a><br>

## 🛠 Build
1. Create a venv environment `python -m venv ./venv` and activate it `source venv/bin/activate`
2. Create `.env` file in main direction and insert values from `.env.example`
  ```
  # DEBAG MODE of WebApp. If it's true, all exception will show you.
  DEBUG_MODE=
  TOKEN=
  
  # Values from postgres database
  DB_NAME=
  DB_USER=
  DB_USER_PASSWORD=
  DB_HOST=
  DP_PORT=
  ```
 3. Download all needest requirements from `requirements.txt` - `pip3 install -r requirements.txt`
 4. Start bot with command `python3 main.py`

## 📄 License
 Copyright ©2022 RecorderPlayer. Released under the **GNU GPLv3** license.

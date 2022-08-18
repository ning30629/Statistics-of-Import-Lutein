import csv
import sqlite3


def execute_db(filename, sql_cmd):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    c.execute(sql_cmd)
    conn.commit()
    conn.close()


def select_db(filename, sql_cmd):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    c.execute(sql_cmd)
    rows = c.fetchall()
    conn.close()
    return rows


def main():
    db_name = "import_lutein"
    print("建立資料庫及資料表")
    cmd = 'CREATE TABLE FDA_data (id INTEGER PRIMARY KEY AUTOINCREMENT, item_name TEXT,' \
          ' firm_name TEXT, firm_number TEXT, origin TEXT)'
    execute_db(db_name, cmd)
    print("插入csv檔")
    with open("lutein.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cmd = 'INSERT INTO FDA_data(item_name, firm_name, firm_number, origin) VALUES ("%s", "%s", "%s", "%s")' \
                  % (row['中文品名'], row['申請商名稱'], row['申請商電話'], row['產地'])
            execute_db(db_name, cmd)

    print("選擇資料")
    cmd = 'SELECT * FROM FDA_data WHERE origin = "日本"'
    for row in select_db(db_name, cmd):
        print(row)

main()
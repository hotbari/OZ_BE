import pymysql

def execute_query(connection, query, args=None) : # 개수 제한 x

    with connection.cursor() as cursor: #cursor = 대신
        cursor.execute(query, args or ())
        if query.strip().upper().startswith('SELECT'): # 공백 삭제, 대문자로 변경했을 때 SELECT로 시작하면
            return cursor.fetchall()
        else:
            connection.commit() # 업데이트, 딜리트는 커밋

def main():
    connection = pymysql.coonect(host='localhost',
                                 user='username',
                                 password='010913',
                                 db='database_name',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    try :
        # SELECT 연산
        result = execute_query(connection, "SELECT * FROM table_name")
        print("SELECT 연산 결과:")
        for row in result:
            print(row)


        # INSERT 연산
        execute_query(connection, "INSERT INTO table_name (column1, column2) VALUES (%s, %s)", ('data1','data2'))
        print("INSERT 연산 수행됨")

        # UPDATE 연산
        execute_query(connection, "UPDATE table_name SET column1=%s WHERE column2=%s", ('new_date','criteria') )
        print("UPDATE 연산 수행됨")

        # DELETE 연산
        execute_query(connection, "DELETE FROM table_name WHERE column_name=%s", ('criteria',))
        print("DELETE 연산 수행됨")

    finally :
        connection.close() 


if __name__ == "__main__":
    main()

    results = execute_query(connection, "SELECT * FROM table_name")

    for i in results:
        print(i)
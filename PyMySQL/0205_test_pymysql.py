import pymysql

# (1) db connection
connection = pymysql.connect (
    host = 'localhost',
    user='root',
    password = '010913',
    db = 'classicmodels',
    charset = 'utf8mb4', # 유니코드(이모지 포함)지원
    cursorclass = pymysql.cursors.DictCursor # 이게 없으면 튜플로 가져옴, 딕셔너리 형태로 키 값을 가져와야 추후 추출이 용이

    # 데이터가 많을 때 SSDictCursor, 적을 때 DictCursor(오버헤드 이슈) => ORM

)
    
# (2) CRUD

#R
## 1. SELCT * FROM
def customers():
    cursor = connection.cursor()

    sql = "SELECT * FROM customers"
    cursor.execute(sql) # 쿼리 실행
    customers = cursor.fetchone() # 하나의 데이터
    # customers = cursor.fetchall() # 전체 데이터
    print('customers : ', customers['country'])
    cursor.close()

# 2. INSERT INTO
def add_customer():
    cursor = connection.cursor()

    customer_name = 'bari'
    customer_last_name = 'hot'
    sql = f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES ({10913},'{customer_name}','{customer_last_name}')" #여기 10913을 중괄호에 넣고 안넣고 상관없나요?
    cursor.execute(sql)
    connection.commit() # 실제 DB에 반영하는 코드
    cursor.close()


# add_customer()

# 3. UPDATE INTO
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_bari'
    update_late_name = 'update_hot'
    sql = f"UPDATE customers SET customerName='{update_name}', contactLastName='{update_late_name}' WHERE customerNumber = 10913"
    cursor.execute(sql)
    connection.commit()
    cursor.close() # 데이터 손실 방지

# update_customer()
    

# 4. DELETE FROM
    
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 10913"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()
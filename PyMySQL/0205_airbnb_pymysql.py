import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='oz-password',
    db='AIRBNB2',
)

try :
    with conn.cursor() as cursor:
        # 새로운 제품 추가
        # sql문 작성
        sql = "INSERT INTO Products (productName, price, stockQuantity) VALUES (%s, %s, %s)"
        #execute로 실행(sql문과 %s에 들어갈 값)
        cursor.execute(sql, ('Python Book',29.99, 50))
        conn.commit()

        # 고객 목록 조회
        sql = "SELECT * FROM Customers"
        # fetchall()로 전체 조회해서 for문으로 하나씩 불러옴
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

        # 제품 재고 업데이트
        sql = "UPDATE Products SET stockQuantity = stockQuntity - %s WHERE productID = %s "
        cursor.execute(sql, (quantity_sold, product_id))
        conn.commit()

        # 고객별 총 주문 금액 계산
        sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
        cursor.execute(sql)
        for row in cursor.fetchall():
            print(row)

        # 고객 이메일 업데이트
        sql = "UPDATE Customers SET email = %s WHERE customerID = %s"
        cursor.execute(sql, (new_email, customer_id))
        conn.commit()

        # 주문 취소
        sql = "DELETE FROM Orders WHERE orderID = %s"
        cursor.execute(sql, (order_id,))
        conn.commit()

        # 특정 제품 검색
        sql = "SELECT * FROM Products WHERE productName LIKE %s"
        cursor.execute(sql, ('%Book%')) #Book이 들어가는 단어를 전부 찾아준다
        for row in cursor.fetchall():
            print(row)

        # 특정 고객의 모든 주문 조회
        sql = "SELECT * FROM Order WHERE customerID = %s"
        cursor.execute(sql, (1,))
        for now in cursor.fetchall():
            print(row)

        # 가장 많이 주문한 고객 찾기
        sql = """
            SELECT customerID, COUNT(*) as orderCount
            FROM Orders
            GROUP BY customerID
            ORDER BY orderCount DESC
            LIMIT 1    
            """
        
        cursor.execute(sql)
        top_customer = cursor.fetchone()
        print(f"Top Customer ID: {top_customer[0], Orders: {top_customer[1]}}")


finally :
    conn.close()
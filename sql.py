import pymysql

# 创建数据库连接
conn = pymysql.connect(
    host='47.115.205.240',  # 数据库服务器地址
    user='abc',  # 数据库用户名
    password='369852',  # 数据库密码
    database='huamingce',  # 要连接的数据库名
)

def insert(data):
    name = data['name']
    pic = data['pic']
    reason = data['reason']

    try:
        with conn.cursor() as cursor:
            # 创建一个新记录
            sql = "INSERT INTO huaming (name, pic, reason) VALUES (%s, %s, %s)"
            cursor.execute(sql, (name, pic, reason))

        # 提交更改
        conn.commit()
        print("Insertion successful!")

    except Exception as e:
        # 如果发生错误则回滚
        conn.rollback()
        print(f"Error: {e}")

    finally:
        # 关闭连接
        conn.close()

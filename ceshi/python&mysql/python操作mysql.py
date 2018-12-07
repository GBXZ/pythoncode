# 导入pymyslq光标
import pymysql.cursors

# 进行连接，创建连接实例
connect = pymysql.connect(host='localhost', user='root', password='',
                          database='shop')
# # 查找数据
# try:
#     # 创建一个光标
#     with connect.cursor() as cursor:
#         # 原生数据库数据
#         sql = 'select * from user'
#         # 光标执行数据库语句
#         cursor.execute(sql)
#         # 查询所有记录
#         result = cursor.fetchall()
#         # 进行遍历
#         for row in result:
#             print(row[0], row[1], row[2])
#     # 进行提交
#     connect.commit()
# finally:
#     # 关闭连接
#     connect.close()


# 插入数据
# try:
#     with connect.cursor() as insert_cursor:
#         sql = 'insert into mark (id, mark, stu_id) values(5, 70, 1)'
#         insert_cursor.execute(sql)
#     connect.commit()
# except Exception as e:
#     # 错误回滚
#     connect.rollback()
# finally:
#     connect.close()

# 更新操作
# try:
#     with connect.cursor() as update_cursor:
#         sql = 'update  mark set mark=50 where id=5'
#         update_cursor.execute(sql)
#     connect.commit()
# finally:
#     connect.close()


# s删除操作

try:
    with connect.cursor() as update_cursor:
        sql = 'delete from mark where id=5 '
        update_cursor.execute(sql)
    connect.commit()
finally:
    connect.close()

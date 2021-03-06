import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database=db_name
    )
    return cnx


def get_all_records():
    try:
        db_name = 'Eventsapp'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """SELECT * FROM Likes"""
        cur.execute(query)
        all_records = cur.fetchall()

        for item in all_records:
            print(item)
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def insert_new_record(record):
    try:
        db_name = 'EventsApp'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """INSERT INTO Likes ({}) VALUES ({}, {}, {}) """.format(
            ', '.join(record.keys()),
            record['id'],
            record['likes'],
            record['dislikes'],

        )

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def update_dislikes(record):
    try:
        db_name = 'EventsApp'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        newDislikes = record['dislikes'] + 1
        query = """UPDATE Likes SET dislikes = {} WHERE id = '{}'""".format(newDislikes, record['id'])

        cur.execute(query)
        db_connection.commit()
        cur.close()


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def update_likes(record):
    try:
        db_name = 'EventsApp'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        newLikes = record['likes'] + 1
        query = """UPDATE Likes SET likes = {} WHERE id = '{}'""".format(newLikes, record['id'])

        cur.execute(query)
        db_connection.commit()
        cur.close()


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def delete_record(record):
    try:
        db_name = 'EventsApp'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """DELETE from Likes WHERE id = {}""".format(record['id'])
        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def main():
    # insert_new_record(record)
    # delete_record(record)
    # update_dislikes(record)
    # update_likes(record)
    # get_all_records()


if __name__ == '__main__':
    main()

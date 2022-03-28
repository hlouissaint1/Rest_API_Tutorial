__author__ = "Himmler Louissaint"

import sqlite3

class Database:
    _NAME = r'C:\Users\hlouissaint\OneDrive - Secureworks Inc\LinuxSharedFolder\Sandbox\ATF\Web_Development\Web_Tutorial_SQLAchemy\data.db'

    @classmethod
    def get_name(cls):
        return cls._NAME

    @classmethod
    def _connect_to_db(cls):
        connection = None
        try:
            connection = sqlite3.connect(Database.get_name())
        except ConnectionError as e:
            print(e)
            raise Exception(f'Failure connecting to database {Database.get_name()}')
#        finally:
#            if connection:
#                connection.close()
        return connection

    @classmethod
    def executeDataQuery(cls, query, params=()):
        results = {}
        conn = Database._connect_to_db()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            conn.commit()
            results['status'] = 'success'
        except conn.Error as e:
                results['status'] = 'failure'
                results['results'] = e.args[0]
                conn.rollback()
        finally:
            if conn:
                conn.close()
        return results


    @classmethod
    def retrieveDataQuery(cls, query, params = ()):
        results = {}
        conn = cls._connect_to_db()
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            rows = cursor.fetchall()
            results['status'] = 'success'
            result = []
            if rows:
                column = list(map(lambda x: x[0], cursor.description))
                for row in rows:
                    result.append(dict(zip(column, row)))
            results['results'] = result
        except conn.Error as e:
            results['status'] = 'failure'
            results['results'] = e.args[0]
        finally:
            if conn:
                conn.close()
        return results

if "__main__" == __name__:
    # query = "SELECT * FROM items WHERE name=?"
    # name = ('piano',)
    # resp = Database.retrieveDataQuery(query, name)
    # print(resp)
    query = "SELECT * FROM items"
    resp = Database.retrieveDataQuery(query)
    print(resp)

    query = "SELECT * FROM users "
    resp = Database.retrieveDataQuery(query)
    print(resp)
    query = "SELECT * FROM stores"
    resp = Database.retrieveDataQuery(query)
    print(resp)
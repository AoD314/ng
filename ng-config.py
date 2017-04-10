import argparse
import sqlite3

from os import path

PATH_TO_DB = 'ng-config.db'


def find_library(name):
    with open('findlibs.conf', 'r') as f:
        lines = f.readlines()

    # include -> /usr/include
    # libraries -> /usr/lib

    lst = []
    for line in lines:
        r = line.split(':')
        lst.append({
            'name': r[0],
            'ver': r[1],
            'inc': r[2],
            'libs': r[3]
        })

    print(lst)


class Config:
    def __create_db(self):
        conn = sqlite3.connect(PATH_TO_DB)
        cur = conn.cursor()

        cur.execute('CREATE TABLE conf (name text, ver text, inc text, lib text);')

        conn.commit()
        conn.close()

    def __init__(self):
        if not path.exists(PATH_TO_DB):
            self.__create_db()

        self.conn = sqlite3.connect(PATH_TO_DB)
        self.c = self.conn.cursor()

        pass

    def list(self):
        self.c.execute('SELECT name, ver from conf;')
        lst = self.c.fetchall()
        return lst


def main():
    parser = argparse.ArgumentParser(description='Ninja Generator Config')
    parser.add_argument('cmd', choices=['list', 'add', 'del', 'find'], help='command')

    args = parser.parse_args()

    conf = Config()

    if args.cmd == 'list':
        print(conf.list())

    if args.cmd == 'find':
        print(find_library('opencv'))


if __name__ == '__main__':
    main()


import sqlite3

class Unit:
    def __init__(self, unit_id, unit_name):
        self.unit_id = unit_id
        self.name = unit_name

class UnitModel:
    def __init__(self):
        self.conn = sqlite3.connect('my-macro.sqlite3')
        self.cursor = self.conn.cursor()

    def get_units(self):
        units = []
        for row in self.cursor.execute('SELECT * FROM Units'):
            units.append(Unit(row[0], row[1]))
        return units

    def get_unit(self, unit_id):
        for row in self.cursor.execute('SELECT * FROM Units WHERE unit_id = ?', (unit_id,)):
            return Unit(row[0], row[1])

    def get_unit_by_name(self, unit_name):
        for row in self.cursor.execute('SELECT * FROM Units WHERE name = ?', (unit_name,)):
            return Unit(row[0], row[1])

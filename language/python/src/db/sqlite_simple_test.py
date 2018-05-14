# coding:utf8
"""
Sqlite3 简单测试
"""
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
from sqlalchemy import create_engine
engine = create_engine('sqlite:///orm_in_detail.sqlite')

from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return 'Department: {}'.format(self.id)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    department = relationship(
        Department,
        backref=backref('employees', uselist=True, cascade='delete,all'))

    def __repr__(self):
        return 'Employee: {}'.format(self.id)


if __name__ == '__main__':
    # Create tabe
    Base.metadata.create_all(engine)
    # Add record
    d = Department(name="IT")
    emp1 = Employee(name="John", department=d)
    s = session()
    s.add(d)
    s.add(emp1)
    s.commit()
    print s.query(Employee).all()

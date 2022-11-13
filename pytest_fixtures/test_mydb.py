# We are writing two unit tests
    # 1. Verify Jhon's employee id
    # 2. Verify Tom's employee id

from mydb import MyDB

# def test_jhons_id():
#     db=MyDB()
#     conn=db.connect("server")
#     cur=conn.cursor()
#     id=cur.execute("select id from employee_db where name=Jhon")
#     assert id==123

# def test_toms_id():
#     db=MyDB()
#     conn=db.connect("server")
#     cur=conn.cursor()
#     id=cur.execute("select id from employee_db where name=Tom")
#     assert id==789

# Problems with the above approach
    # 1. code repetition
    # 2. creating expensive DB connection in every test case
    # 3. we have connect again and again
    # 4. connection is costly

# Two ways to fix those issues:
# 1. setup and teardown methods(classic xunit style) > it will initialize whatever we need for the test caese in the beginning
# conn=None
# cur =None

# def setup_module(module):
#     global conn
#     global cur
#     db=MyDB()
#     conn=db.connect("server")
#     cur = conn.cursor()

# def teardown_module(module):
#     cur.close()
#     conn.close()

# def test_jhons_id():
#     id=cur.execute("select id from employee_db where name=Jhon")
#     assert id==123

# def test_toms_id():
#     id=cur.execute("select id from employee_db where name=Tom")
#     assert id==789

# 2. fixtures (recommended) > 
import pytest

# @pytest.fixture() # creating DB again and again
@pytest.fixture(scope="module") # to restrict the "repeatation" at a module level
def cur():
    print("setting up") # 'pytest -v --capture=no' to see, no means don't accept the output but show it on stdout
    db=MyDB()
    conn=db.connect("server")
    curs = conn.cursor()

    # teardown
    # return curs
    yield curs
    curs.close()
    conn.close()
    print("closing database")

def test_jhons_id(cur):
    id=cur.execute("select id from employee_db where name=Jhon")
    assert id==123

def test_toms_id(cur):
    id=cur.execute("select id from employee_db where name=Tom")
    assert id==789

# fixtures levarage a concept of dependency injection

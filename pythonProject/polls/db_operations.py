import sqlite3 as sql
import random
import json

questions = [
    ["What is the maximum possible length of an identifier?", "['16','32','64','None of these above']",
     "None of these above"],
    ["Who developed the Python language?", "['Zim Den','Guido van Rossum','Niene Stom','Wick van Rossum']",
     "Guido van Rossum"],
    ["In which language is Python written?", "['English','PHP','C','All of the above']", "C"],
    ["What do we use to define a block of code in Python language?", "['Key','Brackets','Indentation','None of these']",
     "Indentation"],
    ["What is the method inside the class in python language?", "['Object','Function','Attribute','Argument']",
     "Function"],
    ["Which of the following is not a keyword in Python language?", "['val','raise','try','with']", "val"],
    ["Which of the following words cannot be a variable in python language?", "['_val','val','try','_try_']", "try"],
    ["Which of the following operators is the correct option for power(ab)?", "['a ^ b','a**b','a ^ ^ b','a ^ * b']",
     " a**b"],
    [" Which one of the following has the highest precedence in the expression?",
     "['Division','Subtraction','Power','Parentheses']", "Parentheses"],
    ["What will be the output of this function?\\n all([2,4,0,6])", "['False','True','0','Invalid code']", "False"],
    ["What will be the output of this code?\\n any([5>8, 6>3, 3>1])", "['False','True','Invalid code','None of these']",
     "True"],
    ["What will be the output of this code?\\n 'javatpoint'[5:]", "['javatpoint','java','point','None of these']",
     "point"],
    ["Which of the following option is not a core data type in the python language?",
     "['Dictionary','Lists','Class','All of the above']", "Class"],
    ["What happens when '2' == 2 is executed?", "['False','True','ValueError occurs','TypeError occurs']", "False"],
    ["What will be the output of this program?\\n print(6 + 5 - 4 * 3 / 2 % 1)", "['7','7.0','15','11.0']", "11.0"],
    ["How many control statements python supports?", "['Four','Five','Three','None of the these']", "Three"],
    ["What will be the output of this program?\\n\\n a = '123789'\\n while x in a:\\n\t print(x, end=' ')",
     "['i i i i i i …','123789','SyntaxError','NameError']", "NameError"],
    ["PVM is often called _________.",
     "['Python interpreter','Python compiler','Python volatile machine','Portable virtual machine']",
     "Python interpreter"],
    ["Which of the following keywords is used for function declaration in Python language?",
     "['def','function_name','define','None of these']", "def"],
    [
        "When a user does not use the return statement inside a function in Python, what will return the function in that case.?",
        "['0','1','None','No Output']", "None"]
]


class DbOperations:

    def __init__(self) -> None:
        self.conn = sql.connect("test.db")

    # def get_connection(self):
    # 	conn = sql.connect("test.db")
    # 	return conn

    def user_exist_check(self, username=''):
        # conn = self.get_connection()
        cursor = self.conn.execute(f"select * from users where username = '{username}'")
        users = cursor.fetchall()
        return users

    def create_table_user(self):
        # conn = self.get_connection()
        self.conn.execute("CREATE TABLE USERS (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
        USERNAME VARCHAR(45) UNIQUE NOT NULL, PASSWORD VARCHAR(50) NOT NULL)")

    def get_table(self, table_name):
        # conn = self.get_connection()
        cursor = self.conn.execute(f"select * from {table_name}")
        print(cursor.fetchall())

    def validate_user(self, username="", password=""):
        cursor = self.conn.execute(
            f"select * from USERS as U where U.username='{username}' and U.password='{password}'")
        user = cursor.fetchall()
        return user

    def create_user(self, username="", password=""):
        self.conn.execute(f"insert into USERS(`username`,`password`) values('{username}', '{password}')")
        self.conn.commit()
        return True

    def create_question(self):
        self.conn.execute("CREATE TABLE questionData (id INTEGER PRIMARY KEY AUTOINCREMENT, question LONGTEXT NOT NULL, \
        options LONGTEXT NOT NULL, correct_ans LONGTEXT NOT NULL)")
        for question in questions:
            ques = question[0]
            options = question[1]
            correct_ans = question[2]
            self.conn.execute(
                f"""insert into questionData(`question`,`options`,`correct_ans`) values("{ques}","{options}","{correct_ans}")""")
            self.conn.commit()

    def view_all(self, username=""):
        cursor = self.conn.execute(f"select * from users")
        print(cursor.fetchall())

    def get_questions(self):
        cursor = self.conn.execute("select * from questionData")
        all_questions = cursor.fetchall()
        q_to_ask = random.sample(range(20), 5)
        return all_questions, q_to_ask

    def store_result(self, score, username):
        user = self.user_exist_check(username)
        past_scores = self.get_all_scores(username=username)
        if past_scores:
            _ = json.loads(past_scores)
            _.append(score)
            self.conn.execute(f"update test_data set all_tests = '{json.dumps(_)}' where username = '{username}'")
            self.conn.commit()
        else:
            self.conn.execute(f"insert into test_data(`username`,`all_tests`) values('{username}', '{json.dumps([score])}')")
            self.conn.commit()

    def get_all_scores(self, username):
        # self.conn.execute(f"Delete from test_data where username='{username}'")
        # self.conn.commit()
        scores = self.conn.execute(f"Select all_tests from test_data where username = '{username}'").fetchone()
        return scores[0] if scores else []

    def create_test_data(self):
        self.conn.execute("CREATE TABLE test_data (id INTEGER PRIMARY KEY AUTOINCREMENT, username LONGTEXT NOT NULL,\
        all_tests LONGTEXT NOT NULL)")


# DbOperations().create_table_user()
# DbOperations().get_questions()
# DbOperations().create_question()
# DbOperations().create_test_data()
print("GET", DbOperations().get_all_scores('harshPanchal'))
print("DB OPERATIONS ", DbOperations().get_questions())

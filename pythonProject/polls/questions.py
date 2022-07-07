import sqlite3 as s
import random

conn = s.connect("test.db")

# conn.execute("CREATE TABLE questionData (id INTEGER PRIMARY KEY AUTOINCREMENT, question LONGTEXT NOT NULL, options LONGTEXT NOT NULL, correct_ans LONGTEXT NOT NULL)")

questions = [
	["What is the maximum possible length of an identifier?", "['16','32','64','None of these above']", "None of these above"],
	["Who developed the Python language?", "['Zim Den','Guido van Rossum','Niene Stom','Wick van Rossum']", "Guido van Rossum"],
	["In which language is Python written?", "['English','PHP','C','All of the above']", "C"],
	["What do we use to define a block of code in Python language?", "['Key','Brackets','Indentation','None of these']", "Indentation"],
	["What is the method inside the class in python language?", "['Object','Function','Attribute','Argument']", "Function"],
	["Which of the following is not a keyword in Python language?", "['val','raise','try','with']", "val"],
	["Which of the following words cannot be a variable in python language?", "['_val','val','try','_try_']", "try"],
	["Which of the following operators is the correct option for power(ab)?", "['a ^ b','a**b','a ^ ^ b','a ^ * b']", " a**b"],
	[" Which one of the following has the highest precedence in the expression?", "['Division','Subtraction','Power','Parentheses']", "Parentheses"],
	["What will be the output of this function?\\n all([2,4,0,6])", "['False','True','0','Invalid code']", "False"],
	["What will be the output of this code?\\n any([5>8, 6>3, 3>1])", "['False','True','Invalid code','None of these']", "True"],
	["What will be the output of this code?\\n 'javatpoint'[5:]", "['javatpoint','java','point','None of these']", "point"],
	["Which of the following option is not a core data type in the python language?", "['Dictionary','Lists','Class','All of the above']", "Class"],
	["What happens when '2' == 2 is executed?", "['False','True','ValueError occurs','TypeError occurs']", "False"],
	["What will be the output of this program?\\n print(6 + 5 - 4 * 3 / 2 % 1)", "['7','7.0','15','11.0']", "11.0"],
	["How many control statements python supports?", "['Four','Five','Three','None of the these']", "Three"],
	["What will be the output of this program?\\n\\n a = '123789'\\n while x in a:\\n\t print(x, end=' ')", "['i i i i i i …','123789','SyntaxError','NameError']", "NameError"],
	["PVM is often called _________.", "['Python interpreter','Python compiler','Python volatile machine','Portable virtual machine']", "Python interpreter"],
	["Which of the following keywords is used for function declaration in Python language?", "['def','function_name','define','None of these']", "def"],
	["When a user does not use the return statement inside a function in Python, what will return the function in that case.?", "['0','1','None','No Output']", "None"]
]

for question in questions:
   ques = question[0]
   options = question[1]
   correct_ans = question[2]
   conn.execute(f"""insert into questionData(`question`,`options`,`correct_ans`) values("{ques}","{options}","{correct_ans}")""")
   conn.commit()
    

print(conn.execute(f"select * from questionData").fetchall())

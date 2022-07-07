# Create your views here.
import json

from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect

from .db_operations import DbOperations
from .models import Question


username = ''


def index(request):
    context = {'authorized': True, 'message': 'Welcome back..!'}
    return render(request, 'polls/index.html', context)


# login method
def login(request):
    if request.method == 'POST':
        form = request.POST
        global username
        username = form.get('username')
        password = form.get('password')
        user_list = DbOperations().user_exist_check(username=username)
        print(f"USER : {user_list}")
        if user_list:
            is_valid = DbOperations().validate_user(username=username, password=password)
            if is_valid:
                return quiz_redirect(request)
            else:
                context = {'authorized': False, 'message': 'Please enter correct username or password'}
                return render(request, "polls/index.html", context)
        else:
            context = {'authorized': False, 'message': 'User does not exists'}
            return render(request, "polls/index.html", context)


# Register method
def register(request):
    form = request.POST
    global username
    username = form.get('userName')
    password = form.get('password')
    user_list = DbOperations().user_exist_check(username=username)
    if user_list:
        context = {'authorized': False, 'message': 'User Already Exist ..!'}
        return render(request, "polls/index.html", context)

    DbOperations().create_user(username=username, password=password)
    context = {'authorized': True, 'message': 'User successfully signed up.. Please login..!'}
    return render(request, "polls/index.html", context)


questions = []
indexes = []
array = []
correct_counter = 1


# Take quiz
def take_test(request):
    global indexes
    global questions
    global array
    global correct_counter
    global username
    form = request.POST
    count = form.get('count')
    radio = form.get('radio')
    answer = form.get('answer')
    username = form.get('username')

    if int(count) == 0:
        questions, indexes = DbOperations().get_questions()
        print("index ", indexes)
        correct_counter = 1
        array = []
        for i in indexes:
            object_que = {'questionNo': questions[i][0], 'question': questions[i][1], 'options': eval(questions[i][2]),
                          'answer': questions[i][3]}
            array.append(object_que)
    print("count",count)
    display_quiz = True
    current_question = ''
    message = ''
    if int(count) < 5:
        current_question = array[int(count)]
        # check answer
        if int(count) != 0:
            print("VALUE :", radio, answer)
            if radio == answer:
                correct_counter += 1
        count = int(count) + 1
    else:
        display_quiz = False
        if correct_counter < 3:
            message = "Please Try Again...."
        elif correct_counter == 3:
            message = "Good Job!"
        elif correct_counter == 4:
            message = "Excellent Work!"
        elif correct_counter == 5:
            message = "You are a genius!"
        DbOperations().store_result(correct_counter, username)

    context = {
        'displayQuiz': display_quiz,
        'question': current_question,
        'username': username,
        'count': count,
        'correct_answer': correct_counter,
        'message': message
    }
    return render(request, "polls/quizQuestion.html", context)


# User Menu select
def user_menu(request):
    form = request.POST
    radio = form.get('radio')
    take_test_flag = False
    view_all_scores = False
    view_average = False
    show_menu = False
    test_data = []
    if radio == '0':
        take_test_flag = True
        view_all_scores = False
        view_average = False
    elif radio == '1':
        take_test_flag = False
        view_all_scores = True
        view_average = False
        results = DbOperations().get_all_scores(username)
        data = []
        if len(results) > 0:
            scores = json.loads(results)
            if scores:
                for _ in scores:
                    data.append(_)
        test_data = data
    elif radio == '2':
        take_test_flag = False
        view_all_scores = False
        view_average = True
        results = DbOperations().get_all_scores(username)
        if len(results) > 0:
            scores = json.loads(results)
            if scores:
                test_data = {
                    'min': min(scores),
                    'max': max(scores),
                    'avg': sum(scores)/len(scores)
                }
    context = {
        'take_test': take_test_flag,
        'view_all_scores': view_all_scores,
        'view_average': view_average,
        'show_menu': show_menu,
        'question': [],
        'username': username,
        'count': 0,
        'correct_answer': 0,
        'message': '',
        'test_data': test_data,
    }
    return render(request, "polls/quiz.html", context)


# quiz page redirect
def quiz_redirect(request):
    print("sier name",username)
    context = {
        'take_test': False,
        'view_average': False,
        'view_all_scores': False,
        'show_menu': True,
        'question': [],
        'username': username,
        'count': 0,
        'correct_answer': 0,
        'message': ''
    }
    return render(request, "polls/quiz.html", context)


# login page redirect
def login_redirect(request):
    context = {'authorized': True, 'message': 'Hello User..!'}
    return render(request, "polls/index.html", context)


# register page redirect
def register_redirect(request):
    context = {'authorized': True, 'message': 'Hello User..!'}
    return render(request, "polls/register.html", context)


# logout redirect
def logout_redirect(request):
    context = {'authorized': False, 'message': 'Logged out successfully..!'}
    return render(request, "polls/index.html", context)

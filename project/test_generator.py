import HTML
import os
import re 
import subprocess
from xhtml2pdf import pisa

def question_1(x):
    q = open(str(x)+"_test.txt","a")
    q.write('1.\n')
    q.write('x^2+2x-3=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('1.\n')
    q.write('x^2+2x-3=0\n')
    q.write('Answer: x1=1; x2=-3;\n\n')

def question_2(x):
    q = open(str(x)+"_test.txt","a")
    q.write('2.\n')
    q.write('2x^2+x+5=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('2.\n')
    q.write('2x^2+x+5=0\n')
    q.write('Answer: NRK\n\n')

def question_3(x):
    q = open(str(x)+"_test.txt","a")
    q.write('3.\n')
    q.write('2x^2+5x-10=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('3.\n')
    q.write('2x^2+5x-10=0\n')
    q.write('Answer: x1=5; x2=-2;\n\n')

def question_4(x):
    q = open(str(x)+"_test.txt","a")
    q.write('4.\n')
    q.write('3x^2-2x-4=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('4.\n')
    q.write('3x^2-2x-4=0\n')
    q.write('Answer: x1=1/2; x2=-1/4;\n\n')

def question_5(x):
    q = open(str(x)+"_test.txt","a")
    q.write('5.\n')
    q.write('x^2+6x+2=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('5.\n')
    q.write('x^2+6x+2=0\n')
    q.write('Answer: x1=4; x2=8;\n\n')

def question_6(x):
    q = open(str(x)+"_test.txt","a")
    q.write('6.\n')
    q.write('x^3+2x^2+4x+10=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('6.\n')
    q.write('x^3+2x^2+4x+10=0\n')
    q.write('Answer: x1=21; x2=1/5; x3=32;\n\n')

def question_7(x):
    q = open(str(x)+"_test.txt","a")
    q.write('7.\n')
    q.write('2x^3+x^2+5x+2=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('7.\n')
    q.write('2x^3+x^2+5x+2=0\n')
    q.write('Answer: NRK\n\n')

def question_8(x):
    q = open(str(x)+"_test.txt","a")
    q.write('8.\n')
    q.write('8x^3-3x^2+6x-12=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('8.\n')
    q.write('8x^3-3x^2+6x-12=0\n')
    q.write('Answer: x1=15;\n\n')

def question_9(x):
    q = open(str(x)+"_test.txt","a")
    q.write('9.\n')
    q.write('2x^3+x^2-9x+18=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('9.\n')
    q.write('2x^3+x^2-9x+18=0\n')
    q.write('Answer: NRK\n\n')

def question_10(x):
    q = open(str(x)+"_test.txt","a")
    q.write('10.\n')
    q.write('5x^3+3x^2+3x+7=0\n\n')

    q = open(str(x)+"_test_answers.txt","a")
    q.write('10.\n')
    q.write('5x^3+3x^2+3x+7=0\n')
    q.write('Answer: x1=1/4; x2=2/7; x3=3;\n\n')

print 'Write the number of tests you want:'
n = raw_input()
n = int(n)

for x in xrange(1,n+1):
    question_1(x)
    question_2(x)
    question_3(x)
    question_4(x)
    question_5(x)
    question_6(x)
    question_7(x)
    question_8(x)
    question_9(x)
    question_10(x)

for x in xrange(1,n+1):
    with open(str(x)+"_test.txt", "r") as task:
        task = task.read()
        task = task.split('\n\n')
        task = [w.replace('\n', '<br />') for w in task]

    table_data = [
        [task[0], task[1]],
        [task[2], task[3]],
        [task[4], task[5]],
        [task[6], task[7]],
        [task[8], task[9]],
    ]

    f = open(str(x)+"_test.html","w")
    htmlcode = HTML.table(table_data)
    f.write("<center><h1>Quad and Cubic equations test</br> {v}</h1></center></br>".format(v=id))
    f.write(htmlcode)

for x in xrange(1,n+1):
    with open(str(x)+"_test_answers.txt", "r") as task:
        task = task.read()
        task = task.split('\n\n')
        task = [w.replace('\n', '<br />') for w in task]

    table_data = [
        [task[0], task[1]],
        [task[2], task[3]],
        [task[4], task[5]],
        [task[6], task[7]],
        [task[8], task[9]],
    ]
    f = open(str(x)+"_test_answers.html","w")
    htmlcode = HTML.table(table_data)
    f.write("<center><h1>Quad and Cubic equations test</br> {v}</h1></center></br>".format(v=id))
    f.write(htmlcode)

for x in xrange(1,n+1):
    p = subprocess.Popen("pisa "+str(x)+"_test_answers.html", shell=True, stdout=subprocess.PIPE)
    p.wait()
    p = subprocess.Popen("pisa "+str(x)+"_test.html", shell=True, stdout=subprocess.PIPE)
    p.wait()
    os.remove(str(x)+"_test.txt")
    os.remove(str(x)+"_test_answers.txt")

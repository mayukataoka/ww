

## Question 1 

### Script
https://github.com/mayukataoka/ww/blob/master/question_one.py (Python)

### Output

```
(venv) MAYUs-MacBook-Pro:ww mayukataoka$ python question_one.py 
An input file ./dict exists.

Apple
a fruit
a tech firm

Table
an object
contains rows and columns when used in context of computers

Orange
a fruit

```

## Question 2 
### Script
https://github.com/mayukataoka/ww/blob/master/question_two_test.py (Python + Pytest)
https://github.com/mayukataoka/ww/blob/master/pages/StudioSchedulePage.py
https://github.com/mayukataoka/ww/blob/master/pages/Locators.py
https://github.com/mayukataoka/ww/blob/master/pages/HeaderPage.py
https://github.com/mayukataoka/ww/blob/master/pages/FindAMeetingPage.py

```
    schedule.get_schedule_summary('Mon')
    schedule.get_schedule_summary('Tue')
    schedule.get_schedule_summary('Wed')
```

### Output

```
Testing started at 10:56 ...
/Users/mayukataoka/PycharmProjects/ww/venv/bin/python "/Applications/PyCharm CE.app/Contents/helpers/pycharm/_jb_pytest_runner.py" --path /Users/mayukataoka/PycharmProjects/ww/question_two_test.py
Launching pytest with arguments /Users/mayukataoka/PycharmProjects/ww/question_two_test.py in /Users/mayukataoka/PycharmProjects/ww

============================= test session starts ==============================
platform darwin -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0
rootdir: /Users/mayukataoka/PycharmProjects/ww, inifile:collected 1 item

question_two_test.py .WW Studio Flatiron

0.49 mi.

On mon
Name:DANA F.  Total: 1 times
Name:LISA S.  Total: 2 times
On tue
Name:LAUREN C.  Total: 2 times
Name:ARANSAS S.  Total: 2 times
On wed
Name:RICARDO M.  Total: 1 times
Name:DANA F.  Total: 1 times
Name:KENDRA V.  Total: 2 times
                                                   [100%]

========================== 1 passed in 12.99 seconds ===========================
Process finished with exit code 0

```

![Alt text](schedule_table.png?raw=true)

## Question 3
### Script
https://github.com/mayukataoka/ww/blob/master/question_three.py (python)


### Output

```
(venv) MAYUs-MacBook-Pro:ww mayukataoka$ python question_three.py 499
999
(venv) MAYUs-MacBook-Pro:ww mayukataoka$ python question_three.py 0
4
(venv) MAYUs-MacBook-Pro:ww mayukataoka$ python question_three.py 100
222

(venv) MAYUs-MacBook-Pro:ww mayukataoka$ python question_three.py 499
999
(venv) MAYUs-MacBook-Pro:ww mayukataoka$ python question_three.py 0
1
(venv) MAYUs-MacBook-Pro:ww mayukataoka$ python question_three.py 100
210

```


Please let me know if you have any questions. 
Thank you,
Mayu

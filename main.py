import re

segment = ('_' * 31)


def add_affair_to_list(affair, status):
    with open('info.txt', 'a') as f:
        f.write(f'{status} <{affair}> \n')


def show_all_tasks(num=0):
    with open('info.txt', 'r') as f:
        print(segment)
        file = f.readlines()
        for line in file:
            num += 1
            affair = re.findall(r"<.*?>", line)
            print(f'{num}.{affair[0]}')
        print(segment)


def show_done_tasks():
    with open('info.txt', 'r') as f:
        file = f.readlines()
        print(segment)
        for line in file:
            if line.startswith('done'):
                print(line.strip())
        print(segment)


def show_not_done_tasks():
    with open('info.txt', 'r') as f:
        file = f.readlines()
        print(segment)
        for line in file:
            if line.startswith('not done'):
                print(line.strip())
        print(segment)


def clear_all_affairs():
    with open('info.txt', 'w') as f:
        f.write('')


clear_all_affairs()

status1 = 'done'
status2 = 'not done'
task1 = 'read book'
task2 = 'clear room'
add_affair_to_list(task1, status1)
add_affair_to_list(task2, status2)
show_all_tasks()
show_done_tasks()
show_not_done_tasks()

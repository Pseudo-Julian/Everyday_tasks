import re


class EverydayTasks:

    def __init__(self, segment=('_' * 31)):
        self.__segment = segment
        self.old_list = []

    @classmethod
    def task_search(cls, file, status):
        for line in file:
            if line.startswith(status):
                print(line.strip())

    @staticmethod
    def task_add(task, status) -> None:
        with open('info.txt', 'a') as f:
            f.write(f'{status} <{task}>\n')

    def show_all_tasks(self, num=0):
        with open('info.txt', 'r') as f:
            new_old_list = []
            file = f.readlines()
            print(self.__segment)
            for line in file:
                num += 1
                task = re.findall(r'<.*?>', line)
                new_old_list.append(task[0])
                print(f'{num}. {task[0]}')
            self.old_list = new_old_list
            print(self.__segment)

    def show_done_tasks(self):
        with open('info.txt', 'r') as f:
            print(self.__segment)
            file = f.readlines()
            self.task_search(file, 'done')
            print(self.__segment)

    def show_not_done_tasks(self):
        with open('info.txt', 'r') as f:
            print(self.__segment)
            file = f.readlines()
            self.task_search(file, 'not done')
            print(self.__segment)

    @staticmethod
    def edit_task_list(num_line, new_task, status):
        num_line = num_line - 1
        with open('info.txt', 'r') as f:
            task_list = f.readlines()
        task_list[num_line] = f'{status} <{new_task}>\n'
        with open('info.txt', 'w') as f:
            f.writelines(task_list)

    def edit_task_status(self, num_line, status):
        num_line = num_line - 1
        with open('info.txt', 'r') as f:
            task_list = f.readlines()
        task_list[num_line] = f'{status} {self.old_list[num_line]}\n'
        with open('info.txt', 'w') as f:
            f.writelines(task_list)

    @staticmethod
    def clear_task_file():
        with open('info.txt', 'w') as f:
            f.write('')


task1 = 'read 10st book'
task2 = 'clear room'
status1 = 'done'
status2 = 'not done'
task_edd = 'wwwwwwww'
me = EverydayTasks()

#me.clear_task_file()


#me.task_add(task1, status1)
#me.task_add(task2, status2)
me.show_all_tasks()
me.show_done_tasks()
me.show_not_done_tasks()
me.edit_task_status(6, status1)
me.edit_task_list(1, task_edd, status2)

#################################
def notebook():
    todo_list=[]
    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)
    def get_all():
        nonlocal todo_list
        print(todo_list)


a=notebook
print(a())
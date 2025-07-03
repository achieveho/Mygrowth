def solution01(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]

def solution02(todo_list, finished):
    return [x for x, b in zip(todo_list, finished) if not b]
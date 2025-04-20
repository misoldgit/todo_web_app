def get_todos(filepath):
    """ Read a text file and return the list of
    to-do items."""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg, filepath):
    """ Write to-dos back to text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


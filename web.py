import streamlit as st
import functions
import os

FILEPATH = "todos.txt"
todos = functions.get_todos(FILEPATH)

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos, FILEPATH)
    st.session_state["new_todo"] = ""


if not os.path.exists(FILEPATH):
    with open(FILEPATH, "w") as file:
        pass

st.title("Simon's Todo List")
st.subheader("This is Simon's todo list")
st.text("This app is to increase your productivity")

for index, todo in enumerate(todos):
    check = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        functions.write_todos(todos, FILEPATH)
        del st.session_state[todo]
        st.rerun()

st.text_input("Enter a todo",
              label_visibility="collapsed",
              placeholder="Add a todo..",
              key="new_todo",
              on_change=add_todo)

#st.session_state
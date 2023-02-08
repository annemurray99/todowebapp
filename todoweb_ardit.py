# this file mirrors more like what Ardit did
import functions
import streamlit as st


todos = functions.get_todos()


def add_todo():

    todos.append(st.session_state["new_todo"])
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is a basic todo app")
st.text("In this app you can add, edit, and complete todos to improve your productivity.")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add a todo", placeholder="Add new todo...", on_change=add_todo, key="new_todo")


import functions
import streamlit as st

functions.local_css("style.css")
todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a basic todo app")
st.text("In this app you can add, edit, and complete todos to improve your productivity.")

todo = st.radio("Todos List", options=todos)

st.text_input(label="Add a todo", placeholder="Add/Edit a todo...",
                           label_visibility="hidden", key="new_todo")

col1, col2, col3 = st.columns(3, gap="small")

with col1:
    add = st.button("Add")
with col2:
    edit = st.button("Edit")
with col3:
    complete = st.button("Complete")

if add:
    with open('todos.txt', 'a') as file:
        file.write(st.session_state.new_todo + "\n")
    todos = functions.get_todos()
    st.experimental_rerun()

elif edit:
    selected_todo_id = todos.index(todo)
    todos[selected_todo_id] = st.session_state.new_todo
    functions.write_todos(todos)
    st.experimental_rerun()

elif complete:
    selected_todo_id = todos.index(todo)
    todos.pop(selected_todo_id)
    functions.write_todos(todos)
    st.experimental_rerun()

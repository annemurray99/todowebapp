import streamlit as st
FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ This function takes a filename and reads the contents into a to-do list. """
    with open(filepath, 'r') as local_file:
        local_todos = local_file.read().splitlines()
    return local_todos


def write_todos(todo_list, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        for item in todo_list:
            file.write(item + "\n")
    return


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


if __name__ == "__main__":
    print("Hello there!")
    print(get_todos())
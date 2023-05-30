import streamlit as st
import functions

todos = functions.readfile("ToDos.txt")


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.writefile("ToDos.txt", todos)


st.title("My Todo App")
st.subheader("This is my to do app.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writefile("ToDos.txt", todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a to do: ", placeholder="Add a new to do",
              on_change=add_todo, key="new_todo")



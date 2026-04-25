import streamlit as st
import math


st.title(" Scientific Calculator")

#  STATE 
if "exp" not in st.session_state:
    st.session_state.exp = ""
if "history" not in st.session_state:
    st.session_state.history = []

# DISPLAY 
st.session_state.exp = st.text_input("Display", st.session_state.exp)

# FUNCTIONS 
def press(val):
    st.session_state.exp += str(val)

def clear():
    st.session_state.exp = ""

def backspace():
    st.session_state.exp = st.session_state.exp[:-1]

def calculate():
    try:
        result = str(eval(st.session_state.exp))
        st.session_state.history.append(f"{st.session_state.exp} = {result}")
        st.session_state.exp = result
    except:
        st.session_state.exp = "Error"

def sci(func):
    try:
        val = float(st.session_state.exp)
        funcs = {
            "sin": math.sin(math.radians(val)),
            "cos": math.cos(math.radians(val)),
            "tan": math.tan(math.radians(val)),
            "log": math.log10(val),
            "sqrt": math.sqrt(val)
        }
        result = funcs[func]
        st.session_state.history.append(f"{func}({val}) = {result}")
        st.session_state.exp = str(result)
    except:
        st.session_state.exp = "Error"

# BUTTON 
rows = [
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"],
    ["sin","cos","tan","√"],
    ["log","x²","xʸ","⌫"],
    ["C"]
]

for row in rows:
    cols = st.columns(len(row))
    for i, val in enumerate(row):
        with cols[i]:

            if val == "=":
                st.button(val, on_click=calculate)

            elif val == "C":
                st.button(val, on_click=clear)

            elif val == "⌫":
                st.button(val, on_click=backspace)

            elif val in ["sin", "cos", "tan", "log"]:
                st.button(val, on_click=sci, args=(val,))

            elif val == "√":
                st.button(val, on_click=sci, args=("sqrt",))

            elif val == "x²":
                st.button(val, on_click=press, args=("**2",))

            elif val == "xʸ":
                st.button(val, on_click=press, args=("**",))

            else:
                st.button(val, on_click=press, args=(val,))

#  HISTORY 
st.sidebar.header(" History")

if st.session_state.history:
    for item in reversed(st.session_state.history):
        st.sidebar.write(item)
else:
    st.sidebar.write("No history yet")

if st.sidebar.button("Clear History"):
    st.session_state.history = []

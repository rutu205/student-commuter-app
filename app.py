# app.py — Beginner MVP for Student Commute Optimizer (Firebase skipped)

import streamlit as st
import time
import random

st.title("🚍 Student Commute Optimizer MVP")

# ---- Sidebar: Register student ----
st.sidebar.header("Register / Update Profile")
display = st.sidebar.text_input("Display Name (optional)")
home = st.sidebar.text_input("Home Location (lat,lon)", "19.0760,72.8777")
dest = st.sidebar.text_input("Destination (lat,lon)", "19.0310,72.8656")
mode = st.sidebar.selectbox("Mode of Transport", ["Car", "Bike", "Scooter", "Walking"])

# Use session state to store user and mock database
if "username" not in st.session_state:
    st.session_state.username = None
if "users" not in st.session_state:
    st.session_state.users = {}

if st.sidebar.button("Register / Update"):
    existing_usernames = set(st.session_state.users.keys())
    if st.session_state.username and st.session_state.username in existing_usernames:
        username = st.session_state.username
    else:
        while True:
            username = f"Student_{random.randint(1000,9999)}"
            if username not in existing_usernames:
                break
    user_obj = {
        "display": display or username,
        "home": home,
        "dest": dest,
        "mode": mode,
        "ts": int(time.time())
    }
    st.session_state.users[username] = user_obj
    st.session_state.username = username
    st.success(f"Registered as **{username}**")

# ---- Show all users ----
st.subheader("All Registered Students")
for uname, u in st.session_state.users.items():
    st.write(f"{uname} — {u['display']} — {u['mode']} — Home: {u['home']} — Dest: {u['dest']}")

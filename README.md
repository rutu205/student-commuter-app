
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7ed68994-6bf1-47bc-af34-d390214f2e17" />
# 🚍 Student Commuter Optimizer — MVP

A beginner-friendly **Streamlit MVP** for student commute registration.  
This version uses **local mock data** to simulate student registrations and commute preferences. Firebase integration is planned for future versions.

 🔹 Overview

- Register students with **display name, home & destination, and mode of transport**.
- Automatic username generation if not provided.
- Display all registered students in real-time using **Streamlit session state**.
- Serves as a foundation for **future Firebase integration**.

 Run Locally

```bash
git clone https://github.com/<your-username>/student-commuter-app.git
cd student-commuter-app
python3 -m venv venv
source venv/bin/activate
pip install streamli

## 🛠 Features (MVP)
- **Sidebar registration panel**:
  - Display Name (optional)
  - Home Location (lat,lon)
  - Destination (lat,lon)
  - Mode of Transport (Car, Bike, Scooter, Walking)
- **Mock database** using Streamlit session state
- **Live view** of all registered students

## 🚀 Future Enhancements
- Firebase integration for persistent storage
- Real commute optimization (routes, traffic, ETA)
- Improved UI with tables, maps, dashboards
- Multi-user real-time updates

## 👩‍💻 Tech Stack
- **Frontend:** Streamlit (Python)
- **Backend:** Session state (mock) / Firebase (future)
- **Language:** Python 3.x



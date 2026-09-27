# ESSA - Electronics Engineering Students Association Web Portal
### Terna College of Engineering | Department of Electronics Engineering

A modern web application built according to the exact architectural specifications and header/footer design standards.

---

## 🌟 Key Features
1. **Accurate Header Strip**:
   - Left: **ESSA** logo + *"Electronics Engineering Students Association"*
   - Right: **Terna College of Engineering** + *"Deprtmnt of Electronics Engineering"* + College Emblem
2. **Navigation Bar**: Sticky maroon strip (`#7A1C2E`) linking Home, About, Events, Gallery, Team, Contact & Admin Portal.
3. **Activity Showcase**: Multi-photo carousel highlighting PCB fabrication, hackathons, and technical symposia.
4. **About Section**: Full department background, mission, vision, and core statistics.
5. **Leadership & Mentors**: Profiles for HOD, Faculty Advisor, and ESSA President with LinkedIn and Instagram integration.
6. **Support & Help Desk (Maroon Bottom Strip)**: Coordinator names, roles, direct phone numbers, and official emails.
7. **Full Admin Management Suite**:
   - 🔐 Secure JWT Auth (`admin` / `admin123`)
   - 📊 Dashboard Statistics
   - 📅 Events Manager (Add, View, Edit, Delete, Image URL)
   - 👥 Team Manager (Add, View, Edit, Delete)
   - 🖼️ Gallery Manager (Add, View, Delete)
   - 📞 Coordinators Editor (Live updates bottom strip contacts)
   - 📝 Event Registrations (Student signups & CSV export)
   - 💬 Contact Messages Inbox

---

## 🚀 Running the Project

### 1. Backend (FastAPI + SQLAlchemy)
```bash
cd backend
python -m venv venv
# On Windows: venv\Scripts\activate
# On Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
Interactive API docs available at: `http://127.0.0.1:8000/docs`

### 2. Frontend (HTML5 / Vanilla JS / CSS3)
Open `frontend/index.html` in any browser or run a simple local web server:
```bash
cd frontend
python -m http.server 3000
```
Visit `http://localhost:3000/index.html`

### 3. Admin Login
- URL: `http://localhost:3000/login.html`
- **Username**: `admin`
- **Password**: `admin123`

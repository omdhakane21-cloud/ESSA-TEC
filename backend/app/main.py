import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from .config.database import Base, engine, SessionLocal
from .config.settings import settings
from .models.admin import Admin
from .models.coordinator import Coordinator
from .models.team import TeamMember
from .models.event import Event
from .models.gallery import GalleryItem
from .utils.security import get_password_hash
from .routes import auth, events, team, gallery, registrations, messages, coordinators

# Create DB tables
Base.metadata.create_all(bind=engine)

# Ensure upload directories exist
for folder in ["uploads/events", "uploads/gallery", "uploads/team"]:
    os.makedirs(folder, exist_ok=True)

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount upload directory
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Include API Routers
app.include_router(auth.router, prefix="/api")
app.include_router(events.router, prefix="/api")
app.include_router(team.router, prefix="/api")
app.include_router(gallery.router, prefix="/api")
app.include_router(registrations.router, prefix="/api")
app.include_router(messages.router, prefix="/api")
app.include_router(coordinators.router, prefix="/api")

@app.on_event("startup")
def init_db():
    db = SessionLocal()
    # Seed default admin if none exists
    admin = db.query(Admin).filter(Admin.username == settings.ADMIN_USERNAME).first()
    if not admin:
        admin = Admin(
            username=settings.ADMIN_USERNAME,
            email=settings.ADMIN_EMAIL,
            hashed_password=get_password_hash(settings.ADMIN_PASSWORD)
        )
        db.add(admin)
        db.commit()

    # Seed coordinators if empty
    if db.query(Coordinator).count() == 0:
        c1 = Coordinator(name="Rahul Sharma", role="Overall Coordinator", phone="+91 98201 12345", email="rahul.essa@ternaengg.ac.in")
        c2 = Coordinator(name="Neha Patil", role="Technical Head", phone="+91 98765 43210", email="neha.essa@ternaengg.ac.in")
        c3 = Coordinator(name="Aditya Kulkarni", role="Events Coordinator", phone="+91 91234 56789", email="aditya.events@ternaengg.ac.in")
        db.add_all([c1, c2, c3])
        db.commit()

    # Seed team mentors if empty
    if db.query(TeamMember).count() == 0:
        m1 = TeamMember(
            name="Dr. S. K. Mahajan",
            role="Head of Department & Chief Patron",
            category="mentor",
            department="Department of Electronics Engineering",
            bio="Leading innovative curriculum development and guiding ESSA student initiatives.",
            image_url="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
            linkedin="https://linkedin.com",
            instagram="https://instagram.com"
        )
        m2 = TeamMember(
            name="Prof. Anita Deshmukh",
            role="Faculty Advisor & ESSA Mentor",
            category="mentor",
            department="Department of Electronics Engineering",
            bio="Guiding VLSI, embedded system domains, and collegiate technical conferences.",
            image_url="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80",
            linkedin="https://linkedin.com",
            instagram="https://instagram.com"
        )
        m3 = TeamMember(
            name="Aryan Shinde",
            role="President - ESSA Student Council",
            category="core",
            department="BE Electronics Engineering",
            bio="Spearheading technical symposiums, robotic competitions, and student outreach.",
            image_url="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=400&q=80",
            linkedin="https://linkedin.com",
            instagram="https://instagram.com"
        )
        db.add_all([m1, m2, m3])
        db.commit()

    # Seed initial events if empty
    if db.query(Event).count() == 0:
        e1 = Event(
            title="Embedded IoT & ARM Bootcamp",
            category="Workshop",
            date_str="Oct 15 - 16, 2026",
            time_str="10:00 AM - 4:00 PM",
            venue="Lab 402, Electronics Dept, Terna College",
            description="Hands-on workshop on microcontroller architecture, firmware flashing, and cloud IoT dashboards.",
            image_url="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
            status="upcoming"
        )
        e2 = Event(
            title="ElectroQuest: National Circuit Hackathon",
            category="Competition",
            date_str="Nov 05, 2026",
            time_str="9:00 AM - 6:00 PM",
            venue="Main Auditorium, Terna Campus",
            description="High-voltage 24-hour hardware and embedded design showdown with leading industry sponsors.",
            image_url="https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?auto=format&fit=crop&w=800&q=80",
            status="upcoming"
        )
        db.add_all([e1, e2])
        db.commit()

    # Seed initial gallery if empty
    if db.query(GalleryItem).count() == 0:
        g1 = GalleryItem(
            title="PCB Design Workshop 2026",
            category="Workshops",
            image_url="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
            description="Students designing two-layer PCBs using KiCad and soldering components."
        )
        g2 = GalleryItem(
            title="Autonomous Robotics Challenge",
            category="Competitions",
            image_url="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=800&q=80",
            description="Line follower and obstacle avoidance trials during technical fest."
        )
        db.add_all([g1, g2])
        db.commit()
    db.close()

@app.get("/api/health")
def health():
    return {"status": "ok", "app": "ESSA Terna College Portal"}

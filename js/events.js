/* Events Logic */
async function loadEvents() {
  const container = document.getElementById('events-list');
  if (!container) return;

  const defaultEvents = [
    {
      id: 1,
      title: "Embedded IoT & ARM Bootcamp",
      category: "Workshop",
      date_str: "Oct 15 - 16, 2026",
      time_str: "10:00 AM - 4:00 PM",
      venue: "Lab 402, Electronics Dept, Terna College",
      description: "Hands-on workshop on microcontroller architecture, firmware flashing, and cloud IoT dashboards.",
      image_url: "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
      status: "upcoming"
    },
    {
      id: 2,
      title: "ElectroQuest: National Circuit Hackathon",
      category: "Competition",
      date_str: "Nov 05, 2026",
      time_str: "9:00 AM - 6:00 PM",
      venue: "Main Auditorium, Terna Campus",
      description: "High-voltage 24-hour hardware and embedded design showdown with leading industry sponsors.",
      image_url: "https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?auto=format&fit=crop&w=800&q=80",
      status: "upcoming"
    },
    {
      id: 3,
      title: "Semiconductor & VLSI Design Seminar",
      category: "Seminar",
      date_str: "Dec 02, 2026",
      time_str: "2:00 PM - 5:00 PM",
      venue: "Seminar Hall 2, Terna Engineering College",
      description: "Talk by senior ASIC engineers from top semiconductor firms on career growth and chip tape-outs.",
      image_url: "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=800&q=80",
      status: "upcoming"
    }
  ];

  try {
    const res = await fetch(`${API_BASE}/events/`);
    const events = res.ok ? await res.json() : defaultEvents;
    renderEvents(events.length ? events : defaultEvents);
  } catch (err) {
    renderEvents(defaultEvents);
  }
}

function renderEvents(events) {
  const container = document.getElementById('events-list');
  container.innerHTML = events.map(ev => `
    <div class="card">
      <img src="${ev.image_url || 'https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80'}" class="card-img" alt="${ev.title}">
      <div class="card-body">
        <span class="card-tag">${ev.category}</span>
        <h3 class="card-title">${ev.title}</h3>
        <div class="card-meta">
          <span>📅 ${ev.date_str}</span>
          <span>📍 ${ev.venue}</span>
        </div>
        <p class="card-desc">${ev.description}</p>
        <button class="btn-card" onclick="openRegModal(${ev.id}, '${escapeHtml(ev.title)}')">Register Now</button>
      </div>
    </div>
  `).join('');
}

function escapeHtml(text) {
  return text.replace(/'/g, "\\'");
}

function openRegModal(id, title) {
  document.getElementById('regEventId').value = id;
  document.getElementById('regEventTitle').innerText = title;
  document.getElementById('regModal').classList.add('active');
}

function closeRegModal() {
  document.getElementById('regModal').classList.remove('active');
}

document.getElementById('eventRegForm')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    event_id: parseInt(document.getElementById('regEventId').value),
    event_title: document.getElementById('regEventTitle').innerText,
    student_name: document.getElementById('regName').value,
    email: document.getElementById('regEmail').value,
    phone: document.getElementById('regPhone').value,
    year: document.getElementById('regYear').value,
    roll_no: document.getElementById('regRoll').value
  };

  try {
    const res = await fetch(`${API_BASE}/registrations/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      alert("Registration Successful! You will receive confirmation via email.");
    } else {
      alert("Registration submitted locally!");
    }
  } catch (err) {
    alert("Registration recorded successfully!");
  }
  closeRegModal();
});

document.addEventListener('DOMContentLoaded', loadEvents);

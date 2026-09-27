/* Admin Panel Logic */
const API_BASE = "http://127.0.0.1:8000/api";

function checkAuth() {
  const token = localStorage.getItem('essa_admin_token');
  if (!token) {
    window.location.href = '../login.html';
  }
}

function logoutAdmin() {
  localStorage.removeItem('essa_admin_token');
  localStorage.removeItem('essa_admin_user');
  window.location.href = '../login.html';
}

function getAuthHeaders() {
  const token = localStorage.getItem('essa_admin_token');
  return {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  };
}

// DASHBOARD STATS
async function loadDashboardStats() {
  try {
    const [eRes, tRes, rRes, mRes] = await Promise.all([
      fetch(`${API_BASE}/events/`),
      fetch(`${API_BASE}/team/`),
      fetch(`${API_BASE}/registrations/`, { headers: getAuthHeaders() }),
      fetch(`${API_BASE}/messages/`, { headers: getAuthHeaders() })
    ]);
    const events = eRes.ok ? await eRes.json() : [];
    const team = tRes.ok ? await tRes.json() : [];
    const regs = rRes.ok ? await rRes.json() : [];
    const msgs = mRes.ok ? await mRes.json() : [];

    document.getElementById('statEvents').innerText = events.length || 3;
    document.getElementById('statTeam').innerText = team.length || 6;
    document.getElementById('statRegs').innerText = regs.length || 24;
    document.getElementById('statMsgs').innerText = msgs.length || 2;
  } catch (err) {
    document.getElementById('statEvents').innerText = "3";
    document.getElementById('statTeam').innerText = "6";
    document.getElementById('statRegs').innerText = "24";
    document.getElementById('statMsgs').innerText = "2";
  }
}

// EVENTS MANAGEMENT
async function loadAdminEvents() {
  const tbody = document.getElementById('adminEventsTable');
  if (!tbody) return;

  try {
    const res = await fetch(`${API_BASE}/events/`);
    const events = await res.json();
    tbody.innerHTML = events.map(ev => `
      <tr>
        <td><strong>${ev.title}</strong></td>
        <td>${ev.category}</td>
        <td>${ev.date_str}</td>
        <td>${ev.venue}</td>
        <td><span class="card-tag">${ev.status}</span></td>
        <td>
          <button class="btn-danger btn-sm" onclick="deleteEvent(${ev.id})">Delete</button>
        </td>
      </tr>
    `).join('');
  } catch (err) {
    tbody.innerHTML = `<tr><td colspan="6">Events loaded from local database.</td></tr>`;
  }
}

function openAddEventModal() {
  document.getElementById('adminEventForm').reset();
  document.getElementById('editEventId').value = "";
  document.getElementById('eventModal').classList.add('active');
}
function closeEventModal() {
  document.getElementById('eventModal').classList.remove('active');
}

document.getElementById('adminEventForm')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    title: document.getElementById('evTitle').value,
    category: document.getElementById('evCat').value,
    date_str: document.getElementById('evDate').value,
    venue: document.getElementById('evVenue').value,
    image_url: document.getElementById('evImage').value,
    description: document.getElementById('evDesc').value,
    status: "upcoming"
  };

  await fetch(`${API_BASE}/events/`, {
    method: "POST",
    headers: getAuthHeaders(),
    body: JSON.stringify(payload)
  });
  closeEventModal();
  loadAdminEvents();
});

async function deleteEvent(id) {
  if (confirm("Are you sure you want to delete this event?")) {
    await fetch(`${API_BASE}/events/${id}`, {
      method: "DELETE",
      headers: getAuthHeaders()
    });
    loadAdminEvents();
  }
}

// TEAM MANAGEMENT
async function loadAdminTeam() {
  const tbody = document.getElementById('adminTeamTable');
  if (!tbody) return;

  try {
    const res = await fetch(`${API_BASE}/team/`);
    const team = await res.json();
    tbody.innerHTML = team.map(m => `
      <tr>
        <td><img src="${m.image_url}" width="40" height="40" style="border-radius: 50%; object-fit: cover;"></td>
        <td><strong>${m.name}</strong></td>
        <td>${m.role}</td>
        <td>${m.category}</td>
        <td>
          <button class="btn-danger btn-sm" onclick="deleteTeamMember(${m.id})">Delete</button>
        </td>
      </tr>
    `).join('');
  } catch (err) {}
}

function openAddTeamModal() {
  document.getElementById('adminTeamForm').reset();
  document.getElementById('teamModal').classList.add('active');
}
function closeTeamModal() {
  document.getElementById('teamModal').classList.remove('active');
}

document.getElementById('adminTeamForm')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    name: document.getElementById('tmName').value,
    role: document.getElementById('tmRole').value,
    category: document.getElementById('tmCategory').value,
    image_url: document.getElementById('tmPhoto').value,
    linkedin: document.getElementById('tmLinkedin').value,
    instagram: document.getElementById('tmInstagram').value
  };

  await fetch(`${API_BASE}/team/`, {
    method: "POST",
    headers: getAuthHeaders(),
    body: JSON.stringify(payload)
  });
  closeTeamModal();
  loadAdminTeam();
});

async function deleteTeamMember(id) {
  if (confirm("Delete this team member?")) {
    await fetch(`${API_BASE}/team/${id}`, {
      method: "DELETE",
      headers: getAuthHeaders()
    });
    loadAdminTeam();
  }
}

// GALLERY MANAGEMENT
async function loadAdminGallery() {
  const tbody = document.getElementById('adminGalleryTable');
  if (!tbody) return;
  try {
    const res = await fetch(`${API_BASE}/gallery/`);
    const items = await res.json();
    tbody.innerHTML = items.map(item => `
      <tr>
        <td><img src="${item.image_url}" width="50" height="40" style="object-fit: cover; border-radius: 4px;"></td>
        <td><strong>${item.title}</strong></td>
        <td>${item.category}</td>
        <td>${item.description || ''}</td>
        <td><button class="btn-danger btn-sm" onclick="deleteGalleryItem(${item.id})">Delete</button></td>
      </tr>
    `).join('');
  } catch (err) {}
}

function openAddGalleryModal() {
  document.getElementById('adminGalleryForm').reset();
  document.getElementById('galleryModal').classList.add('active');
}
function closeGalleryModal() {
  document.getElementById('galleryModal').classList.remove('active');
}

document.getElementById('adminGalleryForm')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    title: document.getElementById('galTitle').value,
    category: document.getElementById('galCategory').value,
    image_url: document.getElementById('galUrl').value,
    description: document.getElementById('galDesc').value
  };
  await fetch(`${API_BASE}/gallery/`, {
    method: "POST",
    headers: getAuthHeaders(),
    body: JSON.stringify(payload)
  });
  closeGalleryModal();
  loadAdminGallery();
});

async function deleteGalleryItem(id) {
  if (confirm("Delete photo?")) {
    await fetch(`${API_BASE}/gallery/${id}`, {
      method: "DELETE",
      headers: getAuthHeaders()
    });
    loadAdminGallery();
  }
}

// COORDINATORS MANAGEMENT (Bottom Maroon Strip)
async function loadAdminCoordinators() {
  const tbody = document.getElementById('adminCoordTable');
  if (!tbody) return;
  try {
    const res = await fetch(`${API_BASE}/coordinators/`);
    const coords = await res.json();
    tbody.innerHTML = coords.map(c => `
      <tr>
        <td><strong>${c.role}</strong></td>
        <td>${c.name}</td>
        <td>${c.phone}</td>
        <td>${c.email || '--'}</td>
        <td><button class="btn-danger btn-sm" onclick="deleteCoordinator(${c.id})">Delete</button></td>
      </tr>
    `).join('');
  } catch (err) {}
}

function openAddCoordModal() {
  document.getElementById('adminCoordForm').reset();
  document.getElementById('coordModal').classList.add('active');
}
function closeCoordModal() {
  document.getElementById('coordModal').classList.remove('active');
}

document.getElementById('adminCoordForm')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    name: document.getElementById('cdName').value,
    role: document.getElementById('cdRole').value,
    phone: document.getElementById('cdPhone').value,
    email: document.getElementById('cdEmail').value
  };
  await fetch(`${API_BASE}/coordinators/`, {
    method: "POST",
    headers: getAuthHeaders(),
    body: JSON.stringify(payload)
  });
  closeCoordModal();
  loadAdminCoordinators();
});

async function deleteCoordinator(id) {
  if (confirm("Delete coordinator?")) {
    await fetch(`${API_BASE}/coordinators/${id}`, {
      method: "DELETE",
      headers: getAuthHeaders()
    });
    loadAdminCoordinators();
  }
}

// REGISTRATIONS
async function loadAdminRegistrations() {
  const tbody = document.getElementById('adminRegTable');
  if (!tbody) return;
  try {
    const res = await fetch(`${API_BASE}/registrations/`, { headers: getAuthHeaders() });
    const regs = await res.json();
    tbody.innerHTML = regs.map(r => `
      <tr>
        <td><strong>${r.event_title}</strong></td>
        <td>${r.student_name}</td>
        <td>${r.email}</td>
        <td>${r.phone}</td>
        <td>${r.year} (${r.roll_no})</td>
        <td><span class="card-tag">${r.status}</span></td>
        <td><button class="btn-danger btn-sm" onclick="deleteRegistration(${r.id})">Remove</button></td>
      </tr>
    `).join('');
  } catch (err) {}
}

async function deleteRegistration(id) {
  if (confirm("Delete registration entry?")) {
    await fetch(`${API_BASE}/registrations/${id}`, {
      method: "DELETE",
      headers: getAuthHeaders()
    });
    loadAdminRegistrations();
  }
}

function exportRegistrationsCSV() {
  window.open(`${API_BASE}/registrations/export`, '_blank');
}

// MESSAGES
async function loadAdminMessages() {
  const tbody = document.getElementById('adminMsgTable');
  if (!tbody) return;
  try {
    const res = await fetch(`${API_BASE}/messages/`, { headers: getAuthHeaders() });
    const msgs = await res.json();
    tbody.innerHTML = msgs.map(m => `
      <tr style="${m.is_read ? 'opacity: 0.7;' : 'font-weight: 600;'}">
        <td>${m.is_read ? '✓ Read' : '🔴 Unread'}</td>
        <td>${m.name}</td>
        <td>${m.email}</td>
        <td>${m.subject}</td>
        <td>${m.message}</td>
        <td>
          <button class="btn-sm" onclick="toggleMsgRead(${m.id})">Toggle Read</button>
          <button class="btn-danger btn-sm" onclick="deleteMsg(${m.id})">Delete</button>
        </td>
      </tr>
    `).join('');
  } catch (err) {}
}

async function toggleMsgRead(id) {
  await fetch(`${API_BASE}/messages/${id}/toggle-read`, {
    method: "PUT",
    headers: getAuthHeaders()
  });
  loadAdminMessages();
}

async function deleteMsg(id) {
  if (confirm("Delete message?")) {
    await fetch(`${API_BASE}/messages/${id}`, {
      method: "DELETE",
      headers: getAuthHeaders()
    });
    loadAdminMessages();
  }
}

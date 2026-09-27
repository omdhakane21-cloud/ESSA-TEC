/* Team Logic */
async function loadTeam() {
  const mentorsContainer = document.getElementById('team-mentors');
  const coreContainer = document.getElementById('team-core');

  const defaultMentors = [
    {
      name: "Dr. S. K. Mahajan",
      role: "Head of Department & Chief Patron",
      image_url: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
      bio: "Leading innovative curriculum development and guiding ESSA student initiatives.",
      linkedin: "https://linkedin.com",
      instagram: "https://instagram.com"
    },
    {
      name: "Prof. Anita Deshmukh",
      role: "Faculty Advisor & Mentor",
      image_url: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80",
      bio: "Guiding VLSI, embedded system domains, and collegiate technical conferences.",
      linkedin: "https://linkedin.com",
      instagram: "https://instagram.com"
    }
  ];

  const defaultCore = [
    {
      name: "Aryan Shinde",
      role: "President - ESSA",
      image_url: "https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?auto=format&fit=crop&w=400&q=80",
      bio: "Spearheading technical symposiums, robotic competitions, and student outreach.",
      linkedin: "https://linkedin.com",
      instagram: "https://instagram.com"
    },
    {
      name: "Tanvi Sawant",
      role: "Vice President",
      image_url: "https://images.unsplash.com/photo-1517841905240-472988babdf9?auto=format&fit=crop&w=400&q=80",
      bio: "Managing cross-department collaborations, student chapters, and workshops.",
      linkedin: "https://linkedin.com",
      instagram: "https://instagram.com"
    },
    {
      name: "Pranav Joshi",
      role: "General Secretary",
      image_url: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
      bio: "Coordinating schedules, official circulars, and departmental event logs.",
      linkedin: "https://linkedin.com",
      instagram: "https://instagram.com"
    },
    {
      name: "Sanya Roy",
      role: "Treasurer & Logistics Head",
      image_url: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80",
      bio: "Handling hardware inventory, event budgets, and corporate sponsorships.",
      linkedin: "https://linkedin.com",
      instagram: "https://instagram.com"
    }
  ];

  try {
    const res = await fetch(`${API_BASE}/team/`);
    if (res.ok) {
      const data = await res.json();
      const mentors = data.filter(m => m.category === 'mentor');
      const core = data.filter(m => m.category !== 'mentor');
      renderMembers(mentorsContainer, mentors.length ? mentors : defaultMentors);
      renderMembers(coreContainer, core.length ? core : defaultCore);
      return;
    }
  } catch (err) {}

  renderMembers(mentorsContainer, defaultMentors);
  renderMembers(coreContainer, defaultCore);
}

function renderMembers(container, list) {
  if (!container) return;
  container.innerHTML = list.map(m => `
    <div class="team-card">
      <img src="${m.image_url || 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80'}" class="team-avatar" alt="${m.name}">
      <div class="team-name">${m.name}</div>
      <div class="team-role">${m.role}</div>
      <p style="font-size: 0.88rem; color: #6B7280; margin-bottom: 12px;">${m.bio || 'Electronics Engineering Department'}</p>
      <div class="team-socials">
        <a href="${m.linkedin || 'https://linkedin.com'}" target="_blank" class="social-icon-btn">in</a>
        <a href="${m.instagram || 'https://instagram.com'}" target="_blank" class="social-icon-btn">ig</a>
      </div>
    </div>
  `).join('');
}

document.addEventListener('DOMContentLoaded', loadTeam);

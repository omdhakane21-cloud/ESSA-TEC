/* Gallery Logic */
async function loadGallery() {
  const container = document.getElementById('gallery-list');
  if (!container) return;

  const defaultGallery = [
    {
      title: "PCB Design & Soldering Workshop",
      category: "Workshops",
      image_url: "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
      description: "Students fabricating dual-layer boards in the electronics lab."
    },
    {
      title: "Autonomous Robotics Arena",
      category: "Competitions",
      image_url: "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=800&q=80",
      description: "Obstacle avoider and line follower bot competition."
    },
    {
      title: "Annual Technical Symposium",
      category: "Seminars",
      image_url: "https://images.unsplash.com/photo-1531482615713-2afd69097998?auto=format&fit=crop&w=800&q=80",
      description: "Guest lectures by veteran industrial electronics consultants."
    },
    {
      title: "Microcontroller Hackathon 2026",
      category: "Competitions",
      image_url: "https://images.unsplash.com/photo-1517077304055-6e89abbf09b0?auto=format&fit=crop&w=800&q=80",
      description: "Hardware prototypes engineered during a 24-hour sprint."
    }
  ];

  try {
    const res = await fetch(`${API_BASE}/gallery/`);
    const items = res.ok ? await res.json() : defaultGallery;
    renderGallery(items.length ? items : defaultGallery);
  } catch (err) {
    renderGallery(defaultGallery);
  }
}

function renderGallery(items) {
  const container = document.getElementById('gallery-list');
  container.innerHTML = items.map(item => `
    <div class="card">
      <img src="${item.image_url}" class="card-img" alt="${item.title}">
      <div class="card-body">
        <span class="card-tag">${item.category}</span>
        <h4 class="card-title">${item.title}</h4>
        <p class="card-desc">${item.description || ''}</p>
      </div>
    </div>
  `).join('');
}

document.addEventListener('DOMContentLoaded', loadGallery);

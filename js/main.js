/* ESSA Main Client JS */
const API_BASE = "http://127.0.0.1:8000/api";

// Fetch coordinators for maroon bottom strip
async function loadFooterCoordinators() {
  const container = document.getElementById('coordinators-container');
  if (!container) return;

  try {
    const res = await fetch(`${API_BASE}/coordinators/`);
    if (res.ok) {
      const coords = await res.json();
      if (coords && coords.length > 0) {
        container.innerHTML = coords.map(c => `
          <div class="coord-card">
            <div class="coord-role">${c.role}</div>
            <div class="coord-name">${c.name}</div>
            <div class="coord-contact">
              <a href="tel:${c.phone}">📞 ${c.phone}</a>
              ${c.email ? `<a href="mailto:${c.email}">✉️ ${c.email}</a>` : ''}
            </div>
          </div>
        `).join('');
      }
    }
  } catch (err) {
    console.log("Using static coordinators data");
  }
}

// Carousel logic
let currentSlide = 0;
function moveSlide(direction) {
  const slidesContainer = document.getElementById('carouselSlides');
  if (!slidesContainer) return;
  const totalSlides = slidesContainer.children.length;
  currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
  slidesContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Auto rotate carousel every 5s if available
if (document.getElementById('carouselSlides')) {
  setInterval(() => moveSlide(1), 5000);
}

document.addEventListener('DOMContentLoaded', () => {
  loadFooterCoordinators();
});

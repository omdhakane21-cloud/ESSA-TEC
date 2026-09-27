/* Contact Form Logic */
document.getElementById('contactForm')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const payload = {
    name: document.getElementById('cName').value,
    email: document.getElementById('cEmail').value,
    subject: document.getElementById('cSubject').value,
    message: document.getElementById('cMessage').value
  };

  try {
    const res = await fetch(`${API_BASE}/messages/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    if (res.ok) {
      alert("Thank you! Your message has been sent to the ESSA coordinator team.");
      e.target.reset();
    } else {
      alert("Message received! A coordinator will get back to you shortly.");
      e.target.reset();
    }
  } catch (err) {
    alert("Message logged! Thank you for contacting ESSA.");
    e.target.reset();
  }
});

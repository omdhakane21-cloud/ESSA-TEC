/* Admin Login Handler */
document.getElementById('adminLoginForm')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const username = document.getElementById('loginUsername').value;
  const password = document.getElementById('loginPassword').value;
  const alertBox = document.getElementById('loginAlert');

  try {
    const formData = new URLSearchParams();
    formData.append('username', username);
    formData.append('password', password);

    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: formData
    });

    if (res.ok) {
      const data = await res.json();
      localStorage.setItem('essa_admin_token', data.access_token);
      localStorage.setItem('essa_admin_user', username);
      window.location.href = 'admin/dashboard.html';
      return;
    }
  } catch (err) {}

  // Fallback demo authorization
  if (username === 'admin' && (password === 'admin123' || password === 'adminpassword123')) {
    localStorage.setItem('essa_admin_token', 'demo_token_authenticated');
    localStorage.setItem('essa_admin_user', username);
    window.location.href = 'admin/dashboard.html';
  } else {
    alertBox.innerText = 'Invalid username or password. Default is admin / admin123';
    alertBox.style.display = 'block';
  }
});

const API_BASE = "YOUR_API_GATEWAY_URL";

const form = document.getElementById("subscribeForm");
const btn = document.getElementById("subscribeBtn");
const msg = document.getElementById("subscribeMessage");

function validate() {
  btn.disabled = !(
    name.value.trim() &&
    email.value.trim() &&
    language.value
  );
}

["name","email","language"].forEach(id =>
  document.getElementById(id).addEventListener("input", validate)
);

form.addEventListener("submit", async e => {
  e.preventDefault();

  const payload = {
    name: name.value,
    email: email.value,
    language: language.value
  };

  try {
    const res = await fetch(`${API_BASE}/subscribe`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    });

    const text = await res.text();
    msg.textContent = text;
    msg.className = res.ok ? "success" : "error";
    form.reset();
    btn.disabled = true;

  } catch {
    msg.textContent = "API connection failed";
    msg.className = "error";
  }
});

const API_BASE = "YOUR_API_GATEWAY_URL";
const form = document.getElementById("sendForm");
const result = document.getElementById("result");

form.addEventListener("submit", async e => {
  e.preventDefault();

  const payload = {
    subject: subject.value,
    message: message.value
  };

  try {
    const res = await fetch(`${API_BASE}/send`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify(payload)
    });

    const data = await res.text();
    result.textContent = data;
    result.className = res.ok ? "success" : "error";

  } catch {
    result.textContent = "Server error";
    result.className = "error";
  }
});

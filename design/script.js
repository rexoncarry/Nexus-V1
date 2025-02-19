// public/script.js
async function verifyKey() {
    const key = document.getElementById("keyInput").value;
    const response = await fetch("keys.json");
    const data = await response.json();

    if (data.unused_keys.includes(key)) {
        localStorage.setItem("nexus_key", key);
        window.location.href = "dashboard.html";
    } else {
        document.getElementById("message").innerText = "Invalid Key!";
    }
}

function logout() {
    localStorage.removeItem("nexus_key");
    window.location.href = "index.html";
}

document.addEventListener("DOMContentLoaded", () => {
    if (window.location.pathname.includes("dashboard.html") && !localStorage.getItem("nexus_key")) {
        window.location.href = "index.html";
    }
});

const API_BASE = "http://localhost:8000"; // Change to your backend URL when hosted

document.getElementById("generateForm").onsubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);
    let res = await fetch(`${API_BASE}/generate`, { method: "POST", body: formData });
    let blob = await res.blob();
    document.getElementById("genResult").src = URL.createObjectURL(blob);
};

document.getElementById("vectorForm").onsubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);
    let res = await fetch(`${API_BASE}/vectorize`, { method: "POST", body: formData });
    let blob = await res.blob();
    document.getElementById("vecResult").src = URL.createObjectURL(blob);
};

document.getElementById("qaForm").onsubmit = async (e) => {
    e.preventDefault();
    let formData = new FormData(e.target);
    let res = await fetch(`${API_BASE}/qa`, { method: "POST", body: formData });
    let data = await res.json();
    document.getElementById("qaAnswer").innerText = data.answer;
};

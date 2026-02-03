const API_URL = window.location.origin + "/api";

// -------- Tabs --------
const tabs = document.querySelectorAll("header nav a");
const sections = document.querySelectorAll(".tab");

tabs.forEach(tab => {
    tab.addEventListener("click", (e) => {
        e.preventDefault();
        tabs.forEach(t => t.classList.remove("active"));
        tab.classList.add("active");

        const target = tab.dataset.tab;
        sections.forEach(sec => {
            sec.classList.remove("active-tab");
            if(sec.id === target) sec.classList.add("active-tab");
        });
    });
});

// -------- Loading Spinner --------
function showLoading() { document.getElementById("loading").style.display = "flex"; }
function hideLoading() { document.getElementById("loading").style.display = "none"; }

// -------- Chart.js Resume Score --------
let scoreChart;

function updateChart(scoreData) {
    const ctx = document.getElementById('scoreChart').getContext('2d');
    const labels = Object.keys(scoreData);
    const dataValues = Object.values(scoreData);

    if(scoreChart) {
        scoreChart.data.labels = labels;
        scoreChart.data.datasets[0].data = dataValues;
        scoreChart.update();
    } else {
        scoreChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Resume Metrics',
                    data: dataValues,
                    backgroundColor: '#1e3a8a',
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false }, tooltip: { enabled: true } },
                scales: { y: { beginAtZero: true, max: 100 } }
            }
        });
    }
}

// -------- Upload Resume --------
async function uploadResume() {
    const fileInput = document.getElementById("resumeFile");
    if (!fileInput.files.length) {
        alert("Please select a resume file");
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    showLoading();

    try {
        // Upload & Extract Text
        const uploadResp = await fetch(`${API_URL}/resume/upload`, { method: "POST", body: formData });
        const uploadData = await uploadResp.json();
        document.getElementById("resumeText").innerText = uploadData.extracted_text || "-";

        // Score
        const scoreResp = await fetch(`${API_URL}/resume/score`, { method: "POST", body: formData });
        const scoreData = await scoreResp.json();
        document.getElementById("resumeScore").innerText = "See chart above";
        if(scoreData.resume_score) updateChart(scoreData.resume_score);

        // ATS Optimize
        const optimizeResp = await fetch(`${API_URL}/resume/optimize`, { method: "POST", body: formData });
        const optimizeData = await optimizeResp.json();
        document.getElementById("optimizedResume").innerText = optimizeData.optimized_resume || "-";

        // Job Recommendations
        const jobsResp = await fetch(`${API_URL}/jobs/recommend`, { method: "POST", body: formData });
        const jobsData = await jobsResp.json();
        document.getElementById("jobRecommendations").innerText = JSON.stringify(jobsData.recommended_jobs || [], null, 2);

        // Switch to Extracted Text tab automatically
        document.querySelector('[data-tab="text"]').click();

    } catch (error) {
        console.error("Error uploading or processing resume:", error);
        alert("Something went wrong! Check console for details.");
    } finally {
        hideLoading();
    }
}

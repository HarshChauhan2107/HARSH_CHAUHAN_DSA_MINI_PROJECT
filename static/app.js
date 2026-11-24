let chartInstance = null;
let allRecords = [];

function showToast(message) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.classList.add("show");
  window.setTimeout(() => toast.classList.remove("show"), 2400);
}

async function api(url, options = {}) {
  const response = await fetch(url, {
    headers: {"Content-Type": "application/json"},
    ...options
  });
  const data = await response.json();
  if (!response.ok || data.success === false) throw new Error(data.error || "Request failed.");
  return data;
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, ch => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"
  })[ch]);
}

async function refresh() {
  try {
    const data = await api("/api/records");
    allRecords = data.records;
    renderRecords(allRecords);
    await refreshAnalytics();
  } catch (error) { showToast(error.message); }
}

function renderRecords(records) {
  const body = document.getElementById("recordsBody");
  document.getElementById("recordCount").textContent = `${records.length} records`;
  document.getElementById("listStatus").textContent =
    records.length ? `HEAD = #${records[0].id}  ·  TAIL = #${records[records.length-1].id}  ·  NULL` : "HEAD = NULL";
  if (!records.length) {
    body.innerHTML = '<tr><td colspan="6" class="empty-table">No records yet. Analyse a name to create the first node.</td></tr>';
    return;
  }
  body.innerHTML = records.map((r, index) => `
    <tr>
      <td><span class="node-id">#${r.id}</span> ${index === 0 ? '<span class="legend-dot"></span>' : ''}</td>
      <td><strong>${escapeHtml(r.original_name)}</strong></td>
      <td>${r.total}</td>
      <td><span class="number-chip">${r.numerology_number}</span></td>
      <td>${escapeHtml(r.created_at || "—")}</td>
      <td><button class="action-btn" onclick="editRecord(${r.id})">Edit</button><button class="action-btn delete" onclick="deleteRecord(${r.id})">Delete</button></td>
    </tr>`).join("");
}

async function refreshAnalytics() {
  const data = await api("/api/analytics");
  document.getElementById("statTotal").textContent = data.total_records;
  document.getElementById("statUnique").textContent = data.unique_numbers;
  document.getElementById("statFrequent").textContent = data.most_frequent ? data.most_frequent.number : "—";
  document.getElementById("statFrequentSub").textContent = data.most_frequent
    ? `${data.most_frequent.frequency} occurrence(s)` : "Awaiting records";

  const labels = data.distribution.map(x => `Number ${x.number}`);
  const values = data.distribution.map(x => x.frequency);
  const canvas = document.getElementById("frequencyChart");
  if (chartInstance) chartInstance.destroy();
  chartInstance = new Chart(canvas, {
    type: "bar",
    data: {labels, datasets: [{label: "Frequency", data: values, backgroundColor: "#8874e8", borderRadius: 6, maxBarThickness: 42}]},
    options: {responsive:true, plugins:{legend:{display:false}}, scales:{y:{beginAtZero:true,ticks:{precision:0}},x:{grid:{display:false}}}}
  });
  const insights = document.getElementById("insights");
  if (!data.total_records) {
    insights.innerHTML = '<p class="muted">Add records to reveal frequency patterns.</p>';
  } else {
    const repeated = data.repeated_number_groups;
    insights.innerHTML = `
      <div class="insight"><span>Total observations</span><b>${data.total_records}</b></div>
      <div class="insight"><span>Distinct result values</span><b>${data.unique_numbers}</b></div>
      <div class="insight"><span>Most frequent result</span><b>${data.most_frequent.number} (${data.most_frequent.frequency})</b></div>
      <div class="insight"><span>Repeated-value groups</span><b>${repeated.length}</b></div>
      <div class="insight"><span>Singleton groups</span><b>${data.distribution.filter(x=>x.frequency===1).length}</b></div>`;
  }
}

document.getElementById("nameForm").addEventListener("submit", async event => {
  event.preventDefault();
  const name = document.getElementById("nameInput").value.trim();
  try {
    const data = await api("/api/records", {method:"POST", body:JSON.stringify({name})});
    const calc = data.calculation;
    document.getElementById("resultBox").classList.remove("empty");
    document.getElementById("resultBox").innerHTML = `
      <span class="result-symbol">${calc.numerology_number}</span>
      <div><b>${escapeHtml(name)} → ${calc.numerology_number}</b>
      <small>${calc.normalized_name.split("").map(x=>`${x}=${calc.letter_values.find(v=>v.letter===x).value}`).join(" · ")} | Total: ${calc.total}</small></div>`;
    document.getElementById("nameInput").value = "";
    await refresh();
    showToast("Name analysed and inserted as a linked-list node.");
  } catch (error) { showToast(error.message); }
});

async function deleteRecord(id) {
  if (!window.confirm("Delete this record from the linked list and database?")) return;
  try { await api(`/api/records/${id}`, {method:"DELETE"}); await refresh(); showToast("Node deleted successfully."); }
  catch (error) { showToast(error.message); }
}

async function editRecord(id) {
  const record = allRecords.find(item => item.id === id);
  if (!record) return;
  const name = window.prompt("Enter the corrected name:", record.original_name);
  if (name === null) return;
  try {
    await api(`/api/records/${id}`, {method:"PUT", body:JSON.stringify({name})});
    await refresh();
    showToast("Node updated successfully.");
  } catch (error) { showToast(error.message); }
}

document.getElementById("searchInput").addEventListener("input", event => {
  const term = event.target.value.toLowerCase().trim();
  renderRecords(allRecords.filter(r =>
    r.original_name.toLowerCase().includes(term) ||
    String(r.numerology_number).includes(term) ||
    String(r.id).includes(term)
  ));
});

refresh();

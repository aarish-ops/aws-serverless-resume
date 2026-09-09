const API_URL = "https://1w987xptwg.execute-api.us-east-1.amazonaws.com/count";

fetch(API_URL)
  .then(res => res.json())
  .then(data => {
    document.getElementById("visitor-count").innerText = data.count;
  })
  .catch(() => {
    document.getElementById("visitor-count").innerText = "N/A";
  }); 
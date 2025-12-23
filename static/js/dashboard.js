document.getElementById("predictBtn").addEventListener("click", async () => {
    const symptoms = document.getElementById("userSymptoms").value;
    if (!symptoms.trim()) {
        document.getElementById("predictionResult").innerText = "Enter symptoms!";
        document.getElementById("precautionResult").innerText = "";
        return;
    }

    const response = await fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ symptoms: symptoms })
    });

    const data = await response.json();

    document.getElementById("predictionResult").innerText = "Condition: " + data.prediction;
    document.getElementById("precautionResult").innerText = "Precaution: " + data.precaution;
});

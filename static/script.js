// ===============================
// Predict Button Click Event
// ===============================

console.log("script.js loaded successfully!");

document
    .getElementById("predict-btn")
    .addEventListener("click", checkMessage);


// ===============================
// Check Spam Function
// ===============================

async function checkMessage() {

    console.log("Button Clicked!");

    // Read user's message
    const message = document.getElementById("message").value;

    console.log("User Message:", message);

    // Prevent empty message
    if (!message.trim()) {

        alert("Please enter a message.");
        return;

    }

    try {

        console.log("Sending request to Flask...");

        // Send message to Flask
        const response = await fetch("/predict", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: message

            })

        });

        // Show response status
        console.log("Response Status:", response.status);

        // Convert JSON response
        const data = await response.json();

        // Print Flask response
        console.log("Response Data:", data);

        // Result Div
        const resultDiv = document.getElementById("result");

        resultDiv.style.display = "block";

        // Display Result
        if (data.label === "SPAM") {

            resultDiv.className = "spam";

            resultDiv.innerHTML = `
                🚨 SPAM DETECTED!<br>
                <small>Confidence: ${data.confidence}%</small>
            `;

        }

        else {

            resultDiv.className = "safe";

            resultDiv.innerHTML = `
                ✅ SAFE MESSAGE<br>
                <small>Confidence: ${data.confidence}%</small>
            `;

        }

    }

    catch (error) {

        console.error("Error:", error);

        alert("Something went wrong! Please try again.");

    }

}
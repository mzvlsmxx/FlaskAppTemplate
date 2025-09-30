const exampleBtn = document.getElementById("test-btn")

exampleBtn.addEventListener("click", sendDemoData)

function sendData(data) {
    fetch(
        "http://localhost:7777/process_data",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
}

function sendDemoData() {
    const dataToSend = {
        someData: "Some data to process"
    };
    sendData(dataToSend);
}
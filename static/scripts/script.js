const exampleBtn = document.getElementById("test-btn")


exampleBtn.addEventListener("click", sendDemoData)


async function sendDemoData() {
    const dataToSend = {
        someData: "Some data to process"
    };
    await sendData(dataToSend);
}


async function sendData(data) {
    await fetch(
        "/process_data",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
}


async function fetchData() {
    const response = await fetch(
        '/process_data',
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        }
    );
    const data = await response.json();
    console.log(data);
}
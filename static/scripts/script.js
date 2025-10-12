const exampleBtn = document.getElementById("test-btn")
exampleBtn.addEventListener("click", test)


async function test() {
    const dataToSend = {
        someData: "Some data to process"
    };
    await sendData(dataToSend).then(
        () => {
            fetchData().then(
                data => {
                    console.log(data)
                }
            )
        }
    );
}


async function fetchData() {
    const params = new URLSearchParams(
        {
            "query_parameter_1": "some_value",
            "query_parameter_2": "another_value"
        }
    )
    const response = await fetch(
        `/fetch_data?${params.toString()}`,
        {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        }
    );
    return await response.json();
}


async function sendData(data) {
    const params = new URLSearchParams(
        {
            "query_parameter_1": "some_value",
            "query_parameter_2": "another_value"
        }
    )
    await fetch(
        `/process_data?${params.toString()}`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
}
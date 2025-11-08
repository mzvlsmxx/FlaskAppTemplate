export async function fetchData() {
    const params = new URLSearchParams(
        {
            "query_parameter_1": "some_value",
            "query_parameter_2": "another_value"
        }
    );
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


export async function sendData(data) {
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

function testClick(url) {
    fetch(url)
    .then(response => {
        // Check if the response is OK (status code 200)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        // Assuming the response is JSON, you can parse it
        return response.json();
    })
    .then(data => {
        // Do something with the data from the response
        console.log(data);
    })
    .catch(error => {
        // Handle any errors that occur during the fetch operation
        console.error('There was a problem with the fetch operation:', error);
    });
}

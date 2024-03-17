fetch('http://localhost:8001/get_answer', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question: 'Joey played Dr. Drake Ramoray on which soap opera show?' }),
})
.then(response => response.text())
.then(data => console.log(data));


// Joey played Dr. Drake Ramoray on which soap opera show?
// How many times did Ross get divorced?

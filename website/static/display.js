fetch('http://127.0.0.1:5000/admin/api/question/get')
    .then(res => {
        return res.json();
    })
    .then(data => {
        tor = Object.keys(data);
        console.log(data[tor[0]])
        tor.forEach(q =>{
            const markup = `
            <div class="col">
                <div class="card shadow-sm">
                    <svg class="bd-placeholder-img card-img-top" width="50%" height="50" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>wowoow</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em"></text></svg>
                    <div class="card-body">
                        <p class="card-text" id = "context">${data[q]["context"]}</p>
                        <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                            <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                        </div>
                        <small class="text-muted">Replies: </small>
                        </div>
                    </div>
                </div>
            </div>`;
            document.getElementById("questionArea").insertAdjacentHTML("beforeend", markup);
        })
        tor.forEach(q => {
            console.log(data[q]);
        })
    })
    .catch(error => console.log(error))


    
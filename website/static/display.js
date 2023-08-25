//` + window.location.href + `
function addFromAPI(apiURL, adjHtmlID, subjectID){
    fetch(apiURL)
    .then(res => {
        return res.json();
    })
    .then(data => {
        tor = Object.keys(data);
        tor.forEach(q =>{
            if(data[q]["subjectid"] == subjectID){
                const markup = `
                <a href = ` + window.location.href + `/${q}>
                    <div class="col" >
                        <div class="card shadow-sm" style="text-decoration:none; color: #000000;">
                            <svg class="bd-placeholder-img card-img-top" width="50%" height="50" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>wowoow</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em"></text></svg>
                            <div class="card-body">
                                <p class="card-text" id = "context">${data[q]["context"]}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                <small class="text-muted">Replies: </small>
                                </div>
                            </div>
                        </div>
                    </div>
                </a>`;
                document.getElementById(adjHtmlID).insertAdjacentHTML("beforeend", markup);
            }
        })
    })
    .catch(error => console.log(error))

}

function addSubjectsAPI(apiURL, adjHtmlID){
    fetch(apiURL)
    .then(res => {
        return res.json();
    })
    .then(data => {
        tor = Object.keys(data);
        console.log(tor)
        tor.forEach(q =>{
                const markup = `
                <a href = "/${data[q]["Subject"]}">
                    <div class="col" >
                        <div class="card shadow-sm" style="text-decoration:none; color: #000000;">
                            <svg class="bd-placeholder-img card-img-top" width="50%" height="50" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false"><title>wowoow</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em"></text></svg>
                            <div class="card-body">
                                <p class="card-text" id = "context">${data[q]["Subject"]}</p>
                                <div class="d-flex justify-content-between align-items-center">
                                <small class="text-muted">Number of Questions: </small>
                                </div>
                            </div>
                        </div>
                    </div>
                </a>`;
                
                document.getElementById(adjHtmlID).insertAdjacentHTML("beforeend", markup);
        })
    })
    .catch(error => console.log(error))

}


window.onload = function () { 
    addFromAPI('http://127.0.0.1:5000/admin/api/question/get', "questionArea", "CALCAB")
    addSubjectsAPI('http://127.0.0.1:5000/admin/api/subjects/get', "subjectArea")
}


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
                console.log(data[q]);
                const markup = `
                <div class="col-xl-4 col-md-6">

                    <!-- Start Card-->
                    <article class="blog-details">

                    <div class="card border-0 rounded-0 position-relative box-shadow">
        
                        <div class="card-body">
                        <!-- insert Header-->

                        
                            <h5 class="card-title">${data[q]["title"]}</h5>

                        <!-- Insert Date and Author as subtitle of the card-->
                        <h8 class="card-subtitle mb-2 text-muted">on Aug 23, 2023</h8>

                            <p class="card-text">${data[q]["context"]}</p>
                        </br>
                        <a href="blog-details.html" class="btn btn-success" id="${q}">More</a>


                        </div>
                    </div>

                    </article>
                    <!-- End Card -->

                </div><!-- End post list item -->
                `;
                document.getElementById(adjHtmlID).insertAdjacentHTML("beforeend", markup);
                
            }
        })
    })
    .catch(error => console.log(error))

     
}
//${data[q]["context"]}

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
                <div class="col-xl-4 col-md-6">

                    <!-- Start Card-->
                    <article class="blog-details">

                    <div class="card border-0 rounded-0 position-relative box-shadow">
        
                        <div class="card-body">
                        <!-- insert Header-->

                        
                            <h5 class="card-title">Question Header</h5>

                        <!-- Insert Date and Author as subtitle of the card-->
                        <h8 class="card-subtitle mb-2 text-muted">on Aug 23, 2023</h8>

                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                        </br>
                        <a href="blog-details.html" class="btn btn-success">More</a>


                        </div>
                    </div>

                    </article>
                    <!-- End Card -->

                </div><!-- End post list item -->
                `;
                
                document.getElementById(adjHtmlID).insertAdjacentHTML("beforeend", markup);
        })
    })
    .catch(error => console.log(error))

}


window.onload = function () { 
    
    var QID = addFromAPI('http://www.tinotutor.com/admin/api/question/get', "BlogArea", "CALCAB");

    


    document.getElementById('postQuestionButton').onclick = function(){
        //document.getElementById("questionBox").value
        console.log(document.getElementById("postQuestionTitle").value)
        fetch('http://www.tinotutor.com/admin/api/question/post', {
            
            // Declare what type of data we're sending
            headers: {
                'Content-Type': 'application/json'
                
            },

            // Specify the method
            method: 'POST',

            // A JSON payload
            body: JSON.stringify({
                "Title": document.getElementById("postQuestionTitle").value,
                "Question": document.getElementById("postQuestionContext").value
            })
        })
        .then(response => console.log("awjdlbawkl"))
    }
}


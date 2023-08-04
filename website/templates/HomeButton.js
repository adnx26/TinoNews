window.onload = function () {
  function submit(box) {
    console.log("ran");
    var question = document.getElementById(box).value;

    finalQuestionbox(question);
  }

  function finalQuestionbox(q) {
    var element = document.createElement("div");
    element.appendChild(document.createTextNode(q));
    element.id = "out";
    document.getElementById("questions").appendChild(element);
  }

  document.getElementById("submitButton").onclick = function () {
    //document.getElementById("questionBox").value
    fetch("/api/question/post", {
      // Declare what type of data we're sending
      headers: {
        "Content-Type": "application/json",
      },

      // Specify the method
      method: "POST",

      // A JSON payload
      body: JSON.stringify({
        Question: document.getElementById("questionBox").value,
      }),
    })
      .then((response) => console.log("why is this an error"))
      .then((response) => console.log(JSON.stringify(response)));
  };

  document.getElementById("repliesButton").onclick = function () {
    //document.getElementById("questionBox").value
    fetch("/api/replies/post", {
      // Declare what type of data we're sending
      headers: {
        "Content-Type": "application/json",
      },

      // Specify the method
      method: "POST",

      // A JSON payload
      body: JSON.stringify({
        Replies: document.getElementById("replyBox").value,
      }),
    })
      .then((response) => console.log("why is this an error"))
      .then((response) => console.log(JSON.stringify(response)));
  };
};

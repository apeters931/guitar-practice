// to do:
// make it so questions repeat
// keep score (this should happen after we figure out how to make it repeat becuase they will relate to each other)
//  - question number
//  - number correct
//  - percent correct
//  - average answer time
//  - score based on time and correctness
// add difficulty selector
// add it so syntax is less important in answer (how to input will be explained in the instructions section though but i'm not adding instructions till all other modules are done)

var answer;
var title = "Name the notes in ";
var full_title;
var correct_response = "Correct!";
var incorrect_str = "Incorrect: ";
var incorrect_response;
var play_again_message = 'Press enter for next question';
var randIndex;
var flag = true;

function askQuestion() {

    fetch("chords.json")
    .then(response => response.json())
    .then(data => {
        console.log(data.length)
        console.log(data)
        while (flag) {
            randIndex = Math.floor(Math.random() * data.length);
            if (data[randIndex].Multiplier == "1") {
                flag = false
            }
        }
        console.log(randIndex);
        chord = data[randIndex].Chords;
        correct_answer = data[randIndex].Notes;
        full_title = title + chord;
        document.getElementById("main_title").textContent = full_title;
    })
}

function clickFunction(){
    answer = document.getElementById("user_input").value
    incorrect_response = incorrect_str + correct_answer

    if (answer == correct_answer) {
        document.getElementById("message").textContent = correct_response
    }

    else {
        document.getElementById("message").textContent = incorrect_response
    }

    document.getElementById("play_again").textContent = play_again_message

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            console.log("test");
        }
      });

}

window.onload = askQuestion;
document.getElementById("my_submit").onclick = clickFunction;

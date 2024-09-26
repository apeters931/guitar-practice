// to do:
// make it so questions repeat
// keep score (this should happen after we figure out how to make it repeat becuase they will relate to each other)
// add difficulty selector
// add it so syntax is less important in answer (how to input will be explained in the instructions section though but i'm not adding instructions till all other modules are done)

let answer;
let title = "Name the notes in ";
let full_title;
let correct_response = "Correct!";
let incorrect_str = "Incorrect: ";
let incorrect_response;
let randIndex;
let flag = true;

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
    full_title = title.concat(chord);
    document.getElementById("main_title").textContent = full_title;
})


document.getElementById("my_submit").onclick = function(){
    answer = document.getElementById("user_input").value
    incorrect_response = incorrect_str.concat(correct_answer)

    if (answer == correct_answer) {
        document.getElementById("message").textContent = correct_response
    }

    else {
        document.getElementById("message").textContent = incorrect_response
    }
}

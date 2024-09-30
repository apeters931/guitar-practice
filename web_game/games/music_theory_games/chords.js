// to do:
// can only submit answer once -- right now you can click submit multiple times and it keeps counting the answer for that question
// round percentage
// average answer time
// score based on time, correctness, and points multiplier
// add it so syntax is less important in answer (how to input will be explained in the instructions section though but i'm not adding instructions till all other modules are done)

// for developing
// python3 -m http.server
// http://localhost:8000/guitar-practice/web_game/games/music_theory_games/chords.html

var counter = 1;
let correctAnswer = 0;

function gameLoop() {

    var answer;
    var title = "Name the notes in ";
    var full_title;
    var correct_response = "Correct!";
    var incorrect_str = "Incorrect: ";
    var incorrect_response;
    var randIndex;
    var probabilityArray = Array("1","1","1","1","1","1","1","2","2","3") // 70% easy difficulty, 20% medium, 10% hard
    var difficulty;
    var flag = true;
    var clickedFlag = false;
    var correctPercent;
    var question_str = "Question: ";
    var correct_str = "Correct: ";
    var percent_str = "Percentage: ";
    var time_str = "Average time: ";
    var score_str = "Score: ";

    console.log(counter)
    fetch("chords.json")
    .then(response => response.json())
    .then(data => {
        // console.log(data.length)
        // console.log(data)
        console.log(clickedFlag);
        while (flag) {
            difficulty = probabilityArray[Math.floor(Math.random()*probabilityArray.length)];
            // console.log(difficulty)
            randIndex = Math.floor(Math.random() * data.length);
            if (data[randIndex].Multiplier == difficulty) {
                flag = false
            }
        }
        // console.log(randIndex);
        chord = data[randIndex].Chords;
        correct_answer = data[randIndex].Notes;
        full_title = title + chord;
        document.getElementById("main_title").textContent = full_title;

        // set scoreboard
        question_number = question_str + counter.toString();
        document.getElementById("question_num").textContent = question_number;
        if (counter == 1) {
            document.getElementById("correct_num").textContent = correct_str + "--";
            document.getElementById("correct_perc").textContent = percent_str + "--";
        }
        // temp until this is calculated
        document.getElementById("avg_time").textContent = time_str + "--";;
        document.getElementById("scoreboard").textContent = score_str + "--";;
    })

    document.getElementById("my_submit").onclick = function() {
        if (document.getElementById("user_input").value != '') {
            // console.log("clicked");
            // console.log(document.getElementById("user_input").value);
            answer = document.getElementById("user_input").value
            incorrect_response = incorrect_str + correct_answer
            clickedFlag = true;

            if (answer == correct_answer) {
                document.getElementById("message").textContent = correct_response;
                correctAnswer++;
            }

            else {
                document.getElementById("message").textContent = incorrect_response;
            }

            if (correctAnswer > 0) {
                correctPercent = (correctAnswer/counter) * 100;
            }

            else {
                correctPercent = 0;
            }

            // update scoreboard
            question_number = question_str + counter.toString();
            correct_count = correct_str + correctAnswer.toString();
            correct_percentage = percent_str + correctPercent.toString() + "%";
            document.getElementById("question_num").textContent = question_number;
            document.getElementById("correct_num").textContent = correct_count;
            document.getElementById("correct_perc").textContent = correct_percentage;

        }

    }

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && clickedFlag == true) {
            // reset variables
            clickedFlag = false;
            document.getElementById('user_input').value = '';
            document.getElementById('message').textContent = '';
            counter++;
            gameLoop(); 
        }
    });

}

if (counter == 1) {
    gameLoop();
}
// to do:
// keep score (this should happen after we figure out how to make it repeat becuase they will relate to each other)
//  - question number
//  - number correct
//  - percent correct
//  - average answer time
//  - score based on time, correctness, and points multiplier
// add it so syntax is less important in answer (how to input will be explained in the instructions section though but i'm not adding instructions till all other modules are done)

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
    var question_str = "Number of questions: ";
    var correct_str = "Number correct: ";
    var percent_str = "Correct percentage: ";
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
                correctPercent = correctAnswer/counter;
            }

            else {
                correctPercent = 0;
            }

            // set scoreboard
            question_number = question_str + counter.toString();
            correct_count = correct_str + correctAnswer.toString();
            correct_percentage = percent_str + correctPercent.toString();
            average_time = "Average time: 0";
            total_score = "Score: 0";
            document.getElementById("question_num").textContent = question_number;
            document.getElementById("correct_num").textContent = correct_count;
            document.getElementById("correct_perc").textContent = correct_percentage;
            document.getElementById("avg_time").textContent = average_time;
            document.getElementById("scoreboard").textContent = total_score;

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
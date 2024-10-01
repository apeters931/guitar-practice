// to do:
// score based on time, correctness, and points multiplier
// - x 2 if you're answer time is less than you're median time
// move score down so it won't move when the correct/incorrect message appears
// add instructions window when you first open game
// move logic to it's own function to make game flow more obvious

// for developing
// python3 -m http.server
// http://localhost:8000/guitar-practice/web_game/games/music_theory_games/chords.html

var counter = 1;
let correctAnswer = 0;
var avgTimeList = [];
var score = 0;

function gameLoop() {

    var answer;
    var answerCleaned;
    var correct_answer;
    var correctAnswerCleaned;
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
    var avgTime;
    let time = 0;
    var timerElement;
    var countUp;

    fetch("chords.json")
    .then(response => response.json())
    .then(data => {
        while (flag) {
            difficulty = probabilityArray[Math.floor(Math.random()*probabilityArray.length)];
            randIndex = Math.floor(Math.random() * data.length);
            if (data[randIndex].Multiplier == difficulty) {
                flag = false
            }
        }
        chord = data[randIndex].Chords;
        correct_answer = data[randIndex].Notes;
        correctAnswerCleaned = standardize_string(correct_answer);
        full_title = title + chord;
        document.getElementById("main_title").textContent = full_title;

        // timer
        timerElement = document.getElementById("timer")
        countUp = setInterval(() => {
            time++;
            timerElement.textContent = time;

        },1000);

        // set scoreboard
        question_number = question_str + counter.toString();
        if (counter == 1) {
            document.getElementById("scoreboard").textContent = score_str + "--";;
            document.getElementById("score_line_1").textContent = question_number + ", " + correct_str + "--" +  ", " + percent_str + "--" +  ", " + time_str + "--";
        }
        
    })

    document.getElementById("my_submit").onclick = function() {
        if (document.getElementById("user_input").value != '') {
            pausedTime = time;
            avgTimeList.push(pausedTime);
            avgTime = avg_array(avgTimeList);
            clearInterval(countUp);
            answer = document.getElementById("user_input").value;
            answerCleaned = standardize_string(answer);
            incorrect_response = incorrect_str + format_answer(correct_answer);
            clickedFlag = true;

            //console.log(ans)

            if (answerCleaned == correctAnswerCleaned) {
                document.getElementById("message").textContent = correct_response;
                correctAnswer++;
                score = score + (100 * parseInt(difficulty));
            }

            else {
                document.getElementById("message").textContent = incorrect_response;
                score = score - 100;
            }

            if (correctAnswer > 0) {
                correctPercent = ((correctAnswer/counter) * 100).toFixed(2);
            }

            else {
                correctPercent = 0;
            }

            // update scoreboard
            if (counter >= correctAnswer) {
                question_number = question_str + counter.toString();
                correct_count = correct_str + correctAnswer.toString();
                correct_percentage = percent_str + correctPercent.toString() + "%";
                average_time_string = time_str + avgTime + "s";
                total_score = score_str + score.toString();
                document.getElementById("scoreboard").textContent = total_score;
                document.getElementById("score_line_1").textContent = question_number + ", " + correct_count + ", " + correct_percentage + ", " + average_time_string;
            }

        }

    }

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && clickedFlag == true) {
            // reset variables
            time = 0;
            clickedFlag = false;
            document.getElementById('user_input').value = '';
            document.getElementById('message').textContent = '';
            counter++;
            gameLoop(); 
        }
    });

}

// find average for items in array
function avg_array(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return (sum / arr.length).toFixed(2);
}

// make string lowercase and comma seperated
function standardize_string(str){
    let lowerStr = str.toLowerCase();
    let standardizedStr = lowerStr.replaceAll(" ",",")
    return standardizedStr
}

// format answer string for screen
function format_answer(str){
    let answer  = str.replaceAll(",",", ")
    return answer
}

if (counter == 1) {
    gameLoop();
}
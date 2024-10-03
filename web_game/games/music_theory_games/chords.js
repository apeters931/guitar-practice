// to do:
// score variable going up if you hit the submit button
// add timed version
// add set number of questions version

// for developing:
// python3 -m http.server
// http://localhost:8000/guitar-practice/web_game/games/music_theory_games/chords.html

// game variables used for score
var counter = 1;
var correctAnswer = 0;
var correctPercent;
var avgTimeList = [];
var avgTime;
var medianTimeList = [];
var score = 0;

// function for each question
function gameLoop() {
    // set variables
    var answer;
    var answerCleaned;
    var correct_answer;
    var correctAnswerCleaned;
    var title = "What notes are in ";
    var full_title;
    var correct_response = "Correct!";
    var incorrect_str = "Incorrect: ";
    var incorrect_response;
    var randIndex;
    var probabilityArray = Array("1","1","1","1","1","1","1","2","2","3") // 70% easy difficulty, 20% medium, 10% hard
    var difficulty;
    var flag = true;
    var clickedFlag = false;
    let time = 0;
    var timerElement;
    var countUp;

    // read JSON data
    fetch("chords.json")
    .then(response => response.json())
    .then(data => {
        // loop through until a chord is found that is the correct difficulty
        while (flag) {
            // pick random item in probability array to be used as difficulty
            difficulty = probabilityArray[Math.floor(Math.random()*probabilityArray.length)];
            // pick a random chord from th data
            randIndex = Math.floor(Math.random() * data.length);
            // if the chord is the right difficulty stop looping
            if (data[randIndex].Multiplier == difficulty) {
                flag = false
            }
        }
        // get chord name from JSON
        chord = data[randIndex].Chords;
        // get notes in chord from JSON
        correct_answer = data[randIndex].Notes;
        // format string to be consistent for comparing
        correctAnswerCleaned = standardize_string(correct_answer);
        // create title w/ chord name and add it to screen
        full_title = title + chord;
        document.getElementById("main_title").textContent = full_title;

        // timer
        timerElement = document.getElementById("timer")
        countUp = setInterval(() => {
            time++;
            timerElement.textContent = time;

        },1000);

        // set scoreboard
        generate_score(counter,correctAnswer,correctPercent,avgTime,score);
        
    })

    // triggers when button gets clicked
    document.getElementById("my_submit").onclick = function() {
        // need to have input for button clicked logic to run
        if (document.getElementById("user_input").value != '') {
            // get the time the submit button was pressed
            pausedTime = time;
            // add time to average time array
            avgTimeList.push(pausedTime);
            // add time to median time array
            medianTimeList.push(pausedTime);
            // calculate average and median times
            avgTime = avg_array(avgTimeList);
            medianTime = median(medianTimeList);
            // stop the timer
            clearInterval(countUp);
            // get user's answer
            answer = document.getElementById("user_input").value;
            // convert to standard format for comparing
            answerCleaned = standardize_string(answer);
            // create string for incorrect response by concatenating the correct answer
            incorrect_response = incorrect_str + format_answer(correct_answer);
            // set flag to true that the button has been clicked
            clickedFlag = true;
            
            // checks if input answer is equal to the correct answer from the data
            if (answerCleaned == correctAnswerCleaned) {
                // add correct message to screen
                document.getElementById("message").textContent = correct_response;
                document.getElementById("message").style.color = "white";
                // adds one to the correct answer variable
                correctAnswer++;
                // adds 100 x the difficulty multiplier to the score variable
                score = score + (100 * parseInt(difficulty));
                // adds an addition 100 in the answer time was less than the median answer time
                if (pausedTime < medianTime) {
                    score = score + 100;
                }
            }

            // when answer is not correct
            else {
                // adds incorrect message to screen
                document.getElementById("message").textContent = incorrect_response;
                document.getElementById("message").style.color = "white";
                // subtracts 100 from score
                score = score - 100;
            }

            // calculate correct percentage - MAKE FUNCTION
            correctPercent = correct_percent(correctAnswer,counter);

            // update scoreboard
            generate_score(counter,correctAnswer,correctPercent,avgTime,score);

        }

    }

    // trigger when the enter key is clicked
    document.addEventListener('keydown', function(event) {
        // only want enter key to do anything when the subit button was already clicked
        if (event.key === 'Enter' && clickedFlag == true) {
            // reset variables
            time = 0;
            clickedFlag = false;
            document.getElementById('user_input').value = '';
            document.getElementById("message").style.color = "#2c3135";
            document.getElementById('message').textContent = 'placeholder';
            // add one to the counter
            counter++;
            // start from beging of game loop
            gameLoop(); 
        }
    });

}

// create scoreboard
function generate_score(count,countCorrect=0,perecent=0,average=0,totalScore=0){
    // labels for scores
    var question_str = "Question: ";
    var correct_str = "Correct: ";
    var percent_str = "Percentage: ";
    var time_str = "Average time: ";
    var score_str = "Score: ";

    if (count == 1) {
        question_number = question_str + count.toString();
        document.getElementById("scoreboard").textContent = score_str + "--";;
        document.getElementById("score_line_1").textContent = question_number + ", " + correct_str + "--" +  ", " + percent_str + "--" +  ", " + time_str + "--";
    }

    else if (counter >= correctAnswer) {
        question_number = question_str + counter.toString();
        correct_count = correct_str + correctAnswer.toString();
        correct_percentage = percent_str + correctPercent.toString() + "%";
        average_time_string = time_str + avgTime + "s";
        total_score = score_str + totalScore.toString();
        document.getElementById("scoreboard").textContent = total_score;
        document.getElementById("score_line_1").textContent = question_number + ", " + correct_count + ", " + correct_percentage + ", " + average_time_string;
    }
}

// calculate correct percentage
function correct_percent(countCorrect,count){
    if (countCorrect > 0) {
        return ((countCorrect/count) * 100).toFixed(2);
    }

    else {
        return 0;
    }
}

// find average for items in array
function avg_array(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return (sum / arr.length).toFixed(2);
}

function median(arr) {
    // Sort the array in ascending order
    arr.sort((a, b) => a - b);
  
    // Check if the array length is even or odd
    if (arr.length % 2 === 0) {
      // If even, return the average of the two middle elements
      const mid1 = arr[arr.length / 2 - 1];
      const mid2 = arr[arr.length / 2];
      return (mid1 + mid2) / 2;
    } else {
      // If odd, return the middle element
      return arr[Math.floor(arr.length / 2)];
    }
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

function closePopup() {
    var popup = document.getElementById("popup");
    popup.classList.add("close-popup");
}

function hideObjects() {
    var user_input = document.getElementById("user_input");
    var my_submit = document.getElementById("my_submit");
    var timer = document.getElementById("timer");
    user_input .classList.add("hide-objects");
    my_submit.classList.add("hide-objects");
    timer.classList.add("hide-objects");
}

function unhideObjects() {
    var user_input = document.getElementById("user_input");
    var my_submit = document.getElementById("my_submit");
    var timer = document.getElementById("timer");
    user_input .classList.remove("hide-objects");
    my_submit.classList.remove("hide-objects");
    timer.classList.remove("hide-objects");
}

document.getElementById("play").onclick = function() {
    unhideObjects()
    gameLoop();
    closePopup();
}

hideObjects();
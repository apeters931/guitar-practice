// game variables used for score
var counter = 1;
var clickCount = 0;
var correctAnswer = 0;
var correctPercent;
var avgTimeList = [];
var avgTime;
var medianTimeList = [];
var score = 0;
let countDownTime = 101;
var gameTest;

// function for each question
function gameLoop(gameType) {
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
    var flag = true;
    var clickedFlag = false;
    let time = 0;
    var timerElement;
    var countUp;
    var countDown;

    // read JSON data
    fetch("../../../json/modes.json")
    .then(response => response.json())
    .then(data => {
        randIndex = Math.floor(Math.random() * data.length);
        // get key name from JSON
        key = data[randIndex].ROOT + ' ' + data[randIndex].MODE;
        // get notes in key from JSON
        correct_answer = data[randIndex].NOTES;
        // format string to be consistent for comparing
        correctAnswerCleaned = standardize_string(correct_answer);
        // create title w/ key name and add it to screen
        full_title = title + key;
        document.getElementById("main_title").textContent = full_title;

        // timer
        if (gameType == 'timed') {
            if (counter == 1) {
                timerElement = document.getElementById("timer")
                countDown = setInterval(() => {
                    countDownTime--;
                    timerElement.textContent = countDownTime;
                    if (countDownTime == 0) {
                        hideObjects()
                        generate_score(counter,correctAnswer,correctPercent,avgTime,score,true,true);
                        closePopup("gameover");
                        clearInterval(countDown)
                        document.getElementById("play-again").onclick = function() {
                            playAgain('timed')
                        }
                    }
        
                },1000);
            }
        }
        else {
            timerElement = document.getElementById("timer")
            countUp = setInterval(() => {
                time++;
                timerElement.textContent = time;
    
            },1000);
        }

        // set scoreboard
        if (gameType == 'timed') {
            generate_score(counter,correctAnswer,correctPercent,avgTime,score,false,true);
        }
        else {
            generate_score(counter,correctAnswer,correctPercent,avgTime,score);
        }
        
    })

    // triggers when button gets clicked
    document.getElementById("my_submit").onclick = function() {
        clickCount++;
        // need to have input for button clicked logic to run
        if (document.getElementById("user_input").value != '' && clickCount == 1) {
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
            if (gameType != 'timed') {
                clearInterval(countUp);
            }
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
                // adds 100
                score = score + 100;
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
            if (gameType == 'timed') {
                generate_score(counter,correctAnswer,correctPercent,avgTime,score,false,true);
            }
            else {
                generate_score(counter,correctAnswer,correctPercent,avgTime,score);
            }

        }

    }

    // trigger when the enter key is clicked
    document.addEventListener('keydown', function(event) {
        // only want enter key to do anything when the subit button was already clicked
        if (event.key === 'Enter' && clickedFlag == true) {
            if (counter == 20 && gameType == 'test'){
                hideObjects()
                generate_score(counter,correctAnswer,correctPercent,avgTime,score,true);
                clearInterval(countUp);
                closePopup("gameover");
                document.getElementById("play-again").onclick = function() {
                    playAgain('test');
                    generate_score(counter,correctAnswer,correctPercent,avgTime,score);
                }
            }
            // reset variables
            if (gameType != 'timed') {
                time = 0;
            }
            clickedFlag = false;
            clickCount = -1;
            document.getElementById('user_input').value = '';
            document.getElementById("message").style.color = "#2c3135";
            document.getElementById('message').textContent = 'placeholder';
            // add one to the counter
            counter++;
            // start from beging of game loop
            gameLoop(gameType); 
        }
    });

}

// create scoreboard
function generate_score(count,countCorrect=0,perecent=0,average=0,totalScore=0,gameOver=false,timed=false){
    // labels for scores
    var question_str = "Question: ";
    var correct_str = "Correct: ";
    var percent_str = "Percentage: ";
    var time_str = "Average time: ";
    var score_str = "Score: ";

    if (count == 1) {
        question_number = question_str + count.toString();
        document.getElementById("scoreboard").textContent = score_str + "--";
        if (timed) {
            document.getElementById("score_line_1").textContent = question_number + ", " + correct_str + "--" +  ", " + percent_str + "--";
        }
        else {
            document.getElementById("score_line_1").textContent = question_number + ", " + correct_str + "--" +  ", " + percent_str  + "--" +  ", " + time_str + "--";
        }
    }

    else if (counter >= correctAnswer) {
        question_number = question_str + counter.toString();
        correct_count = correct_str + correctAnswer.toString();
        correct_percentage = percent_str + correctPercent.toString() + "%";
        average_time_string = time_str + avgTime + "s";
        total_score = score_str + totalScore.toString();
        document.getElementById("scoreboard").textContent = total_score;
        if (timed) {
            document.getElementById("score_line_1").textContent = question_number + ", " + correct_count + ", " + correct_percentage;
        }
        else {
            document.getElementById("score_line_1").textContent = question_number + ", " + correct_count + ", " + correct_percentage + ", " + average_time_string;
        }
    }

    if (gameOver && count == 1) {
        question_number = question_str + count.toString();
        document.getElementById("final-score").textContent = score_str + "--";
        if (timed) {
            document.getElementById("final-score-details").textContent = question_number + ", " + correct_str + "--" +  ", " + percent_str + "--";
        }
        else {
            document.getElementById("final-score-details").textContent = question_number + ", " + correct_str + "--" +  ", " + percent_str + "--" +  ", " + time_str + "--";
        }
    }
    else if (gameOver) {
        question_number = question_str + counter.toString();
        correct_count = correct_str + correctAnswer.toString();
        correct_percentage = percent_str + correctPercent.toString() + "%";
        average_time_string = time_str + avgTime + "s";
        total_score = score_str + totalScore.toString();
        document.getElementById("final-score").textContent = total_score;
        if (timed) {
            document.getElementById("final-score-details").textContent = question_number + ", " + correct_count + ", " + correct_percentage;
        }
        else {
            document.getElementById("final-score-details").textContent = question_number + ", " + correct_count + ", " + correct_percentage + ", " + average_time_string;
        }
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

function closePopup(type) {
    if (type == 'instructions') {
        var popup = document.getElementById("popup");
        popup.classList.add("close-popup");
    }

    else if (type == 'gameover') {
        var gameover_popup = document.getElementById("game-over-popup");
        gameover_popup.classList.add("popup");
        gameover_popup.classList.remove("close-popup");
    }

    else if (type == 'gameover-close') {
        var gameover_popup = document.getElementById("game-over-popup");
        gameover_popup.classList.add("close-popup");
    }
}

function hideObjects() {
    var main_title = document.getElementById("main_title");
    var user_input = document.getElementById("user_input");
    var my_submit = document.getElementById("my_submit");
    var timer = document.getElementById("timer");
    var scoreboard = document.getElementById("scoreboard");
    var score_line_1 = document.getElementById("score_line_1");
    main_title.classList.add("hide-objects");
    user_input.classList.add("hide-objects");
    my_submit.classList.add("hide-objects");
    timer.classList.add("hide-objects");
    scoreboard.classList.add("hide-objects");
    score_line_1.classList.add("hide-objects");
}

function unhideObjects() {
    var main_title = document.getElementById("main_title");
    var user_input = document.getElementById("user_input");
    var my_submit = document.getElementById("my_submit");
    var timer = document.getElementById("timer");
    var scoreboard = document.getElementById("scoreboard");
    var score_line_1 = document.getElementById("score_line_1");
    main_title.classList.remove("hide-objects");
    user_input .classList.remove("hide-objects");
    my_submit.classList.remove("hide-objects");
    timer.classList.remove("hide-objects");
    scoreboard.classList.remove("hide-objects");
    score_line_1.classList.remove("hide-objects");
}

function playAgain(gameType) {
    if (gameType == 'timed') {
        counter = 1;
        countDownTime = 10;
        unhideObjects();
        gameLoop('timed');
        closePopup('gameover-close');
    }

    else if (gameType == 'test') {
        counter = 1;
        correctAnswer = 0;
        correctPercent;
        avgTimeList = [];
        avgTime;
        medianTimeList = [];
        score = 0;
        unhideObjects();
        closePopup('gameover-close');
    }
}

document.getElementById("play-infinite").onclick = function() {
    unhideObjects();
    gameLoop('infinite');
    closePopup('instructions');
}

document.getElementById("play-timed").onclick = function() {
    unhideObjects();
    gameLoop('timed');
    closePopup('instructions');
}

document.getElementById("play-test").onclick = function() {
    var gameTest = true;
    unhideObjects();
    gameLoop('test');
    closePopup('instructions');
}

hideObjects();

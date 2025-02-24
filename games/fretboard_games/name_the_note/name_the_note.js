// keys
keys = [
    ['a','b','c#/db','d','e','f#/gb','g#/ab'],
    ['a#/bb','c','d','d#/eb','f','g','a'],
    ['b','c#/db','d#/eb','e','f#/gb','g#/ab','a#/bb'],
    ['c','d','e','f','g','a','b'],
    ['c#/db','d#/eb','f','f#/gb','g#/ab','a#/bb','c'],
    ['d','e','f#/gb','g','a','b','c#/db'],
    ['d#/eb','f','g','g#/ab','a#/bb','c','d'],
    ['e','f#/gb','g#/ab','a','b','c#/db','d#/eb'],
    ['f','g','a','a#/bb','c','d','e'],
    ['f#/gb','g#/ab','a#/bb','b','c#/db','d#/eb','f'],
    ['g','a','b','c','d','e','f#/gb'],
    ['g#/ab','a#/bb','c','c#/db','d#/eb','f','g'],
    ['a','a#/bb','b','c','c#/db','d','d#/eb','e','f','f#/gb','g','g#/ab']
];

var counter = 1;
var clickCount = 0;
var correctAnswer = 0;
var correctPercent;
var avgTimeList = [];
var avgTime;
var medianTimeList = [];
var score = 0;
var randIndex;

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

function closePopup(type) {
    if (type == 'instructions') {
        var popup = document.getElementById("popup");
        popup.classList.add("close-popup");
    }
}

function hideObjects() {
    var container = document.getElementById("container");
    container.classList.add("hide-objects");
}

function unhideObjects() {
    var container = document.getElementById("container");
    container.classList.remove("hide-objects");
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

function correct_percent(countCorrect,count){
    if (countCorrect > 0) {
        return ((countCorrect/count) * 100).toFixed(2);
    }

    else {
        return 0;
    }
}

function gameLoop(gameType) {

    var dot = document.getElementById("dot");
    var clickedFlag = false;
    var time = 0;
    var minFret = document.getElementById("start-fret").value;
    var maxFret = document.getElementById("end-fret").value;
    var key = document.getElementById("key").value;
    var strings = [];
    if (document.getElementById("all").checked){ 
       strings = ['e-low','a','d','g','b','e-high'];
    }

    else {
        if (document.getElementById("e-low").checked) {
            strings.push(document.getElementById("e-low").value)
        }
        if (document.getElementById("a").checked) {
            strings.push(document.getElementById("a").value)
        }
        if (document.getElementById("d").checked) {
            strings.push(document.getElementById("d").value)
        }
        if (document.getElementById("g").checked) {
            strings.push(document.getElementById("g").value)
        }
        if (document.getElementById("b").checked) {
            strings.push(document.getElementById("b").value)
        }
        if (document.getElementById("e-high").checked) {
            strings.push(document.getElementById("e-high").value)
        }
    }

    if (strings.length == 0) {
        strings = ['e-low','a','d','g','b','e-high'];
    }

    fetch("../../../json/fretboard.json")
    .then(response => response.json())
    .then(data => {
        var flag = true;
        while (flag) {
            randIndex = Math.floor(Math.random() * data.length);
            if (parseInt(data[randIndex].Fret) >= minFret && parseInt(data[randIndex].Fret) <= maxFret && strings.includes(data[randIndex].String) && keys[key].includes(data[randIndex].Note)) {
                flag = false;
            }
        }
        console.log(keys[key]);
        console.log(data[randIndex].Note);
        flag = true;
        note = data[randIndex].Note;
        toppx = data[randIndex].Top + "px";
        leftpx = data[randIndex].Left + "px";
        dot.style.top = toppx; // Set the top position
        dot.style.left = leftpx; // Set the left position

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

    document.getElementById("my-submit").onclick = function() {
        clickCount++;
        // need to have input for button clicked logic to run
        if (document.getElementById("user-input").value != '' && clickCount == 1) {
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
            answer = document.getElementById("user-input").value;
            clickedFlag = true;
            if (answer == note) {
                console.log("correct");
                document.getElementById("message").textContent = "Correct";
                document.getElementById("message").style.color = "white";
                correctAnswer++;
                // adds 100 x the difficulty multiplier to the score variable
                score = score + 100;
                // adds an addition 100 in the answer time was less than the median answer time
                if (pausedTime < medianTime) {
                    score = score + 100;
                }
            }
            else {
                console.log("incorrect");
                document.getElementById("message").textContent = "Incorrect";
                document.getElementById("message").style.color = "white";
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

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && clickedFlag == true) {
            // reset vars
            clickedFlag = false;
            clickCount = -1;
            document.getElementById('user-input').value = '';
            document.getElementById("message").style.color = "#2c3135";
            document.getElementById('message').textContent = 'placeholder';
            // add one to the counter
            counter++;
            gameLoop()
        }
    })
}

document.getElementById("play-button").onclick = function() {
    unhideObjects();
    closePopup('instructions');
    gameLoop('infinite');
}

hideObjects();
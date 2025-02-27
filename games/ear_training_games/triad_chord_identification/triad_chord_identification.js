var root;
var third;
var fifth;
var minorThird;
var majorThird;
var perfectFifth;
var flatFifth;
var sharpFifth;
var randIndex;
var filePrefix = '../mp3/';
var fileSuffix = '.mp3';
var rootSound;
var thirdSound;
var fifthSound;
var triadRoot;
var triadThird;
var triadFifth;
var answer;

fetch("../../../json/intervals.json")
.then(response => response.json())
.then(data => {
    randIndex = Math.floor(Math.random() * data.length);
    root = filePrefix + data[randIndex].root_id + fileSuffix;
    majorThird = filePrefix + data[randIndex].third + fileSuffix;
    minorThird = filePrefix + data[randIndex].minor_third + fileSuffix;
    perfectFifth = filePrefix + data[randIndex].fifth + fileSuffix;
    flatFifth = filePrefix + data[randIndex].flat_fifth + fileSuffix;
    sharpFifth = filePrefix + data[randIndex].sharp_fifth + fileSuffix;
    

    let randomNumber = Math.random();
    if (randomNumber < 0.25) {
        third = majorThird
        fifth = perfectFifth
        answer = 'major';
    }
    else if (randomNumber >= 0.25 && randomNumber < 0.5) {
        third = minorThird
        fifth = perfectFifth
        answer = 'minor';
    }
    else if (randomNumber >= 0.5 && randomNumber < 0.75) {
        third = majorThird
        fifth = sharpFifth
        answer = 'aug';
    }
    else {
        third = minorThird
        fifth = flatFifth
        answer = 'dim';
    }

    rootSound = new Audio(root);
    thirdSound = new Audio(third);
    fifthSound = new Audio(fifth);
    triadRoot = new Audio(root);;
    triadThird = new Audio(third);
    triadFifth = new Audio(fifth);

    document.getElementById("root").onclick = function() {
        console.log(root);
        rootSound.play();
    }
    document.getElementById("third").onclick = function() {
        console.log(third);
        thirdSound.play();
    }
    document.getElementById("fifth").onclick = function() {
        console.log(fifth);
        fifthSound.play();
    }
    document.getElementById("triad").onclick = function() {
        triadRoot.play(); triadThird.play(); triadFifth.play();
    }

    document.getElementById("major").onclick = function() {
        if (answer == 'major') {
            document.getElementById("results").textContent = "Correct!";
        }
        else {
            document.getElementById("results").textContent = "Incorrect";
        }
    }

    document.getElementById("minor").onclick = function() {
        if (answer == 'minor') {
            document.getElementById("results").textContent = "Correct!";
        }
        else {
            document.getElementById("results").textContent = "Incorrect";
        }
    }

    document.getElementById("aug").onclick = function() {
        if (answer == 'aug') {
            document.getElementById("results").textContent = "Correct!";
        }
        else {
            document.getElementById("results").textContent = "Incorrect";
        }
    }

    document.getElementById("dim").onclick = function() {
        if (answer == 'dim') {
            document.getElementById("results").textContent = "Correct!";
        }
        else {
            document.getElementById("results").textContent = "Incorrect";
        }
    }

});
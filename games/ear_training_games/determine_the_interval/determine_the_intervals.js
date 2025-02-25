var root;
var rootSound;
var third;
var minorThird;
var intervalNote;
var randIndex;
var noteSound;
var intervalRootSound;
var intervalNoteSound;
var filePrefix = '../mp3/';
var fileSuffix = '.mp3';
var interval;

fetch("../../../json/intervals.json")
.then(response => response.json())
.then(data => {
    randIndex = Math.floor(Math.random() * data.length);
    root = filePrefix + data[randIndex].root_id + fileSuffix;
    third = filePrefix + data[randIndex].third + fileSuffix;
    minorThird = filePrefix + data[randIndex].minor_third + fileSuffix;

    let randomNumber = Math.random();
    if (randomNumber >= 0.5) {
        intervalNote = minorThird;
        interval = 'minor 3rd'
    }
    else {
        intervalNote = third;
        interval = 'major 3rd'
    }

    rootSound = new Audio(root);
    intervalRootSound = new Audio(root);
    noteSound = new Audio(intervalNote);
    intervalNoteSound = new Audio(intervalNote);

    document.getElementById("root").onclick = function() {
        console.log(root);
        rootSound.play();
    }
    document.getElementById("interval-note").onclick = function() {
        console.log(intervalNote);
        noteSound.play();
    }
    document.getElementById("interval").onclick = function() {
        console.log(root);
        console.log(intervalNote);
        intervalRootSound.play(); intervalNoteSound.play();
    }

    document.getElementById("min-button").onclick = function() {
        if (interval == 'minor 3rd') {
            document.getElementById("results").textContent = "Correct!";
        }
        else {
            document.getElementById("results").textContent = "Incorrect";
        }
    }

    document.getElementById("maj-button").onclick = function() {
        if (interval == 'major 3rd') {
            document.getElementById("results").textContent = "Correct!";
        }
        else {
            document.getElementById("results").textContent = "Incorrect";
        }
    }

});
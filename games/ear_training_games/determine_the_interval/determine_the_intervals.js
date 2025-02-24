var root;
var intervalNote;

fetch("../../../json/intervals.json")
.then(response => response.json())
.then(data => {
    randIndex = Math.floor(Math.random() * data.length);
    root = data[randIndex].root_id;
    intervalNote = data[randIndex].third
});
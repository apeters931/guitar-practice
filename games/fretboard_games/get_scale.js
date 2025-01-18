var randIndex;
var scale;
var scaleName;
var type;
var scaleArray;
var returnArray = [];

function get_scale() {
    fetch("scales.json")
    .then(response => response.json())
    .then(data => {
        randIndex = Math.floor(Math.random() * data.length);
        scale = data[randIndex].SCALE;
        scaleArray = scale.split(',');
        returnArray.push(scaleArray);
        scaleName = data[randIndex].NAME;
        returnArray.push(scaleName);
        type = data[randIndex].TYPE;
        returnArray.push(type);

        return returnArray;
    });
}

export { get_scale };
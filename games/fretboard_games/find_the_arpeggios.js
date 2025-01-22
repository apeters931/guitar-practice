    var randIndex;
    var scale;
    var note;
    var scaleName;
    var type;
    var scaleArray;
    var returnArray = [];
    var difficulty;
    var flag = true;
    var probabilityArray = ["1","1","1","1","1","1","1","1","1","1","1","1","2","2","3"];
    
    
    fetch("chords.json")
    .then(response => response.json())
    .then(data => {
        // loop through until a chord is found that is the correct difficulty
        //while (flag) {
            // pick random item in probability array to be used as difficulty
            difficulty = probabilityArray[Math.floor(Math.random()*probabilityArray.length)];
            // pick a random chord from th data
            randIndex = Math.floor(Math.random() * data.length);
            // if the chord is the right difficulty stop looping
            if (data[randIndex].Multiplier == difficulty) {
                flag = false
            }
        //}
        scale = data[randIndex].Notes;
        scaleArray = scale.split(',');
        returnArray.push(scaleArray);
        note = data[randIndex].Chords;
        returnArray.push(note);

        // initialize variables
        let x;
        let y;
        const canvas = document.getElementById("myCanvas");
        const ctx = canvas.getContext("2d");
        canvas.width = 110;
        canvas.height = 650;
        var key = returnArray[0];
        var keyNote = returnArray[1];
        var keyType = returnArray[3];
        var keyScaleName = returnArray[2];
        var lowerKey = key.map(key => key.toLowerCase());
        console.log(note);
        document.getElementById("main_title").textContent = note;
        console.log(lowerKey);

        // MAIN GAME LOGIC
        // read JSON fretboard data
        fetch("fretboard.json")
        .then(response => response.json())
        .then(data => {
            // save JSON data as fretboard
            let fretboard = data;
            // draw guitar neck on load
            const img = new Image();
            img.src = "images/guitar_neck_vertical.png";
            img.addEventListener("load", function(){
                ctx.drawImage(img, 0, 0, 110, 650)
            })
            // find location of clicks
            canvas.addEventListener("click", function(event){
                // gets x & y cordinates for click position
                x = event.offsetX;
                y = event.offsetY;
                // gets cordinates for closest note
                let final_xy = findClosestNote(x, y, fretboard)
                // draws dot using the closest note cordinates
                var color;
                var noteClickedArray = []
                if (final_xy[2].length == 5) {
                    noteClickedArray = final_xy[2].split('/');
                    // console.log(noteClickedArray);
                    // console.log(lowerKey);
                    if (lowerKey.includes(noteClickedArray[0]) || lowerKey.includes(noteClickedArray[1])) {
                        color = '#47ca7c';
                    }
                    else {
                        color = '#ff0000';
                    }
                }
                else {
                    if (lowerKey.includes(final_xy[2])) {
                        color = '#47ca7c';
                    }
                    else {
                        color = '#ff0000';
                    }
                }
                ctx.fillStyle = color;
                ctx.beginPath();
                ctx.arc(final_xy[0], final_xy[1], 4, 0, Math.PI*2);
                ctx.fill();
                ctx.stroke;
                //e.log(final_xy[2])
            });
            // clear dots when the backspacen key is pressed
            document.addEventListener("keydown", function(event){
                if (event.key == 'Backspace') {
                    ctx.clearRect(0, 0, 110, 650);
                    ctx.drawImage(img, 0, 0, 110, 650)
                }
            });
        });
    });

    // HELPER FUNCTIONS
    // function to find closet note cordinates from where a user clicked
    function findClosestNote(clicked_x, clicked_y, json) {
        // initialize varibles
        let differenceX = [];
        let differenceY = [];
        let differenceCombined = [];
        let minDifference;
        let minIndex;
        let xi;
        let yi;
        let finalCords = [];
        // loop through JSON data
        for (let i = 0; i < json.length; i++) {
            // find difference between the user input and the cordinates in the JSON for that index
            let obj = json[i];
            xi = parseFloat(obj.x);
            yi = parseFloat(obj.y);
            differenceX.push(Math.abs(clicked_x - xi));
            differenceY.push(Math.abs(clicked_y - yi));
            // add together the differences of the cordinates 
            differenceCombined.push(differenceX[i] + differenceY[i]);
        }
        // calculate what the minimum combined difference is
        minDifference = Math.min(...differenceCombined);
        // loop through and find the index of the minimum combined difference
        for (let i = 0; i < differenceCombined.length; i++) {
            if (differenceCombined[i] == minDifference) {
                minIndex = i;
            }
        }
        // return the JSON x and y at that index
        finalCords.push(json[minIndex].x);
        finalCords.push(json[minIndex].y);
        finalCords.push(json[minIndex].Note);
        return finalCords
    }
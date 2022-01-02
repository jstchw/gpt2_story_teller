let counter = 0
let local_srv = "http://localhost:8000/"

let memeArray = []

let currentIndex = 0

populateMemeArray()
loadMore()


// Load more function gets the array length and hides the button if there's nothing to load (shouldn't be a problem to a meme generator)
// When a button is clicked, the for loop appends an image from an array which is populated beforehand

function loadMore() {
    let maxResult = 1

    if(currentIndex >= memeArray.length) {
        $("#lmbutton").hide()
        return
    }

    for(let i = 0; i < maxResult; i++) {
        $("#content").append("<div>" + "<img src='" + memeArray[i+currentIndex].src + "' />" + "</div>")
    }
    currentIndex += maxResult
}

// Function to populate the array with images located in a specific folder
// The loop iterates through numbers and loads an image to an array slot with an according number
function populateMemeArray() {
    for(let i = 0; i<5; i++) {
        memeArray[i] = new Image()
        memeArray[i].src = 'img/meme' + i + '.jpg'
    }
}



for(let i = 0; i<5; i++) {
    assignNumberToImage('memeDIV' + (counter + 1))
    counter++;
}

function assignNumberToImage(memeDIV) {
    document.getElementById(memeDIV).innerHTML = '<img src="img/meme' + counter + '.jpg"/>';
}

function nextImage() {
    counter++
    assignNumberToImage();
}

function prevImage() {
    counter--
    assignNumberToImage();
}
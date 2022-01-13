let counter = 0
let local_srv = "http://localhost:8000/"

let memeArray = []

let currentIndex = 0

const memeDIR = 'img/memes/'

populateMemeArray()
loadMore()
document.addEventListener('contextmenu', event => event.preventDefault())


// Load more function gets the array length and hides the button if there's nothing to load (shouldn't be a problem to a meme generator)
// When a button is clicked, the for loop appends an image from an array which is populated beforehand

function loadMore() {
    let maxResult = 1

    for(let i = 0; i < maxResult; i++) {
        $("#content").append("<div>" + "<img src='" + memeArray[i+currentIndex].src + "' />" + "</div>")
    }
    currentIndex += maxResult

    if(currentIndex >= memeArray.length) {
        //$("#lmbutton").hide()
        document.getElementById("lmbutton").innerHTML = 'Nothing to Load'
    }
}

// Function to populate the array with images located in a specific folder
// The loop iterates through numbers and loads an image to an array slot with an according number
function populateMemeArray() {
    for(let i = 0; i<5; i++) {
        memeArray[i] = new Image()
        memeArray[i].src = memeDIR + 'meme' + i + '.jpg'
    }
}
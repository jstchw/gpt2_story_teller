let counter = 0
let local_srv = "http://localhost:8000/"

let memeArray = []

let currentIndex = 0

populateMemeArray()
loadMore()

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
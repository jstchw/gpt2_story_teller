let counter = 0
let local_srv = "http://localhost:8000/"

for(let i = 0; i<5; i++) {
    assignNumberToImage('memeDIV' + (counter + 1))
    counter++;
}

function assignNumberToImage(memeDIV) {
    document.getElementById(memeDIV).innerHTML = '<img src="img/meme' + counter + '.jpg"/ usemap="#clickmap">';
}

function nextImage() {
    counter++
    assignNumberToImage();
}

function prevImage() {
    counter--
    assignNumberToImage();
}
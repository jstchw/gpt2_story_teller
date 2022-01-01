let counter = 0
let local_srv = "http://localhost:8000/"

assignNumberToImage();

function assignNumberToImage() {
    document.getElementById('memeDIV').innerHTML = '<img data-src="img/meme' + counter + '.jpg"/>';
}

function nextImage() {
    counter++
    assignNumberToImage();
}

function prevImage() {
    counter--
    assignNumberToImage();
}
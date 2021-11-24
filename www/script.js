let counter = 0
let local_srv = "http://localhost:8000/"

function nextImage() {
    let memeIMG = document.getElementById("memeIMG")
    counter++
    memeIMG.src = "img/meme" + counter + ".jpg"
}

function prevImage() {
    let memeIMG = document.getElementById("memeIMG")
    counter--
    memeIMG.src = "img/meme" + counter + ".jpg"
}
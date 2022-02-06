/*
TODO:
    PARTLY-DONE 1. Work on like and dislike buttons
    DONE 2. Change color theme of the app to: white (off-white) and implement a dark theme
    3. Build a meme repository (Reddit API)
 */

"use strict"

let counter = 0
let memeArray = []
let currentIndex = 0
const memeDIR = 'img/memes/'
const startTime = Date.now()
const themeToggleBtn = document.querySelector('#theme-toggle');
const navbar = document.querySelector('.navbar');
const menu = document.querySelector('.offcanvas');

/*
This event handler blocks the menu items from closing on click. Disabled for now
*/
/*$('nav').on('hide.bs.dropdown', function (e) {
    if (e.clickEvent) {
        e.preventDefault()
    }
});*/


populateMemeArray()
loadMore()
displayElapsedTime()

// Check for the time spent in the app every minute, displayed in the menu
let intervalId = window.setInterval(function(){
  displayElapsedTime()
}, 60000);

// Adding listeners
document.addEventListener('contextmenu', event => event.preventDefault())
lmbutton.addEventListener('click', loadMore)

themeToggleBtn.addEventListener('click', toggleTheme)


// Load more function gets the array length and hides the button if there's nothing to load (shouldn't be a problem to a meme generator)
// When a button is clicked, the for loop appends an image from an array which is populated beforehand

function loadMore() {
    let maxResult = 1

    for (let i = 0; i < maxResult; i++) {
        $(".meme").append("<div>" + "<img class='append-img img-fluid' src='" + memeArray[i + currentIndex].src + "' />" + "</div>")
        $(".meme").append("<div class='container overflow-hidden'>" +
            "<div class='row'>" +
            "<div class='col like'>&#128077</div>" +
            "<div class='col'></div>" +
            "<div class='col dislike'>&#128078</div>" +
            "</div>" +
            "</div>")
        /*$(".meme").append("<div class='like'>&#128077</div>")
        $(".meme").append("<div class='dislike'>&#128078</div>")*/
        //$(".meme").append("<div>" + "<img class='reaction-heart' src='style/icons/like.gif' />" + "</div>")
    }
    currentIndex += maxResult

    if (currentIndex >= memeArray.length) {
        document.getElementById("lmbutton").innerHTML = 'Nothing to Load'
    }
}

// Function to populate the array with images located in a specific folder
// The loop iterates through numbers and loads an image to an array slot with an according number
function populateMemeArray() {
    for (let i = 0; i < 5; i++) {
        memeArray[i] = new Image()
        memeArray[i].src = memeDIR + 'meme' + i + '.jpg'
    }
}

function displayElapsedTime() {
    // Getting the current time
    let currentTime = Date.now()
    // Calculating the time and converting it to minutes from milliseconds

    let timeSpent = Math.trunc((currentTime - startTime) / 60000)
    if(timeSpent === 1) {
        document.querySelector('#offcanvasNavbarTime').textContent = `Time spent: ${timeSpent.toString()} minute`
    } else {
        document.querySelector('#offcanvasNavbarTime').textContent = `Time spent: ${timeSpent.toString()} minutes`
    }

}

function toggleTheme() {
    // Then toggle (add/remove) the .dark-theme class to the body
    document.body.classList.toggle('dark-theme')

    // Toggling the navbar
    navbar.classList.toggle('bg-dark')
    navbar.classList.toggle('bg-light')
    navbar.classList.toggle('navbar-dark')
    navbar.classList.toggle('navbar-light')

    // Toggling the menu color
    document.querySelector('.btn-close').classList.toggle('btn-close-white')

    document.querySelector('#offcanvasNavbarTime').classList.toggle('text-light')
    document.querySelector('#offcanvasNavbarLabel').classList.toggle('text-light')

    document.querySelector('.offcanvas').classList.toggle('bg-dark')
    document.querySelector('#settingsDrop').classList.toggle('dropdown-menu-dark')
    document.querySelector('#aboutDrop').classList.toggle('dropdown-menu-dark')
}


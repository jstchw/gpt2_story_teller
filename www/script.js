// REACTIONS WORK PARTIALLY
// EVERY SECOND GROUP OF IMAGES CAN BE REACTED AT
"use strict"

// Set theme

getSettings().then(function(settings) {
    if(settings.theme === 'dark') {
        toggleTheme()
    }
})

let counter = 0
let memeArray = []
const startTime = Date.now()

const themeToggleBtn = document.querySelector('#theme-toggle')
const navbar = document.querySelector('.navbar')
const menu = document.querySelector('.offcanvas')
let modelIsLoaded = false

/*
ON STARTUP
*/

// A number of functions which will be executed one after another.
// Listeners for reactions should be added only after the images are loaded

loadMore()
displayElapsedTime()

// Check for the time spent in the app every minute, displayed in the menu
let intervalId = window.setInterval(function(){
  displayElapsedTime()
}, 60000);

/*
LISTENERS
 */
document.addEventListener('contextmenu', event => event.preventDefault())
themeToggleBtn.addEventListener('click', toggleTheme)


// Special listener to load everything when user reaches the end of page
document.addEventListener('scroll',()=>{
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        loadMore()
    }
})


// Load more function gets the array length and hides the button if there's nothing to load (shouldn't be a problem to a meme generator)
// When a button is clicked, the for loop appends an image from an array which is populated beforehand

async function loadMore() {
    //let isEmpty = Boolean(memeArray.length === 0)
    // let spinner = document.createElement('div')
    // spinner.classList.add('spinner-border')
    // document.body.append(spinner)

    $("body").append('<div class="spinner-border">')

    let object = await eel.generate_text('alice', 100, 6)()


    // When the maxResult value is bigger or the modulus of it and the array length is not 0 -> endless scrolling problem
    // !!! ABSOLUTELY MUST  BE THE SAME AS THE NUMBER OF ARRAY LENGTH (MAY BE LESS THAN COUNT OF FILES, BUT NOT GREATER) !!!
    // CAUSES ISSUES IF GREATER
    let maxResult = 6

    await populateImageArray('alice')

    for (let i = 0; i < maxResult; i++) {

        $(".content").append(
        "<div><img class='append-img img-fluid' alt='Everything went wrong' src='" + memeArray[i].src + "'/></div>" +
        "<div class='container overflow-hidden'>" +
            "<div class='row px-5'>" + object[i] + "</div>" +
            "<div class='row px-5'>" +
                "<div class='col like' id='like_" + counter + "'>&#128077</div>" +
                "<div class='col'></div>" +
                "<div class='col dislike' id='dislike_" + counter + "'>&#128078</div>" +
            "</div>" +
        "</div>")
        counter++
    }

    $('.like').click(selectReaction)
    $('.dislike').click(selectReaction)
    //currentIndex += maxResult

    $('.spinner-border').fadeOut('fast', 'swing', function() {
        $('.spinner-border').remove()
    })
}

// Function to populate the array with images located in a specific folder
// The loop iterates through numbers and loads an image to an array slot with an according number
async function populateImageArray(topic) {

    let isEmpty = Boolean(memeArray.length === 0)

    switch(topic) {
        case 'alice':
            if(isEmpty) {
                for(let i = 0; i < await eel.count_files('www/img/alice')(); i++) {
                    memeArray[i] = new Image()
                    memeArray[i].src = 'img/alice/' + 'alice' + i + '.jpg'
                }
            } else {
                shuffleArray(memeArray)
            }
    }

    console.log('populate function complete')
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

    // If the body tag contains dark-theme then change the dark theme settings
    if(document.body.classList.contains('dark-theme')) {
        setSettings('theme', 'dark')
    }
    else {
        setSettings('theme', 'light')
    }


}

/*
Just an adaptation of the Eel functions in JS
 */
function setSettings(key, value) {
    eel.set_settings(key, value)()
}

async function getSettings() {
    return await eel.get_settings('settings.json')()
}

function selectReaction() {
    let id = (this.id).replace(/\D/g, "");
    let like_pressed, dislike_pressed

    like_pressed = document.querySelector('#like_' + id).classList.contains('reaction-selected')
    dislike_pressed = document.querySelector('#dislike_' + id).classList.contains('reaction-selected')


    if(!like_pressed && this.id.includes('dislike')) {
        document.querySelector('#' + this.id).classList.add('reaction-selected')
    }
    if(!dislike_pressed && this.id.includes('like')) {
        document.querySelector('#' + this.id).classList.add('reaction-selected')
    }
    if(like_pressed && this.id.includes('like')) {
        document.querySelector('#' + this.id).classList.remove('reaction-selected')
    }
    if(dislike_pressed && this.id.includes('dislike')) {
        document.querySelector('#' + this.id).classList.remove('reaction-selected')
    }
}

function shuffleArray(array) {
    let currentIndex = array.length,  randomIndex
    while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex)
        currentIndex--
        [array[currentIndex], array[randomIndex]] = [
        array[randomIndex], array[currentIndex]]
    }
    return array
}
// Join Button
function joinPlaySet() {
    var newBody = document.getElementById("modal-body-join").innerHTML;
    document.getElementById("modal-body").innerHTML = newBody;
}

// Snackbar
function addSong() {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");

    // Add the "show" class to DIV
    x.className = "show";

    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

// Create session (display a notification) 
function createSession() {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar2");

    // Add the "show" class to DIV
    x.className = "show";

    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}

// Join session
function joinSession() {
    document.getElementById('modal-body').innerHTML = 'Session does not exist! Please try again.';
}

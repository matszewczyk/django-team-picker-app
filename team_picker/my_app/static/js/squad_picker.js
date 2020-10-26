// all players
var players = document.querySelectorAll('#players');
// determining which team starts
var red_turn;

function playerPlaying() {
    this.setAttribute('id', 'player-playing');
    // if player is playing add second method so that he can be chosen
    this.onclick = moveItem;
    this.classList.add('player-chosen');
    console.log(document.querySelectorAll('#player-playing'));
}

for (player in players){
    players[player].onclick = playerPlaying;
}

var teamSelection = false;
function teamSelectionPhase(){
    teamSelection = true;
    // hiding the button
    document.getElementById('players-chosen-button').classList.add('hide');
    for (var index=0; index < players.length; index++) {
        id = players[index].getAttribute('id');
        if (id === 'players'){
            // deleting players who are not playing
            players[index].innerHTML = '';
        } else {
            players[index].classList.remove('player-chosen');
        }
    }
    // losowanie kto zaczyna
    var startingTeam = Math.round(Math.random());
    var message= '';
    if (startingTeam === 0){
        red_turn = true;
        message = 'Red team starts';
    } else {
        red_turn = false;
        message = 'Blue team starts';
    }
    document.getElementById('click_to_mark').innerText = 'Click to choose a player';
    document.getElementById('who_is_playing').innerText = 'Now choose your teams.';
    document.getElementById('who_starts').innerText = message;

}

// team picking
const red_team = document.querySelector('#red-team-table');
const blue_team = document.querySelector('#blue-team-table');

function moveItem(){
    // when players chosen button pressed team selection can be started
    if (teamSelection) {
        if ((this.parentNode === red_team)||(this.parentNode === blue_team)){
        alert('Player already chosen!!');
        } else {
            if (red_turn) {
            red_team.appendChild(this);
            red_turn = false;
            } else {
                blue_team.appendChild(this);
                red_turn = true;
            }
        }
    }
}





//COLORS
//get list of cells
// var tds = document.getElementsByTagName('td');
// // define a function
// var red_turn = true;

//COLORS
//get list of cells
// var tds = document.getElementsByTagName('td');
// // define a function
// var red_turn = true;
// function changeColor(){
//     if ((this.style.color == 'red') || (this.style.color == 'blue')) {
//         alert('player already chosen by the opponent')
//     } else {
//         if (red_turn) {
//         this.style.color = 'red';
//         red_turn = false;
//         } else {
//             this.style.color = 'blue';
//             red_turn = true
//         }
//     }
// }
//
// //add onclick listener
// for (td in tds)
//     tds[td].onclick = changeColor;
// // #############################################
//


// ####################
// console.log('test')
//
// var myHeading = document.querySelector("div h1");
// console.log(myHeading);
// console.log("{{team}}");
// myHeading.textContent = 'Hi';
//
// function changeColorr() {
//     this.style.color = 'red';
// }
// myHeading = document.querySelector('div h1');
// myHeading.onclick = changeColorr;
// function changeColor(){
//     if ((this.style.color == 'red') || (this.style.color == 'blue')) {
//         alert('player already chosen by the opponent')
//     } else {
//         if (red_turn) {
//         this.style.color = 'red';
//         red_turn = false;
//         } else {
//             this.style.color = 'blue';
//             red_turn = true
//         }
//     }
// }
//
// //add onclick listener
// for (td in tds)
//     tds[td].onclick = changeColor;
// // #############################################
//


// ####################
// console.log('test')
//
// var myHeading = document.querySelector("div h1");
// console.log(myHeading);
// console.log("{{team}}");
// myHeading.textContent = 'Hi';
//
// function changeColorr() {
//     this.style.color = 'red';
// }
// myHeading = document.querySelector('div h1');
// myHeading.onclick = changeColorr;
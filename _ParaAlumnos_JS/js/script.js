// ----- EJERCICIO 2 -----//
function blanco(){
    document.getElementById("h2").style.backgroundColor = "white"
}

function rojo() {
    document.getElementById("h2").style.backgroundColor = "red"
}

function naranja() {
    document.getElementById("h2").style.backgroundColor = "orange"
}

function amarillo() {
    document.getElementById("h2").style.backgroundColor = "yellow"
}

function verde() {
    document.getElementById("h2").style.backgroundColor = "green"
}

function azul() {
    document.getElementById("h2").style.backgroundColor = "blue"
}

function morado() {
    document.getElementById("h2").style.backgroundColor = "purple"
}

function rosa() {
    document.getElementById("h2").style.backgroundColor = "pink"
}

function gris() {
    document.getElementById("h2").style.backgroundColor = "grey"
}

// ----- EJERCICIO 3 ----- //
function changeSizeColor(){
    var caja = document.getElementById("caja2")
    caja.className = "caja_gris"
}

function reset(){
    var caja = document.getElementById("caja2")
    caja.className = "caja caja2"
}

// ----- EJERCICIO 4 ----- //
function circunferencia(){
    var radio = parseFloat(Number(prompt("Dame el radio:")))
    alert(radio)
}
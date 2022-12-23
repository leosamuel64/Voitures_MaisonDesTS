function message(nom,fl,flcible) {
    switch (nom) {
        case "B777":
            if (fl<=flcible) {
                console.log("Le "+nom+" a atteri \n")
            } else {
                console.log("Le "+nom+" est au FL"+fl+" \n")
                message(nom,fl-10,flcible)
            }
            break;
        case "A320":
            if (fl>=flcible) {
                console.log("Le "+nom+" est en croisière"+ "\n")
            } else {
                console.log("Le "+nom+" est au FL"+fl+" \n")
                message(nom,fl+10,flcible)
            }
            break
        default:
            break;
    }

    
}

function truc() {
    console.log(document.querySelector('header').innerHTML)

    document.querySelector('h1#titre').innerHTML="Modification de la flotte"
    
    document.querySelector('img#imageA380').style.border = '2px solid red'

    document.querySelector('img#imageB777').style.display='none'
    setTimeout(function() {document.querySelector('img#imageB777').style.display='block'}, 2000)
    
    
}

function truc2() {
    document.querySelector('img#imageA380').setAttribute('src','../static/images/B747.jpg')
}
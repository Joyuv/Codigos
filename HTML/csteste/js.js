function randint(max){
    return Math.floor(Math.random() * max);
}

function textchange(ele){
    const elemento = document.getElementById(ele.id)
    if (elemento.innerText == "Teste2"){
        elemento.innerText = "Teste"
    }
    else{
    elemento.innerText="Teste2"
    }
        let r = randint(255)
        let b = randint(255)
        let g = randint(255)
        elemento.style.backgroundColor = `rgb(${r},${g},${b})`
}

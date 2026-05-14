function mensagem() {
    alert('Olá Mundo')
    campo = document.getElementById('item1').value 
    alert(campo)
}

function mais(){
    novo = document.createElement("input");
    novo.name = "item";
    novo.type = "text"
    itens = document.getElementsByName("item");
    novo.id = "item"+itens.length;
    novo.addEventListener("keypress", function(){mudarCor(this)});

    div_itens = document.getElementById("div-itens");
    div_itens.appendChild(novo);
    br = document.createElement("br");
    div_itens.appendChild(br); 
}
function mudarCor(obj) {
    obj.style.backgroundColor = 'yellow';
}
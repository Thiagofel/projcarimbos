function preencherNome() {
    const sugestoes = document.getElementById("sugestoes");
    const nome = document.getElementById("nome");
    nome.value = sugestoes.value;
}

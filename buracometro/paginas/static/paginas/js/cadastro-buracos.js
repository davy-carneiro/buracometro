document.addEventListener('DOMContentLoaded', function () {
    let areaFoto = document.getElementById('area-foto');
    let areaBotoesFoto = document.getElementById('area-botoes-foto');
    let iptEscolherArquivo = document.getElementById('iptEscolherArquivo');
    let btnMaximizarImagem = document.getElementById('btnMaximizarImagem');

    let btnSelecionarLocal = document.getElementById('btnSelecionarLocal');
    let btnCancelarFundoEscuro = document.getElementById('btnCancelarFundoEscuro');
    let fundoEscuro = document.getElementById('fundoEscuro');
    let btnAvancarLocal = document.getElementById('btnAvancarLocal');
    let areaMapaOculto = document.getElementById('areaMapaOculto');
    let mapa = document.getElementById('mapa');
    var map = L.map('mapa').setView([-2.5184, -44.2054], 16);

    let defaultMaps = document.querySelectorAll('.default-map');

    // btnSelecionarLocal
    // .addEventListener('click', function () {
    //     fundoEscuro.classList.remove('oculto');
    //     areaMapaOculto.classList.remove('oculto');
    // });

    btnCancelarFundoEscuro
    .addEventListener('click', function () {
        fundoEscuro.classList.add('oculto');
        areaMapaOculto.classList.add('oculto');
    });

    btnAvancarLocal
    .addEventListener('click', function () {

    });

    iptEscolherArquivo
    .addEventListener('change', function () {
        mostrarImagem(this, areaFoto);
    });

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([-2.5184, -44.2054] ).addTo(map)
        .bindPopup("Aqui está o ponto!")
        .openPopup();

    // var bounds = [
    //     [-2.4025, -43.8717], // Coordenada sudoeste
    //     [-2.8044, -44.5679]  // Coordenada nordeste
    // ];

    // map.setMaxBounds(bounds);


    let cont = 0;
    defaultMaps
    .forEach(defaultMap => {
        let id = `id${cont}`;
        defaultMap.id = id;

        let map = L.map(id).setView([-2.5184, -44.2054], 16); 

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        defaultMap.style = "width:100%; height:400px; position:relative;";
    
        cont++;
    });

    function mostrarImagem(input, container) {
        if (input.files && input.files[0]) {
            let reader = new FileReader();

            let style = [];
            style.push("max-width: 100%")
            style.push("max-height: 100%")
            style.push("object-fit: contain");

            reader.onload = function(e) {
                container.innerHTML = `<img src="${e.target.result}" style="${style.join(';') + ";"}">`;
                // container.innerHTML = `<img src="${e.target.result}" style="width: 100%;max-width: 100%;max-height: 100%;object-fit: contain;">`;
            };

            reader.readAsDataURL(input.files[0]);
        }
    }
});
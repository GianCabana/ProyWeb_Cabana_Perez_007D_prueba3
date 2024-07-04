function mostrarProductos() {
    fetch('http://localhost:3300/producto')
    .then(response => response.json())
    .then(data => mostrarArticulo(data))
    .catch(error => console.log(error));
}

function mostrarArticulo(data) {
    let texto = "";
    data.forEach(producto => {
        texto += `<tr>
            <td>${producto.id}</td>
            <td>${producto.nombre}</td>
            <td>${producto.tipo}</td>
            <td>${producto.lumenes}</td>
            </tr>`;
    });
    document.getElementById('Productos').innerHTML = texto;
}

function buscarTipo() {
    let tipo = document.getElementById('tipo').value;
    fetch('http://localhost:3300/producto')
    .then(response => response.json())
    .then(data => {
        let texto = "";
        data.forEach(producto => {
            if (tipo === producto.tipo) {
                texto += `<tr>
                    <td>${producto.id}</td>
                    <td>${producto.nombre}</td>
                    <td>${producto.tipo}</td>
                    <td>${producto.lumenes}</td>
                    <td>${producto.disponible}</td>
                    </tr>`;
            }
        });
        document.getElementById('Productos').innerHTML = texto;
    })
    .catch(error => console.log(error));
}




(function () {

    const btnEliminacion = document.querySelectorAll(".btn-outline-danger");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Desea eliminar el elemento seleccionado?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
    
})();


function detalles(nombre, price,foto1){
    url = "infoproducto?nombre=" + nombre + "&precio="+ price + "&foto1="+foto1 + "&anadir_c="+ 'false';
    window.location.href = url ;
}

function carrito(){
    window.location.href = "bolsa?nombre=" + nombre + "&precio="+ precio + "&foto1="+foto1 ;

}

function cargarValorescarrito(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    precio = urlParams.get('precio');
    let pre = document.getElementById("valPrecio1");
    pre.innerHTML = "<h4>Precio: " + precio + "</h4>";     
    nombre = urlParams.get('nombre');
    let nom = document.getElementById("nombre");
    nom.innerHTML = "<h2>" + nombre + "</h2>"; 
    foto1 = urlParams.get('foto1');
    let foto0 = document.getElementById("imgPrincipal");
    foto0.src= foto1;
}

function cargarValoresprod(){
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    precio = urlParams.get('precio');
    pre = document.getElementById("valPrecio1");
    pre.innerHTML = "<h4>Precio: " + precio + "</h4>";     
    nombre = urlParams.get('nombre');
    var nom = document.getElementById("nombre");
    nom.innerHTML = "<h2>" + nombre + "</h2>"; 
    foto1 = urlParams.get('foto1');
    let foto0 = document.getElementById("imgPrincipal");
    foto0.src= foto1;
    let img0 = document.getElementById("img0");
    img0.src= foto1;
    let img1 = document.getElementById("img1");
    img1.src= foto1;
    let img2 = document.getElementById("img2");
    img2.src= foto1;
    let img3 = document.getElementById("img3");
    img3.src= foto1;
}

function añadir(){
    console.log("Entrnado a añadir")
    var nom = document.getElementById("nombre").textContent;
    var pre = document.getElementById("valPrecio1").textContent.substring(8);
    var foto0 = document.getElementById("imgPrincipal").src;
    console.log(nom,pre,foto0)

    url = "infoproducto?nombre=" + nom + "&precio="+ pre + "&foto1="+foto0 + "&anadir_c="+ 'true'
    window.location.href = url

    // let btn = document.getElementById('btn_añadir')
    // btn.href = url.substring(0,n-5) + 'true';
//    window.location.href = url.substring(0,n-5) + 'true' ;

}

$(document).ready(function(){
    // $('.items_options .i_option[category="p_oferta"]').addClass('ct_item-active');  // Se agrega la clase para cambiar el estilo a la categoría que se encuentra seleccionada por defecto
    // $('.item').hide();                                 // Se ocultan los artículos 
    // $('.item[offer="si"]').show();                     // Se muestran los artículos que corresponden a la categoría por defecto
    $('.i_option').click(function(){                   // Función que se implementa al oprimir cualquiera de los 3 botones para selección de categoría 
        var categoria = $(this).attr('category');
        $('.i_option').removeClass('ct_item-active');  // Se remueve la clase que cambia el estilo a todos los botones 
        $(this).addClass('ct_item-active');            // Se aplica el estilo a el botón de la categoría seleccionado

        $('.item').css('transform', 'scale(0)');       // Se aplica una transformación al objeto artículo para aplicar el efecto
        function ocultarItems() {
            $('.item').hide();
        } setTimeout(ocultarItems,400);                // Se aplica un temporizador para que se note el efecto y después ocultar todos los artículos 

        function mostrarItems() {
            if (categoria == "p_oferta"){
                $('.item[offer="si"]').show();
                $('.item[offer="si"]').css('transform', 'scale(1)');
            } else{
                $('.item[category="'+categoria+'"]').show();
                $('.item[category="'+categoria+'"]').css('transform', 'scale(1)');    
            }
            console.log("Aquí se quedaa")
        } setTimeout(mostrarItems,400);                // De igual forma se usa el temporizador para mostrar los artículos filtrados por categoría 

    });
})


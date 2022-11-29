$(document).ready(function(){
    $('.items_options .i_option[category="p_oferta"]').addClass('ct_item-active');  // Se agrega la clase para cambiar el estilo a la categoría que se encuentra seleccionada por defecto
    $('.item').hide();                                 // Se ocultan los artículos 
    $('.item[offer="si"]').show();                     // Se muestran los artículos que corresponden a la categoría por defecto
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


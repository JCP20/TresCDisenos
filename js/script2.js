$(document).ready(function(){

    $('.items_options .i_option[category="p_oferta"]').addClass('ct_item-active');
    $('.item').hide();
    $('.item[category="p_oferta"]').show();
    $('.i_option').click(function(){
        var categoria = $(this).attr('category');

        $('.i_option').removeClass('ct_item-active');
        $(this).addClass('ct_item-active');

        $('.item').css('transform', 'scale(0)');
        function ocultarItems() {
            $('.item').hide();
        } setTimeout(ocultarItems,400);

        function mostrarItems() {
            $('.item[category="'+categoria+'"]').show();
            $('.item[category="'+categoria+'"]').css('transform', 'scale(1)');            
        } setTimeout(mostrarItems,400);

    });
})

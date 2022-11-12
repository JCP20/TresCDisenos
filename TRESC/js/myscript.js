function cargarImagen(ind){
    let imgP= document.getElementById("imgPrincipal");
    let imgsel= document.getElementById("img"+ind);
    let sizep = imgP.size;
    let heightp = imgP.height;
    let sizes = imgsel.size;
    let heights = imgsel.height;

    let tempimg = imgP.src;
    imgP.src= imgsel.src;
    imgsel.src= tempimg;
    imgP.size = sizep;
    imgP.height = heightp;
    imgsel.size = sizes;
    imgsel.height = heights;

}

function iratienda(){
 location.href="bolsa.html";
}
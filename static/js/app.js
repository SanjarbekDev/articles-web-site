function checkDelete(){
    var conf = false;

    if (confirm('Maqolani o\'chirishnni tasdiqlang ')){
        document.getElementById("submited").submit();
    }else{
        document.getElementById("cancel").submit();
    }
}

var validation = (sessin_id , author_id) =>{
    return sessin_id == author_id
}
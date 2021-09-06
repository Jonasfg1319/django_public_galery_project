
function previewImage(){
   
   reader = new FileReader()
   var image = document.querySelector('input[name=image]').files[0];

    var preview = document.querySelector("#img");
        
        var reader = new FileReader();
        
        reader.onloadend = function () {
          preview.src = reader.result;
        }
        
        if(image){
          reader.readAsDataURL(image);
        }else{
          preview.src = "";
        }
      
   
}

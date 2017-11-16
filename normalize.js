  function getNormalized(){
    var $dl, $font, strResult, teste, testinho;
    $dl = document.querySelectorAll('dl');
    for(var k in $dl){
      $font = $dl.item(k).querySelectorAll('font');
      for(var j in $font){
        strResult = "";
        teste = $font[j].innerHTML;
        if(teste[0] == '['){
          console.log(teste);
        }else{
          if(j>0){
            testinho = $font[j].querySelectorAll('b');
            if(!!testinho && !!testinho[0]){
              console.log(testinho[0].textContent);
            }
          }
        }
      }
    }
  }

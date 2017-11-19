  function getNormalized(){
    var $dl, $font, strResult, teste, testinho;
    strResult = "";
    $dl = document.querySelectorAll('dl');
    for(var k = 0; k < $dl.length ; k++){
      $font = $dl.item(k).querySelectorAll('font');
      var nWords = 0
      for(var j in $font){
        teste = $font[j].innerHTML;
        if(!!teste && teste[0] == '[' && teste != '[,]'){
          strResult = strResult + teste;
        }else{
          if(j>0){
            testinho = $font[j].querySelectorAll('b');
            if(!!testinho && !!testinho[0] && testinho[0].innerHTML[0] != '@'){
              strResult = strResult +" "+ testinho[0].innerHTML + "\n";
              j = $font.lenght + 1;
            }
          }
        }
      }
    }
    console.log(strResult);
  }


function getNormalized(){
  var $dl, $font;
  $dl = document.querySelectorAll('dl');
  for(var k in $dl){
    $font = $dl.item(k).querySelectorAll('font');
    for(var j in $font){
      var teste = $font[j].innerHTML;
      if(teste[0] == '[')
        console.log(teste);
    }
  }
}

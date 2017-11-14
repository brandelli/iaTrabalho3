function getNormalized(){
  var $dl, $font;
  $dl = document.querySelectorAll('dl');
  for(var k in $dl){
    $font = $dl.item(k).querySelectorAll('font');
    for(var j in $font){
      console.log($font[j].innerHTML);
    }
  }
}

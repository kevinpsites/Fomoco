$(function(context) {
    return function() {
        $('.jq img').mouseenter(function(){
          $('#big_image').attr("src",$(this).attr('src'))
          $('.jq img').removeClass('activ')
          $(this).addClass('activ')
        })
        $('.jq img').first().mouseenter()



    }
}(DMP_CONTEXT.get()))

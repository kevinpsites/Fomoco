$(function(context) {
    return function() {
        $("#Ajax").load("/catalog/index.products/"+context.cat+"/0")

        $("#previous_page").click(function(){
          var page = $('#PageNum').text();
          page = Number(page);
          if (page != 1){
            $('#Ajax').load("/catalog/index.products/"+context.cat+"/"+(page-2));
            $('#PageNum').text(page-1);
        }

        })

        $("#next_page").click(function(){
          var page = $('#PageNum').text();
          page = Number(page);
          if(page != context.maxpage){
          $('#Ajax').load("/catalog/index.products/"+context.cat+"/"+(page));
          $('#PageNum').text(page+1);
        }
        })
    }
}(DMP_CONTEXT.get()))

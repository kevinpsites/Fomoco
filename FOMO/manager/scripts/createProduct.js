$(function(){
  View()


    $('#id_type').on('change', function() {View()})

    function View(){
      var tp = $('#id_type').val()

        if (tp == 'BulkProduct'){
          $('#form > p').show(300)
          $('.individual').closest('p').hide(1000)
          $('.rental').closest('p').hide(1000)
          $('#id_pid').closest('p').hide(1000)
        }
        else if(tp == 'IndividualProduct')
        {
          $('#form > p').show(300)
          $('.bulk').closest('p').hide(1000)
          $('.rental').closest('p').hide(1000)
        }
        else if(tp == 'RentalProduct')
        {
          $('#form > p').show(300)
          $('.bulk').closest('p').hide(1000)
          $('.individual').closest('p').hide(1000)
        }

    }
})

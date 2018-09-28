$(function(){

  var tp = $('#id_type').val()


        if (tp == 'BulkProduct'){

          $('#form > p').show()
          $('#id_type').closest('p').hide()
          $('.individual').closest('p').hide()
          $('.rental').closest('p').hide()
          $('#id_pid').closest('p').hide()
        }
        else if(tp == 'IndividualProduct')
        {
          $('#form > p').show()
          $('#id_type').closest('p').hide()
          $('.bulk').closest('p').hide()
          $('.rental').closest('p').hide()
        }
        else if(tp == 'RentalProduct')
        {
          $('#form > p').show()
          $('#id_type').closest('p').hide()
          $('.bulk').closest('p').hide()
          $('.individual').closest('p').hide()
        }


})

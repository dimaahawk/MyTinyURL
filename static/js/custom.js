$(function(){
    console.log('Ready!')

    $('#new_url_button').click(function(){
        $.ajax({
            url: '/add',
            data: $('#url_form').serialize(),
            type: 'POST',
            success: function(response){
                console.log(response)
                $('#success_link').attr(
                    'href',
                    window.location.origin + '/s/' + response
                );
                $('#success_link').text(
                    window.location.origin + '/s/' + response
                );
                $('#success_alert').toggle(true);
            },
            error: function(error){
                console.log(error);
                alert(error.responseText);
            }
        });
    });  // End run_button ajax

});  // End doc ready
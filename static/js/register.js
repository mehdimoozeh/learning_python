$(document).ready(function() {
        $(document).on('submit', '#register_form', function(e) {
        e.preventDefault();
        let form = $("#register_form").serialize()
        console.log("form: ", form);
        $.ajax({
            url: '/register',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response);
            }
        })
    })
})
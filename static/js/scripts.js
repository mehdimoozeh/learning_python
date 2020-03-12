$(document).ready(function() {
        $(document).on('submit', '#register_form', function(e) {
        e.preventDefault();
        let form = $("#register_form").serialize()
        $.ajax({
            url: '/register',
            type: 'POST',
            data: form,
            success: function(response){
                $("#result").html("User created successfully, user Id: " + response)
                $("#result").css("visibility", "visible")
            }
        })
    })

    $(document).on('submit', '#login', function(e) {
        e.preventDefault();
        let form = $("#login").serialize()
        $.ajax({
            url: '/login',
            type: 'POST',
            data: form,
            success: function(response) {
                if (response === 'error') {
                    alert('Cant login!')
                } else {
                    window.location.href = '/'
                }
            }
        })
    })
    
    $(document).on('click', '#logout', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(response){
                if (response === 'success'){
                    window.location.href = '/login'
                } else {
                    alert('Something went wrong!')
                }
            }
        })
    })
})
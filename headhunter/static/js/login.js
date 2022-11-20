let urlBase = 'http://localhost:8000/'


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function onClickLogin(event){
    event.preventDefault();
    let email = document.getElementById('id_email').value;
    let password = document.getElementById('id_password').value;
    data = JSON.stringify({'email': email, 'password': password});
    let alert = document.getElementById('alert');
    $.ajax({
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        method: 'POST',
        url: 'auth/login/',
        data: data,
        success: function(response){
            console.log(response.answer)
            let url = urlBase + 'auth/profile/' + response.answer
            console.log(url)
            window.location.replace(url)
        },
        error: function(response){
            if (response.status === 400){
                $('#alert').text(response.responseJSON.error).removeClass('d-none')
            }
            console.log('error')
        }
    })
}

let but_login = document.getElementById('submit');
but_login.onclick = onClickLogin;

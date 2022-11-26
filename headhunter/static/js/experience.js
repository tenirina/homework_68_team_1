
let cardExperience = document.getElementById('experience_card');
let div_card = document.createElement('div');
div_card.classList.add('card');
let div_card_header = document.createElement('div');
div_card.classList.add('card-header');
let div_card_body = document.createElement('div');
div_card.classList.add('card-body');
let company_name = document.createElement('h4');
let position = document.createElement('p');
let label_start_work = document.createElement('label');
let start_work = document.createElement('p');
let label_end_work = document.createElement('label');
let end_work = document.createElement('p');


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

    function createCard(){
        company_name.classList.add('card-title')
        company_name = document.getElementById('id_company_name').value;
        position.classList.add('card-text')
        position = document.getElementById('id_position').value;
        label_start_work.innerText = 'Дата начала работы ';
        start_work = document.getElementById('id_start_work').value;
        label_end_work.innerText = 'Дата окончания работы ';
        end_work = document.getElementById('id_end_work').value;
        div_card_header.append(company_name);
        div_card_body.append(position, " ", label_start_work, " ", start_work,  " ", label_end_work, " ", end_work);
        div_card.append(div_card_header, div_card_body)
        cardExperience.append(div_card);
    }


    $(document).on('click', '#add_experience', function(event){
        event.preventDefault();
        let resumeId = document.getElementById('link_experience').dataset.resumeId;
        createCard();
        data = {'company_name': company_name, 'position': position, 'start_work': start_work, 'end_work': end_work};
        url = urlBase;
        $.ajax({
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            method: 'POST',
            url: urlBase + `resume/${resumeId}/create/experience/` ,
            data: data,
            success: function(response){
                console.log(response)
                let url_fun = url + 'resume/' + resumeId +'/edit/'
                console.log(url_fun);
                window.close();
            },
            error: function(response){
                if (response.status === 400){
                    $('#alert').text(response.responseJSON.error).removeClass('d-none')
                }
                console.log(response)
                console.log('error')
            }
        })
    })

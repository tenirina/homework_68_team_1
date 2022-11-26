
let cardExperience = document.getElementById('experience_card');
let label_company_name = document.createElement('label');
let company_name = document.createElement('spam');
let label_position = document.createElement('label');
let position = document.createElement('spam');
let label_start_work = document.createElement('label');
let start_work = document.createElement('spam');
let label_end_work = document.createElement('label');
let end_work = document.createElement('spam');

@(document).ready(function(){

    const authHeaders = {'X-CSRFToken': 'xYVavrIiypW3jPAHYDB174EmZDKY7RoK'};

    function createCard(){
        label_company_name.innerText = 'Название компании';
        company_name = document.getElementById('id_company_name').value;
        label_position.innerText = 'Описание обязательств';
        position = document.getElementById('id_position').value;
        label_start_work.innerText = 'Дата начала работы';
        start_work = document.getElementById('id_start_work').value;
        label_end_work.innerText = 'Дата окончания работы';
        end_work = document.getElementById('id_end_work').value;
        cardExperience.append(label_company_name, company_name, label_position, position, label_start_work, start_work, label_end_work, end_work);
    }


    $(document).on('click', '#add_experience', function(event){
        event.preventDefault();
        const resumeId  = $(this).data('resume-id');
        data = {'company_name': company_name, 'position': position, 'start_work': start_work, 'end_work': end_work};
        console.log(this)
        url = urlBase + `resume/${resumeId}/create/experience/`;
        $.ajax({
            headers: authHeaders,
            method: 'POST',
            url: url,
            data: data,
            success: function(response){
                console.log(response.answer)
                let url_fun = url + '/resume/' +response.answer.pk +'/edit'
                console.log(url_fun);
                createCard();
                window.location.replace(url_fun)
            },
            error: function(response){
                if (response.status === 400){
                    $('#alert').text(response.responseJSON.error).removeClass('d-none')
                }
                console.log('error')
            }
        })
    })

    $('.link_resume').click(function(event){
        const resumeId = $(this).data('resume-id');
        console.log(resumeId)
    })

})


let cardExperience = document.getElementById('experience_card');
let label_company_name = document.createElement('label');
let company_name = document.createElement('spam');
let label_position = document.createElement('label');
let position = document.createElement('spam');
let label_start_work = document.createElement('label');
let start_work = document.createElement('spam');
let label_end_work = document.createElement('label');
let end_work = document.createElement('spam');


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


function onClickAdd(event){    
    event.preventDefault();
    createCard();
    data = {'company_name': company_name, 'position': position, 'start_work': start_work, 'end_work': end_work};
    url = 'http://localhost:8000/resume/15/';
    $.ajax({
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        method: 'POST',
        url: url + 'create/experience/',
        data: data,
        success: function(response){
            console.log(response.answer)
            let url_fun = 'http://localhost:8000/resume/14/edit/'
            console.log(url_fun)
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

let butAddExperience = document.getElementById('add_experience');
butAddExperience.onclick = onClickAdd;
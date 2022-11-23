let butAddExperience = document.getElementById('add_experience');
let cardExperience = document.getElementById('experience_card');
let company_name = document.createElement('label');
let input_company = document.createElement('input');
let position = document.createElement('label');
let input_position = document.createElement('input');


butAddExperience.addEventListener('click', function(event){
    company_name.innerText = 'Название компании';
    position.innerText = 'Описание обязательств';
    cardExperience.append(company_name, input_company, position)
})
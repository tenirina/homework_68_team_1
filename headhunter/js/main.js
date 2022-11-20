let labels = document.getElementsByTagName('label');
let forms = document.getElementsByTagName('form');
let nameInput = document.getElementById('id_first_name');
let birthDateInput = document.getElementById('id_birthday');
let worker = document.getElementById('id_is_worker');


function findLableForControl(name) {
    for( var i = 0; i < labels.length; i++ ) {
       if (labels[i].htmlFor == name)
            return labels[i];
    }
}

worker.addEventListener('change', (event) => {
    var firstNameLable = findLableForControl('id_first_name')
    var lastNameLable = findLableForControl('id_last_name')
    var birthDateLable = findLableForControl('id_birthday')
    if (event.currentTarget.checked) {
        firstNameLable.innerText = 'Имя';
        lastNameLable.parentElement.style.display = 'block';
        nameInput.placeholder = 'Имя';
        birthDateLable.innerText = 'Дата рождения';
        birthDateInput.placeholder = 'Дата рождения';
    } else {
        firstNameLable.innerText = 'Наименование компании';
        lastNameLable.parentElement.style.display = 'none';
        nameInput.placeholder = 'Наименование компании';
        birthDateLable.innerText = 'Дата основания компании';
        birthDateInput.placeholder = 'Дата основания компании';
    }
})




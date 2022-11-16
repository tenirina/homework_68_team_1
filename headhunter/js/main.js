var worker = document.getElementById('id_is_worker');
var labels = document.getElementsByTagName('label');
var forms = document.getElementsByTagName('form')
var nameInput = document.getElementById('id_first_name')
var birthDateInput = document.getElementById('id_birthday')

function findLableForControl(name) {
    for( var i = 0; i < labels.length; i++ ) {
       if (labels[i].htmlFor == name)
            return labels[i];
    }
}

function changeFirstName (){
    var firstNameLable = findLableForControl('id_first_name')
    var lastNameLable = findLableForControl('id_last_name')
    var birthDateLable = findLableForControl('id_birthday')
    if (worker) {
        firstNameLable.innerText = 'Наименование компании' 
        lastNameLable.parentElement.style.display = 'none'
        nameInput.placeholder = 'Наименование компании'
        birthDateLable.innerText = 'Дата основания компании'
        birthDateInput.placeholder = 'Дата основания компании'
    }
    else {
        firstNameLable.innerText = 'Имя'
        lastNameLable.parentElement.style.display = 'block'
        nameInput.placeholder = 'Имя'
        birthDateLable.innerText = 'Дата рождения'
        birthDateInput.placeholder = 'Дата рождения'
    }
}

worker.setAttribute('onchange', 'changeFirstName()')



let form = document.getElementById('registrationForm');
form.addEventListener('submit', function(event){
    event.preventDefault();
    let username = document.querySelector('[name="username"]').value;
    let password = document.querySelector('[name="password"]').value;
    let passwordConfirm = document.querySelector('[name="password-confirm"]').value;


    
    // ---------- ВАЛИДАЦИЯ ----------
    let isValid = true;

    // Проверка имени пользователя
    if (username.trim() === "") {
        document.getElementById('username-error').textContent = "Пожалуйста, введите имя пользователя.";
        isValid = false;
    } else {
        document.getElementById('username-error').textContent = "";
    }
    // Проверка пароля
    if (password.trim() === "" || password.length < 4) {
        document.getElementById('password-error').textContent = "Пароль должен быть не менее 4 символов.";
        isValid = false;
    } else {
        document.getElementById('password-error').textContent = "";
    }
    // Проверка подтверждения пароля
    if (passwordConfirm.trim() === "" || passwordConfirm !== password) {
        document.getElementById('password-confirm-error').textContent = "Пароли не совпадают.";
        isValid = false;
    } else {
        document.getElementById('password-confirm-error').textContent = "";
    }


    // ---------- ОТПРАВКА НА СЕРВЕР ----------
    if (isValid) {
        // alert('Форма валидна.')
        const data = {"username": username, "password": password};
        fetch('http://127.0.0.1:8000/api/v1/users/register/', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        // alert("Форма отправлена");
    } 
})




/*


    console.log(username);

















// ДОКРУТИТЬ ВАЛИДАЦИЮ НА unername 

// Например, допустимый формат: Ксюша_ЧеКм03
                                // НЕ ТАК: KsEnIa_Che_Шка003
                                // ТО ЕСТЬ: ЛИБО РУС, ЛИБО АНГЛ, без микса





// Если форма прошла проверку, отправляем данные на сервер
if (isValid) {
    document.getElementById('registrationForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        const data = {};
        
        alert(data)

        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch('/api/v1/users/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = result.message;
            if (result.success) {
                form.reset();
            }
        })
        .catch(error => {
            const messageDiv = document.getElementById('message');
            messageDiv.textContent = 'Произошла ошибка: ' + error;
        });
    });
        alert("Форма отправлена");
}else {
    event.preventDefault();
    alert('Поздравляем, вы бубун.')
}

*/
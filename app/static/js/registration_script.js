let form = document.getElementById('registrationForm');
form.addEventListener('submit', async function(event){
    event.preventDefault();
    const username = document.querySelector('[name="username"]').value;
    const password = document.querySelector('[name="password"]').value;
    const passwordConfirm = document.querySelector('[name="password-confirm"]').value;

    // ---------- ВАЛИДАЦИЯ ----------
    let isValid = true;

    // Проверка пользователя
    if (username.trim() === "") {
        document.getElementById('username-error').textContent = "Пожалуйста, введите имя пользователя.";
        isValid = false;
    }else if (username.length > 30){
        ('username-error').textContent = "Имя пользователя не может быть длиннее 30 символов.";
        isValid = false;
    }else {
        document.getElementById('username-error').textContent = "";
    }
    // Проверка пароля
    if (password.trim() === "" || password.length < 4) {
        document.getElementById('password-error').textContent = "Пароль должен быть не менее 4 символов.";
        isValid = false;
    }else if(password.length > 255) {
        ('password-error').textContent = "Пароль не может быть длиннее 255 символов.";
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
        const data = {"username": username, "password": password};
        fetch('http://127.0.0.1:8000/api/v1/users/register/', {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        }
        alert(`Добро пожаловать на борт, капитан ${username}!`)
        window.location.href = '/my_projects';

})


password = document.getElementById('password-original').value;
passwordConfirm = document.getElementById('password-confirm').value;

username = document.getElementById('username').value;

let isValid = true;

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
alert(username)
alert(password)
// Если форма прошла проверку, отправляем данные на сервер
if (isValid) {
    document.getElementById('registrationForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        const data = {};

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
    }


        /*
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
            const passwordConfirm = document.getElementById('password-confirm').value;
*/
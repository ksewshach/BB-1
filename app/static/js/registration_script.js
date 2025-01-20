

// password = document.getElementsByClassName('password-original');
// passwordConfirm = document.getElementsByClassName('password-confirm');

// if (passwordOriginal != password_Confirm) {
//     const messageDiv = document.getElementById('message');
//     messageDiv.textContent = 'Произошла ошибка: ' + error;
// }




// Валидация введенных данных
let isValid = true;

// Проверка имени пользователя (можно добавить более строгую валидацию)
if (username.trim() === "") {
    document.getElementById('username-error').textContent = "Пожалуйста, введите имя пользователя.";
    isValid = false;
} else {
    document.getElementById('username-error').textContent = "";
}

// // Проверка email (можно добавить более строгую валидацию)
// if (email.trim() === "" || !email.includes("@")) {
//     document.getElementById('email-error').textContent = "Пожалуйста, введите корректный email.";
//     isValid = false;
// } else {
//     document.getElementById('email-error').textContent = "";
// }

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

        fetch('/register', {
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
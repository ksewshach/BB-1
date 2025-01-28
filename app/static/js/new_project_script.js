newProjectButton = document.getElementById('new_project_button');
newProjectDiv = document.getElementById('new_project_div');
newProjectButton.addEventListener('click', function(){
    newProjectDiv.style.display = 'block';
    newProjectButton.style.display = 'none';
})

let isValid = True;


if (title.trim() === "") {
    document.getElementById('title-error').textContent = "Пожалуйста, введите название проекта.";
    isValid = false;
} else {
    document.getElementById('title-error').textContent = "";
}

if (isValid) {
    document.getElementById('new_project_form').addEventListener('submit', function(event) {
        event.preventDefault();
        const form = event.target;
        const formData = new FormData(form);
        const data = {};

        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch('/api/v1/units/create_unit', {
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
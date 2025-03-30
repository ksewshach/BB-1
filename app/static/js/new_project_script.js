
const newProjectButton = document.getElementById('new_project_button');
const newProjectDiv = document.getElementById('login_container');
const newProjectForm = document.getElementById('new_project_form');

newProjectButton.addEventListener('click', function(){
    newProjectDiv.style.display = 'block';
    newProjectButton.style.display = 'none';
}); // конец слушателя событий на кнопке нового проекта

// слушатель событий на форме
newProjectForm.adddEventListener('submit', async function(event) {
    event.preventDefault();
    let isValid = true;
    const title = document.getElementById('project_title').value;
    if (title.trim() === "") {
        document.getElementById('title-error').textContent = "Пожалуйста, введите название проекта.";
        isValid = false;
    } else {
        document.getElementById('title-error').textContent = "";
    }
    if (isValid) {
        const project_title = document.getElementById('project_title').value;            
        const data = {
            title: project_title,
        };
        try {
            const response = await fetch('http://127.0.0.1:8000/api/v1/users/my_projects/', { 
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // 'X-CSRFToken': getCookie('csrftoken') // CSRF token
                },
                body: JSON.stringify(data)
            });

                console.log('ПРЕОБРАЗОВАЛИ В JSON')

                if (response.ok) {
                    const result = await response.json();
                    console.log('Успех: ', result);
                }else{
                    console.error('Error: ', response.status, response.statusText)
                }
            } catch (error) {
                console.error('Error: ', error);
            };
            alert("Форма отправлена");
    }
});// конец слушателя событий на форме
/* 

 -----------------------------------------    COOKIES    -------------------------------------------------------------------
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++){
            let cookie = cookies[i].trim(); // начинается ли эта куки-строка с названия, которое мы хотим?
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookie.value = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken')
//  -----------------------------------------    COOKIES    -------------------------------------------------------------------

 */


// Мы используем cookies, чтобы вы могли оставаться в системе. Продолжая использовать данное веб-приложение, вы даёте согласие на их использование.



    
    
    /* 
    
    function renderTasks(){
        // Блок запроса и получения данных
        
        fetch(reqGetListTask).then(response=>response.json()).then(
            tasks => {
                const ulTask = document.getElementById('ulTask');
                ulTask.innerHTML = '' // Эта конструкция позволяет не дублировать списки и легко-и-просто обновлять список при добавлении новых задач.
                for(let i=0; i < tasks.length; i++){
                    // Создаем элементы, которым в будущем присвоим значение
                    element_li = document.createElement('li');
                    element_title = document.createElement('h3');
                    element_description = document.createElement('p');
                    element_status = document.createElement('p');
                    element_button_delete = document.createElement('button');
                    element_button_update = document.createElement('button')
                    // Присваиваем значение из переменной tasks
                    element_button_delete.textContent = 'Удалить задачу';
                    element_button_update.textContent = 'Редактировать задачу';
                    element_button_delete.id = `delete_task_id=${tasks[i].id}`;
                    element_button_update.id = `update_task_id=${tasks[i].id}`
                    element_button_delete.addEventListener('click', function(event){
                        // event.preventDefault();// Страничку пере-рендеривать не надо, мы перегружаем сервер.
                        url = 'http://127.0.0.1:8000/api/v1/tasks/delete' + '?' + this.id.slice(7,this.id.length);
                        // СЛАЙС: обрезаем "delete_" со строки выше в тильде ЧТОБЫ хоть у нас разные айди, для проги нужен только кончик
                        fetch(url, {
                            method: 'DELETE'
                        })
                        renderTasks() // можно два раза вызвать чтобы не кликать два раза, но это сильно нагрудает сервер
                    }) 
    
                    element_title.textContent = tasks[i].title;
                    element_description.textContent = tasks[i].description;
                    element_status.textContent = tasks[i].status;
                    element_div = document.createElement('div');
                    element_div.append(element_title,
                    element_description,
                    element_status,
                    element_button_delete);
                    element_li.append(element_div);
                    ulTask.append(element_li);
                    console.log('asdas')
                }
            }
        )
    }
    
    
    
    
    
    // Разультат записываем в дату, и дату в лист_таск
    
    // ).then(data => taskObject.list_task.push(data)) // Добавляем в list_object[переменная - пустой массив] данные.
    
    
        
    const taskFormCreateBtn = document.getElementById('taskFormCreateBtn');
    taskFormCreateBtn.addEventListener('click', function(event) {
        event.preventDefault(); // когда обрабатываем post запрос, хтмл перезагружается, но этой строчкой мы это предотвращаем, и страница не обновляется 
        let project_title = document.getElementById('project_title');
        let taskFormDescription = document.getElementById('taskFormDescription');
        data = {'title': project_title.value, 'description': taskFormDescription.value};
        fetch(reqPostCreateTask, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // взяли с docs
            },
            body: JSON.stringify(data)
        })
        project_title.value = '';
        taskFormDescription.value = '';
        renderTasks()
        // alert('Задача создалась!')
    })
    
     */
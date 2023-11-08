// Получение всех моделей
async function getModels() {
    // отправляет запрос и получаем ответ
    const response = await fetch("/api/models", {
        method: "GET",
        headers: { "Accept": "application/json" }
    });
    // если запрос прошел нормально
    if (response.ok === true) {
        // получаем данные
        const models = await response.json();
        const rows = document.querySelector("tbody");
        // добавляем полученные элементы в таблицу
        models.forEach(model => rows.append(row(model)));
    }
}

// Получение моделей по заданным параметрам
async function getSelectorsModels() {
    const response = await fetch(`/api/users/${id}`, {
        method: "GET",
        headers: { "Accept": "application/json" }
    });
    if (response.ok === true) {
        const user = await response.json();
        document.getElementById("userId").value = user.id;
        document.getElementById("userName").value = user.name;
        document.getElementById("userAge").value = user.age;
    }
    else {
        // если произошла ошибка, получаем сообщение об ошибке
        const error = await response.json();
        console.log(error.message); // и выводим его на консоль
    }
}
// Создание строки для таблицы
function row(model) {
    const tr = document.createElement("tr");
    tr.setAttribute("data-rowid", model[0]);

    const imageTd = document.createElement("td");
    const image = document.createElement("img");
    image.src = model[1]
    imageTd.appendChild(image);
    tr.appendChild(imageTd);

    const nameTd = document.createElement("td");
    nameTd.append(model[2]);
    tr.append(nameTd);

    const brandTd = document.createElement("td");
    brandTd.append(model[3]);
    tr.append(brandTd);

    const categoryTd = document.createElement("td");
    categoryTd.append(model[4]);
    tr.append(categoryTd);

    const priceTd = document.createElement("td");
    priceTd.append(model[5]);
    tr.append(priceTd);

    return tr;
}

// Загрузка пользователей
getModels();
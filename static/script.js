const selector = document.getElementById("selectorBtn")
//const brandInfo = document.getElementById("brandInfoBtn")
//const modelInfo = document.getElementById("modelInfoBtn")

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

selector.onclick = async function getModels() {
    const nameCategory = document.getElementById("category").value
    const minPrice = document.getElementById("minPrice").value
    const maxPrice = document.getElementById("maxPrice").value
    // отправляет запрос и получаем ответ
    const response = await fetch(`/api/models/${nameCategory}/${minPrice}/${maxPrice}`, {
        method: "GET",
        headers: { "Accept": "application/json" }
    });
    // если запрос прошел нормально
    if (response.ok === true) {
        console.log("response ok")
        // сбрасываем все значения таблицы
        reset()
        // получаем данные
        const models = await response.json();
        const rows = document.querySelector("tbody");
        // добавляем полученные элементы в таблицу
        models.forEach(model => rows.append(row(model)));
    }
}

//// Получение моделей по заданным параметрам
//selector.onclick = async function getSelectorsModels() {
//    console.log("click selector")
//    const category = document.getElementById("category")
//    const minPrice = document.getElementById("minPrice")
//    const maxPrice = document.getElementById("maxPrice")
//    // отправляет запрос и получаем ответ
//    const response = await fetch("/api/models/{category}", {
//        method: "GET",
//        headers: { "Accept": "application/json" }
//    });
//    // если запрос прошел нормально
//    if (response.ok === true) {
//        console.log("response.ok")
//        // получаем данные
//        const models = await response.json();
//        const rows = document.querySelector("tbody");
//        // Это удалит все строки из tbody
//        while (rows.firstChild) {
//            rows.removeChild(rows.firstChild);
//        }
//        // добавляем полученные элементы в таблицу
//        models.forEach(model => rows.append(row(model)));
//    }
//    else {
//        console.log("!!!response")
//        // если произошла ошибка, получаем сообщение об ошибке
//        const error = await response.json();
//        console.log(error.message); // и выводим его на консоль
//    }
//}

//// Получение информации об одной модели
//modelInfo.onclick = async function getModel(modelName) {
//    const response = await fetch("/api/models/${name}", {
//        method: "GET",
//        headers: { "Accept": "application/json" }
//    });
//    if (response.ok === true) {
//        const model = await response.json();
//    }
//    else {
//        // если произошла ошибка, получаем сообщение об ошибке
//        const error = await response.json();
//        console.log(error.message); // и выводим его на консоль
//    }
//}
//
//// Получение информации о бренде
//brandInfo.onclick = async function getBrand(brandName) {
////    const response = await fetch("/api/brands/${name}", {
////        method: "GET",
////        headers: { "Accept": "application/json" }
////    });
////    if (response.ok === true) {
////        const brand = await response.json();
////    }
////    else {
////        // если произошла ошибка, получаем сообщение об ошибке
////        const error = await response.json();
////        console.log(error.message); // и выводим его на консоль
////    }
//    await fetch("/api/brands/${brandName}", {
//        method: "GET",
//        headers: { "Accept": "application/json" }
//    });
//}

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

// Удалит все значения в таблице
async function reset() {
    const rows = document.querySelector("tbody");
    while (rows.firstChild) {
        rows.removeChild(rows.firstChild);
    }
}

// Загрузка пользователей
getModels();
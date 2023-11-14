const selector = document.getElementById("selectorBtn")

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
        // выводим кол-во всех моделей
        const rowsCount = getRowsCount();
        var count = "Найдено: " + rowsCount;
        document.getElementById("countModel").textContent = count;
    }
}

// Получение моделей по заданным параметрам
selector.onclick = async function getModels() {
    // сбор параметров и преобразование значений
    const brandForm = document.getElementById("brandForm")
    const brandData = new FormData(brandForm)
    const brandsValues = brandData.getAll("brandName")
    var brands = brandsValues.join(",")
    if (brands.length === 0)
        brands = ["Chery", "Haval", "Geely", "Exeed", "Changan", "Zeekr"].join(",")

    const categoryForm = document.getElementById("categoryForm")
    const categoryData = new FormData(categoryForm)
    const categoriesValues = categoryData.getAll("categoryName")
    var categories = categoriesValues.join(",")
    if (categories.length === 0)
        categories = ["Седан", "Кроссовер", "Хэтчбек", "Универсал", "Внедорожник", "Купе", "Кабриолет", "Пикап", "Минивэн"].join(",")

    const priceForm = document.getElementById("priceForm")
    const priceData = new FormData(priceForm)
    const pricesValues = priceData.getAll("priceName")
    const prices = pricesValues.join(",")

    // отправляет запрос и получаем ответ
    const response = await fetch(`/api/models/${brands}/${categories}/${prices}`, {
        method: "GET",
        headers: { "Accept": "application/json" }
    });
    // если запрос прошел нормально
    if (response.ok === true) {
        // сбрасываем все значения таблицы
        reset()
        // получаем данные
        const models = await response.json();
        const rows = document.querySelector("tbody");
        // добавляем полученные элементы в таблицу
        models.forEach(model => rows.append(row(model)));
        // выводим кол-во найденных моделей
        const rowsCount = getRowsCount();
        var count = "Найдено: " + rowsCount;
        document.getElementById("countModel").textContent = count;
    }
}

// Создание строки для таблицы
function row(model) {
    const tr = document.createElement("tr");
    tr.setAttribute("data-rowid", model[0]);

    // Создание ссылки для изображения
    const imageLink = document.createElement("a");
    imageLink.href = "/model/" + encodeURIComponent(model[0]);
    const imageTd = document.createElement("td");
    imageTd.classList.add("image-cell");
    const image = document.createElement("img");
    image.src = model[1];
    imageTd.appendChild(image);
    imageLink.appendChild(imageTd);
    tr.appendChild(imageLink);

    // Создание ссылки для имени
    const nameLink = document.createElement("a");
    nameLink.href = "/model/" + encodeURIComponent(model[0]);
    const nameTd = document.createElement("td");
    nameTd.classList.add("cell");
    nameTd.append(model[2]);
    nameLink.appendChild(nameTd);
    tr.append(nameLink);

    const brandLink = document.createElement("a");
    brandLink.href = "/brand/" + encodeURIComponent(model[3]);
    const brandTd = document.createElement("td");
    brandTd.classList.add("cell");
    brandTd.append(model[3]);
    brandLink.appendChild(brandTd);
    tr.append(brandLink);

    const categoryTd = document.createElement("td");
    categoryTd.classList.add("cell");
    categoryTd.append(model[4]);
    tr.append(categoryTd);

    const priceTd = document.createElement("td");
    priceTd.classList.add("cell");
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

// Подсчитывает кол-во строк в таблице
function getRowsCount() {
  let table = document.getElementById('content')
  let tBody = table.querySelector('tbody');
  return tBody.querySelectorAll('tr').length;
}

// Загрузка пользователей
getModels();

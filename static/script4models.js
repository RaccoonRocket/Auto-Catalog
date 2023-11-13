async function modelInfo() {
    // Получаем текущий URL
    var currentUrl = window.location.href;
    // Создаем объект URL
    var url = new URL(currentUrl);
    // Извлекаем параметры из URL
    var itemPath = url.pathname.replace(/^\/|\/$/g, ''); // убираем начальный и конечный слэш, если есть
    var modelId = itemPath.split('/').pop(); // берем последнюю часть пути

    const response = await fetch(`/api/models/${modelId}`, {
        method: "GET",
        headers: { "Accept": "application/json" }
    });
    if (response.ok === true) {
        reset()
        // получаем данные
        const modelInfo = await response.json();
        const rows = document.querySelector("tbody");
        // добавляем полученные элементы в таблицу
        modelInfo.forEach(info => rows.append(row(info)));
    }
}

// Создание строки для таблицы
function row(model) {
    const tr = document.createElement("tr");
    console.log(model[0])
    tr.setAttribute("data-rowid", model[0]);

    const imageTd = document.createElement("td");
    const image = document.createElement("img");
    image.src = model[1]
    imageTd.appendChild(image);
    tr.appendChild(imageTd);

    const nameTd = document.createElement("td");
//    nameTd.classList.add("price-cell");
    nameTd.append(model[2]);
    tr.append(nameTd);

    const brandTd = document.createElement("td");
//    priceTd.classList.add("price-cell");
    brandTd.append(model[3]);
    tr.append(brandTd);

    const categoryTd = document.createElement("td");
//    priceTd.classList.add("price-cell");
    categoryTd.append(model[4]);
    tr.append(categoryTd);

    const priceTd = document.createElement("td");
//    priceTd.classList.add("price-cell");
    priceTd.append(model[5]);
    tr.append(priceTd);

    const descriptionTd = document.createElement("td");
//    priceTd.classList.add("price-cell");
    descriptionTd.append(model[6]);
    tr.append(descriptionTd);

    return tr;
}

// Удалит все значения в таблице
async function reset() {
    const rows = document.querySelector("tbody");
    while (rows.firstChild) {
        rows.removeChild(rows.firstChild);
    }
}

modelInfo();
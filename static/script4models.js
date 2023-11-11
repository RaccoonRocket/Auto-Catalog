const sendBtn = document.getElementById("modelInfoBtn")

sendBtn.onclick = async function modelInfo() {
    const modelName = document.getElementById("modelName").value
    console.log(modelName)
    const response = await fetch(`/api/models/${modelName}`, {
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

    const nameTd = document.createElement("td");
    console.log(model[1])
    nameTd.append(model[1]);
    tr.append(nameTd);

    return tr;
}

// Удалит все значения в таблице
async function reset() {
    const rows = document.querySelector("tbody");
    while (rows.firstChild) {
        rows.removeChild(rows.firstChild);
    }
}
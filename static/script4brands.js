const sendBtn = document.getElementById("brandInfoBtn")

sendBtn.onclick = async function brandInfo() {
    const brandName = document.getElementById("brandName").value
    console.log(brandName)
    const response = await fetch(`/api/brands/${brandName}`, {
        method: "GET",
        headers: { "Accept": "application/json" }
    });
    if (response.ok === true) {
        reset()
        // получаем данные
        const brandInfo = await response.json();
        const rows = document.querySelector("tbody");
        // добавляем полученные элементы в таблицу
        brandInfo.forEach(info => rows.append(row(info)));
    }
}

// Создание строки для таблицы
function row(manufacturer) {
    const tr = document.createElement("tr");
    console.log(manufacturer[0])
    tr.setAttribute("data-rowid", manufacturer[0]);

    const nameTd = document.createElement("td");
    console.log(manufacturer[1])
    nameTd.append(manufacturer[1]);
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
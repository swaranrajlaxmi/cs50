document.addEventListener('DOMContentLoaded', function () {
    getExpenseCategory()
})


function getExpenseCategory() {
    fetch('/expense_category', {
        method: 'GET'
    })
        .then(response => response.json())
        .then(function (responseJson) {
            chartData = getLabelAndData(responseJson.res);
            buildChart(chartData.labels, chartData.data)
        })
}

function buildChart(label, data) {
    const ctx = document.getElementById('myChart');
    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: label,
            datasets: [{
                label: 'Expense Category',
                data: data,
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(54, 162, 235)',
                    'rgb(255, 205, 86)'
                ],
                hoverOffset: 4
            }]
        },
    });
}

function getLabelAndData(categoryList) {
    const labels = [];
    const data = [];
    if (categoryList && categoryList.length > 0) {
        categoryList.forEach(c => {
            labels.push(c.category_name)
            data.push(c.total)
        });
    }

    return {
        labels: labels,
        data: data
    }
}

document.addEventListener('DOMContentLoaded', function() {
    
})

function saveSettings(){

    fetch('/settings', {
        method: 'POST',
        body: JSON.stringify({
            currency: document.querySelector('#currency-settings').value,
            day: document.querySelector('#day-settings').value
        })
    })
    .then(response => response.json())
    .then(function(responseJson) {
        
    })
}





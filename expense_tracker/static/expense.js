document.addEventListener('DOMContentLoaded', function() {
    
})


function changePassword(){
    const div = document.getElementById("error-message")
    fetch('/change_password', {
        method: 'POST',
        body: JSON.stringify({
            oldPassword: document.querySelector('#old-Password').value,
            newPassword: document.querySelector('#new-Password').value,
            confirmPassword: document.querySelector('#confirm-Password').value
        })
    })
    .then(response => response.json())
    .then(function(responseJson) {
        div.style.display = "block";
        div.innerText = responseJson.message;

        document.querySelector('#old-Password').value = ''
        document.querySelector('#new-Password').value = ''
        document.querySelector('#confirm-Password').value = ''
    })

    setTimeout(() => {
        div.style.display = "none";
    }, 5000)
}






document.addEventListener('DOMContentLoaded', function() {
    btn = document.querySelector('#add-btn');
    document.querySelector('#inbox').addEventListener('click', () => load('index'));
    // By default, load the index
    load('index');

    btn.addEventListener("click", () => {
        fetch('create_post', {
            method: 'POST',
            body: JSON.stringify({
                content : document.querySelector('#add-text').value
            })
        })
        .then(response => response.json())
        .then(function(responseJson) {
            console.log("result",responseJson);
        })
  })
})


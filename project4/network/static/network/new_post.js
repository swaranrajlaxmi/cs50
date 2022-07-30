document.addEventListener('DOMContentLoaded', function() {
    const addBtn = document.querySelector('#add-btn');
    if (addBtn != null) {
        addBtn.addEventListener("click", createNewPost)
    }   
    const followBtn = document.querySelector('#follow-btn');
    if (followBtn != null) {
        followBtn.addEventListener("click", follow)
    }
    // By default, load the allPosts
    allPosts();
})

function createNewPost() {
    fetch('/create_post', {
        method: 'POST',
        body: JSON.stringify({
            content : document.querySelector('#add-text').value
        })
    })
    .then(response => response.json())
    .then(function(responseJson) {
        console.log("result",responseJson);
        document.querySelector('#add-text').value = "";
        singlePost(responseJson, 'before');
    })
}

function allPosts() {
    fetch('/posts') 
    .then(response => response.json())
    .then(res => {
    
        console.log(res.posts);
        for (let i = 0; i < res.posts.length; i++) {
            // take values from posts
            singlePost(res.posts[i], 'after');

        }

    });
}


function singlePost(post, direction) {

    const postHtml = `
    <div class="card">
        <div class="card-header" >
        <a href="/profile/${post.username}" class="card-link">${post.username}</a>
        </div>
        <div class="card-body">
        <p class="card-text">${post.content}</p>
        <a href="#" class="btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16">
                <path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/>
            </svg>
        </a>
        <span>${post.likes}</span>
        </div>
        <div class="card-footer text-muted">
            <div class="text-right">${post.timestamp}</div>
        </div>
    </div>
    `
    const postDiv = document.createElement("div")
    postDiv.innerHTML = postHtml
    //if want to show new_post on top of all posts
    if(direction === 'before') {
        let parentElement = document.getElementById('allposts')
        let theFirstChild = parentElement.firstChild
        document.querySelector("#allposts").insertBefore(postDiv, theFirstChild);
    }
    else{
        document.querySelector("#allposts").appendChild(postDiv);
    }
}


function follow(){
    fetch('/follow', {
        method: 'POST',
        body: JSON.stringify({
            username: document.querySelector('#target_user').innerText  
        })
    })
    .then(response => response.json())
    .then(function(responseJson) {
        if (document.querySelector('#follow-btn').innerText == 'Follow') {
            document.querySelector('#follow-btn').innerText = 'Unfollow';
        } else if (document.querySelector('#follow-btn').innerText = 'Unfollow') {
            document.querySelector('#follow-btn').innerText = "Follow";
        }
        document.querySelector('#followers').innerText = responseJson.followers_count;
    })
}

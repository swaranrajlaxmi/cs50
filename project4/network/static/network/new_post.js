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

function like() {
    const likeBtn = this.event.currentTarget;

    fetch('/like', {
        method: 'POST',
        body: JSON.stringify({
            postId: likeBtn.dataset.postid  
        })
    })
    .then(response => response.json())
    .then(function(responseJson) {
        console.log("result",responseJson);

        likeBtn.querySelector("i").classList.toggle("heart-icon-gray");
        likeBtn.querySelector("i").classList.toggle("heart-icon-red");
        likeBtn.parentElement.querySelector(".like-count-span").innerText = responseJson.likes
    })
}

function singlePost(post, direction) {

    const postHtml = `
    <div class="card">
        <div class="card-header" >
            <div class="d-flex mb-2">
                <div class="d-flex justify-content-start">
                    <a href="/profile/${post.username}" class="card-link">${ post.username }</a>
                </div>
                <div class="w-100 d-flex justify-content-end">
                    <button class="btn btn-link">Edit</button>
                </div>
            </div>
        </div>
        <div class="card-body">
        <p class="card-text">${post.content}</p>
        <div class="like-section">
            <button class="btn btn-link" name="like" data-postid="${ post.id }" onclick="like()">
                <i class="bi bi-heart-fill ${post.isLiked == false ? 'heart-icon-gray': 'heart-icon-red'}"></i>
            </button>
            <span class="like-count-span">${post.likes}</span> likes
        </div>
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

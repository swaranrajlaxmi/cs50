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
    let postHttp;
    if (location.pathname === '/following') {
        postHttp = fetch('/posts?following=true')
    } else {
        postHttp = fetch('/posts')
    }

    postHttp
    .then(response => {
        return response.json()
    })
    .then(res => {
    
        console.log("in then",res.posts);
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
        likeBtn.querySelector("i").classList.toggle("text-secondary");
        likeBtn.querySelector("i").classList.toggle("text-danger");
        likeBtn.parentElement.querySelector(".like-count-span").innerText = responseJson.likes
    })
}


function edit(){
    const editBtn = this.event.currentTarget;
    const postCardDiv = editBtn.closest(".post-card");
    postCardDiv.classList.toggle("post-card-edit");
}

function saveEditedPost(){
    const saveBtn = this.event.currentTarget;
    const postCardDiv = saveBtn.closest(".post-card");
    const content = postCardDiv.querySelector('textarea').value;
    fetch('/save_edited_post', {
        method: 'POST',
        body: JSON.stringify({
            content: content,
            postId: saveBtn.dataset.postid 
        })
    })
    .then(response => response.json())
    .then(function(responseJson) {
        postCardDiv.classList.toggle("post-card-edit");
        postCardDiv.querySelector(".content-section .content-p").innerText = content
    })
}


function singlePost(post, direction) {

    const postHtml = `
    <div class="card post-card ">
        <div class="card-header" >
            <div class="d-flex mb-2">
                <div class="d-flex justify-content-start">
                    <a href="/profile/${post.username}" class="card-link">${ post.username }</a>
                </div>
                <div class="w-100 d-flex justify-content-end">
                    <button class="btn btn-link edit-btn ${post.isPostOwner == false ? 'd-none': ''}" onclick="edit()">Edit</button>
                </div>
            </div>
        </div>
        <div class="card-body">
            <div class="content-section">
                <p class="card-text content-p">${post.content}</p>
            </div>
            <div class="textarea-section">
                <textarea class="mt-2 form-control " rows="3">${post.content}</textarea>
                <div class="mt-2 d-flex justify-content-end">
                    <button type="button" class="btn btn-success" data-postid="${ post.id }" onclick="saveEditedPost()">Save</button>
                </div>
            </div>
            <div class="like-section">
                <button class="btn btn-link" name="like" data-postid="${ post.id }" onclick="like()">
                    <i class="bi bi-heart-fill ${post.isLiked == false ? 'text-secondary': 'text-danger'}"></i>
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

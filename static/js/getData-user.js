window.addEventListener("load", function(){
    getPosts();
})

async function getPosts(){
    let response = await fetch('/data')
    let data = await response.json()

    let posts = document.getElementById('posts')
    posts.innerHTML = ""

    for(let post of data){

        if (post.buy == false) {
            console.log("None")
        } else {
            postsHTML = `<li><div class="border"><img class="image" src="${post.img}"><h2><b>Marka: </b>${post.marka}</h2><h2><b>Modelis: </b>${post.model}</h2><h2><b>Gads: </b>${post.year}</h2><h2><b>Nomas punkts: </b>${post.place}</h2><div class="button"><a href="/cars/buy/${post.id}">Buy now</a></div></div></li>`
            posts.innerHTML = posts.innerHTML + postsHTML
        }
    }
}
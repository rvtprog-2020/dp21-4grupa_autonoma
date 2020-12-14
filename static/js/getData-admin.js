window.addEventListener("load", function(){
    getPosts();
})

async function getPosts(){
    let response = await fetch('/data')
    let data = await response.json()

    let posts = document.getElementById('posts')
    posts.innerHTML = ""

    for(let post of data){

        /* Tas norada automobiļa statusu */

        if (post.buy == true) {
            post.buy = "Pieejams!"
        } else {
            post.buy = "Izīrēts!"
        }
            /* Tas ir daļa kur admins var pievienot vai nodzest automašinu. */
            
            postsHTML = `<li><div class="border"><img class="image" src="${post.img}"><h2><b>Marka: </b>${post.marka}</h2><h2><b>Modelis: </b>${post.model}</h2><h2><b>Gads: </b>${post.year}</h2><h2><b>Nomas punkts: </b>${post.place}</h2><h1>${post.buy}</h1><div class="button"><a href="/panel/buy/${post.id}">Kas izīrēja?</a><a href="/panel/delete/${post.id}">Dzēst</a></div></div></li>`
            posts.innerHTML = posts.innerHTML + postsHTML
    }
}
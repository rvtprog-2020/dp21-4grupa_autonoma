window.addEventListener("load", function(){
    getUsers();
})

async function getUsers(){
    let response = await fetch('/users')
    let data = await response.json()

    console.log(data)
    let users = document.getElementById('users')
    users.innerHTML = ''

    for(let user of data){
        msgHTML = `<p>Vards: ${user.vards} Uzvards: ${user.uzvards} </p><button type='button' onClick="editUser(${user.id})">Edit</button>`
        users.innerHTML = users.innerHTML + msgHTML
    }
}

async function editUser(id){
    let response = await fetch(`/user/${id}`)
    let data = await response.json()

    console.log(data)
}
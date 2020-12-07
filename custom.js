window.addEventListener("load", function(){
    getUsers();
})

if (parole.text == "admin"){
    function GoToAdmin()
}


function GoToAdmin()
{
    var url1 = document.getElementById('admin.html');
    document.location.href = url1value;
}


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


// Trijstūris izvēlei

function filter_changed(){
    var list = document.getElementsByClassName("home");
    for (var i=0;i<list.length;i++)
        hide(list[i], is_filtred(list[i]));
}

function is_filtred(node){
    if (no_text(node, "style")) return true;
}
 
function no_text(node, filter){
    var style_filter = get(document.getElementById(filter),["value"]);
    var home_style = get(node.getElementsByClassName(filter),[0,"textContent"]);
    if (style_filter && (!home_style || (home_style.indexOf(style_filter)<0)))
        return true;
}

function hide(node, h){
    node.style.display = h?"none":"block";
}


function is_filtred(node){
    if (no_text(node, "style")) return true;
    if (compare(node, "square")) return true;
}
 
function compare(node, filter, comparer){
    var square_filter = get(document.getElementById(filter),["value"]);
    var home_square = get(node.getElementsByClassName(filter),[0,"textContent"]);
    if (square_filter && !home_square)
        return true;
    else if (square_filter && home_square){
        square_filter = parseFloat(square_filter)
        home_square = parseFloat(home_square)
        if ((!comparer||comparer==">")?square_filter > home_square:comparer=="<"?square_filter < home_square:comparer=="="?square_filter!=home_square:false)
            return true;
    }
}


// Randoma skaitlis
window.onload = function() {
    document.getElementById("random-number").innerHTML = Math.random(); 
};
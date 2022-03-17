//!This Is MyFavorite Film Js
console.log('Hello MyFavorite')

//!getCookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


const removeFavariteList = document.querySelector('.filmFavClass')
const currentUrl = window.location.href.replace('myfavorite/','removefilmsfavoritelist/')
const filmFavClass = document.getElementsByClassName('filmFavClass')

console.log(filmFavClass);


//!removeFavariteList Ajax
removeFavariteList.addEventListener('submit',(e)=>{
    e.preventDefault()
    //console.log(e.target.children[0].value)
    //id deyerini almag ucun filmin e.target.value dan istifade ederem belke ele alindi gedib inputun hemen andaki tiklanan valuesini alaram type='hidden' olan yerinden
    $.ajax({
        type:'POST',
        url:currentUrl,
        data:{
            'csrfmiddlewaretoken':csrftoken
        }
    })
})
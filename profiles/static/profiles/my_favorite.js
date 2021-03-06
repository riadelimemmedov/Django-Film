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


const removeFavariteListForm = document.getElementsByClassName('removeFavariteList')
const currentUrl = window.location.href.replace('myfavorite/','removefilmsfavoritelist/')
const filmsIds = [...document.getElementsByClassName('filmsIds')]
const notFavFilm = document.getElementById('notFavFilm')
const favFilmCount = document.getElementById('favFilmCount')
console.log(favFilmCount)


for(let i=0;i<removeFavariteListForm.length;i++){
    removeFavariteListForm[i].addEventListener('submit',(e)=>{
        e.preventDefault()
        const dataFavFilmId = removeFavariteListForm[i].lastElementChild.children[1].getAttribute('data-favfilmId') 
        const hideFilm = removeFavariteListForm[i].parentElement.parentElement
        $.ajax({
            type: 'POST',
            url:currentUrl,
            data:{
                'csrfmiddlewaretoken':csrftoken,
                'idFilm':dataFavFilmId
            },
            success:function(response){
                console.log('Response Remove Film List')
                console.log('Fav Film Number ', response.counfFavFilm)
                hideFilm.style.display = 'none'
                if(response.counfFavFilm <= 0){
                    notFavFilm.style.display = 'block'
                }
                favFilmCount.innerHTML = `${response.counfFavFilm}`
                console.log(response.counfFavFilm)
            },
            error:function(err){
                console.log('Error')
                console.log(err)
            }
        })
    })
}


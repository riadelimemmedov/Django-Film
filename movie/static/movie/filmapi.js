

//Html Tag
const tiklabutonu = document.getElementById('tiklabutonu')
const movielistapidata = document.getElementById('movielistapidata')
const loadingadata = document.querySelector('.loadingadata')
const findapimoviecount = document.getElementById('findapimoviecount')
const filmdetailform = document.getElementById('filmdetailform')
console.log(filmdetailform)

const currentUrl = window.location.href.replace('/popular/','')



//Api Data
const api_key = '6eb08bbd168a23902ff08b4d31a3c687'

//Token
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

setTimeout(()=>{
    loadingadata.style.display = 'none'
},2000)



axios.get('https://api.themoviedb.org/3/trending/movie/day?api_key=6eb08bbd168a23902ff08b4d31a3c687')
    .then((response)=>{
        const resultFilms = response.data.results;
        findapimoviecount.textContent = `${resultFilms.length} movies`

        //forEach
        resultFilms.forEach(function(rf,index){
            if(rf.original_title==undefined){

            }
            else{
                movielistapidata.innerHTML += `
                    <div class="movie-item-style-2 movie-item-style-1">
                        
                        <span style="display:none" id="filmsingledata">
                            ${rf.id}
                        </span>
                        
                        <img src="https://image.tmdb.org/t/p/w500/${rf.backdrop_path}" style="min-width: 170px;min-height: 170px;" alt="">
                        <div class="hvr-inner">

                            <a href="" dataid="${rf.id}" class="clickedDetailFilm dataidfilm" style="display:block"> Read more <i class="ion-android-arrow-dropright"></i> </a>
                        </div>
                        <div class="mv-item-infor">
                            <h6><a>${rf.title}</a></h6>
                            <p class="rate"><i class="ion-android-star"></i><span>${parseFloat(rf.vote_average).toFixed(1)}</span> /10</p>
                        </div>
                    </div>
                `
                
            }
        })
        const clickedDetailFilm = document.getElementsByClassName('clickedDetailFilm')
        const filmsingledata = document.getElementById('filmsingledata')
        for(let i=0;i<clickedDetailFilm.length;i++){
            clickedDetailFilm[i].addEventListener('click',(e)=>{
                e.preventDefault()
                console.log(e.target.href)
                loadingadata.style.display = 'block'
                setTimeout(()=>{
                    loadingadata.style.display = 'none'
                    let idFilm = e.target.getAttribute('dataid')
                    clickedDetailFilm[i].href = `${currentUrl}/detailapifilm/${idFilm.trim()}`
                    location.href = ''
                    location.href = clickedDetailFilm[i].href
                },3000)
            })
        }

    })
    .catch((err)=>{
        console.log(err);
    })




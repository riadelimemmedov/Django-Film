

//Html Tag
const tiklabutonu = document.getElementById('tiklabutonu')
const movielistapidata = document.getElementById('movielistapidata')
const loadingadata = document.querySelector('.loadingadata')
const findapimoviecount = document.getElementById('findapimoviecount')
const filmdetailform = document.getElementById('filmdetailform')
console.log(filmdetailform)
//const currentUrl = window.location.href.substring(0,window.location.href.lastIndexOf('/')).replace('/popular','')
//ve ya
const currentUrl = window.location.href.replace('/popular/','')
//console.log('Hal Hazir Url', `${currentUrl}/actor/morgan`)



//Api Data
const api_key = '6eb08bbd168a23902ff08b4d31a3c687'
//https://api.themoviedb.org/3/movie/${rf.id}?api_key=${api_key}&language=en-US

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
},2000)//burani sonra 7 cekersen saniye olarag yeni 7000 ne 10 ustunden 3 kimi dusunsen eger

//https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=<<api_key>>&language=en-US



axios.get('https://api.themoviedb.org/3/trending/movie/day?api_key=6eb08bbd168a23902ff08b4d31a3c687')
    .then((response)=>{
        const resultFilms = response.data.results;
        console.log('Gelen data', resultFilms)
        findapimoviecount.textContent = `${resultFilms.length} movies`

        //forEach
        resultFilms.forEach(function(rf,index){
            //!let a = `https://api.themoviedb.org/3/movie/${rf.id}/credits?api_key=6eb08bbd168a23902ff08b4d31a3c687&language=en-US`//aktyorlar her filme gore gelen
            //console.log('film actor',a)
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
        //${currentUrl}/detailapifilm/${rf.id}
        //<p class="rate"><i class="ion-android-star"></i><span>${rf.vote_average == 0 ? rf.vote_average=6.7 : rf.vote_average}</span> /10</p> qeseng koddur bu
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
                    //console.log('Filmin id deyeri', idFilm);
                    //console.log('Kohne url',clickedDetailFilm[i].href)
                    clickedDetailFilm[i].href = `${currentUrl}/detailapifilm/${idFilm.trim()}`
                    //console.log('Tek film url',clickedDetailFilm[i].href)
                    location.href = clickedDetailFilm[i].href
                },3000)
            })
        }

    })
    .catch((err)=>{
        console.log(err);
    })




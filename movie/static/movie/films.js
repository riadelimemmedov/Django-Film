//!Films Js Page
console.table('Hello All Films List')


//*getCookie
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

//*showHideLoader
function showHideLoader(loaderId){
    window.addEventListener('load',function(){
        //console.log('reload')
        const blockloader = document.getElementById(loaderId)
        this.setTimeout(function(){
            blockloader.style.display = 'none'
        },2500)
    })
}
showHideLoader('blockloader')

function findMovieAjax(){
    //Window Elements mean browser window 
    const currentUrl = window.location.href
    console.log(currentUrl);

    //Html Elements
    const searchFormId = document.getElementById('searchFormId')
    const inputSearchText = document.getElementById('inputSearchText')

    searchFormId.addEventListener('submit',(e)=>{
        e.preventDefault()
        $.ajax({
            type: 'POST',
            url : currentUrl,
            data:{
                'csrfmiddlewaretoken':csrftoken,
                'inputSearchText':inputSearchText.value,
                'urlvalue':currentUrl,
                'datareconginizeid':678910
            },
            success:function(response){
                console.log('Ugurlu bir sekilde post request atildi');

                //BackData From Response
                const serilazersFindMovie = [...JSON.parse(response.serilazersFindMovie)]

                //SearchDataHtml                
                const blockloader = document.getElementById('blockloader')
                const filmList = document.getElementById('filmList')
                const paginationData = document.getElementById('paginationData')
                const foundMovieCount = document.getElementById('foundMovieCount')
                //#############################################################################################

                //Display none htmlt tags list
                blockloader.style.display = 'block'
                document.getElementById('notFoundMovieAlert').innerHTML = ''
                foundMovieCount.textContent = ''
                filmList.innerHTML = ''

                console.log(blockloader.style.display)
                //#############################################################################################

                //!setTimeout function
                setTimeout(()=>{
                    blockloader.style.display = 'none'
                    paginationData.innerHTML = ''

                    //embedded html backend data
                    
                    if(response.findCountMovie > 0){
                        console.log(blockloader.style.display)
                        foundMovieCount.textContent = response.findCountMovie

                        serilazersFindMovie.forEach((sermovie,index)=>{
                            
                            var movieImages = undefined
                            console.log(window.location.pathname);
                            if(response.page==null){
                                movieImages = currentUrl.replace(`movies/`,'')
                            }
                            else{
                                movieImages = currentUrl.replace(`movies/?page=${response.page}`,'')
                            }
                            
                            console.log(movieImages)
                            filmList.innerHTML += `
                                <div class="movie-item-style-2 movie-item-style-1">
                                    <img src="${movieImages}media/${sermovie.fields.image_movie}" alt="">
                                    <div class="hvr-inner">
                                        <a href="${movieImages}${sermovie.fields.slug_movie}"> Read more <i class="ion-android-arrow-dropright"></i> </a>
                                    </div>
                                    <div class="mv-item-infor">
                                        <h6><a href="${movieImages}${sermovie.fields.slug_movie}">${sermovie.fields.title_movie}</a></h6>
                                        <p class="rate"><i class="ion-android-star"></i><span>${sermovie.fields.avarage_ibdm}</span> /10</p>
                                    </div>
                                </div>			
                            `
                        })
                    }
                    else if(response.findCountMovie==0){
                        document.getElementById('notFoundMovieAlert')
                            .innerHTML = `
                                <div class="ui message" style="background-color:#f5f6fa;text-align:center !important;text-align:center !important;">
                                    <strong>No relevant info was found on this topic
                                        <a href="${response.homeUrl}">All Movies</a>
                                    </strong>

                                </div>
                            `
                            foundMovieCount.textContent = '0'
                    }

                },2500)
            //alert('Islede amk') => debuglamag ucun burani istifade ede bilersen 
            },
            error:function(err){
                console.log(err)
                console.log('Hata')
            }
        })
    })
}
findMovieAjax()


// const paginationmovievalueForm = document.getElementById('paginationmovievalueForm')
// paginationmovievalueForm.addEventListener('submit',(e)=>{
//     //e.preventDefault()
//     const perpagepaginationcounturl = document.getElementById('allmovies').getAttribute('href')
//     console.log(perpagepaginationcounturl)

//     const dataFivePage = paginationmovievalueForm.firstElementChild.getAttribute('dataFivePage')
//     const dataTenPage = paginationmovievalueForm.lastElementChild.getAttribute('dataTenPage')
    
//     console.log(dataFivePage)
//     console.log(dataTenPage)

    
//     $.ajax({
//         type: 'POST',
//         url : perpagepaginationcounturl,
//         data:{
//             "csrfmiddlewaretoken":csrftoken,
//             "perpagemovieFive":dataFivePage,
//             'perpagemovieTen':dataTenPage,
//             "ididentification":12345
//         },
//         success:function(response){
//             console.log('ugurlu respose oldu selected movie per pageden');
//         },
//         error:function(err){
//             console.log('per page secerken xeta bas verdi');
//         }
        
//     })
// })




//!Detail Film Html

console.log('Hello Film Detail')

//!Cut Year Only Find
const moviedate = document.getElementsByClassName('moviedate')

//!Sort By Film With Ajax
//!Loader atmag istesen ager => https://semantic-ui.com/elements/loader.html burdan gotur belke

const currenturl = window.location.href

const relatedfilmajax = document.getElementById('relatedfilmajax')
const sortlaformagore = document.getElementById('sortlaformagore')
const biletaliram = document.getElementById('biletaliram')
const filmsRelatedArea = document.getElementById('films-related-area')
const loadingrelatedfilmloader = document.getElementById('loadingrelatedfilmloader').firstElementChild

const allrelatedfilmlistdiv = document.getElementById('allrelatedfilmlistdiv')
const loadingrelatedfilmloader2 = document.getElementById('loadingrelatedfilmloader2')

const homeurl = window.location.href.substring(0,window.location.href.lastIndexOf('/'))
const imageurl = `${homeurl}/media`
const slugurlfield = currenturl.substring(currenturl.lastIndexOf('/')+1)

//!xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
// const similargetir = document.getElementById('similargetir')
// similargetir.addEventListener('click',(e)=>{
//     console.log(window.location.href);
//     e.preventDefault()
//     $.ajax({
//         type:'GET',
//     })
// })
//!xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx




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


//!Burdan davam eleyerse InsaAllah
var countajax = 0
const handleGetData = () => sortlaformagore.addEventListener('change',(e)=>{
    $.ajax({
        type: 'POST',
        url:currenturl,
        data:{
            'csrfmiddlewaretoken':csrftoken,
            'targetvalueselect':e.target.value,
        },
        success:function(response){
            const jsondataratingdesc = response.ratingdesc //Burda sortlamag lazimdir gelen imdb deyerlerini azdan coxa dogru
            const jsondataratingasc = response.ratingasc
            const jsondatadatedesc = response.datedesc
            //console.log(Object.keys(response)); //!bu onemlidir eger dictionary tiplerde keyleri ve ya valueleri secmek isteyirsense

            const targetvalueselect = response.targetvalueselect
            const dataDescId = document.getElementById('data-desc')
            const dateEscId = document.getElementById('data-esc')

            const dolumuratingdesc = response.dolumurating_desc
            const dolumuratingasc = response.dolumurating_asc
            const dolumudatedesc = response.dolumudate_desc

            
            function handleBackData(dolumuRatingDesc,dolumuRatingAsc,dolumuDateAsc){
                if(dolumuratingdesc && dolumuratingasc==undefined && dolumudatedesc==undefined){
                    var ratingdescmovielist = JSON.parse(jsondataratingdesc)
                    var ratingdesc  = ratingdescmovielist.slice().sort((a,b)=>b['fields']['avarage_ibdm']-a['fields']['avarage_ibdm'])
                    return ratingdesc
                }
                else if(dolumuratingasc && dolumuratingdesc==undefined && dolumudatedesc==undefined ){
                    var ratingascmovielist = JSON.parse(jsondataratingasc)
                    var ratingasc = ratingascmovielist.slice().sort((a,b)=>a['fields']['avarage_ibdm']-b['fields']['avarage_ibdm'])
                    return ratingasc
                }
                else if(dolumudatedesc && dolumuratingdesc==undefined && dolumuratingasc==undefined){
                    var datedescmovielist = JSON.parse(jsondatadatedesc)
                    var datedesc = datedescmovielist.slice().sort((a,b)=>b['fields']['date_created_movie']-a['fields']['date_created_movie'])
                    var timeyeardesc = []
                    datedescmovielist.forEach(function(item){
                        let i = item['fields']['date_created_movie'].split(',')[1]
                        item['fields']['date_created_movie'] = i
                        timeyeardesc.push(item)
                    })
                } 
                if(targetvalueselect == dataDescId.value){
                    let resulttimeyeardesc = timeyeardesc.slice().sort((a,b)=>b['fields']['date_created_movie']-a['fields']['date_created_movie'])
                    return resulttimeyeardesc
                }
                else if(targetvalueselect==dateEscId.value){
                    let resulttimeyeardesc = timeyeardesc.slice().sort((a,b)=>a['fields']['date_created_movie']-b['fields']['date_created_movie'])
                    return resulttimeyeardesc
                }
            }
            const returnDataHandleBackData =  handleBackData(dolumuratingdesc,dolumuratingasc,dolumudatedesc)

            loadingrelatedfilmloader.style.display = 'block'
            var isActive = true
            if(returnDataHandleBackData){
                if(isActive == true){   
                    console.log('TimeOut EVVEL IsActive',isActive);
                    setTimeout(()=>{
                            loadingrelatedfilmloader.style.display = 'none'

                        isActive = false
                        if(isActive==false){
                            allrelatedfilmlistdiv.innerHTML  = ''
                            for(let i=0;i<returnDataHandleBackData.length;i++){
                                console.log(returnDataHandleBackData[i]['fields']['slug_movie']);

                                if(slugurlfield == returnDataHandleBackData[i]['fields']['slug_movie']){//yeni islemesin bura 
                                    continue
                                }
                                
                                let imagemovie = `${homeurl}/media/${returnDataHandleBackData[i]['fields']['image_movie']}`
                                let ratingurl = `${homeurl}/${returnDataHandleBackData[i]['fields']['slug_movie']}`
                                let titlemovie = returnDataHandleBackData[i]['fields']['title_movie']
                                let createddatemovie = returnDataHandleBackData[i]['fields']['date_created_movie']
                                let avarageimdb = returnDataHandleBackData[i]['fields']['avarage_ibdm']
                                let descriptionmovie = returnDataHandleBackData[i]['fields']['description_movie']
                                let filmvideotime = returnDataHandleBackData[i]['fields']['video_time']
                                let mmparatingmovie = returnDataHandleBackData[i]['fields']['mmpa_rating_movie'] 

                                let cropdate = createddatemovie.split(',')
                                let resultdatindexdate = null
                                if(!cropdate[1]){
                                    resultdatindexdate = cropdate[0]
                                }
                                else{
                                    resultdatindexdate = cropdate[1]
                                }

                                
                                allrelatedfilmlistdiv.innerHTML += `
                                
                                <div class="movie-item-style-2" id="films-related-area">
                                    <img src="${imagemovie}" style="width: 170px;height: 261px;" alt="">
                                    <div class="mv-item-infor">
                                        <h6><a href="${ratingurl}">${titlemovie} &nbsp; <span class="moviedate2">${resultdatindexdate.trim()}</span></a></h6><!-- Burda bu deyer olmalidirki js terefine gedib split olunsun yeniden innerHtml ile span tagi yeni inline olan span taginin icine gomulsun -->
                                        <p class="rate"><i class="ion-android-star"></i><span class="filmajaxrayting">${avarageimdb}</span> /10</p>
                                        <p class="describe">${descriptionmovie}</p>
                                        <p class="run-time"> Run Time: ${filmvideotime} .<span>MMPA: ${mmparatingmovie} </span> .<span>Release: ${createddatemovie}</span></p>
                                    </div>
                                </div>
                            `
                            }
                            sortlaformagore.selectedIndex = 0
                        }
                        
                        
                    },3000)}
                return
            }
        },
        error:function(err){
            console.log(err)
        }

    })
})

handleGetData()


//!Add Favorite List Movie
var addToFavorite = document.getElementById('addToFavorite')
let currentUrlAddToFavorite = `${homeurl}/addtofavorite/`
console.log(currentUrlAddToFavorite)

var isActive = true
addToFavorite.addEventListener('click',(e)=>{
    e.preventDefault()
    const ionHeart = document.getElementById('ionHeart')

    $.ajax({
        type:'POST',
        url : currentUrlAddToFavorite,
        data:{
            'csrfmiddlewaretoken':csrftoken,
            'slugurlfield':slugurlfield

        },
        success:function(response){
            console.log(response.workResponse)
        },
        error:function(err){
            console.log(err)
        }
    })

    if(isActive){
        ionHeart.style.color = '#DD003F'
        ionHeart.style.borderColor = '#DD003F'
        addToFavorite.lastElementChild.textContent = 'Added Successfully Film List'
        isActive = false
    }
    else if(isActive == false){
        ionHeart.style.color = '#fff'
        ionHeart.style.borderColor = '#fff'
        addToFavorite.lastElementChild.textContent = 'Add to Favorite'
        isActive = true
    }
})






//!Detail Film Html

console.log('Hello Film Detail')

//!Cut Year Only Find
const moviedate = String(document.getElementById('moviedate').textContent)
strdatasi = moviedate.split(',')//yeni vergule gore ayirib bir list yarat
let moviedatetext = document.getElementById('moviedate').textContent = ''
moviedatetext = strdatasi[1].trim()
document.getElementById('moviedate').innerHTML = moviedatetext


// let overViewPage1 = document.getElementById('activeolanpage')
// let activeolanrelatedmovie = document.getElementById('activeolanrelatedmovie')
// let overview = document.getElementById('overview')
// let moviesrelated = document.getElementById('moviesrelated')

// console.log(overViewPage1);
// console.log(activeolanrelatedmovie);
// console.log(overview)
// console.log(moviesrelated);


// let seyfeleme = document.getElementsByClassName('seyfeleme')
// for(let i=0;i<seyfeleme.length;i++){
//     seyfeleme[i].addEventListener('click',(e)=>{
//         overViewPage1.classList.remove('active')
//         activeolanrelatedmovie.classList.add('active')

//         console.log('Seyfeleme', seyfeleme[i])
//         console.log(seyfeleme);

//         overview.style.display='none'
//         moviesrelated.style.display='block'

//         console.log('Deyisdi')
//         console.log(overViewPage1.classList);
//         console.log(activeolanrelatedmovie.classList)
        
//         console.log(overview.style.display)
//         console.log(moviesrelated.style.display);

        

//     })
// }


//!Sort By Film With Ajax
//!Loader atmag istesen ager => https://semantic-ui.com/elements/loader.html burdan gotur belke

const currenturl = window.location.href

const relatedfilmajax = document.getElementById('relatedfilmajax')
const sortlaformagore = document.getElementById('sortlaformagore')
const biletaliram = document.getElementById('biletaliram')
const filmsRelatedArea = document.getElementById('films-related-area')
//const loadingrelatedfilmloader = document.getElementById('loadingrelatedfilmloader').firstElementChild

const loadingrelatedfilmloader = document.getElementById('loadingrelatedfilmloader')
console.log(loadingrelatedfilmloader);

const allrelatedfilmlistdiv = document.getElementById('allrelatedfilmlistdiv')
const loadingrelatedfilmloader2 = document.getElementById('loadingrelatedfilmloader2')
//console.log(loadingrelatedfilmloader.classList);
const homeurl = window.location.href.substring(0,window.location.href.lastIndexOf('/'))//yeni en sonuncu / buna qederkini getir
const imageurl = `${homeurl}/media`
console.log(imageurl);


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

            const dolumuratingdesc = response.dolumurating_desc
            const dolumuratingasc = response.dolumurating_asc

            
            function handleBackData(dolumuRatingDesc,dolumuRatingAsc){
                if(dolumuratingdesc && dolumuratingasc==undefined){
                    var ratingdescmovielist = JSON.parse(jsondataratingdesc)
                    var ratingdesc  = ratingdescmovielist.slice().sort((a,b)=>b['fields']['avarage_ibdm']-a['fields']['avarage_ibdm'])
                    console.log('Dolumurating DESC blogu calisti');
                    return ratingdesc
                }
                else if(dolumuratingasc && dolumuratingdesc==undefined){
                    var ratingascmovielist = JSON.parse(jsondataratingasc)
                    var ratingasc = ratingascmovielist.slice().sort((a,b)=>a['fields']['avarage_ibdm']-b['fields']['avarage_ibdm'])
                    console.log('Dolumuneyseneyse ASC blogu calisti');
                    return ratingasc
                }
            }
            const returnDataHandleBackData =  handleBackData(dolumuratingdesc,dolumuratingasc)
            console.log('Data Geriye Dodnu Funksiyadan',returnDataHandleBackData)
            
        


            // let ratingdesc  = ratingdescmovielist.slice().sort((a,b)=>b['fields']['avarage_ibdm']-a['fields']['avarage_ibdm'])
            //console.log(ratingdesc);


            //let ratingasc = ratingascmovielist.slice().sort((a,b)=>a['fields']['avarage_ibdm']-b['fields']['avarage_ibdm'])
            //console.log(ratingasc);

            
            // ratingdesc.forEach(function(item1){
            //     // console.log(item1['fields']['avarage_ibdm']);
            //     console.log(item1['fields']['avarage_ibdm'])
            // })

            var isActive = true
            if(returnDataHandleBackData){
                //console.log('Spinner Evvel',loadingrelatedfilmloader);
                //loadingrelatedfilmloader.classList.add('active')
                loadingrelatedfilmloader.classList.add('active')
                console.log(loadingrelatedfilmloader);
                //console.log('Spinnner Sonra',loadingrelatedfilmloader);
                if(isActive == true){
                    console.log('TimeOut EVVEL IsActive',isActive);
                    setTimeout(()=>{
                        //console.log('Spinnner SetTimeOut Evveli',loadingrelatedfilmloader);
                        //loadingrelatedfilmloader.classList.remove('active')

                        //loadingrelatedfilmloader.classList.remove('active')
                        //console.log('Spinnner SetTimeOut Sonrasi',loadingrelatedfilmloader);
                        loadingrelatedfilmloader.classList.remove('active')
                        console.log(loadingrelatedfilmloader);
                        isActive = false
                        if(isActive==false){
                            //console.log('False olan hisse')
                            //console.log('Bura settime un 2 hissei deyesen')
                            //console.log('////////////////////////////////////////////////////////////////////////////////////////////////')
                            //console.log('Allrelated film dolu olanda',allrelatedfilmlistdiv)
                            allrelatedfilmlistdiv.innerHTML = ''
                            //console.log('Allrelated bosaldi',allrelatedfilmlistdiv.innerHTML)
                            for(let i=0;i<returnDataHandleBackData.length;i++){
                                const description_movie = returnDataHandleBackData[i]['description_movie']
                                const a = returnDataHandleBackData[i]['fields']['avarage_ibdm']
                                
                                let imagemovie = `${homeurl}/media/${returnDataHandleBackData[i]['fields']['image_movie']}`
                                let ratingurl = `${homeurl}/${returnDataHandleBackData[i]['fields']['slug_movie']}`
                                let titlemovie = returnDataHandleBackData[i]['fields']['title_movie']
                                let createddatemovie = returnDataHandleBackData[i]['fields']['date_created_movie']
                                let avarageimdb = returnDataHandleBackData[i]['fields']['avarage_ibdm']
                                let descriptionmovie = returnDataHandleBackData[i]['fields']['description_movie']
                                let filmvideotime = returnDataHandleBackData[i]['fields']['video_time']
                                let mmparatingmovie = returnDataHandleBackData[i]['fields']['mmpa_rating_movie'] 

                                
                                //console.log(description_movie.length)
        
                                
                                
                                // console.log(ratingdesc[i]['image_movie']);
                                // console.log(`${homeurl}/media/${ratingdesc[i]['image_movie']}`)
                                //console.log('Doludu Heleki')
                                allrelatedfilmlistdiv.innerHTML += `
                                
                                <div class="movie-item-style-2" id="films-related-area">
                                    <img src="${imagemovie}" style="width: 170px;height: 261px;" alt="">
                                    <div class="mv-item-infor">
                                        <h6><a href="${ratingurl}">${titlemovie} &nbsp; <span id="moviedate">${moviedatetext}</span></a></h6><!-- Burda bu deyer olmalidirki js terefine gedib split olunsun yeniden innerHtml ile span tagi yeni inline olan span taginin icine gomulsun -->
                                        <p class="rate"><i class="ion-android-star"></i><span class="filmajaxrayting">${avarageimdb}</span> /10</p>
                                        <p class="describe">${descriptionmovie}</p>
                                        <p class="run-time"> Run Time: ${filmvideotime} .<span>MMPA: ${mmparatingmovie} </span> .<span>Release: ${createddatemovie}</span></p>
                                    </div>
                                </div>
                            `
                            }
                            //e.target.value = '' //cunki optionsun value deyeri ele '' bos stringe beraberdir
                            // ve ya selectedIndex den istifade ede bilersen
                            sortlaformagore.selectedIndex = 0
                            isActive = true
                            
                        }
                        
                    },3000)}
            }
            

                //allrelatedfilmlistdiv.classList.add('d-none')

            // else if(ratingasc){
            //     console.log('Yalniz ASC isledi')
            //     console.log('Men niye isleyirem amk')
            // }
        },
        error:function(err){
            console.log(err)
        }

    })
})

handleGetData()




//!Detail Film Html

console.log('Hello Film Detail')
console.log('////////////////////////////////////////////////////////////////')

//!Cut Year Only Find
const moviedate = document.getElementsByClassName('moviedate')


// strdatasi = moviedate.split(',')//yeni vergule gore ayirib bir list yarat
// let moviedatetext = document.getElementById('moviedate').textContent = ''
// moviedatetext = strdatasi[1].trim()
// document.getElementById('moviedate').innerHTML = moviedatetext


// let overViewPage1 = document.getElementById('activeolanpage')
// let activeolanrelatedmovie = document.getElementById('activeolanrelatedmovie')
// let overview = document.getElementById('overview')
// let moviesrelated = document.getElementById('moviesrelated')

// console.log(overViewPage1);
// console.log(activeolanrelatedmovie);
// console.log(overview)
// console.log(moviesrelated);

//!Sort By Film With Ajax
//!Loader atmag istesen ager => https://semantic-ui.com/elements/loader.html burdan gotur belke

const currenturl = window.location.href

const relatedfilmajax = document.getElementById('relatedfilmajax')
const sortlaformagore = document.getElementById('sortlaformagore')
const biletaliram = document.getElementById('biletaliram')
const filmsRelatedArea = document.getElementById('films-related-area')
//const loadingrelatedfilmloader = document.getElementById('loadingrelatedfilmloader').firstElementChild

const loadingrelatedfilmloader = document.getElementById('loadingrelatedfilmloader').firstElementChild
console.log(loadingrelatedfilmloader);

const allrelatedfilmlistdiv = document.getElementById('allrelatedfilmlistdiv')
const loadingrelatedfilmloader2 = document.getElementById('loadingrelatedfilmloader2')
//console.log(loadingrelatedfilmloader.classList);
const homeurl = window.location.href.substring(0,window.location.href.lastIndexOf('/'))//yeni en sonuncu / buna qederkini getir
const imageurl = `${homeurl}/media`
const slugurlfield = currenturl.substring(currenturl.lastIndexOf('/')+1)//yeni / qeder sil deqiq bilki sonuncudu sonra +1 vasitesilede / nu sil



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
            //console.log(Object.keys(response));

            const targetvalueselect = response.targetvalueselect

            // let objectdengelendeyer = Object.keys(response)

            // objectdengelendeyer.forEach(function(x){
            //     if(x=='targetvalueselect'){

            //     }
            // })

            const dataDescId = document.getElementById('data-desc')
            const dateEscId = document.getElementById('data-esc')


            if(targetvalueselect == dataDescId.value){
                console.log('Jsondata neyse coxdan aza geldi bir seyler');
            }
            else if(targetvalueselect == dateEscId.value){
                console.log('ferruxun masin');
            }

            console.log('Cixdigi zamanlar filmin',jsondatadatedesc);

            const dolumuratingdesc = response.dolumurating_desc
            const dolumuratingasc = response.dolumurating_asc
            const dolumudatedesc = response.dolumudate_desc

            
            function handleBackData(dolumuRatingDesc,dolumuRatingAsc,dolumuDateAsc){
                if(dolumuratingdesc && dolumuratingasc==undefined && dolumudatedesc==undefined){
                    var ratingdescmovielist = JSON.parse(jsondataratingdesc)
                    var ratingdesc  = ratingdescmovielist.slice().sort((a,b)=>b['fields']['avarage_ibdm']-a['fields']['avarage_ibdm'])
                    console.log('Dolumurating DESC blogu calisti');
                    return ratingdesc
                }
                else if(dolumuratingasc && dolumuratingdesc==undefined && dolumudatedesc==undefined ){
                    var ratingascmovielist = JSON.parse(jsondataratingasc)
                    var ratingasc = ratingascmovielist.slice().sort((a,b)=>a['fields']['avarage_ibdm']-b['fields']['avarage_ibdm'])
                    console.log('Dolumuneyseneyse ASC blogu calisti');
                    return ratingasc
                }
                else if(dolumudatedesc && dolumuratingdesc==undefined && dolumuratingasc==undefined){
                    var datedescmovielist = JSON.parse(jsondatadatedesc)
                    
                //burdaki if i 137 setire yaz
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
           // console.log('Data Geriye Dodnu Funksiyadan',returnDataHandleBackData['fields']['date_created_movie'])

            console.log('Doenn tarix listesi',returnDataHandleBackData);


            // let ratingdesc  = ratingdescmovielist.slice().sort((a,b)=>b['fields']['avarage_ibdm']-a['fields']['avarage_ibdm'])
            //console.log(ratingdesc);


            //let ratingasc = ratingascmovielist.slice().sort((a,b)=>a['fields']['avarage_ibdm']-b['fields']['avarage_ibdm'])
            //console.log(ratingasc);

            
            // ratingdesc.forEach(function(item1){
            //     // console.log(item1['fields']['avarage_ibdm']);
            //     console.log(item1['fields']['avarage_ibdm'])
            // })
            // loadingrelatedfilmloader.classList.add('active') 
            loadingrelatedfilmloader.style.display = 'block'
            var isActive = true
            if(returnDataHandleBackData){
                //console.log('Spinner Evvel',loadingrelatedfilmloader);
                //loadingrelatedfilmloader.classList.add('active')
                //console.log('Spinnner Sonra',loadingrelatedfilmloader);
                if(isActive == true){   
                    console.log('TimeOut EVVEL IsActive',isActive);
                    setTimeout(()=>{
                            //loadingrelatedfilmloader.classList.remove('active')
                            loadingrelatedfilmloader.style.display = 'none'
                        //console.log('Spinnner SetTimeOut Evveli',loadingrelatedfilmloader);
                        //loadingrelatedfilmloader.classList.remove('active')

                        //loadingrelatedfilmloader.classList.remove('active')
                        //console.log('Spinnner SetTimeOut Sonrasi',loadingrelatedfilmloader);

                        isActive = false
                        if(isActive==false){
                            //console.log('False olan hisse')
                            //console.log('Bura settime un 2 hissei deyesen')
                            //console.log('////////////////////////////////////////////////////////////////////////////////////////////////')
                            //console.log('Allrelated film dolu olanda',allrelatedfilmlistdiv)
                            allrelatedfilmlistdiv.innerHTML  = ''
                            //console.log('Allrelated bosaldi',allrelatedfilmlistdiv.innerHTML)
                            let vaxtlar = []
                            for(let i=0;i<returnDataHandleBackData.length;i++){
                                console.log(returnDataHandleBackData[i]['fields']['slug_movie']);

                                if(slugurlfield == returnDataHandleBackData[i]['fields']['slug_movie']){//yeni islemesin bura 
                                    continue
                                }

                                const description_movie = returnDataHandleBackData[i]['description_movie']
                                const a = returnDataHandleBackData[i]['fields']['avarage_ibdm']

                                //console.log('Film sluglar',returnDataHandleBackData[i]['fields']['slug_movie']);
                                
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
                                
                                //console.log(cropdate.length);

                                var datecoxaz = returnDataHandleBackData[i]['fields']['date_created_movie'].split(',')
                                //vaxtlar.push(datecoxaz[1])

                                console.log('geldi zaman neblm',createddatemovie);


                                
                                // console.log(ratingdesc[i]['image_movie']);
                                // console.log(`${homeurl}/media/${ratingdesc[i]['image_movie']}`)
                                //console.log('Doludu Heleki')
                                
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
                            //e.target.value = '' //cunki optionsun value deyeri ele '' bos stringe beraberdir
                            // ve ya selectedIndex den istifade ede bilersen
                            sortlaformagore.selectedIndex = 0
                            console.log('Vaxtlar',vaxtlar);
                        }
                        
                        
                    },3000)}
                return
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




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
    //checkActive part
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

    //ajax part
    $.ajax({
        type:'POST',
        url : currentUrlAddToFavorite,
        data:{
            'csrfmiddlewaretoken':csrftoken,
            'slugurlfield':slugurlfield,
            'isActive':isActive,
        },
        success:function(response){
            const isAdd = response.isAdd
            console.log('Is Added Value', isAdd)
        },
        error:function(err){
            console.log(err)
        }
    })
})


//!Rating Movie
console.log('Rate Film Js File')

//?get all the stars
const one = document.getElementById('first')
const two = document.getElementById('second')
const third = document.getElementById('third')
const fourth = document.getElementById('fourth')
const fifth = document.getElementById('fifth')
const sixth = document.getElementById('sixth')
const seventh = document.getElementById('seventh')
const eighth = document.getElementById('eighth')
const nineth = document.getElementById('nineth')
const tenth = document.getElementById('tenth')
const messagestatus = document.getElementById('messagestatus')

//?html elements
//const formRating = document.querySelectorAll('.rate-form')//node listlerde forEach ile gezmek olur
const formRating = document.querySelector('.rate-form')//quertSelector ise htmlcollection geri donur
const csrf = document.getElementsByName('csrfmiddlewaretoken')


//!handleSelect function
const handleStarSelect = (size) =>{
    const ratedataform = formRating.children
    for(let i=0;i<ratedataform.length;i++){
        if(i<=size){
            if(ratedataform[i].classList.contains('ion-ios-star-outline')){
                ratedataform[i].classList.remove('ion-ios-star-outline')
                ratedataform[i].classList.add('ion-ios-star')
            }
        }
        else{
            ratedataform[i].classList.add('ion-ios-star-outline')
        }
    }
}

//!handleSelect
const handleSelect = (selection) =>{
    switch(selection){
        case 'first':{
            handleStarSelect(1)
            return//dayandirmaq ucun kodu yeni asagidaki kodlar islemesin artiq eger bu sert dogrudursa
        }
        case 'second':{
            handleStarSelect(2)
            return
        }
        case 'third':{
            handleStarSelect(3)
            return
        }
        case 'fourth':{
            handleStarSelect(4)
            return
        }
        case 'fifth':{
            handleStarSelect(5)
            return
        }
        case 'sixth':{
            handleStarSelect(6)
            return
        }
        case 'seventh':{
            handleStarSelect(7)
            return
        }
        case 'eighth':{
            handleStarSelect(8)
            return
        }
        case 'nineth':{
            handleStarSelect(9)
            return
        }
        case 'tenth':{
            handleStarSelect(10)
            return
        }
    }
}

//!getNumericValue
const getNumericValue = (stringValue) =>{

    let numericValue;
    if(stringValue == 'first'){
        numericValue = 1
    }
    else if(stringValue == 'second'){
        numericValue = 2
    }
    else if(stringValue == 'third'){
        numericValue = 3
    }
    else if(stringValue == 'fourth'){
        numericValue = 4
    }
    else if(stringValue == 'fifth'){
        numericValue = 5
    }
    else if(stringValue == 'sixth'){
        numericValue = 6
    }
    else if(stringValue == 'seventh'){
        numericValue = 7
    }
    else if(stringValue == 'eighth'){
        numericValue = 8
    }
    else if(stringValue == 'nineth'){
        numericValue = 9
    }
    else if(stringValue == 'tenth'){
        numericValue = 10
    }
    else{
        numericValue = 0
    }
    return numericValue
}


const arr = [one,two,third,fourth,fifth,sixth,seventh,eighth,nineth,tenth]

//!Bura renglemek ucundur sadece mausla uzerinde gezende
arr.forEach((item)=>{
    item.addEventListener('mouseover',(e)=>{
        handleSelect(e.target.id)
    })
})

//!Ajax Rated Backend Save
arr.forEach((item) => {
    item.addEventListener('click',(e)=>{
        const val = e.target.id
        
        //!click olan vaxti submit ile POST request gonder
        //!Seyfeni Yenilemeyib dayanmadan ajax atanda addEventListener problem yaradir submit deyeri ile => qarsini almaq ucun isSubmit yazdig
        //!Hemcinin mu;ltiple ajax calldan qacmaq ucun istifade etdik bunu
        let isSubmit = false //isSubmit => adindanda oxundugu kimi formun testiq olun olunmamagini yoxlayaciyqiq addEventListener('submit') icinde
        formRating.addEventListener('submit',(e)=>{
            e.preventDefault()
            if(isSubmit==true){
                return //return olanda temiz funksiyani dayandirir cox dilde beledir yeni
            }
            isSubmit=true
            const id_film = e.target.id//detailinde oldugumuz filmin id deyeri
            const rate_num = getNumericValue(val)//gonderdiyimiz deyer star olarag yeni
            //console.log('Rate Url' ,`${homeurl}/ratefilm/`)

            //*ajax part
            $.ajax({
                type:'POST',
                url:`${homeurl}/ratefilm/`,
                data:{
                    'csrfmiddlewaretoken':csrf[0].value,
                    'id_film':id_film,
                    'rate_num':rate_num
                },
                success: function(response){
                    console.log('Response Value ', response.ugurlu)
                    messagestatus.innerHTML = 'Successfully Rated'
                },
                error:function(err){
                    console.log('Error ', err.xeta)
                    messagestatus.innerHTML = 'Error Rated Neyse'
                }
            })
        })
    })
})

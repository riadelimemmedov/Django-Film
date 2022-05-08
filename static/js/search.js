//!Search Js
console.log('Search Js Page')

const searchForm = document.getElementById('search-form')
const searchInput = document.getElementById('search-input')
const searchResultBox = document.getElementById('search-films-list')
const searchUrl = window.location.href//http://127.0.0.1:8000/
const searhAlert = document.getElementById('search-alert')

console.log('hal hazirdaki url deyeri ', `${window.location.href}blade-runner-2049`)



//`${searchUrl}profile/search`

const sendSearchData = function(filmName){
    $.ajax({
        type:'POST',
        url:`${searchUrl}profile/search/`,
        data:{
            'filmName':filmName
        },
        success:function(response){
            console.log(response)
            console.log('Success send post request search url')
            const filmData = response.data
            console.log(filmData)
            searchResultBox.innerHTML = ''
            if(Array.isArray(filmData)){//yeni gelen data tipi Array Tipindedirmi?
                searhAlert.classList.add('hide')
                filmData.forEach((item)=>{
                    //console.log(`${searchUrl.substring(0,searchUrl.lastIndexOf('/'))}${item.imagemovie}`)//  /media/movieimages/movie-single.jpg bu formatda gelir
                    
                    console.log(`${searchUrl}${item.slugmovie}`)

                    const itemimage_url = `${searchUrl.substring(0,searchUrl.lastIndexOf('/'))}${item.imagemovie}`

                    // console.log(window.location.href.substring(0,window.location.href.lastIndexOf('/')))
                    
                        searchResultBox.innerHTML += `
                            <div class="search-result">
                                <a href="${searchUrl}${item.slugmovie}" class="item">
                                    <div class="row mt-2 mb-2">
                                        <div class="col-2">
                                            <img src="${itemimage_url}" class="searh-image" alt="">
                                        </div>
                                        <div class="col-10" id="films-title">
                                            <h5>${item.title}</h5>
                                        </div>
                                    </div>
                                </a>
                            </div>
                    `
                })
            }
            else{
                //eger istifadeci inputa bir deyer yazib amma o deyere uygun netice tapilmayibse ehtimalinida nezere almaq lazimdir
                if(searchInput.value.length>0){
                    searhAlert.classList.remove('hide')
                    searhAlert.innerHTML = `<div class="alert alert-danger">
                        <strong style="text-align:center">Films Not Found</strong>
                    </div>`
                }
                else{//if user not input value
                    searhAlert.classList.add('hide')
                }
            }
        },
        error:function(err){
            console.log('Error')
            console.log(err)
        }
    })
}

searchInput.addEventListener('keyup',(e)=>{
    e.preventDefault()
    if(searchResultBox.classList.contains('hide')){
        searchResultBox.classList.remove('hide')
    }
    sendSearchData(e.target.value)
})
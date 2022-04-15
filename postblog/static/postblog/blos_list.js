//!Blog List Js 
console.log('Hello Blog List')

const searchFormBlogFilm = document.getElementById('searchFormBlogFilm')
const searchedInputBlogFilm = document.getElementById('searchedInputBlogFilm')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const currentUrl =  window.location.href.substring(0,window.location.href.lastIndexOf('/'))

console.log(currentUrl)

// searchFormBlogFilm.addEventListener('submit',(e)=>{
//     e.preventDefault()
//     $.ajax({
//         type:'POST',
//         url:`${currentUrl}/`,
//         data:{
//             'csrfmiddlewaretoken':csrf[0].value,
//             'searchedTextBlogFilms':searchedInputBlogFilm.value
//         },
//         success:function(response){
//             console.log('Success Searh Restult Return Response')
//             searchFormBlogFilm.reset()
//         },
//         error:function(err){
//             console.log('Hata')
//             console.log(err)
//         }
//     })
// })
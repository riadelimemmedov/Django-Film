//!Detail Film Html

console.log('Hello Film Detail')

//!Cut Year Only Find
const moviedate = String(document.getElementById('moviedate').textContent)
strdatasi = moviedate.split(',')//yeni vergule gore ayirib bir list yarat
let moviedatetext = document.getElementById('moviedate').textContent = ''
moviedatetext = strdatasi[1].trim()
document.getElementById('moviedate').innerHTML = moviedatetext


//!Sort By Film With Ajax
//!Loader atmag istesen ager => https://semantic-ui.com/elements/loader.html burdan gotur belke

const currenturl = window.location.href

const biletaliram = document.getElementById('biletaliram')
// console.log(biletaliram);
// biletaliram.addEventListener('click',(e)=>{
//     e.preventDefault()
//     console.log('noldu amk')
// })

biletaliram.addEventListener('click',(e)=>{
    $.ajax({
        type: 'GET',
        url:currenturl,
        success:function(response){
            console.log('Detail AJAX indan gelirem ve isleyirem')
            //console.log(response.jsonlanandata)
            console.log(response.jsonlanandata)
        },
        error:function(err){
            console.log('HATA')
        }
    })
})


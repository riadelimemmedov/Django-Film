//!Detail Film Html

console.log('Hello Film Detail')

const moviedate = String(document.getElementById('moviedate').textContent)
//console.log(moviedate.textContent.trim().split())

strdatasi = moviedate.split(',')//yeni vergule gore ayirib bir list yarat
let moviedatetext = document.getElementById('moviedate').textContent = ''
moviedatetext = strdatasi[1].trim()
document.getElementById('moviedate').innerHTML = moviedatetext


//console.log(moviedatetext);
// console.log(strdatasi[0])
// console.log(strdatasi[1])
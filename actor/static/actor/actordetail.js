//!Actor Detail Page

console.log('Actor Detail')

let overViewPage = document.getElementById('activeolanpage')
let biographyPage = document.getElementById('activeolanbiography')
let overviewceb = document.getElementById('overviewceb')
let biography = document.getElementById('biography')
let seefullbio = document.getElementById('seefullbio')

seefullbio.addEventListener('click',(e)=>{
    e.preventDefault()
    overViewPage.classList.remove('active')
    biographyPage.classList.add('active') 
    overviewceb.style.display = 'none'
    biography.style.display = 'block'
})
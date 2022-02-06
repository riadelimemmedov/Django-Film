//!Home Page Js

console.log('Home')

const categorylist = document.getElementsByClassName('categorylist')
for (let i = 0; i < categorylist.length; i++) {
    let categoryText = categorylist[i].textContent
    let categorycard = document.getElementsByClassName('categorycard')

    for (let i = 0; i < categorycard.length; i++) {
        let categorycardText = categorycard[i].textContent
        if (categorycardText == 'Adventure') {
            categorycard[i].classList.add('orange')
        } else if (categorycardText == 'Drama') {
            categorycard[i].style.background = '#e74c3c'
        } else if (categorycardText == 'Sci-Fi') {
            categorycard[i].style.background = '#182C61'
        } else if (categorycardText == 'Action') {
            categorycard[i].classList.add('yell')
        } else if (categorycardText == 'Comedy') {
            categorycard[i].classList.add('green')
        }
        else if(categorycardText == 'Crime'){
            categorycard[i].style.background = '#676FA3'
        }
        else if(categorycardText == 'Family'){
            categorycard[i].style.background = '#F7F7F7'
        }
        else if(categorycardText == 'Mystery'){
            categorycard[i].classList.add('blue')
        }
        else if(categorycardText == 'Comedy'){
            categorycard[i].style.background = '#FFC600'
        }
        else if(categorycardText == 'Music'){
            categorycard[i].style.background = '#191919'
        }
        else {
            categorycard[i].style.background = '#222f3e'
        }
    }
}
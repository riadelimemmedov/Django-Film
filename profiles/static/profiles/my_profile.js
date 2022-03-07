//!This Is MyProfile Js
console.log('Hello MyProfile')

const modalProfile = document.getElementById('modalProfile')
const imageProfile = [...document.getElementsByClassName('imageProfile')]
const profPictureSingle = document.getElementById('profPictureSingle')
const description = document.querySelector('.description')
const profileUsername = document.getElementById('profileUsername')
const profileFirstName = document.getElementById('profileFirstName')
const profileLastName = document.getElementById('profileLastName')


//!showRelatedObjectPicture function
function showModalProfilePicture(){
    imageProfile.forEach((imgp)=>{
        imgp.addEventListener('click',(e)=>{
            e.preventDefault()
            console.log(description.childNodes[2]);
            profPictureSingle.setAttribute('src',e.target.src)
            //tek ededlerde deyisir font olcusu yazilan kodda yeni 2 ye bolunmeyen ededlerde
            description.childNodes[1].textContent =  `User : ${profileUsername.value}`            
            description.childNodes[3].textContent = `Firstname : ${profileFirstName.value}`
            description.childNodes[5].textContent = `Lastname : ${profileLastName.value}`
            $('.ui.modal').modal('show');
        })
    })
}
showModalProfilePicture()



//hem displaylik noneden cixmalidir hemde modal classi elave olunmalidiri click olunan zaman
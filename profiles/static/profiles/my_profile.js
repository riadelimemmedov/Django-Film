//!This Is MyProfile Js
console.log('Hello MyProfile')

//?profile modal show data
const modalProfile = document.getElementById('modalProfile')
const imageProfile = [...document.getElementsByClassName('imageProfile')]
const profPictureSingle = document.getElementById('profPictureSingle')
const description = document.querySelector('.description')

//?profile input data
const profileUsername = document.getElementById('profileUsername')
const profileEmail = document.getElementById('profileEmail')
const profileFirstName = document.getElementById('profileFirstName')
const profileLastName = document.getElementById('profileLastName')
const profileCountry = document.getElementById('profileCountry')
const profileState = document.getElementById('profileState')

//!getCookie
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

//!Profile Data Update Function
const profileDetailForm = document.getElementById('profileDetailForm')
const currentUrl = window.location.href
const url = currentUrl.replace('myprofile/','updateprofiledata/')

//?Alert user Function
const alertBoxUsername = document.getElementById('alert-box-username')
const handleAlerts = function(type,text){
    alertBoxUsername.innerHTML = `
        <div class="alert alert-${type} text-center">
            <strong style="color:black">${text}</strong>
        </div>
    `
    setTimeout(()=>{
        alertBoxUsername.style.display = 'none'
    },3000)
}

//?Profile Update Data Form
profileDetailForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    const updateProfileDataAjax = () =>{
        $.ajax({
            method: 'POST',
            url:url,
            data:{
                'csrfmiddlewaretoken':csrftoken,
                'profileUsername':profileUsername.value,
                'profileEmail':profileEmail.value,
                'profileFirstName':profileFirstName.value,
                'profileLastName':profileLastName.value,
                'profileCountry':profileCountry.value,
                'profileState':profileState.value
            },
            success:function(response){//funksiya cavab geri donuyr yeni response o responsi tutmag ucun yazdig biz bu funksiyani
                console.log('Successfully response url')

                if(response.errorUsernameFind){
                    handleAlerts('info',response.errorUsernameFind)
                }
                else{
                    //profileUsername.value = response.username
                    console.log('worked successfully response from backend')
                }
                
            },
            error:function(err){
                console.log('Hata',err)
            }
        })
    }
    updateProfileDataAjax()
})





//hem displaylik noneden cixmalidir hemde modal classi elave olunmalidiri click olunan zaman
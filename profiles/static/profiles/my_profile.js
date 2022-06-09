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
const alertBoxUsername2 = document.getElementById('alert-box-username2')


//?Profile Update Data Form
profileDetailForm.addEventListener('submit',(e)=>{
    e.preventDefault()

    //!Check Email
    function isEmail(emailUser){
        var pattern = /^([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)@([0-9a-zA-Z]([-_\\.]*[0-9a-zA-Z]+)*)[\\.]([a-zA-Z]{2,9})$/;
        return pattern.test(emailUser)
    }

    if(isEmail(profileEmail.value) == false){
        alertBoxUsername.innerHTML = `
        <div class="alert alert-info text-center text-capitalize" style="text-transform: capitalize">
            <strong style="color:black">please enter the correct email</strong>
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
        `
    }

    else{
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
                success:function(response){
                    console.log('Successfully response url')
    
                    if(response.errorUsernameFind){
                        alertBoxUsername.innerHTML = `
                            <div class="alert alert-danger text-center text-capitalize" style="text-transform: capitalize">
                                <strong style="color:black">${response.profileUsername.length < 4 ? 'username must be minimum 4 character': response.errorUsernameFind}</strong>
                                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                        `
                    }
    
                    else if(response.errorEmailFind){
                        alertBoxUsername.innerHTML = `
                            <div class="alert alert-danger text-center text-capitalize" style="text-transform: capitalize">
                                <strong style="color:black">${response.profileEmail.length <4 ? 'email must be minimum 4 character': response.errorEmailFind}</strong>
                                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                        `
                    }
        
    
                    else{
                        console.log('worked successfully response from backend')
                        alertBoxUsername2.innerHTML = `
                            <div class="alert alert-success text-center text-capitalize" style="text-transform: capitalize">
                                <strong style="color:black">${'Your profile data has been successfully updated'}</strong>
                                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                        `
                    }
    
                },
                error:function(err){
                    console.log(err)
                }
            })
        }
        updateProfileDataAjax()
    }
})

//?ChangePasswordForm
const changePasswordForm = document.getElementById('changePasswordId')
// changePasswordForm.addEventListener('submit',(e)=>{
//     $('html,body').animate({scrollTop:4800},200)
// })

//!Register Js
console.log('Register Page')

const usernameRegister = document.getElementById('username-2')
const emailRegister = document.getElementById('email-2')
const passwordRegister = document.getElementById('password-2')
const repasswordRegister = document.getElementById('repassword-2')
const registerButton = document.getElementById('register')


//?Register Ajax
const urlregister = `${window.location.href}profile/register/`
registerButton.addEventListener('click',(e)=>{
    e.preventDefault()
    $.ajax({
        type:'POST',
        url:urlregister,
        data:{
            'usernameRegister':usernameRegister.value,
            'emailRegister':emailRegister.value,
            'passwordRegister':passwordRegister.value,
            'repasswordRegister':repasswordRegister.value,
        },
        success:function(response){
            console.log(response)
            console.log('successfully Send Request Register Url')
        },
        error:function(err){
            console.log(err)
            console.log('error register url')
        }
    })
})

//!Register Js
console.log('Register Page')

const usernameRegister = document.getElementById('username-2')
const emailRegister = document.getElementById('email-2')
const passwordRegister = document.getElementById('password-2')
const repasswordRegister = document.getElementById('repassword-2')
const registerButton = document.getElementById('register')

let registerError = document.getElementById('register-error')


//?catchError
function catchError(error_value){
    registerError.innerHTML = `<div class="alert alert-danger text-center text-capitalize" style="text-transform: capitalize">
            <strong>${error_value}</strong>
        </div>
    `
}

//?Register Ajax
const urlregister = `${window.location.href}profile/register/`
registerButton.addEventListener('click',(e)=>{
    e.preventDefault()
    if(usernameRegister.value =='' || emailRegister.value =='' || passwordRegister.value == '' || repasswordRegister.value == ''){
        catchError('Please fill input gaps')
    }
    else if(passwordRegister.value != repasswordRegister.value){
        catchError('Password not match')
    }
    else{
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
                if(response.success_register){
                    console.log(response.success_register)
                    window.location.reload()
                }
                else if(response.error_register){
                    catchError(response.error_register)
                }
            },
            error:function(err){
                console.log(err)
                console.log('error register url')
            }
        })
    }
})

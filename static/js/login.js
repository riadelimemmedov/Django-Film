//!Login Js
console.log('Login Page')

const login = document.getElementById('login')
const username = document.getElementById('username')
const password = document.getElementById('password')
const checkrememberme = document.getElementById('checkrememberme')
const loginerror = document.getElementById('login-error')


//?Checked Remember ME
let isChecked = ''
function rememberMeFunction(){
    if(checkrememberme.checked == true){
        isChecked = 'true'
    } 
    else if(checkrememberme.checked == false){
        isChecked = 'false'
    }
}
checkrememberme.addEventListener('click',(e)=>{
    rememberMeFunction()
})
//Finish Functiton

//?Login Ajax
const urllogin = `${window.location.href}profile/login/`
login.addEventListener('click',(e)=>{
    e.preventDefault()
    console.log('Remember Me Deyeri', isChecked)
    $.ajax({
        type:'POST',
        url:urllogin,
        data:{
            'username':username.value,
            'password':password.value,
            'checkrememberme':isChecked
        },
        success:function(response){
            console.log('ugurlu bir sekilde isleyir login')
            if(response.success){
                window.location.reload()
            }
            else if(response.error){
                loginerror.innerHTML = `
                <div class="alert alert-danger text-center text-capitalize" style="text-transform: capitalize">
                    <strong>username or password is wrong</strong>
                </div>
                `
            }
        },
        error:function(err){
            console.log('xeta var')
        }
    })
})
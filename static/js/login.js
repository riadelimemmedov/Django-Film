//!Login Js
console.log('Login Page')

const login = document.getElementById('login')
const username = document.getElementById('username')
const password = document.getElementById('password')
const checkrememberme = document.getElementById('checkrememberme')

//Checked Remember ME
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

const currentUrl = `${window.location.href}profile/login/`
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0]

login.addEventListener('click',(e)=>{
    e.preventDefault()
    console.log('Remember Me Deyeri', isChecked)
    $.ajax({
        type:'POST',
        url:currentUrl,
        data:{
            'csrfmiddlewaretoken':csrf.value,
            'username':username.value,
            'password':password.value,
            'checkrememberme':isChecked
        },
        success:function(response){
            console.log('ugurlu bir sekilde isleyir login')
        },
        error:function(err){
            console.log('xeta var')
        }
    })
})
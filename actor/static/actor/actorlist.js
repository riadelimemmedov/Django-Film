//!Actor List

console.log('Actor List')

//!Html require tags for search with ajax
const searchSubmitForm = document.getElementById('searchSubmitForm')
const currentUrl = window.location.href

//!Sender data POST request with ajax
const first_name_actor = document.getElementById('first_name_actor')
const last_name_actor = document.getElementById('last_name_actor')
const select_gender = document.getElementById('select_gender')
const select_duty = document.getElementById('select_duty')
const country_actor = document.getElementById('country_actor')


//!GetCookie
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



//!Select Gender Value
select_gender.addEventListener('change',(e)=>{
    e.preventDefault()
    select_gender.value = e.target.value
})

//!Selected Duty Value
select_duty.addEventListener('change',(e)=>{
    select_duty.value = e.target.value
})




//!Ajax part search form
searchSubmitForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    $.ajax({
        type: 'POST',
        url:currentUrl,
        data : {
            'csrfmiddlewaretoken':csrftoken,
            'first_name_actor':first_name_actor.value,
            'last_name_actor':last_name_actor.value,
            'select_gender':select_gender.value,
            'select_duty':select_duty.value,
            'country_actor':country_actor.value
        },
        success:function(response){
            console.log('Reaksiya verdi SUCCESS');
        },
        error:function(err){
            console.log('Xeta Bas Verdi')
        }
    })
})


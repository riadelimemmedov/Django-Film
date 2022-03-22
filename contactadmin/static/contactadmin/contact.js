//!Contact File Js

console.log('Hello Contact Js');

//!getCookie Function
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

////////////////////////////////

//!Send Post Request and Create Contact Data In With Ajax
const contactForm = document.getElementById('contact-form')
const contact_firstname = document.getElementsByName('contact_firstname')
const contact_lastname = document.getElementsByName('contact_lastname')
const contact_email = document.getElementsByName('contact_email')
const contact_message = document.getElementsByName('contact_message')
const currentUrl = window.location.href

console.log(contact_firstname)
console.log(contact_lastname)
console.log(contact_email)
console.log(contact_message)

//?inputlardaki plaholder deyeri yalniz id ile secilende isleyir name olanda kecersizidi yeni islemir placeholder
// const fsname = document.getElementById('fsname')
// console.log(fsname.placeholder)

contactForm.addEventListener('submit',(e)=>{//butonu secmeye ehtiyac yoxdur burda cunki butonun type deyeri submit verende ele form tagi beraber olur butonun ozune yeni bir sozle submit edende butonu secmeye ehtiyac yoxdur,sadece addEventListener('submit') yazmag kifayet edir
    e.preventDefault()
    $.ajax({
        type:'POST',
        url:currentUrl,
        data:{
            'csrfmiddlewaretoken':csrftoken,
            'salamcontact':'Salam Men Contact Ajaxdan Gelmisem'
        },
        success:function(response){
            console.log('Successfully Send POST CONTACT view')
        },
        error:function(err){
            console.log('Xeta Var Amk')
            console.log(err)
        }
    })
})
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


//!Send Post Request and Create Contact Data In With Ajax
const contactForm = document.getElementById('contact-form')
const contact_firstname = document.getElementsByName('contact_firstname')
const contact_lastname = document.getElementsByName('contact_lastname')
const contact_email = document.getElementsByName('contact_email')
const contact_message = document.getElementsByName('contact_message')
const contactButtonSend = document.getElementById('contactButtonSend')

const currentUrl = window.location.href

const contactErrorShow = document.getElementById('contact-error-show')


contactForm.addEventListener('submit',(e)=>{
    e.preventDefault()

    if(contact_message[0].value.length > 41){
        $.ajax({
            type:'POST',
            url:currentUrl,
            data:{
                'csrfmiddlewaretoken':csrftoken,
                'salamcontact':'Salam Men Contact Ajaxdan Gelmisem',
                'contact_message':contact_message[0].value.trim()
            },
            success:function(response){
                contactErrorShow.innerHTML = `
                <div class="alert alert-success text-center text-capitalize" style="text-transform: capitalize;border-radius:3px;outline:none;">
                    <strong style="color:black">Sucessfully Sent Request</strong>
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            `
                contactForm.reset()
            },
            error:function(err){
                console.log(err)
            }
        })
    }
    else{
        contactErrorShow.innerHTML = `
            <div class="alert alert-danger text-center text-capitalize" style="text-transform: capitalize;border-radius:3px;outline:none;">
                <strong style="color:black">Please Fill Textarea</strong>
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
        `
        contactForm.reset()
    }
    
})
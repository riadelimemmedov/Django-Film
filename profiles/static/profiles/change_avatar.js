//!Change Avatar Js
console.log('Hello Change Avatar Js')

const alertBox = document.getElementById('alert-box')
const imageBox = document.getElementById('image-box')
const imageForm = document.getElementById('image-form')
const confirmBtn = document.getElementById('confirm-btn')
const input = document.getElementById('id_avatar')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

let xchangeimagedata = imageBox.firstElementChild



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


input.addEventListener('change',()=>{

    console.log('Change Image From Input')
    const img_data = input.files[0]
    const url = URL.createObjectURL(img_data)
    imageBox.innerHTML = `<img src="${url}" id="image" style="width:50% !important;text-align: center;display: inline-block;" alt="">`


    var $image = $('#image');
    $image.cropper({
        aspectRatio: 16 / 9,
        crop: function (event) {
            console.log(event.detail.x);
            console.log(event.detail.y);
            console.log(event.detail.width);
            console.log(event.detail.height);
            console.log(event.detail.rotate);
            console.log(event.detail.scaleX);
            console.log(event.detail.scaleY);
        }
    });
    // Get the Cropper.js instance after initialized
    var cropper = $image.data('cropper')

    confirmBtn.addEventListener('click',()=>{
        cropper.getCroppedCanvas().toBlob((blob)=>{
            const fd = new FormData()
            fd.append('csrfmiddlewaretoken',csrftoken)
            fd.append('avatar',blob,'my-image.png')

            console.log('ddd',blob)

            //sendd post request
            $.ajax({
                type: 'POST',
                url:imageForm.action,
                enctype:'multipart/form-data',
                data:fd,
                success:function(response){
                    console.log(response.message)
                },
                error:function(err){
                    console.log(err)
                },
                cache:false,
                contentType:false,
                processData:false
            })

        })
    })

})


var $image = $('#image');
$image.cropper({
    aspectRatio: 16 / 9,
    crop: function (event) {
        console.log(event.detail.x);
        console.log(event.detail.y);
        console.log(event.detail.width);
        console.log(event.detail.height);
        console.log(event.detail.rotate);
        console.log(event.detail.scaleX);
        console.log(event.detail.scaleY);
    }
});

// Get the Cropper.js instance after initialized
var cropper = $image.data('cropper');

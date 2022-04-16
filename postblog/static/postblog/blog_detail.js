//!Blog Detail Js
console.log('Hello Blog Detail')

const commentLikeFormClass = document.getElementsByClassName('comment-like-form-class')
const currentUrl = window.location.href
const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log('Csrf Deyeri ', csrf[0].value)

for(let i=0;i<commentLikeFormClass.length;i++){
    commentLikeFormClass[i].addEventListener('submit',(e)=>{
        e.preventDefault()
        console.log('Send Request for like and unlike comment ',)
        //const commentId = e.target.id
        //console.log('Comment Id', commentId)
        //console.log('Clicked', e.target.firstElementChild.nextElementSibling)
        $.ajax({
            type: 'POST',
            url:e.target.action,
            data:{
                'csrfmiddlewaretoken':csrf[0].value,//hemise birinci bunu gonder sonra digerlerini,amma templatedede ehtiyat ucujn => {% csrf_token %} yaz
                'commentId':e.target.id
            },
            success:function(response){//burda response yazmalisan cunki gonderilen sorgudan url e ordan bize cavab geri donur yeni response geri donur
                console.log('Success Send Like And Unlike Comment Url')
                console.log(response)
            },
            error:function(err){
                console.log('Hata')
                console.log(err)
            }
        })
    })
}
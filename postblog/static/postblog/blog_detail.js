//!Blog Detail Js
console.log('Hello Blog Detail')

const commentLikeFormClass = document.getElementsByClassName('comment-like-form-class')
const commentlikeunlikecount = document.getElementById('commentlikeunlikecount')
const currentUrl = window.location.href
const csrf = document.getElementsByName('csrfmiddlewaretoken')


console.log(parseInt(commentlikeunlikecount.textContent)+5)

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
                console.log(response.liked)
                const like_unlike_btn = e.target
                if(response.liked == 'true'){
                    const imageButtonLike = like_unlike_btn.firstElementChild.nextElementSibling.firstElementChild
                    imageButtonLike.src = '/static/images/thumb-down.png'
                    let likeCount = parseInt(commentlikeunlikecount.textContent)
                }
                else if(response.liked == 'false'){
                    const imageButtonUnlike = like_unlike_btn.firstElementChild.nextElementSibling.firstElementChild
                    imageButtonUnlike.src = '/static/images/thumb-up.png'
                    let unlikeCount = parseInt(commentlikeunlikecount.textContent)
                }
                else{
                    console.log('Liked Error')
                }

                // const like_unlike_btn = document.getElementsByClassName('likeunlike')
                // for(let i=0;i<like_unlike_btn.length;i++){
                //     let x = like_unlike_btn[i].getAttribute('likeunlike-id')
                //     if(e.target.id == x || response.liked == 'true'){
                //         console.log('Like Oldu Comment')
                //         console.log(like_unlike_btn[i])
                //         break
                //     }
                //     //console.log(x)
                // }
                //console.log(like_unlike_btn)

                // let imagelikebtn = like_unlike_btn.firstElementChild.getAttribute('src')
                // imagelikebtn = 'images/thumb-down.png'
                // like_unlike_btn.innerHTML = imagelikebtn
            },
            error:function(err){
                console.log('Hata')
                console.log(err)
            }
        })
    })
}
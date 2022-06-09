//!Blog Detail Js
console.log('Hello Blog Detail')

const commentLikeFormClass = document.getElementsByClassName('comment-like-form-class')
let commentlikeunlikecount = document.getElementById('commentlikeunlikecount')
const currentUrl = window.location.href
const csrf = document.getElementsByName('csrfmiddlewaretoken')

//!Comment Like and Unlike
for(let i=0;i<commentLikeFormClass.length;i++){
    commentLikeFormClass[i].addEventListener('submit',(e)=>{
        e.preventDefault()
        console.log('Send Request for like and unlike comment ',)
        $.ajax({
            type: 'POST',
            url:e.target.action,
            data:{
                'csrfmiddlewaretoken':csrf[0].value,
                'commentId':e.target.id
            },
            success:function(response){
                console.log('Success Send Like And Unlike Comment Url')
                console.log(response.liked)
                const like_unlike_btn = e.target
                console.log('Like Count ', response.likecommentcount)
                let comment_like_count = ''
                if(response.liked == 'true'){
                    const imageButtonLike = like_unlike_btn.firstElementChild.nextElementSibling.firstElementChild
                    comment_like_count = e.target.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild
                    imageButtonLike.src = '/static/images/thumb-down.png'
                    comment_like_count.textContent = ''
                    comment_like_count.textContent = String(response.likecommentcount)
                }
                else if(response.liked == 'false'){
                    const imageButtonUnlike = like_unlike_btn.firstElementChild.nextElementSibling.firstElementChild
                    imageButtonUnlike.src = '/static/images/thumb-up.png'
                    comment_like_count = e.target.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.firstElementChild
                    comment_like_count.textContent = ''
                    comment_like_count.textContent = String(response.likecommentcount)
                }
                else{
                    console.log('Liked Error')
                }
            },
            error:function(err){
                console.log(err)
            }
        })
    })
}

//!Load More Comment

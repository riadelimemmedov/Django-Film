//!Actor List

console.log('Actor List')

//!Html require tags for search with ajax
const searchSubmitForm = document.getElementById('searchSubmitForm')
const currentUrl = window.location.href
const loadingrelatedfilmloader = document.getElementById('loadingrelatedfilmloader')
const search_result_data_hide = document.getElementById('search_result_data_hide')
const paginationpart = document.getElementById('paginationpart')
const foundactorcount = document.getElementById('found-actor-count')
const emptyvalueoferr = document.getElementById('emptyvalueoferr')
let changedurl = window.location.href.substring(0,window.location.href.lastIndexOf('/')).replace('actor','')



//!Sender data POST request with ajax
const first_name_actor = document.getElementById('first_name_actor')
const last_name_actor = document.getElementById('last_name_actor')
const select_gender = document.getElementById('select_gender')


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

// //!Selected Duty Value
// select_duty.addEventListener('change',(e)=>{
//     select_duty.value = e.target.value
// })

//!Username and Lastname test null or undefined



//!Ajax part search form
const searchDataWithAjax = ()=>{
    searchSubmitForm.addEventListener('submit',(e)=>{
        e.preventDefault()
        
        let active = true

        if(active){
            if(first_name_actor.value == '' || last_name_actor.value == ''){
                emptyvalueoferr.style.display='block'
                
                setTimeout(()=>{
                    emptyvalueoferr.style.display='none'
                },2000)
        
                active=false
            }
            else{
                $.ajax({
                    type: 'POST',
                    url:currentUrl,
                    data : {
                        'csrfmiddlewaretoken':csrftoken,
                        'first_name_actor':first_name_actor.value,
                        'last_name_actor':last_name_actor.value,
                        'select_gender':select_gender.value,
                    },
                    success:function(response){
                        console.log('Reaksiya verdi SUCCESS');
                        loadingrelatedfilmloader.firstElementChild.style.display = 'block'
                        paginationpart.style.display = 'none'
                        setTimeout(()=>{//setTimeOut 1500 yeni 1.5 saniye sonra isleyecek menasinda istifade olunur
                            const find_actor = response.find_actor
                            ////////////////////////////////////////////////////////////////
                            emptyvalueoferr.style.display='none'
                            loadingrelatedfilmloader.firstElementChild.style.display = 'none'
                            search_result_data_hide.innerHTML = ''
            
                            if(find_actor == undefined || find_actor==null ){
                                search_result_data_hide.innerHTML = `
                                    <div class="ui message" style="background-color:#E2E3E9;text-align:center !important;">
                                        <strong>No relevant info was found on this topic</strong>
                                    </div>`
                                setTimeout(()=>{
                                    search_result_data_hide.innerHTML = ''
                                },5000)
                                
            
                                
                                foundactorcount.firstElementChild.textContent = ''
                                foundactorcount.firstElementChild.textContent = `0 ` + 'celebrities'
                            }
            
                            //Add Data InnnerHtml
                            else{
                                foundactorcount.firstElementChild.textContent = ''
                                foundactorcount.firstElementChild.textContent = `${find_actor.length}` + 'celebrities'
                                find_actor.forEach((actor)=>{
                                    if(actor.duty_type_actor == 'Actorisa' && actor.gender_actor == 'F')//bu qadin bur aktyordur yeni => Actress dir
                                        actor.duty_type_actor = 'Actress'
                                    else if(actor.duty_type_actor == 'Actorisa' && actor.gender_actor == 'M'){
                                        actor.duty_type_actor = 'Actor'
                                    }
            
                                    let actorurl = window.location.href.substring(0,window.location.href.lastIndexOf('/')).concat(`/${actor.slug_actor}`)
                                    console.log('gelen aktyorun url deyeri slug ile', actorurl)
            
                                    //Bura if else if ve else qarismir sadece ordan gelen datani yazdirmag ucun istifade olunur
                                    search_result_data_hide.innerHTML += `
                                        <div class="col-md-12">
                                            <div class="ceb-item-style-2">
                                                <img src="${changedurl}media/${actor.image_actor}" style="width: 67px !important; height: 98px !important;" alt="">
                                                <div class="ceb-infor">
                                                    <h2><a href="${actorurl}">${actor.first_name_actor} &nbsp;${actor.last_name_actor}</a></h2>
                                                    <span> 
                                                            <span style="color: #ffffff !important;">${actor.duty_type_actor},&nbsp; ${actor.country_actor}</span>
                                                            <p>${actor.biography_actor.substring(0,100)}...</p>
                                                    </span>
                                                </div>
                                            </div>
                                        </div>
            
            
                                    `
                                })
                            }
            
            
                        },2000)
                    },
                    error:function(err){
                        console.log('Xeta Bas Verdi')
                    }
                })
            }
        }

        
    })
}

searchDataWithAjax()



//Actyorun gelib gelmemeyini yoxla ajaxda varsa goster yoxdusa xeta ver
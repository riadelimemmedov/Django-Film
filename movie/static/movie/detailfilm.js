//!Detail Film Html

console.log('Hello Film Detail')

//!Cut Year Only Find
const moviedate = String(document.getElementById('moviedate').textContent)
strdatasi = moviedate.split(',')//yeni vergule gore ayirib bir list yarat
let moviedatetext = document.getElementById('moviedate').textContent = ''
moviedatetext = strdatasi[1].trim()
document.getElementById('moviedate').innerHTML = moviedatetext


//!Sort By Film With Ajax
//!Loader atmag istesen ager => https://semantic-ui.com/elements/loader.html burdan gotur belke

const currenturl = window.location.href

const relatedfilmajax = document.getElementById('relatedfilmajax')
const sortlaformagore = document.getElementById('sortlaformagore')
const biletaliram = document.getElementById('biletaliram')
const filmsRelatedArea = document.getElementById('films-related-area')
const loadingrelatedfilmloader = document.getElementById('loadingrelatedfilmloader').firstElementChild
const allrelatedfilmlistdiv = document.getElementById('allrelatedfilmlistdiv')
//console.log(loadingrelatedfilmloader.classList);
const homeurl = window.location.href.substring(0,window.location.href.lastIndexOf('/'))//yeni en sonuncu / buna qederkini getir
const imageurl = `${homeurl}/media`
console.log(imageurl);


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


//!Burdan davam eleyerse InsaAllah
sortlaformagore.addEventListener('change',(e)=>{
    $.ajax({
        type: 'POST',
        url:currenturl,
        data:{
            'csrfmiddlewaretoken':csrftoken,
            'targetvalueselect':e.target.value,
        },
        success:function(response){
            const ratingdesc = response.ratingdesc //Burda sortlamag lazimdir gelen imdb deyerlerini azdan coxa dogru
            const ratingasc = response.ratingasc

            console.log('Siralanmamamis Json')
            const a = JSON.parse(ratingdesc)// => burda 14 kino var
            a.forEach(function(item){
                let x = (item['fields']['avarage_ibdm']);
                console.log(parseFloat(x))
            })

            console.log('Siralanmis Json')
            let z = a.slice().sort((a,b)=>b['fields']['avarage_ibdm']-a['fields']['avarage_ibdm'])
            z.forEach(function(item1){
                // console.log(item1['fields']['avarage_ibdm']);
                console.log(item1['fields']['avarage_ibdm'].length)
            })

            console.log('##########################################')
            let sorteddatata = JSON.parse(ratingdesc)
            //let netice =  sorteddatata.slice().sort((a,b)=>b.)
            console.log('Siralanmis Json')



            var isActive = true
            if(ratingdesc){
                console.log('Yalniz DESC Isledi')
                loadingrelatedfilmloader.classList.add('active')
                if(isActive == true){
                    setTimeout(()=>{
                        loadingrelatedfilmloader.classList.remove('active')
                        isActive = false
                        if(isActive==false){
                            //console.log('False olan hisse')
                            //console.log('Bura settime un 2 hissei deyesen')
                            //console.log('////////////////////////////////////////////////////////////////////////////////////////////////')
                            //console.log('Allrelated film dolu olanda',allrelatedfilmlistdiv)
                            //allrelatedfilmlistdiv.innerHTML = ''
                            //console.log('Allrelated bosaldi',allrelatedfilmlistdiv.innerHTML)
                            for(let i=0;i<ratingdesc.length;i++){
                                const description_movie = ratingdesc[i]['description_movie']
                                //console.log(description_movie.length)
        
                                
                                
                                // console.log(ratingdesc[i]['image_movie']);
                                // console.log(`${homeurl}/media/${ratingdesc[i]['image_movie']}`)
                                //console.log('Doludu Heleki')
                                allrelatedfilmlistdiv.innerHTML += `
                                
                                <div class="movie-item-style-2" id="films-related-area">
                                    <img src="${homeurl}/media/${ratingdesc[i]['image_movie']}" style="width: 170px;height: 261px;" alt="">
                                    <div class="mv-item-infor">
                                        <h6><a href="${homeurl}/${ratingdesc[i].slug_movie}">${ratingdesc[i].title_movie} &nbsp; <span id="moviedate">${ratingdesc[i].date_created_movie}</span></a></h6><!-- Burda bu deyer olmalidirki js terefine gedib split olunsun yeniden innerHtml ile span tagi yeni inline olan span taginin icine gomulsun -->
                                        <p class="rate"><i class="ion-android-star"></i><span class="filmajaxrayting">${ratingdesc[i].avarage_ibdm}</span> /10</p>
                                        <p class="describe">${ratingdesc[i].description_movie.substring(0,300)}</p>
                                        <p class="run-time"> Run Time: {{film.video_time}} .<span>MMPA: {{film.mmpa_rating_movie}} </span> .<span>Release: {{film.date_created_movie}}</span></p>

                                        <p>
                                            Director:
                                            {% for actor in film.actor_movie.all %}
                                                {% if actor.duty_type_actor == 'Director' %}	
                                                    <a href="{% url 'actor:actorDetailView' actor.slug_actor  %}">{{actor.first_name_actor|title}}&nbsp; {{actor.last_name_actor|title}}</a>,
                                                {% endif %}
                                            {% endfor %}
                                        </p>

                                        <p style="display: inline;">
                                            Stars: 
                                            {% for actor in film.actor_movie.all %}
                                                    {% if actor.duty_type_actor == 'Actorisa' %}
                                                        <a href="{% url 'actor:actorDetailView' actor.slug_actor  %}">{{actor.first_name_actor|title}}&nbsp; {{actor.last_name_actor|title}}</a>,
                                                    {% endif %}
                                            {% endfor %}
                                        </p>
                                    </div>
                                </div>
                            `
                            }
                            //e.target.value = ''//cunki optionsun value deyeri ele '' bos stringe beraberdir
                        }
                    },3000)}
                    

            }

                    
                    //allrelatedfilmlistdiv.classList.add('d-none')

            else if(ratingasc){
                console.log('Yalniz ASC isledi')
                console.log(ratingasc)
            }
        },
        error:function(err){
            console.log(err)
        }
    })
})


//!Api lari getirmek ucun yazilan kodlar
const tiklabutonu = document.getElementById('tiklabutonu')

tiklabutonu.addEventListener('click',(e)=>{
    axios.get('https://api.themoviedb.org/3/trending/all/day?api_key=6eb08bbd168a23902ff08b4d31a3c687')
        .then((response)=>{
            const resultFilms = response.data.results;
            resultFilms.forEach(function(rf,index){
                if(rf.original_title==undefined){

                }
                else{
                    const imageTag = rf.backdrop_path
                    const sekil = `https://image.tmdb.org/t/p/w500/${imageTag}`
                    const original_title = rf.original_title
                    console.log(`Gelen Sekiller: ${sekil}`);
                    console.log(`Titlelar Orginal: ${rf.title}`)
                    console.log(`Orginal Language : ${rf.original_language}`)
                    console.log(`Description : ${rf.overview}`)
                    console.log(`Popularity : ${rf.popularity}`)
                    console.log(`Release Date : ${rf.release_date}`)
                    console.log(`Vote Avarage : ${rf.vote_average}`)
                    console.log(`Vote Count : ${rf.vote_count}`)
                }
            })
        })
        .catch((err)=>{
            console.log(err);
        })
})


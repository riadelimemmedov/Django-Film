//!Blog Create Js 
console.log('hello blog create neyse ne')


//!Select Box Js 
const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");
const optionsList = document.querySelectorAll(".option");
const categoryblog = document.getElementById('categoryblog')

selected.addEventListener("click", () => {
    optionsContainer.classList.toggle("active");
});

optionsList.forEach(o => {
    o.addEventListener("click", () => {
        selected.textContent = o.querySelector("label").textContent;
        categoryblog.value = o.querySelector('label').textContent
        optionsContainer.classList.remove("active");
    });
});
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//!Crete Blog Part
const blogForm = document.getElementById('blog-form')
const titleBlog = document.getElementById('title-blog')
const tagBlog = document.getElementById('tag-blog')
const descriptionBlog = document.getElementById('description-blog')
const blogInputFile = document.getElementById('blog-input-file')
const selectImageButton = document.getElementById('select-image-button')
//const id_category_post = document.getElementById('id_category_post')
const id_category_post = document.getElementById('id_category_post') 

id_category_post.addEventListener('change',(e)=>{
    console.log(e.target.value)
})

console.log(id_category_post)

selectImageButton.addEventListener('click', (e)=>{
    e.preventDefault()
    try{
        blogInputFile.click()
    }
    catch{
        new Error('Xeta')
    }
})


blogInputFile.addEventListener('change',(e)=>{
    let a = e.target.files[0]
    let urlssekil = URL.createObjectURL(a)
    console.log(urlssekil)
})

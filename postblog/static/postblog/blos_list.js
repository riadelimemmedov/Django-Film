//!Blog List Js 
console.log('Hello Blog List')

const searchFormBlogFilm = document.getElementById('searchFormBlogFilm')
const searchedInputBlogFilm = document.getElementById('searchedInputBlogFilm')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const currentUrl =  window.location.href.substring(0,window.location.href.lastIndexOf('/'))

console.log(currentUrl)

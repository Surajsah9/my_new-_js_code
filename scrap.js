const fs = require('fs')
const jsdom=require('jsdom')
const { JSDOM } = jsdom;   
// const dict={}
const list=[]
const axios = require('axios') 
axios.get("https://www.imdb.com/chart/top/") 
.then(res=>{
    const t =res.data
    const tell = new JSDOM(t)
    dwindow.document.querySelectorAll('.titleColumn').forEach(link => {
      var r=link.textContent.trim("           ")
      var t=r.split("     ")
      // dict={"rank":t[0].replace(".\n","")}
      // dict={"year":t[-1].replace("  ","")}
      dict={"movie_name":t[1].replace("\n","")}
      // t.remove(' ')
      // t.remove(t[0])
      // t.remove(t[-1])
      console.log(dict)
      // list.push(dict)
      })
      // console.log(list)
}) 


// const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
// console.log(dom.window.document.querySelector("p").textContent);

// (async () => {
//     const response = await fetch('https://www.imdb.com/chart/top/');
//     const text = await response.text();
//     console.log(text.match(/(?<=\<h1>).*(?=\<\/h1>)/));
//   })()




// axios.get("https://www.imdb.com/chart/top/") 
// .then(res=>{
//     const t =res.data
// const cheerio = require('cheerio');
// const $ = cheerio.load(t);
// console.log($.html())

// console.log($.textContent)






























// const fs = require('fs')     
// // const axios = require('axios') 
// fetch.get("https://www.imdb.com/chart/top/")
// .then(hello=>console.log(hello)) 
// .then(res=>{
//     const t =res.data
//     console.log(t)
// })
// .catch(err=>console.log(err)) 
const axios = require('axios');

const fs = require('fs');
axios.request("https://www.imdb.com/chart/top/")
.then((re)=>{
    for(i in res){
        console.log(i.text)
    }
})
.catch((error)=>{
    console.log("error")
})

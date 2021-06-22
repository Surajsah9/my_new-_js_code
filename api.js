var link="https://saral.navgurukul.org/api/courses" //link to take json data by Api
const fs = require('fs')     // file system to store data
const axios = require('axios') //tool for taking data
// const prompt = require('prompt-sync')({sigint: true});
var b=[]
var d=[]
var f=[]
var c={}
// const we=prompt("i")
function req(){
axios.get(link)   //data we have taken
  .then(function (response) {  //promise to manage error
    for(i in response["data"]["availableCourses"]){
        y=response["data"]["availableCourses"][i]["id"]
      // var we=prompt("input ")
      
        var l=`http://saral.navgurukul.org/api/courses/${74}/exercise/getBySlug?slug=requests__using-json`
        axios.get(`https://saral.navgurukul.org/api/courses/${74}/exercises`)
        .then((sun)=>{ 
          c["detail"]=console.log(sun["data"]["data"])
          for(uu in sun["data"]["data"]){
            console.log(sun["data"]["data"][uu]["childExercises"])
            var nnn=sun["data"]["data"][uu]["childExercises"]
          }
          fs.writeFileSync('suraj/content2.json',"Utf8", d, err => {   //data saving in file
            if (errr) {
              console.error(errr)
               }
              })
        })
        .catch(function (err) {    //catch if we get rejection from web
          console.log(err)})
        axios.get(l)
        .then(function (res) {
          b.push(res["data"]["content"])})
        .catch(function (err) {
            console.log(err)})
       .then(() => {
        fs.writeFile('suraj/content2.json', d, err => {   //data saving in file
          if (err) {
            console.error(err)
             }
        });
       })
      }
  })
  .catch(function (error) {
    console.log(error)
  })
};
req()
// fs.readFile('suraj/suyaa.json', 'utf8' , (err, data) => {
//   if (err) {
//     console.error(err)
//     return
//   }
//   console.log(data)
// // })

// fs.writeFile('suraj/test.json', r, err => {
//   if (err) {
//     console.error(err)
//     return
//   }
// })
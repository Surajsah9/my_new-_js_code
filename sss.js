const axios = require('axios');
axios.get('https://docs.google.com/presentation/d/1ulgJCwI0HSSKz_9osj7uq7OBlgFWAB_IZZZYzKTx6Y4/edit#slide=id.p')
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  })
//   .then(function () {
//     // always executed
//   });
// // var link="https://saral.navgurukul.org/api/courses"
// const fs = require('fs')
// const axios = require('axios')
// axios.get(link)
// .then(function (response) {
//     console.log(response)})
//     for(i in response["data"]["availableCourses"]){
//         consol.log(response["data"]["availableCourses"][i]["id"])
//     }
//   })
  
import { Meteor } from 'meteor/meteor';
import { HTTP } from 'meteor/http';
import { Asteroids } from '../imports/api/asteroids.js'



Meteor.publish('asteroids', function asteroidsPublication() {
  return Asteroids.find();
});

Meteor.methods({
  loadAsteroids: function() {
    console.log("loadAsteroids");
    HTTP.call('GET', 'https://api.nasa.gov/neo/rest/v1/feed', {
      params: { api_key: "NJX1NFkrMnJrkBPTX3MMJ2Yk0PMIjnbwdD2ndnw1", start_date:"2017-10-17", end_date:"2017-10-24" }
    }, (error, result) => {
      if (!error) {

        var data = result.data;
        console.log(data["near_earth_objects"])


        for (var obj in data["near_earth_objects"]) {
          
          console.log(obj)
          for (var i = 0; i < data["near_earth_objects"][obj].length; i++) {
            console.log(data["near_earth_objects"][obj][i].name);
            Asteroids.insert({text:data["near_earth_objects"][obj][i].name, date:new Date()})
          }
        }

        // for (var i=0; i < result.content.length; i++) {
        //   console.log(result.content[i].name);
        // }
      }
    });
  }
})


Meteor.startup(() => {
  // code to run on server at startup


});
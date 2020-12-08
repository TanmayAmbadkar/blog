fetch('http://localhost:8000/get_posts').then(function(response){

  return response.json();

 }).then(function(jsondata){

  console.log(jsondata);

 });


var dbPromise = idb.open('posts-db', 1, function(upgradeDb) {

 upgradeDb.createObjectStore('posts',{keyPath:'pk'});

});



fetch('http://localhost:8000/get_posts').then(function(response){

  return response.json();

 }).then(function(jsondata){

  dbPromise.then(function(db){

   var tx = db.transaction('posts', 'readwrite');
     var feedsStore = tx.objectStore('posts');

     for(var key in jsondata){

      if (jsondata.hasOwnProperty(key)) {

        feedsStore.put(jsondata[key]);

      }

     }

  });

 });

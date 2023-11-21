
f = document.forms[0];
title = f[0];
type = f[1];
search = f[2];
var str;
var stranica = 1;

var movies = document.querySelector('#movies')
var film_info = document.createElement('DIV');
var h = document.createElement('H4');
var films;


search.addEventListener('click',findMovie);

function findMovie() {
    movies.innerHTML = '';    
    film_info.innerHTML='';
    film_info.className = '';
    h.innerHTML = '';

    str = 'https://www.omdbapi.com/?apikey=de2cff15&Type='+type.value+'&s='+title.value+'&page='+stranica;
    var request = new XMLHttpRequest();
    request.open('GET',str);
    request.onload = function() {
        if (request.status != 200){
            alert("Ошибка " + request.status + ": " + request.statusText);     
        }
        else {
            var res=request.response;
            getResult(res);       
        }
    }   
    request.send();
    
}


function getResult(res) {

    if (JSON.parse(res).Response==="False"){

        var film = document.createElement('DIV');
        film.className = 'not';
        film.textContent = 'Movie not found!'
        movies.append(film);
        lenta.style.display = 'none';
    }
    else {
        var obj = JSON.parse(res);   
        films = obj.Search;
        for (var i of films){

            var film = document.createElement('DIV');
            film.className = 'film';
            movies.append(film);

            var img = document.createElement('IMG');
            img.src = i.Poster;
            film.append(img);


            var p = document.createElement('P');
            p.id = 'inf';
            p.innerHTML = type.value+'<br><br><b>'+i.Title+'</b><br><br>'+i.Year;
            film.append(p);

            var details = document.createElement('INPUT');
            details.type = 'button';
            details.value = 'Details';
            details.className ='details';
            film.append(details);

            var full_str;
            details.addEventListener('click', createDetailsHandler(i));
            function createDetailsHandler(filmData) {
                return function() {
                    
                    full_str = 'https://www.omdbapi.com/?apikey=de2cff15&t='+filmData.Title;
                    var request_full = new XMLHttpRequest();
                    request_full.open('GET',full_str);
                    request_full.onload = function() {
                        if (request_full.status != 200){
                            alert("Ошибка " + request_full.status + ": " + request_full.statusText);     
                        }
                        else {
                            var res_full=request_full.response;
                            getFullResult(res_full);
                          
                        }
                    }   
                    request_full.send();
                    
                }   


                    function getFullResult(res_full)  {

                        film_info.innerHTML='';
                        h.innerHTML = '';

                        var obj_f = JSON.parse(res_full)
                    
                        h.innerHTML = '<br>Film info:';
                        document.body.append(h)

                        film_info.className = 'film_info';
                        document.body.append(film_info)

                        var img_big = document.createElement('IMG');
                        img_big.src = filmData.Poster;
                        img_big.className ='img_big';
                        film_info.append(img_big);
                       
                        var text = '<table><tr><td>Title:</td><td>'+obj_f.Title+'</td></tr><tr><td>Released:</td><td>'+obj_f.Released+'</td></tr><td>Genre:</td><td>'+obj_f.Genre+'</td></tr></tr><td>Country:</td><td>'+obj_f.Country+'</td></tr></tr><td>Director:</td><td>'+obj_f.Director+'</td></tr></tr><td>Writer:</td><td>'+obj_f.Writer+'</td></tr></tr><td>Actors:</td><td>'+obj_f.Actors+'</td></tr></tr><td>Awards:</td><td>'+obj_f.Awards+'</td></tr></table>'
                        var tb = document.createElement('DIV');
                        tb.innerHTML = text;
                        var table = tb.querySelector('table');
                        film_info.append(table);

                    }
                    
                }
            }
        }

        var lenta = document.createElement('DIV');
        lenta.id = 'lenta';
        movies.append(lenta)
        

        total=JSON.parse(res).totalResults;
        console.log(total)
        prev = document.createElement('DIV');
        prev.className='btn';
        lenta.append(prev)
        prev.textContent ='<<'
        prev.id = 'prev';

        for (var i=0;i<total/10;i++) {
            btn = document.createElement('DIV');
            btn.className='btn'; 
            lenta.append(btn);
            btn.textContent = i+1;
            if (i>8){
                btn.style.display = 'none';
            }
        }
        next = document.createElement('DIV');
        next.className='btn';
        lenta.append(next)
        next.textContent ='>>'
        next.id = 'next';
        next.addEventListener('click',runNext);
        prev.addEventListener('click',runPrev);

        var page = lenta.children;
        countNext = 10;
        var start;
        function runNext() {
            if(total<100){
                next.removeEventListener('click',runNext)
            }
            else {
            for (var i=1;i<page.length-1;i++){
                if(page[i].style.display != 'none'){
                    page[i].style.display = 'none';
                   
                }
            }
            for (var i=countNext; i<countNext+10;i++){
                page[i].style.display = 'block';
            }
            countNext+=10 
            }
    }
        function runPrev() {
            for (var i=1;i<page.length-1;i++){
                if (page[i].style.display != 'none'){
                    start = i;
                    break;
                }         
            }
            for (var i=1;i<page.length-1;i++){
                if(i>=start-10 && i<start){
         
                    page[i].style.display = 'block';
                }
                else{
                    if(i>10){
                    page[i].style.display = 'none'}
                }
            }
        }


        for (var i=1;i<page.length-1;i++){
            page[i].onclick = function (e){
                sel = e.target             
                    movies.innerHTML = '';    
                    film_info.innerHTML='';
                    film_info.className = '';
                    h.innerHTML = '';
                    str = 'https://www.omdbapi.com/?apikey=de2cff15&Type='+type.value+'&s='+title.value+'&page='+sel.textContent;
                    var request = new XMLHttpRequest();
                    request.open('GET',str);
                    request.onload = function() {
                        if (request.status != 200){
                            alert("Ошибка " + request.status + ": " + request.statusText);     
                        }
                        else {
                            var res=request.response;
                            getResult(res);    
                            console.log(res)   
                        }
                    }   
                    request.send();
                    
                
            }

            
        }

      







}






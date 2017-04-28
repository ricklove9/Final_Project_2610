var doSomething = function(me){
    
    if(me.textContent == "JavaScript"){
        me.textContent = "Again for Random#"
    }
    
    else{
        var num = Math.floor((Math.random()*100)+1)
        me.textContent= num;
    }
    
    
}
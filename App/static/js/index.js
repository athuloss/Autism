function readmore(element) { 

    var a = element.querySelector('.paragraph').style.height
    var b = element.querySelector(".blogbutton")
    var icon1 = '<ion-icon name="arrow-down-outline"></ion-icon>'
    var icon2 = '<ion-icon name="arrow-up-outline"></ion-icon>'
    
    if(b.classList.contains('more')){
        element.querySelector('.blogbutton').classList.add('less')
        element.querySelector('.blogbutton').classList.remove('more')
        element.querySelector('.paragraph').style.height = "fit-content";
        element.querySelector(".blogbutton").innerHTML ="Read Less "+icon2
    }
    else{
        element.querySelector('.paragraph').style.height = "65px"
        element.querySelector(".blogbutton").innerHTML = " Read More "+icon1 
        element.querySelector('.blogbutton').classList.add('more')
        element.querySelector('.blogbutton').classList.remove('less')
    }   
    }
    
    function showLogin() {
        document.querySelector(".login_wrapper").style.display = "flex";
    }
    
    function closeLogin() {
        document.querySelector(".login_wrapper").style.display = "none";
    }
    
    function showsignup() {
        document.querySelector(".signup_wrapper").style.display = "flex";
    }
    function closesignup() {
        document.querySelector(".signup_wrapper").style.display = "none";
    }
    function reshowLogin() {
        document.querySelector(".signup_wrapper").style.display = "none";
        document.querySelector(".login_wrapper").style.display = "flex";
    }
    
    function reshowsignup() {
        document.querySelector(".signup_wrapper").style.display = "flex";
        document.querySelector(".login_wrapper").style.display = "none";
    
    }
    function gameload(reload){
        var count=0;
        
    }
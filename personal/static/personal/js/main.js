//Grab Dom Items

const menubtn = document.querySelector('.menu-btn');
const menu = document.querySelector('.menu');
const menunav = document.querySelector('.menu-nav');
const menuitem = document.querySelectorAll('.menu-item');

//Set initial state of menu
let showmenu = false;

//add event in menubtn
menubtn.addEventListener('click', toggleMenu);

//build function to controll menu
function toggleMenu() {
    if(!showmenu) {
        menubtn.classList.add('close');
        menu.classList.add('show');
        menunav.classList.add('show');
        menuitem.forEach(item => item.classList.add('show'));
    
        //set menu state
        showmenu = true;

    } else {
        menubtn.classList.remove('close');
        menu.classList.remove('show');
        menunav.classList.remove('show');
        menuitem.forEach(item => item.classList.remove('show'));
        
        //set menu state
        showmenu = false;
    
    }
} 

//return top
function reTop() {
    document.documentElement.scrollTop = 0;
}
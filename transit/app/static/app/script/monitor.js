
// get dom element this script depend on.
const body = document.querySelector('body');
const copyButtons = document.querySelectorAll('.para > img');
const removeButtons = document.querySelectorAll('.remove > button');
const links = document.querySelectorAll("#nav > span");
const notify = document.querySelector("#notify > p");
const confirm = document.querySelector("#confirm");
const summary = document.querySelectorAll('summary');
const tripBoxs = document.querySelectorAll("details");
const header = document.querySelector('body > header');
const logo = document.querySelector('#logo');


// document current scroll
let domScroll;


for (let elem of summary) {
   elem.addEventListener('click', open, {once: true});
}
 
for (let elem of copyButtons) {
    elem.addEventListener('click', copy);
 }
 

for (let elem of removeButtons) {
   elem.addEventListener('click', remove);
 }

// set the style prop of active nav button 
for (let elem of links) {
  elem.addEventListener("click", (e) => {
    let elem = e.target;
    let children = elem.parentElement.children;
    for (let child of children) {
      if (child == elem) {
         child.className = "active";
         window.location.assign(child.dataset.url);
      }else {
         child.className = "";
      }
    }
  });
}


function open(e) {
  let elem = e.target;
  let detail = elem.parentElement;
  body.style.overflowY = "hidden";
  logo.parentElement.style.pointerEvents = "none";
  for (let elem of links) {
    elem.style.pointerEvents = "none";
  }
  for (let elem of tripBoxs) {
    if (elem == detail) {
      elem.style.boxShadow = "10px 10px 5px #888888";
      elem.querySelector('#more').scroll(0, 0);
    } else {
      elem.style.pointerEvents = "none";
      elem.style.filter = "blur(1px)";
    }
  }
  header.style.filter = "blur(1px)";
  elem.addEventListener('click', close, {once:true});
    setTimeout(() => {
      domScroll = document.documentElement.scrollTop;
      scroll(detail);
    }, 250);
} 


function close(e) {
  let elem = e.target;
  let parent = elem.parentElement;
  body.style.overflowY = "auto";
  logo.parentElement.style.pointerEvents = "auto";
  document.documentElement.scroll({
     top: domScroll,
     left: 0,
     behaviour: 'smooth'
  });
  for (let elem of links) {
    elem.style.pointerEvents = "auto";
  }
  header.style.filter = "blur(0)";
  for (let elem of tripBoxs) {
    if (elem == parent) {
      elem.style.boxShadow = "";
    } else {
      elem.style.filter = "blur(0)";
      elem.style.pointerEvents = "auto";
    }
  }
  elem.addEventListener('click', open, {once:true});
}


// scroll the dom relative to a trip coord.
function scroll(cont) {
   let box = cont.getBoundingClientRect();
   let headHeight = document.querySelector('body > header').offsetHeight;
   let scrollby = box.top + window.pageYOffset - headHeight - 10;
   document.documentElement.scroll({
       top: scrollby,
       left: 0,
       behaviour: 'smooth'
   });
 }
 
 
 
 
// copy a particular trip id within a trip box.
function copy(e) {
   let elem = e.target;
   let parent = elem.parentElement;
   let parentNodes = parent.children;
   let id = elem.dataset.id.trim();
   let copied = parentNodes[2];
  
   navigator.clipboard.writeText(id).then(() => {
     copied.style.animationPlayState = "running";
     copied.addEventListener('animationend', resetAnime, {once: true});
  }, () => {
      return null;
  });
   
 }



 // remove a trip box with a simple animation.
 function remove(e) {
   let elem = e.target;
   let name = elem.dataset.name;
   
   let ancestor1 = elem.parentElement.parentElement.parentElement;
   let ancestor2 = ancestor1.parentElement;
   let sibling = elem.parentElement.children[1];
   
   document.querySelector("#confirmMsg > span").innerHTML = name;
   confirm.showModal();
   let button = confirm.querySelector('#continue');
   
   button.addEventListener('click', () => {
     sibling.style.animationPlayState = 'running';
     // simulate server request.
     setTimeout(timeIt, 3000);
     
     function timeIt() {
       resetAnime(sibling);
       body.style.overflowY = "auto";
       header.style.filter = "blur(0)";
       for (let elem of tripBoxs) {
           elem.style.filter = "blur(0)";
           elem.style.pointerEvents = "auto"
       }
       ancestor2.style.animationPlayState= "running";
       ancestor1.style.height = "200px";
       ancestor2.addEventListener('animationend', (e) => {
         notify.parentElement.style.display = 'block';
         notify.style.animationPlayState = "running";
         notify.childNodes[1].innerHTML = name;
         notify.childNodes[2].data = " trip closed successfully";
         notify.addEventListener("animationend", resetNotify, {once:true});
         let elem = e.target;
         elem.style.display = "none";
        }, {once:true});
      }
      
   }, {once:true});

 }
 
 
 // reset style animation for passed in element.
 function resetAnime(e) {
     let elem = e.target ?? e;
     elem.style.animation = "none";
     elem.offsetWidth;
     elem.style.animation = null;
  }
  
  
 // reset notify element after notification.
 function resetNotify(e) {
     let elem = e.target;
     let eventArray = ['touchstart', 'scroll', 'click'];
     for (let event of eventArray) {
       document.addEventListener(event, () => {
          resetAnime(elem);
          elem.parentElement.style.display = 'none';
       }, {once:true});
     }
     setTimeout(() => {
       resetAnime(elem)
       elem.parentElement.style.display = 'none';
     }, 4000);
  }
 
 
 
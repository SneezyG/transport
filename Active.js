
const body = document.querySelector('body');
const cancel = document.querySelectorAll('.button');
const summary = document.querySelectorAll('summary');
const copyButtons = document.querySelectorAll('.para > img');
const removeButtons = document.querySelectorAll('.remove');
const copied = document.querySelectorAll('.copy');
const scan = document.querySelectorAll('.para > span');
const not_found = document.querySelector('#not_found');
const barcontainer = document.querySelector('#barcode');
const chat = document.querySelectorAll('#chat');




for (let elem of cancel) {
  elem.addEventListener('click', bodyreset);
 }

 for (let elem of summary) {
    elem.addEventListener('click', open, {once:true});
 }
 
 for (let elem of copyButtons) {
    elem.addEventListener('click', copy);
 }
 
 
 for (let elem of scan) {
    elem.addEventListener('click', lookup);
 }
 
 for (let elem of chat){
    elem.addEventListener('click', openchat);
 }
 
 
 
 
 
 function openchat(e) {
   elem = e.target;
   child1 = elem.children[0];
   child2 = elem.children[1];
   child2.style.display = "none";
   
   child1.style.animationPlayState = "running";
   child1.addEventListener('animationend', () => {
     child1.style.display = "none";
     elem.style.animationPlayState = "running";
     elem.style.backgroundColor = "green";
     elem.addEventListener('animationend', () => {
       
     }, {once:true})
   }, {once:true});
   
 }
 
 
 
 
 function lookup() {
   not_found.showModal();
   //barcontainer.showModal();
   body.style.overflow = "hidden";
 }
 
 
 
 
 
 function open(e) {
    let elem = e.target;
    for (let child of elem.children) {
      let tag = child.tagName;
      //console.log(tag);
      if (tag != "SPAN") {
        child.style.visibility = "hidden";
      }
    }
    elem.addEventListener('click', close, {once:true});
 }
 
 
 
 function close(e) {
    let elem = e.target;
    for (let child of elem.children) {
      child.style.visibility = "visible";
    }
    elem.addEventListener('click', open, {once:true});
 }
 
 
 
 function copy(e) {
   let elem = e.target;
   let parent = elem.parentElement;
   let parentNodes = parent.children;
   let id = parentNodes[0].innerHTML.trim();
   let copied = parentNodes[2];
   // console.log(id);
   
   navigator.clipboard.writeText(id).then(() => {
     copied.style.animationPlayState = "running";
     copied.addEventListener('animationend', resetAnime, {once:true});
  }, () => {
      return null;
  });
   
 }




 function resetAnime(e) {
     let elem = e.target;
     elem.style.animation = "none";
     elem.offsetWidth;
     elem.style.animation = null;
 }
 
 
function bodyreset() {
   body.style.overflow = "auto";
 }
 
 
 
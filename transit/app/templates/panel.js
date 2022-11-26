

const body = document.querySelector('body');
const summary = document.querySelectorAll('summary');
const copyButtons = document.querySelectorAll('.para > img');
const scan = document.querySelectorAll('.para > span');
const not_found = document.querySelector('#not_found');
const barcontainer = document.querySelector('#barcode');
const phone = document.querySelectorAll(".phone");
const contactList  = document.querySelectorAll(".no > span");



 for (let elem of summary) {
    elem.addEventListener('click', open);
 }
 
 for (let elem of copyButtons) {
    elem.addEventListener('click', copy);
 }

 
 for (let elem of scan) {
    elem.addEventListener('click', lookup);
 }
 
 for (let elem of phone) {
    elem.addEventListener('click', () => {
      elem.style.animationPlayState = "running";
      elem.addEventListener("animationend", resetPhone, {once:true});
    });
 };
 
 for (let elem of contactList) {
   elem.addEventListener("click", copyContact);
 }
 
 
 function copyContact(e) {
   let elem = e.target
   let copy = e.target.parentElement.lastElementChild;
   let contact = elem.innerHTML.trim()
   navigator.clipboard.writeText(contact).then(() => {
     console.log("contact");
     copy.style.animationPlayState = "running";
     copy.addEventListener('animationend', resetAnime, {once:true});
  }, () => {
      return null;
  });
 }
 

 
 
 function lookup() {
   //let model = barcontainer;
   let model = not_found;
   model.showModal();
   let child = model.children[1].children[0].children[0];
   body.style.overflow = "hidden";
   child.addEventListener('click', () => {
     body.style.overflow = "auto";
   }, {once:true});
 }
 
 
 
 
 
 function open(e) {
    let elem = e.target;
    for (let child of elem.children) {
      let tag = child.tagName;
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
 }
 
 
 
 function copy(e) {
   let elem = e.target;
   let parent = elem.parentElement;
   let childNodes = parent.children;
   let id = elem.dataset.id.trim();
   let copied = childNodes[2];
   
   navigator.clipboard.writeText(id).then(() => {
     copied.style.animationPlayState = "running";
     copied.addEventListener('animationend', resetAnime, {once:true});
  }, () => {
      return null;
  });
   
 }



 function resetAnime(e) {
     let elem = e.target ?? e;
     elem.style.animation = "none";
     elem.offsetWidth;
     elem.style.animation = null;
 }
 
 
 
 function resetPhone(e) {
    let elem = e.target;
    let parent = elem.parentElement;
    let contact = parent.children[1];
    let cancel = contact.lastElementChild;
    contact.style.display = "block";
    cancel.addEventListener('click', () => {
       contact.style.display = "none";
    });
    resetAnime(elem);
 }
 
 
 
 
 
 

 
 
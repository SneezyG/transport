

// get the dom element this script depend on.
const body = document.querySelector('body');
const summary = document.querySelectorAll('summary');
const copyButtons = document.querySelectorAll('.para > img');
const scan = document.querySelectorAll('.para > span');
const barcontainer = document.querySelector('#barcode');
const phone = document.querySelectorAll(".phone");
const contactList  = document.querySelectorAll(".no > span");
const codeCont = document.querySelector("#qrCode");
const closeQr = document.querySelector("#close");
const map = document.querySelector("#map");
const mapCont = document.querySelector("#map > div");
const locationBtn = document.querySelectorAll("article button");
const backdrop = document.querySelector("#backdrop");



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
 
 for (let button of locationBtn) {
   button.addEventListener("click", () => {
        map.open = true;
        backdrop.style.visibility = 'visible';
        body.style.overflow = 'hidden';
        map.style.animationPlayState = "running";
        map.addEventListener("animationend", () => {
          mapCont.style.visibility = "visible";
        });
    });
 }
  
  backdrop.addEventListener('click', () => {
      map.open = false;
      backdrop.style.visibility = 'hidden';
      mapCont.style.visibility = "hidden";
      body.style.overflow = 'visible';
      // reset dialog animation.
      map.style.animation = "none";
      map.offsetWidth;
      map.style.animation = null;
  });
 
 
 
 // copy contact within a particular trip box.
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
 

 
 
 // generate a barcode for a trip id.
 function lookup(e) {
   // remove previous barcode
   codeCont.replaceChildren();
   let data = e.target.innerHTML.trim()
   var qrcode = new QRCode(codeCont, {
        text: data,
        colorDark : "#000000",
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    });
   barcontainer.showModal();
   body.style.overflow = "hidden";
   closeQr.addEventListener('click', () => {
     body.style.overflow = "auto";
   }, {once:true});
 }
 
 
 
 
 // hide some trip info on trip box open.
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
 
 
 // show some trip info on trip box close.
 function close(e) {
    let elem = e.target;
    for (let child of elem.children) {
      child.style.visibility = "visible";
    }
 }
 
 
 // copy trip id within a particular trip box.
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


// reset style animation of element.
 function resetAnime(e) {
     let elem = e.target ?? e;
     elem.style.animation = "none";
     elem.offsetWidth;
     elem.style.animation = null;
 }
 
 
 
 // show the contact tab within a trip box.
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
 
 
 
 
 
 

 
 
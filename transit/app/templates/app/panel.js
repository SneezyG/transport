

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
const notify = document.querySelector("#notify > p");
const markButtons = document.querySelectorAll('.mark');
const articleConts = document.querySelectorAll('#article');
const confirm = document.querySelector("#confirm");


// set the display value for the first article.
for (let cont of articleConts) {
   let article = cont.querySelector('article');
   let seemore = cont.querySelector('#seeMore');
   let seeless = cont.querySelector('#seeLess');
   article.style.display = 'block';
   
   seemore.addEventListener('click', () =>{
     let articles = cont.querySelectorAll('article');
     for (let elem of articles) {
        setTimeout(() => {
          elem.style.display = 'block';
          seemore.style.display = "none";
          seeless.style.display = "block";
        }, 100);
     }
   });
   
   seeless.addEventListener('click', () =>{
     let articles = cont.querySelectorAll('article');
     let firstArticle = cont.querySelector('article');
     for (let elem of articles) {
        setTimeout(() => {
          elem.style.display = 'none';
          if (elem == firstArticle) {
            firstArticle.style.display = "block";
          }
          seemore.style.display = "block";
          seeless.style.display = "none";
        }, 100);
     }
   });
  
}


for (let elem of markButtons) {
   elem.addEventListener('click', mark);
 }

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
        }, {once:true});
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
    let parent = elem.parentElement;
    for (let child of elem.children) {
      child.style.visibility = "visible";
    }
    
    let articles = parent.querySelectorAll('article');
    let firstArticle = parent.querySelector('article');
    let seemore = parent.querySelector('#seeMore');
    let seeless = parent.querySelector('#seeLess');
    for (let elem of articles) {
        setTimeout(() => {
          elem.style.display = 'none';
          if (elem == firstArticle) {
            firstArticle.style.display = "block";
          }
          seemore.style.display = "block";
          seeless.style.display = "none";
        }, 100);
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
    }, {once:true});
    resetAnime(elem);
 }
 
 
 function mark(e) {
   let parent = e.target.parentElement;
   let name = parent.dataset.name;
   let update = parent.lastElementChild;
   
   document.querySelector("#confirmMsg > span").innerHTML = name;
   confirm.showModal();
   let button = confirm.querySelector('#continue');
   
   button.addEventListener('click', () => {
     update.style.animationPlayState = "running";
     setTimeout(() => {
        resetAnime(update);
        notify.style.animationPlayState = "running";
        notify.childNodes[1].innerHTML = name;
        notify.addEventListener("animationend", resetNotify, {once:true});
     }, 5000);
   }, {once:true});
   
 }

  
 // reset notify element after notification.
 function resetNotify(e) {
     let elem = e.target;
     setTimeout(() => resetAnime(elem), 4000);
  }

 // reset notify element after notification. 
 document.addEventListener('click', () => {
    resetAnime(notify);
 });
 
 
 
 
 
 
 
 

 
 
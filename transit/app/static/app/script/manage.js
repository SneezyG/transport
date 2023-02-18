

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
const mapCont = document.querySelector("#mapCont");
const map = document.querySelector("#map");
const locationBtn = document.querySelectorAll("article button");
const backdrop = document.querySelector("#backdrop");
const notify = document.querySelector("#notify > p");
const markButtons = document.querySelectorAll('.mark');
const articleConts = document.querySelectorAll('#article');
const confirm = document.querySelector("#confirm");
const tripBoxs = document.querySelectorAll("details");
const header = document.querySelector('body > header');
const logo = document.querySelector('#logo');


// document current scroll
let domScroll;




// set the display prop for the first article.
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
    elem.addEventListener('click', open, {once: true});
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
      elem.addEventListener("animationend", setPhone, {once:true});
    });
 };
 
 for (let elem of contactList) {
   elem.addEventListener("click", copyContact);
 }
 
 // show map associated with a report.
 for (let button of locationBtn) {
   button.addEventListener("click", (e) => {
        let elem = e.target;
        let lat = Number(elem.dataset.lat);
        let long = Number(elem.dataset.long);
        let coord = [long, lat];
        mapCont.open = true;
        backdrop.style.visibility = 'visible';
        mapCont.style.animationPlayState = "running";
        mapCont.addEventListener("animationend", () => {
          //alert(coord);
          mapConstruct(coord);
          map.style.visibility = "visible";
        }, {once:true});
    });
 }
  
  backdrop.addEventListener('click', () => {
      mapCont.open = false;
      backdrop.style.visibility = 'hidden';
      map.style.visibility = "hidden";
      // reset dialog animation.
      mapCont.style.animation = "none";
      mapCont.offsetWidth;
      mapCont.style.animation = null;
      
      // remove the previous map
      map.replaceChildren();
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
        colorLight : "#D3D3D3",
        correctLevel : QRCode.CorrectLevel.H
    });
   barcontainer.showModal();
 }
 
 
 
 
 // hide some trip info on trip box open.
 function open(e) {
    let elem = e.target;
    body.style.overflowY = "hidden";
    logo.parentElement.style.pointerEvents = "none";
    let detail = elem.parentElement;
    
    elem.querySelector('p > sub').style.display = "none";

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
 
 
 // show some trip info on trip box close.
 function close(e) {
    body.style.overflowY = "auto";
    logo.parentElement.style.pointerEvents = "auto";
    header.style.filter = "blur(0)";
    document.documentElement.scroll({
       top: domScroll,
       left: 0,
       behaviour: 'smooth'
    });

    let elem = e.target;
    let parent = elem.parentElement;

    for (let elem of tripBoxs) {
      if (elem == parent) {
        elem.style.boxShadow = "";
        let more = elem.querySelector('#more');
        let contact = more.children[1];
        contact.querySelector('div').scroll(0, 0);
        contact.style.display = "none";
        more.style.overflowY = "auto";
        more.style.pointerEvents = "auto";
      } else {
        elem.style.filter = "blur(0)";
        elem.style.pointerEvents = "auto";
      }
    }
    
    parent.querySelector('.contact').style.display = "none";
    
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
     
   elem.addEventListener('click', open, {once:true});
    
 }
 
 // scroll the dom relative to a trip coord.
 function scroll(cont) {
   let box = cont.getBoundingClientRect();
   let headHeight = header.offsetHeight;
   let scrollby = box.top + window.pageYOffset - headHeight - 10;
   document.documentElement.scroll({
       top: scrollby,
       left: 0,
       behaviour: 'smooth'
   });
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
 function setPhone(e) {
    let elem = e.target;
    let parent = elem.parentElement;
    parent.style.overflowY = "hidden";
    parent.style.pointerEvents = "none";
    let contact = parent.children[1];
    let cancel = contact.lastElementChild;
    contact.style.display = "block";
    cancel.addEventListener('click', () => {
       contact.querySelector('div').scroll(0, 0);
       contact.style.display = "none";
       parent.style.overflowY = "auto";
       parent.style.pointerEvents = "auto";
    }, {once:true});
    resetAnime(elem);
 }
 
 // update a trip status
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
        notify.parentElement.style.display = 'block';
        notify.style.animationPlayState = "running";
        notify.childNodes[1].innerHTML = name;
        notify.addEventListener("animationend", resetNotify, {once:true});
     }, 5000);
   }, {once:true});
   
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
  
  
  
// map constructor

function mapConstruct(coord) {
  mapboxgl.accessToken = 'pk.eyJ1Ijoic25lZXp5ZyIsImEiOiJjbGU4c2ltajYwaW5yM29sOGNvc2p6Mm9sIn0.gfgiXz_Snua47-NbzOBEww';
  
  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/sneezyg/cle9qb5o6002h01qiktb021g1',
    center: coord,
    zoom: 15
  });
  
  const marker1 = new mapboxgl.Marker().setLngLat(coord).addTo(map);
  
}


 
 
 
 
 
 

 
 
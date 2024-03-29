
// get dom element this script depend on.
const body = document.querySelector('body');
const main = document.querySelector('main');
const copyButtons = document.querySelectorAll('.para > img');
const removeButtons = document.querySelectorAll('.remove > button');
const notify = document.querySelector("#notify > p");
const confirm = document.querySelector("#confirm");
const summary = document.querySelectorAll('summary');
const tripBoxs = document.querySelectorAll("details");
const header = document.querySelector('body > header');
const logo = document.querySelector('#logo');
const dueHeader = document.querySelectorAll('.due');


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


// open up a trip box
function open(e) {
  let elem = e.target;
  main.style.overflowY = "hidden";
  header.style.filter = "blur(1px)";
  header.style.pointerEvents = "none";
  for (let elem of dueHeader) {
     elem.style.filter = "blur(1px)";
  }
  
  let detail = elem.parentElement;
  for (let elem of tripBoxs) {
    if (elem == detail) {
      elem.style.boxShadow = "10px 10px 5px #888888";
    } else {
      elem.style.pointerEvents = "none";
      elem.style.filter = "blur(1px) opacity(50%)";
    }
  }
  
  elem.addEventListener('click', close, {once:true});
    setTimeout(() => {
      domScroll = main.scrollTop;
      scroll(detail);
    }, 250);
} 

// close a trip box
function close(e) {
  main.style.overflowY = "auto";
  header.style.filter = "none";
  header.style.pointerEvents = "auto";
  for (let elem of dueHeader) {
    elem.style.filter = "none";
  }
  main.scroll({
     top: domScroll,
     left: 0,
     behaviour: 'smooth'
  });
  
  let elem = e.target;
  let parent = elem.parentElement;
  
  for (let elem of tripBoxs) {
    if (elem == parent) {
      elem.style.boxShadow = "";
    } else {
      elem.style.filter = "blur(0) opacity(100%)";
      elem.style.pointerEvents = "auto";
    }
  }
  elem.addEventListener('click', open, {once:true});
}


// scroll the dom relative to a trip coord.
function scroll(cont) {
   let box = cont.getBoundingClientRect();
   let headHeight = header.offsetHeight;
   let scrollby = box.top + domScroll + window.pageYOffset - headHeight - 10;
   main.scroll({
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
   let sn = elem.dataset.sn;
   
   let ancestor1 = elem.parentElement.parentElement.parentElement;
   let ancestor2 = ancestor1.parentElement;
   let sibling = elem.parentElement.children[1];
   
   document.querySelector("#confirmMsg > span").innerHTML = name;
   confirm.showModal();
   let button = confirm.querySelector('#continue');
   
   button.addEventListener('click', async () => {
     sibling.style.animationPlayState = 'running';
     
     let response = await fetch(`/tripclose/${sn}/`);

     if (response.ok) {
       setTimeout(timeIt(), 1000);
     } else {
       resetAnime(sibling);
       console.log("something went wrong");
     }
     
     function timeIt() {
       resetAnime(sibling);
       main.style.overflowY = "auto";
       header.style.filter = "none";
       header.style.pointerEvents = "auto";
       for (let elem of dueHeader) {
          elem.style.filter = "none";
       }
       main.scroll({
          top: domScroll,
          left: 0,
          behaviour: 'smooth'
       });
       
       for (let elem of tripBoxs) {
         elem.style.filter = "blur(0) opacity(100%)";
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
  
  
  
// connecting to web-socket.
const chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/chat/'
        );

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    //console.log(data)
    let tripBox = document.querySelector(`#${data.sn}`);
    if (data.status) {
       let statusElem = tripBox.querySelector('#info').querySelector('span');
       switch(data.status) {
          case 'G':
            statusElem.style.backgroundColor = 'green';
            break;
          case 'Y':
            statusElem.style.backgroundColor = 'yellow';
            break;
          case 'R':
            statusElem.style.backgroundColor = 'red';
       }
    }
    if (data.progress) {
       let progressElem = tripBox.querySelector('summary').querySelector('p');
       let progressInfo = tripBox.querySelector('#progress').querySelector('b');
       switch(data.progress) {
          case '0':
            progressElem.innerHTML = "Pending";
            progressInfo.innerHTML = "Pending";
            break;
          case '1':
            progressElem.innerHTML = "Departed";
            progressInfo.innerHTML = "Departed";
            break;
          case '2':
            progressElem.innerHTML = "Pickup";
            progressInfo.innerHTML = "Pickup";
            break;
          case '3':
            progressElem.innerHTML = "Onroad";
            progressInfo.innerHTML = "Onroad";
            break;
          case '4':
            progressElem.innerHTML = "Delivered";
            progressInfo.innerHTML = "Delivered";
            break;
          case '5':
            progressElem.innerHTML = "Arrived";
            progressInfo.innerHTML = "Arrived";
       }
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};
 
 
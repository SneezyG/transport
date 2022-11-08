

const body = document.querySelector('body');
const summary = document.querySelectorAll('summary');
const copyButtons = document.querySelectorAll('.para > img');
const scan = document.querySelectorAll('.para > span');
const not_found = document.querySelector('#not_found');
const barcontainer = document.querySelector('#barcode');
const chat = document.querySelectorAll('#chat');
const msg = document.querySelector('#msg');
const back = document.querySelector('#close');
const tag = document.querySelector('#tag');
const header = document.querySelector('#msg > header');
const input = document.querySelector('#input');
const textarea = document.querySelector('#textarea');
const send = document.querySelector('#send');
const section = document.querySelector('#msg > section');





 for (let elem of summary) {
    elem.addEventListener('click', open);
 }
 
 for (let elem of copyButtons) {
    elem.addEventListener('click', copy);
 }

 
 for (let elem of scan) {
    elem.addEventListener('click', lookup);
 }
 
 for (let elem of chat){
    elem.addEventListener('click', openchat);
 };
 
 
 textarea.addEventListener('input', () => {
   let charCount = textarea.innerHTML.length;
   if (charCount > 0) {
     send.style.opacity = 1;
     send.style.pointerEvents = "auto";
   }else {
     send.style.opacity = 0.6;
     send.style.pointerEvents = "none";
   }
 });
 
 
 
 
 const inScreen = window.innerHeight;
 send.addEventListener('click', () => {
   if (inScreen != window.innerHeight) {
     textarea.focus();
   }
 })
 
 
 
 
 function openchat(e) {
   let elem = e.target;
   let name = elem.dataset.name;
   let child1 = elem.children[0];
   let child2 = elem.children[1];
   child1.style.animationPlayState = "running";
   child2.style.visibility = "hidden";
   child1.addEventListener('animationend', (e) => {
     
   let rect = elem.getBoundingClientRect();
   let width = window.innerWidth;
   let right = (width - rect.right) + 20;
   
   msg.style.top = rect.top + "px";
   msg.style.right = right + "px";
   msg.style.animationPlayState = "running";
   
   msg.addEventListener('animationend', () => {
     body.style.overflow = "hidden";
     header.style.visibility = "visible";
     input.style.visibility = "visible";
     section.style.visibility = "visible";
     sectionWidth = section.offsetWidth;
     window.addEventListener('resize', reset);
     
     render();
     displace(sectionWidth);
     reset();
     
     tag.innerHTML = name + "gddhjdiekdjdnndncbcbfnbdjdjdjdjdjjdjdjddj";
   }, {once:true});
   
   back.addEventListener('click', () => {
     child2.style.visibility = "visible";
     body.style.overflow = "auto";
     header.style.visibility = "hidden";
     input.style.visibility = "hidden";
     section.style.visibility = "hidden";
     resetAnime(child1);
     resetAnime(msg);
     window.removeEventListener('resize', reset, {once:true});
     
   }, {once: true});
   
   }, {once:true});
   
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
 
 
 function reset() {
   let windowHeight= window.innerHeight;
   let inputHeight = input.offsetHeight;
   let headerHeight = header.offsetHeight;
   let availHeight = windowHeight - inputHeight - headerHeight;
   
   section.style.height = "none";
   section.offsetWidth;
   section.style.height = null;
   
   let sectionHeight = section.offsetHeight;
   if (sectionHeight >= availHeight) {
     section.style.height = availHeight + 'px';
   }
   
   let newWidth = section.offsetWidth;
   if (newWidth != sectionWidth) {
     displace(newWidth);
     sectionWidth = newWidth;
   }

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
 
 
 
 
 function render() {
   for (let key in messages) {
     let p = document.createElement('p');
     p.id = "msgDate";
     let p_span = document.createElement('span');
     p_span.innerHTML = key;
     p.append(p_span);
     section.prepend(p);
     
     for (let index in messages[key]) {
       let item = messages[key][index];
       let div = document.createElement('div');
       let outerSpan = document.createElement('span');
       div.id = item.sender;
       outerSpan.className = "text";
       
       let innerSpan = document.createElement('span');
       innerSpan.innerHTML = item.msg;
       
       let sub = document.createElement('sub');
       sub.innerHTML = item.time;
       
       if (item.status) {
         let img  = document.createElement('img');
         img.src = item.status + ".png";
         img.alt = "status";
         sub.append(img);
       }
       
       outerSpan.append(innerSpan);
       outerSpan.append(sub);
       div.append(outerSpan);
       section.prepend(div);
       
     }
   }
 }
 
 
 
 function displace(width) {
   let spans = document.querySelectorAll(".text > span");
   let maxWidth = width * 0.6;
   for (let elem of spans) {
     elem.style.width = "none";
     elem.offsetWidth;
     elem.style.width = null;
     
     if (elem.offsetWidth > maxWidth) {
       elem.style.width = maxWidth + "px";
     }
     
     let parent = elem.parentElement;
     let ancestor = parent.parentElement;
     if (ancestor.id == "me") {
        let displace = (width - parent.offsetWidth) - 1;
        parent.style.left = displace + "px";
     }
   }
 }
 
 
 
 
let messages = {
   "30 October 2022": [
     {sender: "me", msg: "gehehe hensn bdbdb dgdhh dbdb ", time: "7:30am", status: "read"}, 
     {sender: "you", msg: "gehehe", time: "7:45am"},
     {sender: "you", msg: " gehehe hensn bdbdb", time: "12:50pm"},
     {sender: "me", msg: "gehehe", time: "1:40pm", status: "read" }
   ],
   
   "06 November 2022": [
     {sender: "you", msg: "thehjrbdb dndnjdin ebfbcbbcjejne ndyeieokebc bcbbxbxbxbhcj eirbfbdn dnddn", time: "2:00pm"}, 
     {sender: "me", msg: "thehjr bdbdndnjdinebfb cbbcjejn endyeieoke bcbcbbxbxbxbhcjei rbfbdndnddn", time: "2:20pm", status: "pending"},
   ]
};


 
 
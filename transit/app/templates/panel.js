

const summary = document.querySelectorAll('summary');
const copyButtons = document.querySelectorAll('.para > img');
const removeButtons = document.querySelectorAll('.remove');
const copied = document.querySelectorAll('.copy')






 for (let elem of summary) {
    elem.addEventListener('click', open, {once:true});
 }
 
 for (let elem of copyButtons) {
    elem.addEventListener('click', copy);
 }
 
 
 for (let elem of copied) {
   elem.addEventListener('animationend', resetAnime);
 }
 
 
 
 
 
 
 
 function open(e) {
    let elem = e.target;
    for (let child of elem.children) {
      let tag = child.tagName;
      console.log(tag);
      if (tag != "SPAN" && tag != "P") {
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
 
 
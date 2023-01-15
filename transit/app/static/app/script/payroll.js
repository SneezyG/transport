
// get dom element that this script depend on.
 const body = document.querySelector('body');
 const cancel = document.querySelectorAll('.button');
 const query = document.querySelector('#search > button');
 const not_found = document.querySelector('#not_found');
 const error = document.querySelector('#error');
 const radio = document.querySelectorAll('.radio');
 const id = document.querySelector('#id');
 const time = document.querySelector('#time');
 const payroll = document.querySelector('#payroll');
 const search = document.querySelector('#search');
 const mark = document.querySelector('#mark');
 const spiner = document.querySelector("#spiner");
 
 // set default freelancer.
 let freelancer = 'Driver';
 
 
 
 for (let elem of radio) {
  elem.addEventListener('click', setfreelancer);
 }
 
 for (let elem of cancel) {
  elem.addEventListener('click', bodyreset);
 }
 
 query.addEventListener('click', lookup);
 
 // set a resize event listener for search input.
 const resizeObserver = new ResizeObserver((e) => {
    let rect = search.getBoundingClientRect();
    mark.style.paddingLeft = rect.left + "px";
  });
 resizeObserver.observe(search);


 
 // look up a freelancer trip/wage summary.
 function lookup() {
   body.style.overflow = "hidden";
   if (!id.value || !time.value ) {
     error.innerHTML = "Please enter freelancer ID and date to continue.";
     not_found.showModal();
     
   } else {
     spiner.open = true;
     let searchObj = {
       'freelancer': freelancer,
       'id': id.value,
       'time': time.value
      };
      setTimeout(() => {
        spiner.open = false;
        payroll.showModal();
      }, 5000);
   }
 }
 
 // update the value of freelancer global variable.
 function setfreelancer(e) {
   let elem = e.target;
   freelancer = elem.value;
 }
 
 
 // reset style overflow attr of body elements.
 function bodyreset() {
   body.style.overflow = "auto";
 }
 
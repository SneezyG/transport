
// get dom element that this script depend on.
 const body = document.querySelector('body');
 const cancel = document.querySelectorAll('.button');
 const query = document.querySelector('#search > button');
 const not_found = document.querySelector('#not_found');
 const error = document.querySelector('#error');
 const id = document.querySelector('#id');
 const time = document.querySelector('#time');
 const payroll = document.querySelector('#payroll');
 const search = document.querySelector('#search');
 const spiner = document.querySelector("#spiner");
 
 
 
 for (let elem of cancel) {
  elem.addEventListener('click', bodyreset);
 }
 
 query.addEventListener('click', lookup);
 
 
 // look up a freelancer trip/wage summary.
 function lookup() {
   body.style.overflow = "hidden";
   if (!id.value || !time.value ) {
     error.innerHTML = "Please enter freelancer ID and date to continue.";
     not_found.showModal();
     
   } else {
     spiner.open = true;
     let searchObj = {
       'id': id.value,
       'time': time.value
      };
      setTimeout(() => {
        spiner.open = false;
        payroll.showModal();
      }, 5000);
   }
 }
 

 // reset style overflow attr of body elements.
 function bodyreset() {
   body.style.overflow = "auto";
 }
 
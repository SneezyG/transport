

 const body = document.querySelector('body');
 const cancel = document.querySelectorAll('.button');
 const query = document.querySelector('#search > button');
 const not_found = document.querySelector('#not_found');
 const error = document.querySelector('#error');
 const radio = document.querySelectorAll('.radio');
 const id = document.querySelector('#id');
 const time = document.querySelector('#time');
 const payroll = document.querySelector('#payroll');
 
 
 let freelancer = 'Driver';
 
 
 
 for (let elem of radio) {
  elem.addEventListener('click', setfreelancer);
 }
 
 for (let elem of cancel) {
  elem.addEventListener('click', bodyreset);
 }
 
 query.addEventListener('click', lookup);
 
 
 
 
 function lookup() {
   if (!id.value || !time.value ) {
     error.innerHTML = "Please enter freelancer ID and date to continue";
     //not_found.showModal();
     payroll.showModal();
     body.style.overflow = "hidden";
     
   } else {
     let searchObj = {
       'freelancer': freelancer,
       'id': id.value,
       'time': time.value
     };
     console.log(searchObj);
     payroll.showModal();
   }
 }
 
 
 function setfreelancer(e) {
  // console.log(freelancer);
   elem = e.target;
   freelancer = elem.value;
  // console.log(freelancer);
 }
 
 
 function bodyreset() {
   body.style.overflow = "auto";
 }
 
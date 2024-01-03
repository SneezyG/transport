
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
 async function lookup() {
   body.style.overflow = "hidden";
   if (!id.value || !time.value ) {
     error.innerHTML = "Please enter freelancer ID and date to continue.";
     not_found.showModal();
     
   } else {
     spiner.open = true;
     date = new Date(time.value);
     let searchObj = {
       'id': id.value,
       'year': date.getFullYear(),
       'month': date.getMonth() + 1,
       'day': date.getDate(),
      };
      //console.log(searchObj);
      
      let response = await fetch('/payroll/', {
       method: 'POST',
       headers: {
         'Content-Type': 'application/json;charset=utf-8',
         'X-CSRFToken': getCSRFToken()
       },
       body: JSON.stringify(searchObj)
      });
      
      let data = await response.json(); 
      
      if (response.ok) {
        setTimeout(() => {
          spiner.open = false;
          console.log(data.photo);
          document.querySelector('#profile-name').innerHTML = `• ${data.name}`;
          document.querySelector('#profile-image').src = data.photo;
          document.querySelector('#trip-date').innerHTML = time.value;
          document.querySelector('#short-range').innerHTML = data.short;
          document.querySelector('#mid-range').innerHTML = data.mid;
          document.querySelector('#long-range').innerHTML = data.long;
          document.querySelector('#sum-range').innerHTML = data.sum;
          document.querySelector('#wages').innerHTML = Number(data.wages).toLocaleString('en-US', options);
          payroll.showModal();
        }, 1000);
      } else {
        setTimeout(() => {
          spiner.open = false;
          error.innerHTML = data.error;
          not_found.showModal();
        }, 1000);
      }
     
   }
 }
 

 // reset style overflow attr of body elements.
 function bodyreset() {
   body.style.overflow = "auto";
   document.querySelector('#profile-image').src = "";
 }
 
 
 function getCSRFToken() {
    const csrfCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfCookie) {
        return csrfCookie.split('=')[1];
    }
    return null;
 }
 
 //currency number formatting
 const options = {
    style: 'decimal',
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
 };

 const body = document.querySelector("body");
 const shorts = document.querySelectorAll("#short > span");
 const submit = document.querySelector(".submit");
 const cancel = document.querySelector(".cancel");
 const formBox = document.querySelector("main > div");
 const form = document.querySelector("main form");
 const create = document.querySelector("#create > button");
 const success = document.querySelector("#success");
 const failure = document.querySelector("#failure");
 const spiner = document.querySelector("#spiner");
 const ratio = document.querySelector("#ratio");
 const close = document.querySelectorAll(".button");
 const progress = document.querySelector("#progress > select");
 const remark = document.querySelector("#remark > input");
 const radios = document.querySelectorAll("#status > input");
 

 const nav = document.querySelector('#nav');
 
 // trip sn, due report and submitted report.
 const sn = nav.dataset.sn;
 const dueReport = Number(nav.dataset.due);
 let submitedReport = Number(nav.dataset.submit);
 let status = "Green";
 // set create new report button.
 resetReport();
 
 
 // reset report box style and props
 function resetReport() {
   create.style.pointerEvents = "auto";
   create.style.opacity = "1";
   if (dueReport <= submitedReport) {
      create.style.pointerEvents = "none";
      create.style.opacity = "0.6";
   }
   ratio.innerHTML = dueReport + "(" + submitedReport + ')';
 }
 
 
 for (let elem of radios) {
    elem.addEventListener('click', setStatus);
 }
 
 // handle report submition
 submit.addEventListener('click', async () => {
     // get user location(Navigator.location);
     body.style.overflow = "hidden";
     if (!progress.value || !remark.value || !status ) {
       document.querySelector("#error").innerHTML = "Please enter status, progress and remark to continue.";
       failure.showModal();
       
     } else {
       spiner.open = true;
       let reportData = {
         'sn': sn,
         'status': status[0],
         'progress': progress.value,
         'remark': remark.value,
         'lat': "",
         'long': ""
        };
        console.log(reportData);
        let response = await fetch(`/agent/report/${sn}/`, {
          method: 'POST',
          headers: {
           'Content-Type': 'application/json;charset=utf-8',
           'X-CSRFToken': getCSRFToken()
          },
          body: JSON.stringify(reportData)
        });
      
        let data = await response.json(); 
    
        if (response.ok) {
          setTimeout(() => {
          spiner.open = false;
          success.showModal();
          }, 1000);
          submitedReport += 1;
          if (submitedReport == dueReport) {
             localStorage.clear();
          }
          formBox.style.display = "none";
          resetReport()
          showForm("Green");
        } else {
          setTimeout(() => {
          spiner.open = false;
          document.querySelector("#error").innerHTML = data.error;
          failure.showModal();
          }, 1000);
        }
        
     }
 });
 
 
 for (let elem of close) {
   elem.addEventListener('click', bodyreset);
 }
 
 // prepare page for report creation
 create.addEventListener('click', () => {
     formBox.style.display = "block";
     create.style.opacity = "0";
 });
 
 // prepare page on report create cancel
 cancel.addEventListener('click', () => {
     formBox.style.display = "none";
     create.style.opacity = "1";
     showForm("Green");
 });
    
  


 for (let elem of shorts) {
    elem.addEventListener("click", (e) => {
      let elem = e.target;
      let elemID = elem.dataset.id;
      showForm(elemID);
      elem.style.animationPlayState = "running";
      elem.addEventListener("animationend", () => {
          resetAnime(elem);
       }, {once:true});
   });
 }
 
 
 // show form for a report.
 function showForm(elemID) {
    // set status
    status = elemID;
    let radios = form.children[1].children;
    for (let radio of radios) {
      if (radio.id == elemID) {
        radio.checked = true;
      }
    }
    let input = form.children[7].lastElementChild;
    if (elemID == "Green") {
       input.value = "An awesome trip";
       input.style.backgroundColor = "#B2BEB5";
       form.style.backgroundColor = "#B2BEB5";
    }
    else if (elemID == "Yellow") {
       input.value = "A cool trip";
       input.style.backgroundColor = "#B6B3A8";
       form.style.backgroundColor = "#B6B3A8";
    }
    else {
       input.value = "A wretched trip";
       input.style.backgroundColor = "#C4AEAD";
       form.style.backgroundColor = "#C4AEAD";
    }
 }
 
 // update the value of freelancer global variable.
 function setStatus(e) {
   let elem = e.target;
   status = elem.value;
 }
 
 // reset style animation of element.
 function resetAnime(e) {
     let elem = e.target ?? e;
     elem.style.animation = "none";
     elem.offsetWidth;
     elem.style.animation = null;
 }
 
 // set body overflow style prop
 function bodyreset() {
   body.style.overflow = "auto";
 }
 
 
 function getCSRFToken() {
    const csrfCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));
    if (csrfCookie) {
        return csrfCookie.split('=')[1];
    }
    return null;
 }
 
 
 
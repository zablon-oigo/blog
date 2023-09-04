let blogApp=()=>{
    let dismissButton=document.querySelector('#dismiss-alert')
    dismissButton.classList.toggle('hidden')
    
}
setTimeout(blogApp,3000) 

let app=()=>{
    let alertButton=document.querySelector('#alert');
    alertButton.classList.toggle('hidden')
    console.log('its working')
}
setTimeout(app,4000)


// document.addEventListener('click',()=>{
//     let dismissButton=document.querySelector('#dismiss-alert')
//     dismissButton.classList.toggle('hidden')
           
// })

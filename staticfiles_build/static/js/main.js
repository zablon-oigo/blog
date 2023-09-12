let blogApp=()=>{
    let dismissButton=document.querySelector('#dismiss-alert')
    dismissButton.classList.toggle('hidden')
    
}
setTimeout(blogApp,3000) 

// let app=()=>{
//     let alertButton=document.querySelector('#alert');
//     alertButton.classList.toggle('hidden')
//     console.log('its working')
// }
// setTimeout(app,4000)


// dispaly time on the page footer
let d=new Date()
mymonth=d.toLocaleDateString('default',{
    year:'numeric',
    // month:'short',
    
})
let demo = document.querySelector('#demo')
demo.innerHTML+=` ${mymonth}`

// Toggle Button
const myButton=()=>{
    let toggleButton=document.querySelector('#toggleButton')
    let section=document.querySelector('#section')
    const toggleMenu = () =>{
        section.classList.toggle('hidden')
        section.classList.toggle('flex')
    }
   
    toggleButton.addEventListener('click',toggleMenu)
}
document.addEventListener('DOMContentLoaded',myButton)

// close menu button

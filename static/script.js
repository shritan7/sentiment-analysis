const textarea = document.querySelector("textarea");

const button = document.querySelector("button");

button.addEventListener("click", () => {

button.innerHTML="⏳ Analyzing...";
});

textarea.addEventListener("input", () => {

    document.getElementById("count").innerHTML =
        textarea.value.length + " Characters";

});

textarea.addEventListener("keydown",(e)=>{

if(e.ctrlKey && e.key==="Enter"){

button.click();

}

});

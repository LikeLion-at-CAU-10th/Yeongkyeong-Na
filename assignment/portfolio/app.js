// 다크모드 버튼
const checkbox = document.querySelector('.checkbox');
console.log(checkbox);

checkbox.addEventListener('click',toggleClick);

function toggleClick(){
    document.body.classList.toggle('dark');
    console.log('working!');
}

// contact 사이드바
const contactBtn = document.querySelector('.contact-btn');
const contact = document.querySelector('.contact');
const contactLabel = document.querySelector('.contact-label');
const closeBtn = document.querySelector('.close-btn');

contactBtn.addEventListener('click',function(){
    contact.style.transform = "translate(0%)"
    contactLabel.style.opacity=0;
});

closeBtn.addEventListener('click', function(){
    contact.style.transform = "translate(100%)"
    contactLabel.style.opacity=1;
});
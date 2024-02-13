//id가 Form인 친구를 불러올거ㅔㅇ여
const form = document.getElementById("form")

//form에 submit라는 이벤트가 발생하면 function()을 호출할거에여
form.addEventListener("submit",function(event){

    event.preventDefault()


    let userEmail = event.target.email.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone1 = event.target.phone1.value
    let userPhone2 = event.target.phone2.value
    let userPhone3 = event.target.phone3.value
    let userNum = event.target.num.value
    let userRegion = event.target.region.value
    let userGender = event.target.gender.value

    console.log(userEmail,userPw1,userPw2,userName,userPhone1,
        userPhone2,userPhone3,userNum,userRegion,userGender)

})
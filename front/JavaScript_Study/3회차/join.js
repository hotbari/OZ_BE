// 제출 이벤트를 받는다 (이벤트 핸들링)
const form = document.getElementById("form")

//form에서 이벤트가 발생하면~
form.addEventListener("submit", function(event){
    event.preventDefault()
    let userId = event.target.id.value
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone = event.target.phone.value
    let userPosition = event.target.position.value
    let userGender = event.target.gender.value
    let userEmail = event.target.email.value
    let userIntro = event.target.intro.value

    // 제출된 입력 값들을 참조한다
    // console.log(userId,userPw1,userPw2,userName,userPhone,userPosition,userGender,userEmail,userIntro)

    // 입력값에 문제가 있는 경우 이를 감지한다.(아이디 최소 길이, 비밀번호==비밀번호 확인)
    if(userId.length < 6){
        alert("아이디가 너무 짧습니다 :(")
        return //함수 강제 종료
    }

    if(userPw1 !== userPw2) {
        alert("비밀번호가 일치하지 않습니다.")
        return
    }

    // 가입 환영 인사를 제공
    document.body.innerHTML = "" //아무것도 없는 body 태그로 바꿈
    document.write(`<p>${userId}님 환영합니다 !</p>`)
    document.write(`<p>회원 가입 시 입력하신 내역은 다음과 같습니다.</p>`)
    document.write(`<p>아이디 : ${userId}</p>`)
    document.write(`<p>이름 : ${userName}.</p>`)
    document.write(`<p>전화번호 : ${userPhone}</p>`)
    document.write(`<p>원하는 직무 : ${userPosition}</p>`)

}) 
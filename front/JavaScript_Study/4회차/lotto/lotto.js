//맨 처음에 싹다 선택하세요잉

const todayP = document.querySelector("#today")
const numbersDiv = document.querySelector(".numbers")
const drawBtn = document.querySelector("#draw")
const resetBtn = document.querySelector("#reset")


// 빈 배열 만들어서 여기다 로또 번호 추가
let lottoNumbers = []

const today = new Date()
let year = today.getFullYear() 
let month = today.getMonth() + 1 
let day = today.getDate()
todayP.textContent = `${year}년 ${month}월 ${day}일...` 

function paintNumber(number){
    const eachNumDiv = document.createElement("div")
    eachNumDiv.classList.add("eachnum") //css를 위해 추가
    eachNumDiv.textContent = number
    numbersDiv.append(eachNumDiv)
}

// 배열에 6개의 요소가 들어갈 동안 랜덤 돌림, 단 배열에 없는 숫자만
drawBtn.addEventListener("click",function(){
    numbersDiv.innerHTML = ""
        while(lottoNumbers.length < 6) {
            let rn = Math.floor(Math.random()*45) + 1
            if(lottoNumbers.indexOf(rn) === -1){
                lottoNumbers.push(rn)
                paintNumber(rn)
            }

    }
    lottoNumbers = []
})

// 리셋 버튼
resetBtn.addEventListener("click",function(){
    lottoNumbers.splice(0,6)
    numbersDiv.innerHTML = ""
})

